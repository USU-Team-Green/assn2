import tkinter 
from tkinter import filedialog


from key_gen import generate_keys, encrypt, decrypt

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
    def encryptButton(self):
        self.m = self.entry.get()
        cipher = encrypt(self.m, self.n, self.e)
        self.resultText.insert(0,cipher)
        self.resultText.config(state='readonly')

    def readKey(self, rawstringpublic):
        self.n, self.e = rawstringpublic.split('$')
        self.n = int(self.n)
        self.e = int(self.e)


    def retrieve(self):
        filedirpub = filedialog.askopenfilename(title="Find Public Key File...")
        contentspub = ''
        with open('{}'.format(filedirpub), 'r') as f:
            contentspub = f.read()

        self.readKey(contentspub)
    def __init__(self, master, back):
        super().__init__()
        self.m = ''
        self.n = ''
        self.e = ''
        
        self.resultText = tkinter.Entry(master)
        self.entry = tkinter.Entry(master)
        self.children = [
            tkinter.Button(master, text="Back", command=back),        
            tkinter.Button(master, text="get key", command=self.retrieve),
            tkinter.Button(master, text="Encrypt", command=self.encryptButton),        
            tkinter.Label(master, text="Plain Text"),
            self.entry,
            tkinter.Label(master, text="Result"),
            self.resultText
        ]
        for child in self.children:
            child.pack()

class Decrypt(View):
    def decryptButton(self):
        self.c = self.entry.get()
        result = decrypt(self.c, self.n, self.d)
        self.resultText.insert(0,result)
        self.resultText.config(state='readonly')

    def readKey(self, rawstringprivate, rawstringpublic):
        self.n, self.e = rawstringpublic.split('$')
        self.n = int(self.n)
        self.e = int(self.e)
        self.d = int(rawstringprivate)

    def retrieve(self):
        filedirpub = filedialog.askopenfilename(title="Find Public Key File...")
        filedirpriv = filedialog.askopenfilename(title="Find Private Key File...")
        contentspub = ''
        contentspriv = ''
        with open('{}'.format(filedirpub), 'r') as f:
            contentspub = f.read()
        with open('{}'.format(filedirpriv), 'r') as f:
            contentspriv = f.read()

        self.readKey(contentspriv, contentspub)

    def __init__(self, master, back):
        super().__init__()
        self.n = ''
        self.e = ''
        self.c = ''
        self.d = ''
        self.resultText = tkinter.Entry(master)
        self.entry = tkinter.Entry(master)
        self.children = [
            tkinter.Button(master, text="Back", command=back),        
            tkinter.Button(master, text="get key", command=self.retrieve),
            tkinter.Button(master, text="Decrypt", command=self.decryptButton),        
            tkinter.Label(master, text="Cipher Text"),
            self.entry,
            tkinter.Label(master, text="Result"),
            self.resultText
        ]
        for child in self.children:
            child.pack()
