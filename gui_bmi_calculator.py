from tkinter import *

def BMI(height, weight):
    bmi = (float(weight) * 703)/(float(height) ** 2)
    if bmi<= 18.5:
        return f"Your BMI is {bmi} (Underweight)"
    elif bmi >= 18.5 and bmi < 25:
        return f"Your BMI is {bmi} (Normal)"
    else:
        return f"Your BMI is {bmi} (Overweight)"

def display_bmi():
    l3 = Label(root, text = BMI(e1.get(), e2.get()), padx = 45)
    l3.grid(row = 3, column = 0)
    e1.delete(0,END)
    e2.delete(0,END)

    
root = Tk()

root.title("BMI calculator")

l1 = Label(root, text = "Enter your height(inches):",padx = 45)
l1.grid(row = 0, column = 0)

e1 = Entry(root)
e1.grid(row = 0, column = 1)

l2 = Label(root, text = "Enter your weight (pounds)")
l2.grid(row = 1, column = 0, padx = 45)

e2 = Entry(root)
e2.grid(row = 1, column = 1)

b = Button(root, text = "calculate BMI", command = display_bmi)
b.grid(row =2, column = 1)
root.mainloop()
