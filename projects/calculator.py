import tkinter as tk

# Funkce pro přidávání znaků na obrazovku kalkulačky
def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

# Funkce pro vymazání obrazovky
def clear():
    entry.delete(0, tk.END)

# Funkce pro výpočet výsledku
def calculate():
    try:
        result = eval(entry.get())  # použijeme eval pro výpočet výrazu
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Chyba")

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Kalkulačka")

# Vytvoření textového pole pro zobrazení výrazu a výsledku
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Tlačítka kalkulačky
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Vytvoření tlačítek
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=calculate)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: click(t))
    button.grid(row=row, column=col)

# Tlačítko pro vymazání
clear_button = tk.Button(root, text="Clear", width=5, height=2, font=('Arial', 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=2)

# Spuštění hlavní smyčky aplikace
root.mainloop()
