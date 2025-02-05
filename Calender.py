import calendar
import tkinter as tk
from tkinter import ttk, scrolledtext

def display_calendar():
    year = int(year_entry.get())
    cal_text.delete(1.0, tk.END)  # Clear previous output
    cal_text.insert(tk.INSERT, f"Calendar for the Year {year}\n\n")
    
    for quarter in range(0, 12, 4):  # Display months in horizontal sequence
        month_names = [calendar.month_name[m].center(20, ' ') for m in range(quarter+1, quarter+5)]
        cal_text.insert(tk.INSERT, "   ".join(month_names) + "\n")
        cal_text.insert(tk.INSERT, "-------------------------------------------------------------\n")
        
        month_cals = [calendar.monthcalendar(year, m) for m in range(quarter+1, quarter+5)]
        
        for week_index in range(6):
            week_display = ""
            for month in month_cals:
                if week_index < len(month):
                    week = month[week_index]
                    week_display += " ".join(f"{day:2}" if day != 0 else "  " for day in week) + "   "
                else:
                    week_display += "                     "
            cal_text.insert(tk.INSERT, week_display + "\n")
        cal_text.insert(tk.INSERT, "\n")

# Create main window
root = tk.Tk()
root.title("Yearly Calendar Viewer")
root.geometry("800x600")
root.configure(bg='#2C2F33')

# UI Elements
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="Enter Year:", foreground='red', background='#2C2F33', font=('Arial', 12, 'bold')).pack()
year_entry = ttk.Entry(frame, font=('Arial', 12))
year_entry.pack()

ttk.Button(frame, text="Show Calendar", command=display_calendar, style='TButton').pack()

# Scrolled Text Widget for Displaying Calendar
cal_text = scrolledtext.ScrolledText(frame, width=95, height=25, wrap=tk.WORD, font=('Courier', 10), background='#23272A', foreground='white')
cal_text.pack(fill=tk.BOTH, expand=True)

# Style
style = ttk.Style()
style.configure('TButton', font=('Arial', 12, 'bold'), foreground='red', background='#2C2F33')

root.mainloop()
