from tkinter import *
from tkinter import messagebox as msb
from tkinter import filedialog as  fld

#Funkce pro otevření souboru
def Otevrit():
    try: 
        text.delete(1.0,END)
        cesta = fld.askopenfilename(title="Otevřít soubor")
        soubor = open(cesta,"r")
        for radek in soubor:
            text.insert(END,radek)
        soubor.close()
    except:
        pass

#Funkce pro ukládání souborů
def Ulozit():
    try:
        cesta = fld.asksaveasfilename(title="Uložit soubor",  defaultextension="txt")
        soubor = open(cesta,"r")
        retezec = text.get(1.0.END)
        soubor.write(retezec)
        soubor.close()
    except: pass

#Funkce pro konec aplikace
def Konec():
    x = msb.askyesno("Konec aplikace", "Opravdu chcete skončit?")
    if x: 
        hlavni.destroy()

#Funkce pro velká písmena
def Velka():
    a = text.get(1.0,END)
    a2 = a.upper()
    text.delete(1.0,END)
    text.insert(1.0,a2)

#Fuknce pro okno nahrazování znaků
def OknoNahrad():
    global vstup1, vstup2, oknoN
    oknoN = Toplevel()  #příkaz pro vnořené okno
    oknoN.title("Nahrazení znaku")

    t1 = Label(oknoN,text="Nahradit znak")
    t1.grid(padx=5,pady=5)
    vstup1 = Entry(oknoN,width=5)
    vstup1.grid(row=1,pady=10)

    t2 = Label(oknoN,text="Tímto znakem")
    t2.grid(row=0,column=1,padx=5,pady=5)
    vstup2 = Entry(oknoN,width=5)
    vstup2.grid(column=1,row=1,pady=10)

    tlacitko = Button(oknoN,text="Potvrdit",relief="raised",width=10,command=Nahradit)
    tlacitko.grid(row=2,columnspan=2)

#Funkce pro nahrazení znaku - nutno ošetřit vstupy
def Nahradit():
    puvodni = vstup1.get()
    novy = vstup2.get()
    sez_novy = list(novy)
    sez_puvodni = list(puvodni)
    a=0
    b=0
    for i in sez_novy:
        a = a+1
    for i in sez_puvodni:
        b = b+1
    if a == 1 and b == 1:
        retezec = text.get(1.0,END)
        retezec2 = retezec.replace(puvodni,novy)
        text.delete(1.0,END)
        text.insert(1.0,retezec2)
        oknoN.destroy()
    else:
        msb.showerror("Chyba","Zadejte prosím maximálně 1 znak!")

#Funkce pro zobrazení statisiky písmen
def Statistika():
    oknoS = Toplevel()
    oknoS.title("Statistika")
    texts = Text(oknoS,font="Arial 8", width=20, height=30)
    texts.pack(padx=3,pady=3)
    sez = []
    radky =text.get(1.0,END)
    radky=radky.lower()
    for radek in radky:
        for pismeno in radek:
            sez.append(pismeno)
    for i in abeceda:
        if i in sez:
            texts.insert(END,f"{i}:")
            texts.insert(END,str(sez.count(i)))
            texts.insert(END,"\n")
        else:
            texts.insert(END,f"{i}:0")
            texts.insert(END,"\n")
hlavni=Tk()
hlavni.protocol("WM_DELETE_WINDOW",Konec)

#pro statistiku
abeceda="abcdefghijklmnopqrstuvwxyz"

#vzhled aplikace
text=Text(hlavni,font="Arial 10")
text.pack()

hornimenu=Menu(hlavni)

menusoubor=Menu(hornimenu,tearoff=0)
menusoubor.add_command(label="Otevřít", command=Otevrit)
menusoubor.add_command(label="Uložit", command= Ulozit)
menusoubor.add_separator()
menusoubor.add_command(label="Konec",command=Konec)
hornimenu.add_cascade(label="Soubor",menu=menusoubor)

menuoperace=Menu(hornimenu,tearoff=0)
menuoperace.add_command(label="Velká písmena",command=Velka)
menuoperace.add_command(label="Nahradit znak",command=OknoNahrad)
menuoperace.add_command(label="Statistika znaků",command=Statistika)
hornimenu.add_cascade(label="Operace",menu=menuoperace)

hlavni.config(menu=hornimenu)




hlavni.mainloop()
