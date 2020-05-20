import pycipher
from tkinter import *

root = Tk()
root.title("Plaintext Encrypter")
root.iconbitmap('inkspot.ico')

plaintext = Entry(root, width=200)
plaintext.pack()
plaintext.insert(0, "Enter your text to encrypt...")

label = Label(root, text="Choose your Cipher Type:")
label.pack(anchor=W)
    
mainMenu = StringVar()
subMenu = StringVar()
transMenu = StringVar()
nomMenu = StringVar()
polyMenu = StringVar()
otherMenu = StringVar()
MAINOPTIONS = [("Substitution Ciphers", "Substitution"), ("Transposition Ciphers", "Transposition"), ("Nomenclature Ciphers", "Nomenclature"), ("Polyalphabetic Ciphers", "Polyalphabetic"), ("Other Ciphers", "Other")]
SUBMENU = [("Simple Substitution Cipher", "simple"), ("Atbash Cipher", "atbash"), ("Affine Cipher", "affine"), ("Playfair Cipher", "playfair"), ("Polybius Square Cipher", "polybius"), ("Baconian Cipher", "baconian"), ("Straddle Checkerboard Cipher", "checkerboard")] #baconian and straddle checkerboard not in pycipher
TRANSMENU = [("Rail-Fence Cipher", "rail-fence"), ("Columnar Transposition Cipher", "columnar"), ("ADFGVX Cipher", "adfgvx"), ("ADFGX Cipher", "adfgx"), ("Bifid Cipher", "bifid"), ("Trifid Cipher", "trifid")] # trifid cipher not in pycipher
NOMMENU = [("Nomenclature Cipher", "nomenclature"), ("Code Cipher", "code")] #neither of these are in pycipher
POLYMENU = [("Autokey Cipher", "autokey"), ("Vignere Cipher", "vignere"), ("Gronsfield Cipher", "gronsfield"), ("Beaufort Cipher", "beaufort"), ("Porta Cipher", "porta"), ("Running Key Cipher", "running key")] #running key cipher not in pycipher
OTHERMENU = [("ROT13 Cipher", "ROT13"), ("Caesar Cipher", "caesar"), ("Four-Square Cipher", "four-square"), ("Enigma M3 Cipher", "M3"), ("M-209 Cipher", "M-209"), ("Base64 Cipher", "base64"), ("Hill Cipher", "hill")] #Base64 and hill ciphers are not a part of pycipher

   

def calcSub(value):
    #label = Label(subFrame, text = "Substitution Cipher Features Coming Soon")
    #label.pack()
    if subMenu.get() == "simple":
        ciphertext = pycipher.SimpleSubstitution().encipher(plaintext.get())
        label = Label(subFrame, text = "Simple: " + ciphertext)
        label.pack(anchor=W)
    
    if subMenu.get() == "atbash":
        ciphertext = pycipher.Atbash().encipher(plaintext.get())
        label = Label(subFrame, text = "Atbash: " + ciphertext)
        label.pack(anchor=W)
    
    if subMenu.get() == "affine":
        a = 11 # *a* is an integer that has an inverse (mod 26), Allowable values for *a* are: 1,3,5,7,9,11,15,17,19,21,23,25
        b = 15 #*b* is an integer 0-25 
        ciphertext = pycipher.Affine(a, b).encipher(plaintext.get())
        label = Label(subFrame, text = "Affine: " + ciphertext)
        label.pack(anchor=W)
    
    if subMenu.get() == "playfair":
        ciphertext = pycipher.Playfair().encipher(plaintext.get())
        label = Label(subFrame, text = "Playfair: " + ciphertext)
        label.pack(anchor=W)
    
    if subMenu.get() == "polybius":
        ciphertext = pycipher.PolybiusSquare().encipher(plaintext.get())
        label = Label(subFrame, text = "Polybius Square: " + ciphertext)
        label.pack(anchor=W)
    
    if subMenu.get() =="baconian":
        label = Label(subFrame, text = "Baconian: This feature is in the works. Check back soon.")
        label.pack(anchor=W)
    
    if subMenu.get() == "checkerboard":
        label = Label(subFrame, text = "Checkerboard: This feature is in the works. Check back soon.")
        label.pack(anchor=W)
    
    
def calcTrans(value):
    if transMenu.get() == "rail-fence":
        ciphertext = pycipher.Railfence().encipher(plaintext.get())
        label = Label(transFrame, text = "Railfence: " + ciphertext)
        label.pack(anchor=W)
    
    if transMenu.get() == "columnar":
        ciphertext = pycipher.ColTrans().encipher(plaintext.get())
        label = Label(transFrame, text = "Columnar: " + ciphertext)
        label.pack(anchor=W)
    
    if transMenu.get() == "adfgvx":
        ciphertext = pycipher.ADFGVX().encipher(plaintext.get())
        label = Label(transFrame, text = "ADFGVX: " + ciphertext)
        label.pack(anchor=W)
    
    if transMenu.get() == "adfgx":
        ciphertext = pycipher.ADFGX().encipher(plaintext.get())
        label = Label(transFrame, text = "ADFGX: " + ciphertext)
        label.pack(anchor=W)
    
    if transMenu.get() == "bifid":
        ciphertext = pycipher.Bifid().encipher(plaintext.get())
        label = Label(transFrame, text = "Bifid: " + ciphertext)
        label.pack(anchor=W)
    
    if transMenu.get() == "trifid":
        label = Label(transFrame, text = "Trifid: This feature is in the works. Check back soon.")
        label.pack(anchor=W)

def calcNom(value):
    if nomMenu.get() == "nomenclature":
        label = Label(nomFrame, text = "Trifid: This feature is in the works. Check back soon.")
        label.pack(anchor=W)
    
    if nomMenu.get() == "code":
        label = Label(nomFrame, text = "Trifid: This feature is in the works. Check back soon.")
        label.pack(anchor=W)
    
    label = Label(nomFrame, text = "Nomenclature Cipher Features Coming Soon")
    label.pack()

def calcPoly(value):
    if polyMenu.get() == "autokey":
        ciphertext = pycipher.Autokey().encipher(plaintext.get())
        label = Label(polyFrame, text = "Autokey: " + ciphertext)
        label.pack(anchor=W)
        
    if polyMenu.get() == "vignere":
        ciphertext = pycipher.Vigenere().encipher(plaintext.get())
        label = Label(polyFrame, text = "Vignere: " + ciphertext)
        label.pack(anchor=W)
    
    if polyMenu.get() == "gronsfield":
        ciphertext = pycipher.Gronsfeld().encipher(plaintext.get())
        label = Label(polyFrame, text = "Gronsfield: " + ciphertext)
        label.pack(anchor=W)
    
    if polyMenu.get() == "beaufort":
        ciphertext = pycipher.Beaufort().encipher(plaintext.get())
        label = Label(polyFrame, text = "Beaufort: " + ciphertext)
        label.pack(anchor=W)
    
    if polyMenu.get() == "porta":
        ciphertext = pycipher.Porta().encipher(plaintext.get())
        label = Label(polyFrame, text = "Porta: " + ciphertext)
        label.pack(anchor=W)
    
    if polyMenu.get() == "running key":
        label = Label(polyFrame, text = "Running Key: This feature is in the works. Check back soon.")
        label.pack(anchor=W)

def calcOther(value):
    if otherMenu.get() == "ROT13":
        ciphertext = pycipher.Rot13().encipher(plaintext.get())
        label = Label(otherFrame, text = "ROT13: " + ciphertext)
        label.pack(anchor=W)
    
    if otherMenu.get() == "caesar":
        ciphertext = pycipher.Caesar().encipher(plaintext.get())
        label = Label(otherFrame, text = "Caesar: " + ciphertext)
        label.pack(anchor=W)
    
    if otherMenu.get() == "four-square":
        ciphertext = pycipher.Foursquare().encipher(plaintext.get())
        label = Label(otherFrame, text = "Base64: This feature is in the works. Check back soon.")
        label.pack(anchor=W)
        #label = Label(otherFrame, text = "Four-Square: " + ciphertext)
        #label.pack(anchor=W)
    
    if otherMenu.get() == "M3":
        ciphertext = pycipher.Enigma().encipher(plaintext.get())
        label = Label(otherFrame, text = "Enigma M3: " + ciphertext)
        label.pack(anchor=W)
    
    if otherMenu.get() == "M-209":
        ciphertext = pycipher.M209().encipher(plaintext.get())
        label = Label(otherFrame, text = "M-209: " + ciphertext)
        label.pack(anchor=W)
    
    if otherMenu.get() == "base64":
        label = Label(otherFrame, text = "Base64: This feature is in the works. Check back soon.")
        label.pack(anchor=W)
    
    if otherMenu.get() == "hill":
        label = Label(otherFrame, text = "Hill: This feature is in the works. Check back soon.")
        label.pack(anchor=W)
    

def submitMain(value):
    global subFrame, transFrame, nomFrame, polyFrame, otherFrame
    top = Toplevel()
    top.title(mainMenu.get())
    top.iconbitmap('inkspot.ico')
    
    subFrame = LabelFrame(top)
    transFrame = LabelFrame(top)
    nomFrame = LabelFrame(top)
    polyFrame = LabelFrame(top)
    otherFrame = LabelFrame(top)
    
    if mainMenu.get().lower() == "substitution":
        for text, cipher in SUBMENU:
            Radiobutton(top, text=text, variable=subMenu, value=cipher).pack(anchor=W)
        button = Button(top, text="Calculate CipherText", command=lambda: calcSub(subMenu.get()))
        button.pack()
        subFrame.pack()
    
    if mainMenu.get().lower() == "transposition":
        for text, cipher in TRANSMENU:
            Radiobutton(top, text=text, variable=transMenu, value=cipher).pack(anchor=W)
        button = Button(top, text="Calculate CipherText", command=lambda: calcTrans(transMenu.get()))
        button.pack()
        transFrame.pack()
            
    if mainMenu.get().lower() == "nomenclature":
        for text, cipher in NOMMENU:
            Radiobutton(top, text=text, variable=nomMenu, value=cipher, state='disabled').pack(anchor=W)
        button = Button(top, text="Calculate CipherText", command=lambda: calcNom(nomMenu.get()))
        button.pack()
        nomFrame.pack()
            
    if mainMenu.get().lower() == "polyalphabetic":
        for text, cipher in POLYMENU:
            Radiobutton(top, text=text, variable=polyMenu, value=cipher).pack(anchor=W)
        button = Button(top, text="Calculate CipherText", command=lambda: calcPoly(polyMenu.get()))
        button.pack()
        polyFrame.pack()
            
    if mainMenu.get().lower() == "other":
        for text, cipher in OTHERMENU:
            Radiobutton(top, text=text, variable=otherMenu, value=cipher).pack(anchor=W)
        button = Button(top, text="Calculate CipherText", command=lambda: calcOther(otherMenu.get()))
        button.pack()
        otherFrame.pack()
            
for text, cipher in MAINOPTIONS:
    Radiobutton(root, text=text, variable=mainMenu, value=cipher).pack(anchor=W)
    
button = Button(root, text="Submit", command=lambda: submitMain(mainMenu.get()))
button.pack()




root.mainloop()


