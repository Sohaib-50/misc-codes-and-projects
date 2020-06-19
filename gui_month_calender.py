##TO DO:
#1) alter code so that input for month and year is taken in a gui window and not on terminal.

from tkinter import *
from calender import monthrange, month_name
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def cal(year, month):
    

    
    calender = Tk()

    header = Label(calender, text = f"{month_name[month]}, {(lambda year: year if year >=0 else f'{year * -1} AD')(year)}", font = ("Arial", 35, "bold"))
    header.grid(row = 0, column = 0)

    sub_calender = Frame(calender, relief = RAISED, border = 10)
    sub_calender.grid(row = 1, column = 0)

    #inside = Tk(calender)

    for i, day in enumerate(days):

        day_label = Label(sub_calender, text = day[:3], font = ("Arial", 20), padx = "10p")

        day_label.grid(row = 1, column = i)

    first_day, num_days = monthrange(year,month)

    date_row = 2

    day_of_week = first_day
    
    for i in range(1, num_days  +1):

        date_column = day_of_week % 7

        
        out_date = Label(sub_calender, text = str(i), font = ("Arial", 20))

        out_date.grid(row = date_row, column = date_column)

        day_of_week += 1

        if date_column == 6:
            date_row += 1


    calender.mainloop()
    
year = int(input('year: '))
month = int(input('month: '))
cal(year, month)
