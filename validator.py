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

# all_inputs = [title_entries, widths_entries, heights_entries, fire_entries, fire_growth_entries]


def entry_check(all_inputs):
    for entry_dictionary in all_inputs:
        for entry in entry_dictionary:
            if not entry_dictionary[entry].get():
                return messagebox.showerror(title="Error - Unfilled field", message=f'Please do not leave the "{entry}" '
                                                                                    f'field empty')

    for entry_dictionary in [all_inputs[1], all_inputs[2], all_inputs[3]]:
        for entry in entry_dictionary:
            try:
                float(entry_dictionary[entry].get())
            except ValueError:
                return messagebox.showerror(title="Error - Unaccepted Characters Entered",
                                            message=f'Please enter only numbers in the "{entry}" field')
            if float(entry_dictionary[entry].get()) < 0:
                return messagebox.showerror(title="Error - Negative Number detected",
                                            message=f'Negative numbers are not accepted in the "{entry}" field')

    all_inputs[1] = {entry: float(all_inputs[1][entry].get()) for entry in all_inputs[1]}
    all_inputs[2] = {entry: float(all_inputs[2][entry].get()) for entry in all_inputs[2]}
    all_inputs[3] = {entry: float(all_inputs[3][entry].get()) for entry in all_inputs[3]}

    if all_inputs[1]["End windows' outer width, m"] <= all_inputs[1]["End windows' inner width, m"]:
        return messagebox.showerror(title="Error - Incompatible Dimensions for End Windows",
                                    message=f'Please enter an outer width greater than an inner width')

    if all_inputs[1]["Doors' outer width, m"] <= all_inputs[1]["Doors' inner width, m"]:
        return messagebox.showerror(title="Error - Incompatible Dimensions for Doors",
                                    message=f'Please enter an outer width greater than an inner width')

    if all_inputs[1]["End windows' inner width, m"] <= all_inputs[1]["Centre windows' outer width, m"]:
        return messagebox.showerror(title="Error - Incompatible Dimensions",
                                    message=f'Please enter an inner width for the end windows greater than the width '
                                            f'of the centre windows')

    if all_inputs[1]["End windows' outer width, m"] == all_inputs[1]["Doors' outer width, m"]:
        return messagebox.showerror(title="Error - Incompatible Dimensions",
                                    message=f'Please check door and end window widths')

    if all_inputs[3]["Convection Fraction (0 to 1)"] > 1:
        return messagebox.showerror(title="Error - Incorrect Convection Fraction",
                                    message='Please enter a convection fraction between 0 and 1')

    return all_inputs[1], all_inputs[2], all_inputs[3]

