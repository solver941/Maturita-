#Grafy ze souboru

from tkinter import *
from tkinter import filedialog as fld 
from tkinter import messagebox as msb 
import pylab as py 

#Funkce pro výběr souboru z disku
def Vybersoubor():
    global cesta
    cesta = fld.askopenfilename(title= "Vyberte soubor")
    if cesta != "":
        souborcesta.set(cesta)

#Funkce pro čtení ze souboru a vyktreslení grafu
def Fcesoubor():
    try:
        with open(cesta,"r") as soubor:
            nazev = soubor.readline()
            osaX = soubor.readline()
            osaY = soubor.readline()
            cislaX = []
            cislaY = []
            while True:
                radek = soubor.readline()   #cislo1 cislo2
                if radek =="":
                    break
                cisla = radek.split()   #["cislo1","cislo2"]     -   převede jednotlivá slova stringu do seznamu
                cislaX.append(float(cisla[0]))
                cislaY.append(float(cisla[1]))
        x = py.array(cislaX)
        y = py.array(cislaY)    #Převede seznam na vektor
        py.plot(x,y)            #Vykreslí graf
        py.title(nazev)         #Doplní název
        py.xlabel(osaX)
        py.ylabel(osaY)         #Doplní názvy os
        py.show()               #Zobrazí graf
    except:
        msb.showerror("Chyba!","Graf se nepodařilo vytvořit \n Zkountrolujte formát souboru")
hlavni = Tk()
hlavni.title("Graf ze souboru")
#Vzhled aplikace 
ram = LabelFrame(hlavni,text="Graf ze souboru", bd=2,relief="ridge")
ram.pack(padx=5,pady=5)

souborcesta = StringVar() 
vstupgraf = Entry(ram,width=20,textvariable=souborcesta)
vstupgraf.pack(padx=5,pady=5)

otevrit = Button(ram,text="Vyber soubor pro graf",width=20,command=Vybersoubor)
otevrit.pack(padx=5,pady=5)

vytvorgraf = Button(hlavni,text="Vytvoř graf",width=15,height=5,command=Fcesoubor)
vytvorgraf.pack(padx=5,pady=5)

hlavni.mainloop()