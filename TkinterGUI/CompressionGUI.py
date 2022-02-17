from importlib.resources import path
from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename,asksaveasfilename
from pathlib import Path
import tkinter.messagebox as tmsg
from tkinter import ttk
import Huffman_Compression_Decompression as hcd

def upload_file():
    val=True
    global file
    while val:
        file=askopenfilename();
        file_extension =Path(file).suffix
        if(file_extension!=".txt"):
            val=tmsg.askretrycancel("ERROR!!!","SORRY !!! YOU CANNOT OPEN THIS FILE.PLEASE SELECT TEXT FILE(.txt)")
        else:
            progress()
            break
    
    # p = Path(file)
    # filename=p.with_suffix('')
    # with open(file) as f:
    #     text=f.read()
    #     print(text)
    # with open(f"{filename}_dec.txt",'w') as f:
    #     f.write(text)



def compression():
    # path = "sample.txt"
    path=file
    h=hcd.HuffmanCoding(path)
    # h = HuffmanCoding(path)
    output_path = h.compression()
    print("Compressed file path: " + output_path)
    decom_path = h.decompression(output_path)
    print("Decompressed file path: " + decom_path)



def update_progress_label():
    if pb['value']<100:
        return f"Current Progress: {pb['value']}%"
    else:
        return f"Uploaded Successfully"


def progress():
    
    # pb = ttk.Progressbar(root,orient='horizontal',mode='determinate',length=280)
    pb.grid(column=2, row=3, padx=10, pady=20)
    # value_label = ttk.Label(root, text=update_progress_label())
    value_label.grid(column=2, row=4,pady=3)
    import time
    while  pb['value'] < 100:
        pb['value'] += 20
        value_label['text'] = update_progress_label()
        root.update_idletasks()
        time.sleep(0.5)
            
    tmsg.showinfo(message='File Uploaded Successfully!!!')
    destroy()

def destroy():
    pb.destroy()
    value_label.destroy()


root=Tk()
root.title("Compression-Decompression - Tkinter(Python)")
width=700
height=450
root.geometry(f"{width}x{height}")
root.minsize(width,height)
root.maxsize(width,height)
root.wm_iconbitmap("compress.ico")
root.config(background="#3AAFA9")
header=Label(root,text="--TEXT-COMPRESSION--",font="Sans-serif 20 bold",background="#3AAFA9",pady=30,padx=5)
header.grid(row=1,column=2)






text_lbl1=Label(root,text="Choose text file...",font="Sans-serif 13 bold",background="#3AAFA9")
text_lbl1.grid(row=2,column=1)
button = Button(root, text="upload",border=7,command=upload_file)
_img=Image.open('upload.png')
_img=_img.resize((130,80),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(_img)
button.config(image=photo)
button.grid(row=3,column=1,padx=25,pady=5)





text_lbl2=Label(root,text="Click here...",font="Sans-serif 13 bold",background="#3AAFA9")
text_lbl2.grid(row=2,column=3)
# compress_btn=Button(root,text="Compress",command=compression,border=7)
compress_btn=Button(root,text="Compress",border=7)
c_img=Image.open('cmbtn.png')
c_img=c_img.resize((130,80),Image.ANTIALIAS)
cphoto=ImageTk.PhotoImage(c_img)
compress_btn.config(image=cphoto)
compress_btn.grid(row=3,column=3)





pb = ttk.Progressbar(root,orient='horizontal',mode='determinate',length=280)
value_label = ttk.Label(root, text=update_progress_label(),background="#3AAFA9",font="Sans-serif 10 bold")

root.mainloop()