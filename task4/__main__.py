import tkinter
from views import MainMenu, GetKeys, Encrypt, Decrypt

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
