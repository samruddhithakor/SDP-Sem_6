import os
from pathlib import Path
from tkinter import *
from tkinter import ttk
import time
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename
import main
import JPEG
import Huffman_Compression_Decompression as hcd


def update_inputfile(file):
    input_file["text"]=f"Input File : {file}"

def update_outputfile(file):
    file_extension =Path(file).suffix
    compressfilestr=os.path.splitext(f"{file}")[0];
    if(file_extension=='.txt'):
        output_file["text"]=f"Output File : {compressfilestr}_Compress.bin"
    else:
        output_file["text"]=f"Output File : {compressfilestr}_Compress{file_extension}"

def sel():
    selection = "You selected the option " + str(filetype.get())
    print(selection)

def upload_file():
    fileselection =filetype.get()
    global file
    if(fileselection==1):
        print(fileselection,"Text")
        val=True
        while val:
            file=askopenfilename();
            print(file)
            file_extension = Path(file).suffix
            if(file == ""):
                val=False
            elif(file_extension!=".txt"):
                val=tmsg.askretrycancel("ERROR!!!","SORRY !!! YOU CANNOT OPEN THIS FILE.PLEASE SELECT TEXT FILE(.txt)")
                print(val)
            else:
                progress()
                val=False
                text_lbl4.pack()
                update_inputfile(file)
                input_file.pack()
    elif(fileselection==2):
        print(fileselection,"Image")
        val=True
        while val:
            file=askopenfilename();
            print(file)
            file_extension = Path(file).suffix
            if(file == ""):
                val=False
            elif(file_extension!=".jpeg" and file_extension!=".JPEG" and file_extension!=".JPG" and file_extension!=".jpg"):
                val=tmsg.askretrycancel("ERROR!!!","SORRY !!! YOU CANNOT OPEN THIS FILE.PLEASE SELECT IMAGE FILE(.jpeg/.jpg)")
                print(val)
            else:
                progress()
                val=False
                text_lbl4.pack()
                update_inputfile(file)
                input_file.pack()
    elif(fileselection==3):
        print(fileselection,"Video")
        val=True
        while val:
            file=askopenfilename();
            print(file)
            file_extension = Path(file).suffix
            if(file == ""):
                val=False
            elif(file_extension!=".mp4"):
                val=tmsg.askretrycancel("ERROR!!!","SORRY !!! YOU CANNOT OPEN THIS FILE.PLEASE SELECT Video file(.mp4)")
                print(val)
            else:
                progress()
                val=False
                text_lbl4.pack()
                update_inputfile(file)
                input_file.pack()
    else:
        tmsg.showinfo(title="ERROR!!!",message='Please choose file format !!!')

def update_progress_label():
    if pb['value']<100:
        return f"Current Progress: {pb['value']}%"
    else:
        return f"Uploaded Successfully"

def progress():
    pb.pack(side=BOTTOM,fill=X)
    value_label.pack(pady=10)
    import time
    pb['value']=0
    while  pb['value'] < 100:
        pb['value'] += 20
        value_label['text'] = update_progress_label()
        root.update_idletasks()
        time.sleep(0.5)
    tmsg.showinfo(title="DONE",message='File Uploaded Successfully!!!')
    pb.pack_forget()
    value_label.pack_forget()

def start_loading():
    for i in range(0,3):
        for gif in giflist:
                canvas.delete(ALL)
                canvas.create_image(width/2.0, height/2.0, image=gif)
                canvas.update()
                time.sleep(0.1)

def compress_file():
    fileselection =filetype.get()
    try:
        file_extension = Path(file).suffix
        if(file_extension==".txt" and fileselection==1):
            textcompress(file)
        elif(file_extension==".jpeg" or file_extension==".JPEG" or file_extension==".JPG" or file_extension==".jpg" and fileselection==2):
            imagecompress(file)
        elif(file_extension==".mp4" and fileselection==3):
            videocompress(file)
        else:
            tmsg.showinfo(title="ERROR!!!",message='Please Select proper file !!!')
    except:
        tmsg.showinfo(title="ERROR!!!",message='Please Select proper file !!!')

def videocompress(file):
    print("video",file)
    fileselection =filetype.get()
    file_extension =Path(file).suffix
    if(file_extension==".mp4" and fileselection==3):
            canvas.pack()
            start_loading()
            canvas.pack_forget()
            main.compress_video(f"{file}", 2*1000)
            tmsg.showinfo(title="SUCCESS",message='Video Compressed Successfully!!!')
            text_lbl4.pack_forget()
            update_outputfile(file)
            output_file.pack()
    else:
            tmsg.showinfo(title="ERROR!!!",message='Please Select video file(.MP4) !!!')

def textcompress(file):
    print("text",file)
    fileselection =filetype.get()
    file_extension =Path(file).suffix
    if(file_extension==".txt" and fileselection==1):
            canvas.pack()
            start_loading()
            canvas.pack_forget()
            
            h=hcd.HuffmanCoding(file)
            output_path = h.compression()
            print("Compressed file path: " + output_path)
            decom_path = h.decompression(output_path)
            print("Decompressed file path: " + decom_path)
            tmsg.showinfo(title="SUCCESS",message='Text Compressed Successfully!!!')
            text_lbl4.pack_forget()
            update_outputfile(file)
            output_file.pack()
    else:
            tmsg.showinfo(title="ERROR!!!",message='Please Select Text file(.txt) !!!')

def imagecompress(file):
    print("image",file)
    fileselection =filetype.get()
    file_extension =Path(file).suffix
    if(file_extension==".jpeg" or file_extension==".JPEG" or file_extension==".JPG" or file_extension==".jpg" and fileselection==2):
            canvas.pack()
            start_loading()
            canvas.pack_forget()
            JPEG.JPEG(file)
            tmsg.showinfo(title="SUCCESS",message='Image Compressed Successfully!!!')
            text_lbl4.pack_forget()
            update_outputfile(file)
            output_file.pack()
    else:
            tmsg.showinfo(title="ERROR!!!",message='Please Select Image file(.jpg/.jpeg) !!!')



root=Tk()
root.title("FILE Compression-Decompression---Tkinter(Python)")
width=850
height=650
root.geometry(f"{width}x{height}")
root.minsize(width,height)
root.maxsize(width,height)
root.wm_iconbitmap("compress.ico")
root.config(background="#87cefa")

Header=Label(root,text="FILE Compression-Decompression",font="Sans-serif 22 bold",pady=20,background="#87cefa")
Header.pack(fill=X)

filetype = IntVar()
R1 = Radiobutton(root, text="Text", variable=filetype, value=1,command=sel,background="#87cefa",font="Sans-serif 15 bold")
R1.pack(anchor=W,padx=350)

R2 = Radiobutton(root, text="Image", variable=filetype, value=2,command=sel,background="#87cefa",font="Sans-serif 15 bold")
R2.pack(anchor=W,padx=350)

R3 = Radiobutton(root, text="Video", variable=filetype, value=3,command=sel,background="#87cefa",font="Sans-serif 15 bold")
R3.pack(anchor=W,padx=350)


text_lbl1=Label(root,text="For Text file choose .txt, Image file choose .jpeg/.jpg, Video file choose .mp4",font="Sans-serif 12",pady=5,background="#87cefa")
text_lbl1.pack(fill=X,pady=5)

text_lbl2=Label(root,text="Click here to upload file ↓",font="Sans-serif 11",pady=5,background="#87cefa")
text_lbl2.pack(fill=X)

button = Button(root, text="UPLOAD",font="Sans-serif 13 bold",command=upload_file,pady=5,height=2,width=20,background="#bcd4e6")
button.pack(pady=15)

global input_file
input_file=Label(root,text="",font="Sans-serif 10",pady=5,background="#87cefa")
input_file.pack()



text_lbl3=Label(root,text="Click here to Compress file ↓",font="Sans-serif 11",pady=5,background="#87cefa")
text_lbl3.pack(fill=X)
text_lbl4=Label(root,text="Click Now ↑",font="Sans-serif 13 bold",pady=5,background="#3AAFA9")

button2 = Button(root, text="COMPRESS",font="Sans-serif 13 bold",command=compress_file,pady=5,height=2,width=20,background="#bcd4e6")
button2.pack(pady=15)


global output_file
output_file=Label(root,text="",font="Sans-serif 10",pady=5,background="#87cefa")
output_file.pack()


imagelist = ["dog001.gif","dog002.gif","dog003.gif","dog004.gif","dog005.gif","dog006.gif","dog007.gif"]
pb = ttk.Progressbar(root,orient='horizontal',mode='determinate',length=280)
value_label = ttk.Label(root, text=update_progress_label(),background="#3AAFA9",font="Sans-serif 10 bold")

photo = PhotoImage(file=imagelist[0])
width = photo.width()
height = photo.height()
canvas = Canvas(width=width, height=height,background="#87cefa",highlightthickness=0)

giflist = []
for imagefile in imagelist:
    photo = PhotoImage(file=imagefile)
    giflist.append(photo)


root.mainloop()