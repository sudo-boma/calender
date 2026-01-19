from tkinter import *
import calendar

def showCal():
    try:
        fetch_year = int(year_field.get())
        new_gui = Toplevel()  # Use Toplevel instead of Tk() for new window
        new_gui.config(background="gray")
        new_gui.title("CALENDAR")
        new_gui.geometry("650x700")
        
        # Use calendar.calendar() function to get calendar for the year
        cal_content = calendar.calendar(fetch_year)
        cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold", justify=LEFT)
        cal_year.pack(padx=20, pady=20)
        
    except ValueError:
        # Show error message if input is not a valid number
        error_label = Label(gui, text="Please enter a valid year!", fg="red")
        error_label.grid(row=5, column=1)

if __name__ == "__main__":
    gui = Tk()
    gui.config(background="white")
    gui.title("CALENDAR")  # Fixed: gui.title() not gui_title()
    gui.geometry("300x200")  # Fixed: gui.geometry() not gui_geometry()
    
    # Title label
    cal = Label(gui, text="CALENDAR", bg="dark gray", font=("times", 28, 'bold'))
    
    # Year label
    year = Label(gui, text="Enter Year", bg="light green")
    
    # Year entry field
    year_field = Entry(gui)
    
    # Show Calendar button
    Show = Button(gui, text="Show Calendar", fg="Black", bg="Red", command=showCal)
    
    # Exit button
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=gui.destroy)
    
    # Grid layout
    cal.grid(row=1, column=1, pady=10)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1, pady=5)
    Show.grid(row=4, column=1, pady=5)
    Exit.grid(row=5, column=1, pady=5)
    
    gui.mainloop()