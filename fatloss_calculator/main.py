from tkinter import *

window = Tk()
window.title("Fat Loss Calculator")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

def calcul(weight, deficit):
    weightlbs = round(weight * 2.2)
    fatcal = weightlbs * 3500
    zile = round(fatcal/deficit)
    rezultat = Label(text=f"Vei obtine rezultatul in {zile} zile, aproximativ {round(zile/30)} luni", pady=10)
    rezultat.grid(columnspan=2, row=3)

def button_pressed():
    weight1 = weight.get()
    deficit1 = deficit.get()
    calcul(int(weight1), int(deficit1))

wlabel = Label(text="Cate kg vrei sa slabesti?")
weight = Entry(width=5)
wlabel.grid(column=0, row=1)
weight.grid(column=1, row=1)

dlabel = Label(text="Cat de mare e deficitul caloric?")
deficit = Entry(width=5)
dlabel.grid(column=0, row=2, pady=10)
deficit.grid(column=1, row=2, pady=10)


buton = Button(text="Calculeaza", command=button_pressed)
buton.grid(column=1, row=5)




window.mainloop()
