import tkinter

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
    def __init__(self, master, back):
        super().__init__()
        self.children = [
            tkinter.Button(master, text="Back", command=back),        
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

class MainLoopClass():
    top = tkinter.Tk()

    def __init__(self):
        self.top.geometry("800x480")
        self.go_menu()
        self.top.mainloop()

    def clear(self):
        if hasattr(self,'children'):
            self.children.clear()

    def go_menu(self):
        self.clear()
        self.children = MainMenu(self.top, self.go_keys, self.go_encrypt, self.go_decrypt)

    def go_keys(self):
        self.clear()
        self.children = GetKeys(self.top, self.go_menu)

    def go_encrypt(self):
        self.clear()
        self.children = Encrypt(self.top, self.go_menu)

    def go_decrypt(self):
        self.clear()
        self.children = Decrypt(self.top, self.go_menu)

if __name__ == '__main__':
    main = MainLoopClass()
