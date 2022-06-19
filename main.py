from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

# ------ UI SETUP ------ #

root = Tk()
root.title("Fire Radiation Calculator")
root.config(padx=40, pady=40, width=1740, height=800)

root_style = Style()
root_style.configure("heading.TLabel", font=("Calibri", 20))
root_style.configure("body.TLabel", font=("Calibri", 12))
root_style.configure("body.TEntry", font=("Calibri", 12))
root_style.configure("body.TButton", font=("Calibri", 12))

train_img = PhotoImage(file="toilette.png")


def clear_all():
    end_windows_outer_width_entry.delete(0, END)
    end_windows_inner_width_entry.delete(0, END)
    centre_windows_outer_width_entry.delete(0, END)
    end_windows_height_entry.delete(0, END)
    centre_windows_height_entry.delete(0, END)
    convection_entry.delete(0, END)
    hrrpua_entry.delete(0, END)


def reset_default():
    clear_all()
    convection_entry.insert(0, 0.7)
    hrrpua_entry.insert(0, 290)


canvas = Canvas(width=800, height=300)
canvas.create_image(400, 200, image=train_img)
canvas.grid(row=0, column=0, columnspan=4)

# labels

# labels - train dimensions
train_dim_title_label = Label(root, text="Train Dimensions", style="heading.TLabel", padding=(0, 10))
train_dim_title_label.grid(row=1, column=0, sticky=W)

end_windows_outer_width_label = Label(root, text="End windows' outer width", style="body.TLabel", padding=(0, 5))
end_windows_outer_width_label.grid(row=2, column=0)

outer_windows_inner_width_label = Label(root, text="End windows' inner width", style="body.TLabel", padding=(0, 5))
outer_windows_inner_width_label.grid(row=3, column=0)

centre_windows_outer_width_label = Label(root, text="Centre windows' outer width", style="body.TLabel", padding=(0, 5))
centre_windows_outer_width_label.grid(row=4, column=0)

end_windows_height_label = Label(root, text="End windows' height", style="body.TLabel")
end_windows_height_label.grid(row=2, column=2)

centre_windows_height_label = Label(root, text="Centre windows' height", style="body.TLabel")
centre_windows_height_label.grid(row=4, column=2)

# labels - fire

fire_title_label = Label(root, text="Fire Properties", style="heading.TLabel", padding=(0, 10))
fire_title_label.grid(row=6, column=0, sticky=W)

fire_alpha_label = Label(root, text="Fire Growth Rate, \u03B1", style="body.TLabel", padding=(0, 5))
fire_alpha_label.grid(row=7, column=0)

convection_label = Label(root, text="Convective Fraction (0 to 1)", style="body.TLabel", padding=(0, 5))
convection_label.grid(row=8, column=0)

hrrpua_label = Label(root, text="Heat Release Rate per Unit Area, kW/m\u00B2", style="body.TLabel", padding=(0, 5))
hrrpua_label.grid(row=9, column=0)


# entries

# Train Dimension entries

end_windows_outer_width_entry = Entry(root, width=5)
end_windows_outer_width_entry.grid(row=2, column=1, sticky=W)
end_windows_outer_width_entry.focus()

end_windows_inner_width_entry = Entry(root, width=5, style="body.TEntry")
end_windows_inner_width_entry.grid(row=3, column=1, sticky=W)

centre_windows_outer_width_entry = Entry(root, width=5, style="body.TEntry")
centre_windows_outer_width_entry.grid(row=4, column=1, sticky=W)

end_windows_height_entry = Entry(root, width=5, style="body.TEntry")
end_windows_height_entry.grid(row=2, column=3, sticky=W)

centre_windows_height_entry = Entry(root, width=5, style="body.TEntry")
centre_windows_height_entry.grid(row=4, column=3, sticky=W)

# Fire entries

convection_entry = Entry(root, width=5, style="body.TEntry")
convection_entry.insert(0, 0.7)
convection_entry.grid(row=8, column=1, sticky=W)

hrrpua_entry = Entry(root, width=5, style="body.TEntry")
hrrpua_entry.insert(0, 290)
hrrpua_entry.grid(row=9, column=1, sticky=W)

# Fire comboox

fire_growth_rates = ["Slow", "Medium", "Fast", "Ultra-fast"]
fire_growth_rate_dropdown = Combobox(root, values=fire_growth_rates)
fire_growth_rate_dropdown.state(["readonly"])
fire_growth_rate_dropdown.grid(row=7, column=1, sticky=W)

# Buttons

calculate_button = Button(root, text="Calculate Separation Distances", style="body.TButton", padding=(0, 5))
calculate_button.grid(row=10, column=3, pady=10)

clear_all_button = Button(root, text="Clear All", style="body.TButton", padding=(0, 5), command=clear_all)
clear_all_button.grid(row=10, column=0, pady=10, sticky=W)

reset_default_button = Button(root, text="Reset to Default", style="body.TButton", padding=(0, 5), command=reset_default)
reset_default_button.grid(row=10, column=0, pady=10, padx=10, sticky=E)

quit_button = Button(root, text="Quit", style="body.TButton", padding=(0, 5), command=root.destroy)
quit_button.grid(row=11, column=0, pady=10, sticky=W)
root.mainloop()
