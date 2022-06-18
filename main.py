from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# ------ UI SETUP ------ #

root = Tk()
root.title("Fire Radiation Calculator")
root.config(padx=40, pady=40, width=1740, height=800)

train_img = PhotoImage(file="toilette.png")

canvas = Canvas(width=800, height=300)
canvas.create_image(400, 200, image=train_img)
canvas.grid(row=0, column=0, columnspan=4)

# labels

# labels - train dimensions
train_dim_title_label = Label(root, text="Train Dimensions", font=("Calibri", 20))
train_dim_title_label.grid(row=1, column=0, sticky=W)
train_dim_title_label.config(pady=5)

end_windows_outer_width_label = Label(root, text="End windows' outer width", font=("Calibri", 14))
end_windows_outer_width_label.grid(row=2, column=0)

outer_windows_inner_width_label = Label(root, text="End windows' inner width", font=("Calibri", 14))
outer_windows_inner_width_label.grid(row=3, column=0)

centre_windows_outer_width_label = Label(root, text="Centre windows' outer width", font=("Calibri", 14))
centre_windows_outer_width_label.grid(row=4, column=0)

end_windows_height_label = Label(root, text="End windows' height", font=("Calibri", 14))
end_windows_height_label.grid(row=2, column=2)

centre_windows_height_label = Label(root, text="Centre windows' height", font=("Calibri", 14))
centre_windows_height_label.grid(row=4, column=2)

# labels - fire

fire_title_label = Label(root, text="Fire Properties", font=("Calibri", 20))
fire_title_label.grid(row=6, column=0, sticky=W)
fire_title_label.config(pady=5)

fire_alpha_label = Label(root, text="Fire Growth Rate, \u03B1", font=("Calibri", 14))
fire_alpha_label.grid(row=7, column=0)

convection_label = Label(root, text="Convective Fraction (0 to 1)", font=("Calibri", 14))
convection_label.grid(row=8, column=0)

hrrpua_label = Label(root, text="Heat Release Rate per Unit Area, kW/m\u00B2", font=("Calibri", 14))
hrrpua_label.grid(row=9, column=0)


# entries

# Train Dimension entries

end_windows_outer_width_entry = Entry(root, width=5, font=("Calibri", 14))
end_windows_outer_width_entry.grid(row=2, column=1, sticky=W)

end_windows_inner_width_entry = Entry(root, width=5, font=("Calibri", 14))
end_windows_inner_width_entry.grid(row=3, column=1, sticky=W)

centre_windows_outer_width_entry = Entry(root, width=5, font=("Calibri", 14))
centre_windows_outer_width_entry.grid(row=4, column=1, sticky=W)

end_windows_height_entry = Entry(root, width=5, font=("Calibri", 14))
end_windows_height_entry.grid(row=2, column=3, sticky=W)

centre_windows_height_entry = Entry(root, width=5, font=("Calibri", 14))
centre_windows_height_entry.grid(row=4, column=3, sticky=W)

# Fire entries

convection_entry = Entry(root, width=5, font=("Calibri", 14))
convection_entry.insert(0, 0.7)
convection_entry.grid(row=8, column=1, sticky=W)

hrrpua_entry = Entry(root, width=5, font=("Calibri", 14))
hrrpua_entry.insert(0, 290)
hrrpua_entry.grid(row=9, column=1, sticky=W)

# Fire listbox

fire_growth_rates = ["Slow", "Medium", "Fast", "Ultra-fast"]
fire_growth_rate_dropdown = ttk.Combobox(root, values=fire_growth_rates)
fire_growth_rate_dropdown.state(["readonly"])
fire_growth_rate_dropdown.grid(row=7, column=1, sticky=W)

# Buttons

calculate_button = Button(root, text="Calculate Separation Distances", font=("Calibri", 16))
calculate_button.grid(row=10, column=2, columnspan=2, pady=10)
calculate_button.config(pady=5)

root.mainloop()