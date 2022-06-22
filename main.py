from tkinter import *
from tkinter.ttk import *
from methodology_reader import methodology_text, methodology_equations

# from tkinter import messagebox

# ------ UI SETUP ------ #

root = Tk()
root.title("Fire Radiation Calculator")
root.geometry('850x900+0+0')  # opens window in the top left corner of the screen
# root.config(width=1740, height=800)

root_style = Style()
# root_style.theme_use("alt")
root_style.configure("heading.TLabel", font=("Calibri", 20))
root_style.configure("body.TLabel", font=("Calibri", 12))
root_style.configure("body.TEntry", font=("Calibri", 12))
root_style.configure("body.TButton", font=("Calibri", 12))

# Tab Control

tab_control = Notebook(root)
input_tab = Frame(tab_control, padding=15)
train_img_tab = Frame(tab_control, padding=15)
methodology_tab = Frame(tab_control, padding=15)

tab_control.add(input_tab, text='Inputs')
tab_control.add(train_img_tab, text='Geometry help')
tab_control.add(methodology_tab, text="Methodology")

tab_control.pack(expand=1, fill="both")

# Button commands


def clear_all():
    end_windows_outer_width_entry.delete(0, END)
    end_windows_inner_width_entry.delete(0, END)
    doors_outer_width_entry.delete(0, END)
    doors_inner_width_entry.delete(0, END)
    centre_windows_outer_width_entry.delete(0, END)
    end_windows_height_entry.delete(0, END)
    centre_windows_height_entry.delete(0, END)
    doors_height_entry.delete(0, END)
    convection_entry.delete(0, END)
    hrrpua_entry.delete(0, END)
    fire_size_entry.delete(0, END)
    calc_title_entry.delete(0, END)
    fire_growth_rate_dropdown.set('')


def reset_default():
    clear_all()
    fire_size_entry.insert(0, 8.8)
    convection_entry.insert(0, 0.7)
    hrrpua_entry.insert(0, 290)


# ---- Inputs Tab ---- #

# labels
calc_title_label = Label(input_tab, text="Calculation Title", style="heading.TLabel", padding=(0, 10))
calc_title_label.grid(row=0, column=0, sticky=W)

# labels - train dimensions
train_dim_title_label = Label(input_tab, text="Train Dimensions", style="heading.TLabel", padding=(0, 10))
train_dim_title_label.grid(row=1, column=0, sticky=W)

end_windows_outer_width_label = Label(input_tab, text="End windows' outer width", style="body.TLabel", padding=(0, 5))
end_windows_outer_width_label.grid(row=2, column=0)

outer_windows_inner_width_label = Label(input_tab, text="End windows' inner width", style="body.TLabel", padding=(0, 5))
outer_windows_inner_width_label.grid(row=3, column=0)

centre_windows_outer_width_label = Label(input_tab, text="Centre windows' outer width", style="body.TLabel",
                                         padding=(0, 5))
centre_windows_outer_width_label.grid(row=4, column=0)

doors_outer_width_label = Label(input_tab, text="Doors' outer width", style="body.TLabel", padding=(0, 5))
doors_outer_width_label.grid(row=5, column=0)

doors_inner_width_label = Label(input_tab, text="Doors' inner width", style="body.TLabel", padding=(0, 5))
doors_inner_width_label.grid(row=6, column=0)

end_windows_height_label = Label(input_tab, text="End windows' height", style="body.TLabel")
end_windows_height_label.grid(row=2, column=2)

centre_windows_height_label = Label(input_tab, text="Centre windows' height", style="body.TLabel")
centre_windows_height_label.grid(row=4, column=2)

doors_height_label = Label(input_tab, text="Doors' height", style="body.TLabel")
doors_height_label.grid(row=6, column=2)

# labels - fire

fire_title_label = Label(input_tab, text="Fire Properties", style="heading.TLabel", padding=(0, 10))
fire_title_label.grid(row=7, column=0, sticky=W)

fire_size_label = Label(input_tab, text="Maximum Fire Size, MW", style="body.TLabel", padding=(0, 10))
fire_size_label.grid(row=8, column=0)

fire_alpha_label = Label(input_tab, text="Fire Growth Rate, \u03B1", style="body.TLabel", padding=(0, 5))
fire_alpha_label.grid(row=9, column=0)

convection_label = Label(input_tab, text="Convective Fraction (0 to 1)", style="body.TLabel", padding=(0, 5))
convection_label.grid(row=10, column=0)

hrrpua_label = Label(input_tab, text="Heat Release Rate per Unit Area, kW/m\u00B2", style="body.TLabel", padding=(0, 5))
hrrpua_label.grid(row=11, column=0, padx=10)

# Entries
calc_title_entry = Entry(input_tab, width=40, font=("Calibri", 19))
calc_title_entry.grid(row=0, column=1, columnspan=3)

# Train Dimension entries
end_windows_outer_width_entry = Entry(input_tab, width=5)
end_windows_outer_width_entry.grid(row=2, column=1, sticky=W)
end_windows_outer_width_entry.focus()

end_windows_inner_width_entry = Entry(input_tab, width=5, style="body.TEntry")
end_windows_inner_width_entry.grid(row=3, column=1, sticky=W)

centre_windows_outer_width_entry = Entry(input_tab, width=5, style="body.TEntry")
centre_windows_outer_width_entry.grid(row=4, column=1, sticky=W)

end_windows_height_entry = Entry(input_tab, width=5, style="body.TEntry")
end_windows_height_entry.grid(row=2, column=3)

centre_windows_height_entry = Entry(input_tab, width=5, style="body.TEntry")
centre_windows_height_entry.grid(row=4, column=3)

doors_outer_width_entry = Entry(input_tab, width=5, style="body.TEntry")
doors_outer_width_entry.grid(row=5, column=1, sticky=W)

doors_inner_width_entry = Entry(input_tab, width=5, style="body.TEntry")
doors_inner_width_entry.grid(row=6, column=1, sticky=W)

doors_height_entry = Entry(input_tab, width=5, style="body.TEntry")
doors_height_entry.grid(row=6, column=3)

# Fire entries
fire_size_entry = Entry(input_tab, width=5, style="body.TEntry")
fire_size_entry.insert(0, 8.8)
fire_size_entry.grid(row=8, column=1, sticky=W)

convection_entry = Entry(input_tab, width=5, style="body.TEntry")
convection_entry.insert(0, 0.7)
convection_entry.grid(row=10, column=1, sticky=W)

hrrpua_entry = Entry(input_tab, width=5, style="body.TEntry")
hrrpua_entry.insert(0, 290)
hrrpua_entry.grid(row=11, column=1, sticky=W)

# Fire combobox
fire_growth_rates = ["Slow", "Medium", "Fast", "Ultra-fast"]
fire_growth_rate_dropdown = Combobox(input_tab, values=fire_growth_rates)
fire_growth_rate_dropdown.state(["readonly"])
fire_growth_rate_dropdown.grid(row=9, column=1, sticky=W)

# Buttons
calculate_button = Button(input_tab, text="Calculate Separation Distances", style="body.TButton", padding=(0, 5))
calculate_button.grid(row=12, column=3, pady=(40, 10))

clear_all_button = Button(input_tab, text="Clear All", style="body.TButton", padding=(0, 5), command=clear_all)
clear_all_button.grid(row=12, column=0, pady=10, sticky=W)

reset_default_button = Button(input_tab, text="Reset to Default", style="body.TButton", padding=(0, 5),
                              command=reset_default)
reset_default_button.grid(row=12, column=0, pady=10, padx=10, sticky=E)

quit_button = Button(input_tab, text="Quit", style="body.TButton", padding=(0, 5), command=root.destroy)
quit_button.grid(row=13, column=0, pady=10, sticky=W)


# ----- Geometry Help Tab ----- #

# Images
train_img = PhotoImage(file="diagram_small.png")
img_label = Label(train_img_tab, image=train_img)
img_label.grid(row=0, column=0, rowspan=15, padx=10)

# ---- Methodology Tab ----- #

method_canvas = Canvas(methodology_tab, width=800)
method_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Scrollbar

method_scrollbar = Scrollbar(methodology_tab, orient="vertical", command=method_canvas.yview)
method_scrollbar.pack(side=RIGHT, fill="y", expand=1)

method_canvas.configure(yscrollcommand= method_scrollbar.set)
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


root.mainloop()
