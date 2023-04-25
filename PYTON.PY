from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

Label(root, text="Mohammed Waleed Registration Form", font="arial 15 bold").grid(row=0, column=3)
#field name
name= Label(root, text="Name")
phone= Label(root, text="Phone")
gender= Label(root, text="Gender")
age= Label(root, text="Age")
paymentmood= Label(root, text="Payment Mood")
#packing fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
age.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)
#Variable for stroing data
nameValue = StringVar
phoneValue = StringVar
genderValue = StringVar
ageValue = StringVar
paymentmoodValue = StringVar
checkvalue = IntVar
#Entry fields
nameentry = Entry(root, textvariable=nameValue)
phoneentry = Entry(root, textvariable=phoneValue)
genderentry = Entry(root, textvariable=genderValue)
ageentry = Entry(root, textvariable=ageValue)
paymentmoodentry = Entry(root, textvariable=paymentmoodValue)
#packing the entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
ageentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

#Creating check box
checkbtn = Checkbutton(text=  "remember me?", variable= checkvalue)
checkbtn.grid(row=6, column= 3)

#Sumbit button
Button(text="Sumbit", command=getvals).grid(row=7,column=3)

root.mainloop()