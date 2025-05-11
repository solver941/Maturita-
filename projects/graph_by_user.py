#Graf vytvřený podle zadání uživatele
from tkinter import * 
from tkinter import colorchooser as clr
from tkinter import messagebox as msb
import pylab as py 


#Frunkce pro ukládání zadaných souřadnic do seznamů
def Uloz():
    try:
        global x_ove
        global y_ove
        x_ove.append(float(bodx.get()))
        y_ove.append(float(body.get()))
        vstupx.delete(0,END)
        vstupx.focus_set()
        vstupy.delete(0,END)
        vypis.delete(1.0,END)
        vypis.insert(1.0,"x: ")
        vypis.insert(END,x_ove)
        vypis.insert(END,"\n")
        vypis.insert(END,"y: ")
        vypis.insert(END,y_ove)
    except: 
        msb.showerror("Chyba!","Chyba na vstupu!\nZadejte prosím číslo")
        vstupx.delete(0,END)
        vstupx.focus_set()
        vstupy.delete(0,END)


def Graf():
    x = py.array(x_ove)
    y = py.array(y_ove)

    tl = int(tloustka.get())

    py.plot(x,y,color=b,linewidth=tl)
    if vstupg.get() != "":
        py.title(vstupg.get())
    if vstupox.get() != "":
        py.xlabel(vstupox.get())
    if vstupoy.get() != "":
        py.ylabel(vstupoy.get())
    if m.get():
        py.grid(True)

    py.show()

#Funkce ori výběr barvy
def Barva():
    global b
    col = clr.askcolor(title="Výběr barvy")
    b = col[1]
    zobrbarvy["bg"] = b

#Funkce pro vymazání dat
def Smazat():
     global b, x_ove, y_ove
     vstupx.delete(0,END)
     vstupx.focus_set()
     vstupy.delete(0,END)
     vypis.delete(1.0,END)
     
     x_ove = []
     y_ove = []

    
     vstupg.delete(0,END)
     vstupox.delete(0,END)
     vstupoy.delete(0,END)

     tloustka.set("1")
     m.set(FALSE)
     b = "black"
     zobrbarvy["bg"] = "black"

#Funkce pro ukončení aplikace


def Konec():
    global oprchcete
    oprchcete = Tk()
    oprchcete.title("")
    areyousure = Label(oprchcete,text="Are you sure you want to exit?")
    areyousure.grid(columnspan=2)

    ano = Button(oprchcete,text="Yes", command = Ano)
    ano.grid(row=1,column=0)

    ne = Button(oprchcete,text="No", command = Ne)
    ne.grid(row=1,column=1)
    oprchcete.mainloop()

def Ano():
    oprchcete.destroy()
    hlavni.destroy()

def Ne():
    oprchcete.destroy()
 

hlavni = Tk()
hlavni.title("Grafy")

#proměnné pro souřadnice 
bodx = StringVar()
body = StringVar()
x_ove = []
y_ove = []
b = "black"     #nastavení výchozí barvy grafu


#Vzhled aplikace - zadávání souřadnic

ram = LabelFrame(hlavni,text="Zadání souřadnic",bd=2,relief="ridge",padx=5,pady=5)
ram.pack(padx=5,pady=5)

popis1 = Label(ram,text="Souřadnice x",font="Calibri 10")
popis1.grid(pady=3)

vstupx = Entry(ram,font="Calibri 10",textvariable=bodx)
vstupx.grid(row=0,column=1,pady=3)

popis2 = Label(ram,text="Souřadnice y",font="Calibri 10")
popis2.grid(row=1,pady=3)
vstupy = Entry(ram,font="Calibri 10",textvariable=body)
vstupy.grid(row=1,column=1,pady=3)

uloz = Button(ram,text="Ulož a další",width=15,font="Calibri 12",command=Uloz)
uloz.grid(row=2,columnspan=2,pady=10)

vypis = Text(hlavni,height=4,width=50)
vypis.pack()

#Pro vlastnosti grafu
ram2=LabelFrame(hlavni,text="Parametry grafu",bd=2,relief="ridge",padx=5,pady=5)
ram2.pack(padx=10,pady=10)

popisg=Label(ram2,text="Název grafu",font="Calibri 10")
popisg.grid(pady=3)
vstupg=Entry(ram2,font="Calibri 10")
vstupg.grid(row=0,column=1)

popisox=Label(ram2,text="Název osy x",font="Calibri 10")
popisox.grid(row=1,pady=3)
vstupox=Entry(ram2,font="Calibri 10")
vstupox.grid(row=1,column=1,pady=3)

popisoy=Label(ram2,text="Název osy y",font="Calibri 10")
popisoy.grid(row=2,pady=3)
vstupoy=Entry(ram2,font="Calibri 10")
vstupoy.grid(row=2,column=1,pady=3)

tloustka=StringVar()
tloustka.set("1")
popisc=Label(ram2,text="Tloušťka čáry",font="Calibri 10")
popisc.grid(row=3,column=0,pady=3)
cara=Spinbox(ram2,from_=1,to=10,textvariable=tloustka,font="Calibri 10",width=15)
cara.grid(row=3,column=1)

m=BooleanVar()
mrizka=Checkbutton(ram2,text="Mřížka",font="Calibri 10",variable=m)
mrizka.grid(row=4,column=0,pady=3)

barva=Button(ram2,text="Barva čáry",font="Calibri 10",width=15,command=Barva)
barva.grid(row=5,column=0,pady=3)
zobrbarvy=Label(ram2,width=3,height=1,bg=b,relief="sunken")
zobrbarvy.grid(row=5,column=1,pady=3)

vymazat=Button(ram2,text="Vymazat vše",bg="FireBrick",font="Bold 10",width=10,command=Smazat)
vymazat.grid(row=6,column=0,pady=3)

kresligraf = Button(hlavni,text="Vyresli graf",width=15, font="Calibri 12 bold",command=Graf)
kresligraf.pack(pady=10)

konec = Button(hlavni,text="Konec",font="Arial 10 bold",bg="OrangeRed",command=Konec)
konec.pack(pady=15)

hlavni.mainloop()
