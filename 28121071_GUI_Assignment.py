import tkinter as tk
from tkinter import ttk
from math import *
from winsound import *


def audio():
    audio = lambda: PlaySound('sound.wav', SND_FILENAME)


def cal_sal():
    name = fName.get()
    sName = lName.get()
    salary = eval(gSalary.get())

    thresh2 = in_thresh = 2
    thresh3 = in_thresh = 3
    thresh4 = in_thresh = 4

    nis_tax = 0.025
    nht_tax = 0.02
    edu_tax = 0.0225
    in_tax = 0.25

    thresh_monthly = 42276

    nis = nis_tax * salary
    stat = salary - nis

    nht = nht_tax * salary

    edu = stat * edu_tax

    paye = 0

    if stat > thresh_monthly:
        incom = (stat - thresh_monthly) * in_tax
        paye = incom

    netPay = salary - (nis + nht + edu + paye)
    tax_total = (nis + nht + edu + paye)
    Nis.set(str(nis))
    Nht.set(str(nht))
    edTax.set(str(edu))
    Paye.set(str(paye))
    net.set(str(netPay))
    taxTotal.set(str(tax_total))


def display():
    label = ttk.Label(win, width=15, text=fName.get(), justify='left', font="times 18 bold", background='#856ff8')
    label.grid(column=0, row=9, columnspan=2)
    label = ttk.Label(win, width=15, text=lName.get(), justify='left', font="times 18 bold", background='#856ff8')
    label.grid(column=1, row=9, )
    label = ttk.Label(win, width=15, text='Net Salary is', justify='right', font="times 18 bold", background='#856ff8')
    label.grid(column=1, row=9, columnspan=2)
    label = ttk.Label(win, width=15, text=net.get(), justify='left', font="times 18 bold", background='#856ff8')
    label.grid(column=2, row=9, columnspan=3)


win = tk.Tk()
from PIL import ImageTk, Image

fName = tk.StringVar()
lName = tk.StringVar()
gSalary = tk.StringVar()

# Button audio
audio = lambda: PlaySound('sound.wav', SND_FILENAME)

payroll = ttk.Label(win, text='Employee Pay Roll', font="times 40 bold", background='#856ff8')
payroll.grid(column=1, row=0, padx=20, pady=20, columnspan=2)

# Display image
img = ImageTk.PhotoImage(Image.open("mypic.png"))
imglabel = ttk.Label(win, image=img).grid(row=1, column=2, columnspan=3, rowspan=3)

fName = ttk.Label(win, width=15, text="First Name:", justify='left', font="times 18 bold", background='#856ff8')
fName.grid(column=0, row=1)

fName = tk.StringVar()
fName_entered = ttk.Entry(win, width=30, textvariable=fName)
fName_entered.grid(column=1, row=1)

lName = ttk.Label(win, width=15, text="Last Name:", justify='left', font="times 18 bold", background='#856ff8')
lName.grid(column=0, row=2)

lName = tk.StringVar()
lName_entered = ttk.Entry(win, width=30, textvariable=lName)
lName_entered.grid(column=1, row=2)

gSalary = ttk.Label(win, width=15, text="Gross Salary:", justify='left', font="times 18 bold", background='#856ff8')
gSalary.grid(column=0, row=3)

gSalary = tk.StringVar()
gSalary_entered = ttk.Entry(win, width=30, textvariable=gSalary)
gSalary_entered.grid(column=1, row=3)

button = tk.Button(win, text="Calculate Net Salary", justify='center', font="times 20 bold")
button.grid(column=0, row=4, columnspan=3, padx=25, pady=12)
button.config(command=lambda: [audio(), cal_sal(), display()])

payAdviceLabel = ttk.Label(win, text="Pay Advice", justify='left', font="times 18 bold", background='#856ff8')
payAdviceLabel.grid(column=0, row=5, columnspan=3, padx=25, pady=12)

nisLabel = ttk.Label(win, width=15, text='NIS Amount', justify='left', font="times 18 bold", background='#856ff8')
nisLabel.grid(column=0, row=6, padx=25, pady=12)

Nis = tk.StringVar()
nis_entered = ttk.Entry(win, width=20, textvariable=Nis, state='disabled')
nis_entered.grid(column=1, row=6)

nhtLabel = ttk.Label(win, width=15, text='NHT Amount', justify='left', font="times 18 bold", background='#856ff8')
nhtLabel.grid(column=2, row=6, padx=25, pady=12)

Nht = tk.StringVar()
nht_entered = ttk.Entry(win, width=20, textvariable=Nht, state='disabled')
nht_entered.grid(column=4, row=6, columnspan=3)

edTaxLabel = ttk.Label(win, width=15, text='Education Tax', justify='left', font="times 18 bold", background='#856ff8')
edTaxLabel.grid(column=0, row=7, padx=25, pady=12)

edTax = tk.StringVar()
edTax_entered = ttk.Entry(win, width=20, textvariable=edTax, state='disabled')
edTax_entered.grid(column=1, row=7)

payeLabel = ttk.Label(win, width=15, text='PAYE', font="times 18 bold", background='#856ff8')
payeLabel.grid(column=2, row=7, padx=25, pady=12)

Paye = tk.StringVar()
paye_entered = ttk.Entry(win, width=20, textvariable=Paye, state='disabled')
paye_entered.grid(column=4, row=7, columnspan=3)

taxTotalLabel = ttk.Label(win, width=15, text='Total Tax', justify='left', font="times 18 bold", background='#856ff8')
taxTotalLabel.grid(column=0, row=8, padx=25, pady=12)

taxTotal = tk.StringVar()
taxTotal_entered = ttk.Entry(win, width=20, textvariable=taxTotal, state='disabled')
taxTotal_entered.grid(column=1, row=8)

netLabel = ttk.Label(win, width=15, text='Net Pay', font="times 18 bold", justify='left', background='#856ff8')
netLabel.grid(column=2, row=8, padx=25, pady=12)

net = tk.StringVar()
net_entered = ttk.Entry(win, width=30, textvariable=net, state='disabled')
net_entered.grid(column=3, row=8, columnspan=2)

win.configure(background="#856ff8")
win.mainloop()
