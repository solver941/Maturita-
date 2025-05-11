import tkinter as tk
from tkinter import CENTER, ttk
from time import strftime
from time import gmtime


root = tk.Tk()
root.title("Timer")
root.geometry("1500x600")


class Timer():
    def __init__(self):
        self.time_period = 380
        self.time_left = self.time_period
        self.phase = "First"

        controls = tk.Frame(root)
        controls.pack(pady=20)
        self.progress_bar()   
        
        self.label = tk.Label(controls, text=str(strftime("%M:%S", gmtime(self.time_left))), font=("Helvetica", 60, "bold"), fg="#333")
        self.label.grid(row=1, column=5, pady=10)

        countdown_button = tk.Button(controls, text="▶ Start Timer", bg="#4CAF50", fg="white", font=("Helvetica", 14), width=15, command=self.countdown)
        countdown_button.grid(row=2, column=5, pady=5)

        reset_button = tk.Button(controls, text="⏹ Reset Timer", bg="#f44336", fg="white", font=("Helvetica", 14), width=15, command=self.reset_timer)
        reset_button.grid(row=3, column=5, pady=5)

        
        self.progressbar = ttk.Progressbar(controls, maximum=100, length=400)
        self.progressbar["value"] = progress
        self.progressbar.grid(row=4, column=5, ipadx=200, ipady=10, pady=10)

        phases = tk.Frame(root)
        phases.place(relx=.5, rely=.7,anchor= CENTER)
        self.first_phase = tk.Label(phases, text="First \nphase", background="green", height=4, width=10, font=("Helvetica 20 bold"), borderwidth=5, relief="groove")
        self.first_phase.grid(row=10, column=1, padx=10)

        self.second_phase = tk.Label(phases, text="Second \nphase", height=4, width=10,font=("Helvetica 20 bold"), borderwidth=5, relief="groove")
        self.second_phase.grid(row=10, column=2, padx=10)

        self.third_phase = tk.Label(phases, text="Third \nphase", height=4, width=10,font=("Helvetica 20 bold"), borderwidth=5, relief="groove")
        self.third_phase.grid(row=10, column=3, padx=10)

    def countdown(self):
        global time_left
        global progress
        global phase
        if self.time_left > 0:
            self.time_left -= 1
            progress -= unit
            print(progress)
            self.progressbar.step(-unit)
            self.label.config(text=str(strftime("%M:%S", gmtime(self.time_left))))
            root.after(1000, self.countdown)
        else:
            if self.phase == "First":
                self.first_phase["background"] = "white"
                self.second_phase["background"] = "green"
                self.phase = "Second"
                print("End of phase 1")
                self.reset()
            elif self.phase == "Second":
                self.second_phase["background"] = "white"
                self.third_phase["background"] = "green"
                self.phase = "Third"
                self.reset()
            else:
                self.label.config(text="Time's up!")



    def reset(self):
        global time_left
        self.time_left = self.time_period
        self.progressbar["value"] = 100
        self.progress_bar()
        self.countdown()

    def reset_timer(self):
        global time_left
        self.time_left = self.time_period
        self.phase = "First"
        self.progressbar["value"] = 100
        self.first_phase.config(background="green")
        self.second_phase.config(background="white")
        self.third_phase.config(background="white")
        self.label.config(text=str(strftime("%M:%S", gmtime(self.time_left))))
        self.progress_bar()
        

    def progress_bar(self):
        global unit
        global progress
        progress = 100
        unit = 100/self.time_left


timer = Timer()
root.mainloop()
