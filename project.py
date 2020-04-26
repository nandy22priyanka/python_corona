import tkinter as tk
import csv
from tkinter import messagebox
window=tk.Tk()
window.title("COVID-ALERT")
entry=tk.Entry(window)
entry.pack()
window.geometry("1020x1020")
tk.Label(text="Welcome!!")
cssv=open('covid_19_india.csv')
lines=cssv.readlines()
def button_click():
    count=0
    t=entry.get()
    if t=="":
        messagebox.showinfo("Oops!!!!","You did'nt enter the location!")
    else:
        k=0
        for i in range(1,1223,1):
            txt=lines[i].split(",")
            if t==txt[3]:
                count=1
                k=int(k)+int(txt[8])
        if count!=0:
            if k==0:
                messagebox.showinfo("Alert",t+" is a safe area with"+str(k)+"cases")
            if k<15:
                messagebox.showinfo("Alert!!",t+" is under moderate danger.\nYou are in orange zone.\nThere are total"+str(k)+"cases.")
            if k>15:
                messagebox.showinfo("Alert",t+" is having exploding no. of Covid-19 cases.\nYou are in red zone.\nThere are total "+str(k)+"cases.")
button=tk.Button(window,text="Submit",fg="white",bg="black",command=button_click)
button.pack()
label1=tk.Label(window,text="Enter your State.\n",font=("Charcoal",23,"bold"))
label2=tk.Label(window,text="#example:Assam,West Bengal,etc..i.",font=("Times",13,))
label1.pack()
label2.pack()
tk.Label(window,text="Stay at home,a wise man said.\n Vijay did'nt obey this and went out like a nicompoop.\nHe is dead now.\nDon't be like Vijay.",font=("Arial",30,"bold")).pack()
window.mainloop()
