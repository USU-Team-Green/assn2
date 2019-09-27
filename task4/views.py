import tkinter 
from tkinter import filedialog


from key_gen import generate_keys

class View():
    children = []
    
    def clear(self):
        for child in self.children:
            child.destroy()

class MainMenu(View):
    def __init__(self, master, go_keys, go_e, go_d):
        super().__init__()
        self.children = [
             tkinter.Button(master, text="Generate Public and Private Key", command=go_keys),
             tkinter.Button(master, text="Encrypt Text", command=go_e),
             tkinter.Button(master, text="Decrypt Text", command=go_d),
        ]
        for child in self.children:
            child.pack()

class GetKeys(View):
    def generate(self):
        filedir = filedialog.askdirectory(title="Save in...")
        print(filedir)
        public, private = generate_keys()
        with open('{}/public.key'.format(filedir), 'w') as f:
            f.write(public)
        with open('{}/private.key'.format(filedir), 'w') as f:
            f.write(private)

    def __init__(self, master, back):
        super().__init__()
        self.children = [
            tkinter.Button(master, text="Back", command=back),        
            tkinter.Button(master, text="Keys", command=self.generate),
        ]
        for child in self.children:
            child.pack()

class Encrypt(View):
    def __init__(self, master, back):
        super().__init__()
        self.children = [
            tkinter.Button(master, text="Back", command=back),        
        ]
        for child in self.children:
            child.pack()

class Decrypt(View):
    def __init__(self, master, back):
        super().__init__()
        self.children = [
            tkinter.Button(master, text="Back", command=back),        
        ]
        for child in self.children:
            child.pack()
