from tkinter import *
from tkinter.ttk import *
from methodology_reader import methodology_text, methodology_equations
from input_manager import process_inputs
import os
import sys

# ------ PATHFINDER ----- #


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# ------ UI SETUP ------ #

root = Tk()
root.title("Fire Radiation Calculator")
root.geometry('850x900+0+0')  # opens window in the top left corner of the screen

root_style = Style()
# root_style.theme_use("alt")
root_style.configure("heading.TLabel", font=("Calibri", 20))
root_style.configure("body.TLabel", font=("Calibri", 12))
root_style.configure("body.TEntry", font=("Calibri", 12))
root_style.configure("body.TButton", font=("Calibri", 12))

# Setting up tabs with tab_control

tab_control = Notebook(root)
input_tab = Frame(tab_control, padding=15)
train_img_tab = Frame(tab_control, padding=15)
methodology_tab = Frame(tab_control, padding=(15, 0, 0, 0))

tab_control.add(input_tab, text='Inputs')
tab_control.add(train_img_tab, text='Geometry help')
tab_control.add(methodology_tab, text="Methodology")

tab_control.pack(expand=1, fill="both")

# input parameter lists

widths_fields = ["End windows' outer width, m",
                 "End windows' inner width, m",
                 "Centre windows' outer width, m",
                 "Doors' outer width, m",
                 "Doors' inner width, m"]

heights_fields = ["End windows' height, m",
                  "Centre windows' height, m",
                  "Windows' midpoint height from floor, m",
                  "Doors' height, m",
                  "Doors' midpoint height from floor, m"]

fire_fields = ["Maximum Fire Size, MW",
               "Heat Release Rate per Unit Area, kW/m\u00B2",
               "Convection Fraction (0 to 1)"]

fire_combo_fields = ["Fire Growth Rate, \u03B1, kW/s\u00B2"]

widths_labels = {}
heights_labels = {}
fire_labels = {}

widths_entries = {}
heights_entries = {}
fire_entries = {}

# ---- Inputs Tab ---- #

# Calculation title label and entry
calc_title_label = Label(input_tab, text="Calculation Title", style="heading.TLabel", padding=(0, 10))
calc_title_label.grid(row=0, column=0, sticky=W)

calc_title_entry = Entry(input_tab, width=40, font=("Calibri", 19))
calc_title_entry.grid(row=0, column=1, columnspan=3)
title_entries = {"Calculation Title": calc_title_entry}

# labels - titles
train_dim_title_label = Label(input_tab, text="Train Dimensions, m", style="heading.TLabel", padding=(0, 10))
train_dim_title_label.grid(row=1, column=0, sticky=W)

fire_title_label = Label(input_tab, text="Fire Properties", style="heading.TLabel", padding=(0, 10))
fire_title_label.grid(row=7, column=0, sticky=W)

# Fire alpha

fire_growth_rate_label = Label(input_tab, text="Fire Growth Rate, \u03B1, kW/s\u00B2",
                               style="body.TLabel", padding=(0, 5))
fire_growth_rate_label.grid(row=11, column=0)

fire_growth_rates = ["Slow", "Medium", "Fast", "Ultra-fast"]
fire_growth_rate_dropdown = Combobox(input_tab, values=fire_growth_rates)
fire_growth_rate_dropdown.state(["readonly"])
fire_growth_rate_dropdown.grid(row=11, column=1, sticky="W", padx=3)

fire_growth_entries = {fire_combo_fields[0]: fire_growth_rate_dropdown}

# Train Dimensions and Fire : Labels and Entries

for i in range(len(widths_fields)):
    field_name = widths_fields[i]
    widths_labels[field_name] = Label(input_tab, text=field_name, style="body.TLabel", padding=(0, 5))
    widths_labels[field_name].grid(row=i + 2, column=0)

    widths_entries[field_name] = Entry(input_tab, width=5, style="body.TEntry")
    widths_entries[field_name].grid(row=i + 2, column=1, sticky="W", padx=5)

for i in range(len(heights_fields)):
    field_name = heights_fields[i]
    heights_labels[field_name] = Label(input_tab, text=field_name, style="body.TLabel", padding=(0, 5))
    heights_labels[field_name].grid(row=i + 2, column=2, padx=(0, 20))

    heights_entries[field_name] = Entry(input_tab, width=5, style="body.TEntry")
    heights_entries[field_name].grid(row=i + 2, column=3, sticky="W")

for i in range(len(fire_fields)):
    field_name = fire_fields[i]
    fire_labels[field_name] = Label(input_tab, text=field_name, style="body.TLabel", padding=(0, 5))
    fire_labels[field_name].grid(row=8 + i, column=0)

    fire_entries[field_name] = Entry(input_tab, width=5, style="body.TEntry")
    fire_entries[field_name].grid(row=8 + i, column=1, sticky="W", padx=5)

# Saving inputs

raw_inputs = [title_entries, widths_entries, heights_entries, fire_entries, fire_growth_entries]

# Input Button commands


def clear_all():
    entries = [widths_entries, heights_entries, fire_entries]
    for entry_dictionary in entries:
        for entry in entry_dictionary:
            entry_dictionary[entry].delete(0, END)
    calc_title_entry.delete(0, END)
    fire_growth_rate_dropdown.set('')
    calc_title_entry.focus()


def reset_default():
    clear_all()
    fire_entries["Maximum Fire Size, MW"].insert(0, 8.8)
    fire_entries["Heat Release Rate per Unit Area, kW/m\u00B2"].insert(0, 290)
    fire_entries["Convection Fraction (0 to 1)"].insert(0, 0.7)


# Buttons
calculate_button = Button(input_tab, text="Calculate Separation Distances", style="body.TButton", padding=(0, 5),
                          command=lambda: process_inputs(raw_inputs))
calculate_button.grid(row=12, column=2, pady=(10, 10), sticky=E)

clear_all_button = Button(input_tab, text="Clear All", style="body.TButton", padding=(0, 5), command=clear_all)
clear_all_button.grid(row=12, column=0, pady=10, sticky=W)

reset_default_button = Button(input_tab, text="Reset to Default", style="body.TButton", padding=(0, 5),
                              command=reset_default)
reset_default_button.grid(row=12, column=0, pady=10, padx=10, sticky=E)

quit_button = Button(input_tab, text="Quit", style="body.TButton", padding=(0, 5), command=root.destroy)
quit_button.grid(row=13, column=0, pady=10, sticky=W)

# Copyright Label
revision_label = Label(input_tab, text="Version 0.9, 29/06/2022")
revision_label.grid(row=14, column=0, sticky=W)
credit_label = Label(input_tab, text="Antony Quang")
credit_label.grid(row=15, column=0, sticky=W)

# ----- Geometry Help Tab ----- #

# Images
diagram_file = resource_path("diagram_small.png")
train_img = PhotoImage(file=diagram_file)
img_label = Label(train_img_tab, image=train_img)
img_label.grid(row=0, column=0, rowspan=15, padx=10)

# ---- Methodology Tab ----- #

method_canvas = Canvas(methodology_tab, width=800)
method_canvas.pack(side=LEFT, fill=BOTH, expand=1, pady=20)

# Scrollbar

method_scrollbar = Scrollbar(methodology_tab, orient="vertical", command=method_canvas.yview)
method_scrollbar.pack(side=RIGHT, fill="y", expand=1)

method_canvas.configure(yscrollcommand=method_scrollbar.set)
method_canvas.bind('<Configure>', lambda e: method_canvas.configure(scrollregion=method_canvas.bbox("all")))

method_content_frame = Frame(method_canvas)

method_canvas.create_window((0, 0), window=method_content_frame, anchor="nw")

# Adding the methodology text
methodology_text_widgets = []
text_row_placement = 0
for i in range(len(methodology_text)):
    current_methodology_text = Label(method_content_frame, text=methodology_text[i], justify=LEFT, wraplength=790)
    current_methodology_text.grid(row=text_row_placement, column=0, sticky=W)
    methodology_text_widgets.append(current_methodology_text)
    text_row_placement += 2

# Adding the equations
methodology_equations_widgets = []
methodology_equations_list = []
equation_row_placement = 1
for i in range(len(methodology_equations)):
    current_equation_img = PhotoImage(file=methodology_equations[i])
    methodology_equations_list.append(current_equation_img)

    current_equation = Label(method_content_frame, image=methodology_equations_list[i])
    current_equation.grid(row=equation_row_placement, column=0)

    methodology_equations.append(current_equation)
    equation_row_placement += 2

reset_default()

root.mainloop()
