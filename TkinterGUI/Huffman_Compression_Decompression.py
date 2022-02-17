from base64 import encode
import heapq
import os

class HuffmanCoding:
    def __init__(self,filename):
        self.filename=filename
        self.dict_codes={}
        self.rev_mapping={}
        self.heap=[]

    class HeapNode:
        def __init__(self,char,freq):
            self.char=char
            self.frequency=freq
            self.left=None
            self.right=None

        # defining comparators less_than and equals

        def __lt__(self,other):
            if (self.frequency<other.frequency):
                return True
            else:
                return False 

        def __eq__(self,other):
            if other==None:
                return False
            elif (not isinstance(other,HeapNode)):
                return False
            elif(self.freq==other.freq):
                return True
            else:
                return False

#   Compression starts here....

    def make_frequency_dict(self,content):
        frequency={}
        for char in content:
            if not char in frequency:
                frequency[char]=0
            else:
                frequency[char]+=1
        return frequency

    def make_heap(self,frequency):
        for key in frequency:
            node=self.HeapNode(key,frequency[key])
            heapq.heappush(self.heap,node)

    def merge_nodes(self):
        while(len(self.heap)>1):
            node1=heapq.heappop(self.heap)
            node2=heapq.heappop(self.heap)
            merged=self.HeapNode(None,node1.frequency+node2.frequency)
            merged.left=node1
            merged.right=node2

            heapq.heappush(self.heap,merged)

    def make_codes(self):
        root=heapq.heappop(self.heap)
        current_code=""
        self.make_codes_helper(root,current_code)

    def make_codes_helper(self,root,current_code):
        if(root==None):
            return
        if(root.char != None):
            self.dict_codes[root.char]=current_code
            self.rev_mapping[current_code]=root.char
            return
        self.make_codes_helper(root.left,current_code+"0")
        self.make_codes_helper(root.right,current_code+"1")

    def get_encoded_text(self,text):
        encoded_text=""
        for character in text:
            encoded_text+=self.dict_codes[character]
        return encoded_text

    def pad_encoded_text(self,encoded_text):
        extra_padding=8-len(encoded_text)%8

        for i in range(extra_padding):
            encoded_text+="0"
        padded_info="{0:08b}".format(extra_padding)
        encoded_text=padded_info+encoded_text

        return encoded_text

    def get_byte_array(self,padded_encoded_text):
        if(len(padded_encoded_text)%8!= 0):
            print("Encoded text not padded properly")
            exit(0)

        b=bytearray()
        for i in range(0,len(padded_encoded_text),8):
            byte=padded_encoded_text[i:i+8]
            b.append(int(byte,2))
        
        return b

    def compression(self):
        filename, file_extension = os.path.splitext(self.filename)
        output_path = filename + ".bin"

        with open(self.filename, 'r+') as file, open(output_path, 'wb') as output:
			
            text = file.read()
            text = text.rstrip()
            frequency = self.make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_nodes()
            heapq.heapify(self.heap)
            self.make_codes()
            print(self.dict_codes)

            encoded_text = self.get_encoded_text(text)			
            padded_encoded_text = self.pad_encoded_text(encoded_text)
            b = self.get_byte_array(padded_encoded_text)
        
            output.write(bytes(b))

        print("Compressed")		
        return output_path

#   Decompression starts here....
    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)
        padded_encoded_text = padded_encoded_text[8:] 
        encoded_text = padded_encoded_text[:-1*extra_padding]
        return encoded_text

    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in self.rev_mapping:
                character=self.rev_mapping[current_code]
                decoded_text+=character
                current_code=""
        return decoded_text

    def decompression(self,input_path):
        filename,file_extension=os.path.splitext(self.filename)
        output_path=filename+"_decompressed"+".txt"

        with open(input_path,'rb') as file,open(output_path,'w') as output:
            bit_string=""

            byte=file.read(1)
            while(len(byte)>0):
                byte=ord(byte)
                bits=bin(byte)[2:].rjust(8,'0')
                bit_string+=bits
                byte=file.read(1)

            encoded_text=self.remove_padding(bit_string)
            decompressed_text=self.decode_text(encoded_text)
            
            output.write(decompressed_text)
        print("Decompressed")
        return output_path


if __name__=="__main__":
    path = "sample.txt"
    h = HuffmanCoding(path)
    output_path = h.compression()
    print("Compressed file path: " + output_path)
    decom_path = h.decompression(output_path)
    print("Decompressed file path: " + decom_path)