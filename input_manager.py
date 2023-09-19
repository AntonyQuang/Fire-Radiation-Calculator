from tkinter import messagebox
from calculator import calculate


def process_inputs(raw_inputs):
    all_inputs = raw_inputs.copy()

    for entry_dictionary in all_inputs:
        for entry in entry_dictionary:
            parameter = entry_dictionary[entry].get()
            if not parameter:
                return messagebox.showerror(title="Error - Empty field", message=f'Please do not leave the "{entry}" '
                                                                                 f'field empty')

    for entry_dictionary in [all_inputs[1], all_inputs[2], all_inputs[3]]:
        for entry in entry_dictionary:
            parameter = entry_dictionary[entry].get()
            try:
                float(parameter)
            except ValueError:
                return messagebox.showerror(title="Error - Unaccepted Characters Entered",
                                            message=f'Please enter only numbers in the "{entry}" field')
            if float(parameter) < 0:
                return messagebox.showerror(title="Error - Negative Number detected",
                                            message=f'Negative numbers are not accepted in the "{entry}" field')

    processed_inputs = all_inputs

    processed_inputs[0] = {entry: all_inputs[0][entry].get() for entry in all_inputs[0]}
    processed_inputs[1] = {entry: float(all_inputs[1][entry].get()) for entry in all_inputs[1]}
    processed_inputs[2] = {entry: float(all_inputs[2][entry].get()) for entry in all_inputs[2]}
    processed_inputs[3] = {entry: float(all_inputs[3][entry].get()) for entry in all_inputs[3]}
    processed_inputs[4] = {entry: all_inputs[4][entry].get() for entry in all_inputs[4]}

    forbidden_filename_char = '\/:*?|"<>'

    for char in processed_inputs[0]["Calculation Title"]:
        if char in forbidden_filename_char:
            return messagebox.showerror(title="Error - Unusable Title Name",
                                        message=f'Calculation Title cannot contain any of the following characters:'
                                                f' \ / : * ? | " < >')

    if processed_inputs[1]["End windows' outer width, m"] < processed_inputs[1]["End windows' inner width, m"]:
        return messagebox.showerror(title="Error - Incompatible Dimensions for End Windows",
                                    message=f'Please enter an outer width greater than an inner width')

    if processed_inputs[1]["Doors' outer width, m"] <= processed_inputs[1]["Doors' inner width, m"]:
        return messagebox.showerror(title="Error - Incompatible Dimensions for Doors",
                                    message=f'Please enter an outer width greater than an inner width')

    if processed_inputs[1]["End windows' inner width, m"] <= processed_inputs[1]["Centre windows' outer width, m"]:
        return messagebox.showerror(title="Error - Incompatible Dimensions",
                                    message=f'Please enter an inner width for the end windows greater than the width '
                                            f'of the centre windows')

    if processed_inputs[1]["End windows' outer width, m"] == processed_inputs[1]["Doors' outer width, m"]:
        return messagebox.showerror(title="Error - Incompatible Dimensions",
                                    message=f'Please check door and end window widths')

    if processed_inputs[2]["Doors' midpoint height from floor, m"] > processed_inputs[2]["Doors' height, m"]:
        return messagebox.showerror(title="Error - Incompatible Dimensions",
                                    message=f'Please check door height and midpoint height')

    if processed_inputs[3]["Convection Fraction (0 to 1)"] > 1:
        return messagebox.showerror(title="Error - Incorrect Convection Fraction",
                                    message='Please enter a convection fraction between 0 and 1')

    calculate(processed_inputs)

    all_inputs = []
    processed_inputs = []
    print("Calculation completed")
