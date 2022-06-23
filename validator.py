from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

# widths_fields = ["End windows' outer width",
#                  "End windows' inner width",
#                  "Centre windows' outer width",
#                  "Doors' outer width",
#                  "Doors' inner width"]
#
# heights_fields = ["End windows' height",
#                   "Centre windows' height",
#                   "Doors' height"]
#
# fire_fields = ["Maximum Fire Size, MW",
#                "Heat Release Rate per Unit Area, kW/m\u00B2",
#                "Convection Fraction (0 to 1)"]
#
# fire_combo_fields = ["Fire Growth Rate, \u03B1"]


def entry_check(all_inputs):
    for entry_dictionary in all_inputs:
        for entry in entry_dictionary:
            if not entry_dictionary[entry].get():
                return messagebox.showerror(title="Error - Unfilled field", message=f'Please do not leave the "{entry}" '
                                                                                    f'field empty')
    width_entries = all_inputs[1]
    for entry in width_entries:
        try:
            float(width_entries[entry].get())
        except ValueError:
            return messagebox.showerror(title="Error - Number not entered", message=f'Letters in {entry} not accepted')


