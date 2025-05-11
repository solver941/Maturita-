from tkinter import * 
from tkinter import messagebox as msb

#Přiřazení hodnot ke mněnám
kurzy = {
    "EUR" : 25.12,
    "USD" : 24.14,
    "GBP" : 30.34,
    "AUD" : 15.31
         }

#Funkce pro vpřevod na kč, výpočet poplatku a výsledné hodnoty
def Spocitat():
    try:
        mena = mena_v.get()
        castka_mena = float(castka.get())
        np = vyber.get()

        if np == "nakup":
            vyplatit = (kurzy[mena] * castka_mena)
            poplatek = (kurzy[mena] * castka_mena) / 200 
            celkem = vyplatit - poplatek
            vystup["text"] = f" Základ : {round(vyplatit,2)}kč \n Poplatek : {round(poplatek,2)}kč \n Celková částka : {round(celkem,2)}kč \n --Částku vyplácí směnárna klientovi--"
        elif np =="prodej":
            zaplatit = (kurzy[mena] * castka_mena)
            poplatek = (kurzy[mena] * castka_mena) / 200 
            celkem = zaplatit + poplatek
            vystup["text"] = f"Základ : {round(zaplatit,2)}kč \n Poplatek : {round(poplatek,2)}kč \n Celková částka : {round(celkem,2)}kč \n --Částku platí klient směnárně--"
    except:
        msb.showerror("Chyba!","Zadejt prosím částku v požadované hodnotě (číslo).")

#Funkce pro zobrazení kurzovního lístku
def Listek():
    msb.showinfo("Kurzovní lístek","1 Euro =  25.12Kč \n 1 Americký dolar = 24.14Kč \n 1 Britská libra = 30.34Kč \n 1 Australský dolar = 15.31Kč")


#Vzhled aplikace
hlavni = Tk()

hlavni.geometry("250x400")
hlavni.title("Výpočty pro směnárnu")
hlavni.config(bg="lightgreen")

tlacitko2 = Button(hlavni,text="Kurzovní lístek",command=Listek,width=15,height=2,bg="pink",relief="raised").pack()

vyber = StringVar(value="nakup")
nakup = Radiobutton(hlavni, text="Nákup", variable=vyber, value="nakup",font="Arial 12",bg="lightgreen").pack()
prodej = Radiobutton(hlavni, text="Prodej", variable=vyber, value="prodej",font="Arial 12",bg="lightgreen").pack()


options = ["EUR","USD","GBP","AUD"]
mena_v = StringVar(value="EUR")
o_menu = OptionMenu(hlavni,mena_v,*options)
o_menu.pack(pady=5)
o_menu.config(bg="yellow")
o_menu["menu"].config(bg="pink")

text = Label(hlavni,text="Zadejte částku ve vybrané měně: ",font="bold 12",bg="lightgreen").pack()

castka = IntVar()
vstup = Entry(hlavni,textvariable=castka).pack(pady=3)

tlacitko = Button(hlavni, text="Spočítat",command=Spocitat).pack(pady=5)

ram = LabelFrame(hlavni,bd=3,cursor="hand2",labelanchor=NW,text="Výsledek",bg="#70e4a0")
ram.pack()
vystup = Label(ram,text="",bg="#70e4a0")
vystup.pack()


hlavni.mainloop()