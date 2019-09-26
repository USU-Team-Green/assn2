import tkinter

top = tkinter.Tk()

topChildren = []

genKeys = tkinter.Button(top, text="Generate Public and Private Key")
topChildren.append(genKeys)

encrypt = tkinter.Button(top, text="Encrypt Text")
topChildren.append(encrypt)

decrypt = tkinter.Button(top, text="Decrypt Text")
topChildren.append(decrypt)

for child in topChildren:
    child.pack()

top.mainloop()
