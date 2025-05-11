from tkinter import * 
from tkinter import messagebox
import random as rn

#Fuknce pro generaci příkladů
def Generuj():
    global vysledek, tlacitko
    tlacitko["state"] = DISABLED
    tlacitko2["state"] = NORMAL
    uzivatel.set("")
    kontola["text"] = ""

    operace = clicked.get()

    #Příklad pro sčítání
    if operace == moznosti[0]:
        a = rn.randint(1,100)
        b = rn.randint(1,100-a)
        priklad["text"] = f"{a} + {b}"
        vysledek = a+b

    #Příklad pro odčítání
    elif operace == moznosti[1]:
        a = rn.randint(1,100)
        seznam = []
        for i in range(1,101):
            seznam.append(i)
        mensineza = []
        for i in seznam:
            if i <= a:
                mensineza.append(i)
        b = rn.choice(mensineza)
        priklad["text"] = f"{a} - {b}"
        vysledek = a-b

    #Příklad pro násobení
    elif operace == moznosti[2]:
        a = rn.randint(1,10)
        b = rn.randint(1,10)
        priklad["text"] = f"{a} × {b}"
        vysledek = a*b

    #Příklad pro dělení
    else:
        vhodni_delitele = []
        pocet = 0
        while pocet == 0:
            a = rn.randint(1,100)
            seznam = []
            for i in range(1,11):
                seznam.append(i)
            for i in seznam:
                if a%i == 0 and a/i <= 10:
                    vhodni_delitele.append(i)
            for i in vhodni_delitele:
                pocet += 1
        b = rn.choice(vhodni_delitele)
        priklad["text"] = f"{a} ÷ {b}"
        vysledek = a/b

spravne =0
spatne = 0

#Funkce pro kontrolu správnosti výsledku
def Kontrola():
        global spravne, spatne, tlacitko
        try:
            uz = int(uzivatel.get())
            try:
                if vysledek == uz:
                    kontola["text"] = "Správně!"
                    kontola["bg"] = "lime"
                    spravne += 1
                else:
                    kontola["text"] = f"Špatně! Správný výsledek: {vysledek}"
                    kontola["bg"] = "red"
                    spatne += 1
                tlacitko["state"] = NORMAL
                tlacitko2["state"] = DISABLED
            except:
                messagebox.showerror("Chyba!","Vyberte prosím operaci a stiskněte GENERUJ PŘÍKLAD.")
        except:
            messagebox.showerror("Chyba!","Zadejte prosím číslo")

#Funkce pro ukončení aplikace a zobrazení výsledného hodnocení
def Konec():
    celkem = spatne + spravne
    procentospravne = (spravne/celkem) * 100
    messagebox.showinfo("Hodnocení",f"Z {celkem} výsledků jste odpověděli {spravne} správně a {spatne} špatně. \n Vaše úspěšnost je tedy {round(procentospravne,2)}%")

    
    
    hlavni.destroy()

#Vzhled aplikace
hlavni = Tk()
hlavni.geometry("200x260")
hlavni.title("Příklady")

hlavni.config( bg="lightblue")

nadpis = Label(hlavni, text="Generátor příkladů", font="Arial 15",bg="lightblue")
nadpis.pack()

moznosti = ["Sčítání", "Odčítání", "Násobení", "Dělení"]
clicked = StringVar()
clicked.set(moznosti[0])
dropdown = OptionMenu(hlavni, clicked, *moznosti)
dropdown.config(bg="violet")
dropdown["menu"].config(bg="lightblue")
dropdown.pack()

tlacitko = Button(hlavni,text="Generuj příklad",command=Generuj,bg="gray")
tlacitko.pack(pady=5)

priklad = Label(hlavni,text="",bg="lightblue")
priklad.pack()

text = Label(hlavni, text="Zadejte výsledek: ",bg="lightblue").pack()

uzivatel = StringVar()
vstup = Entry(hlavni,textvariable=uzivatel).pack()

tlacitko2 = Button(hlavni,text="Kontrola",command=Kontrola,width=8,height=2)
tlacitko2.pack(pady=10)

kontola = Label(hlavni,text="",bg="lightblue")
kontola.pack()

konec = Button(hlavni,text="Konec",command=Konec).pack()

hlavni.mainloop()