from tkinter import *
from tkinter import messagebox

# ------ UI SETUP ------ #

window = Tk()
window.title("Fire Radiation Calculator")
window.config(padx=40, pady=40, width=1740, height=800)

train_img = PhotoImage(file="toilette.png")

canvas = Canvas(width=800, height=300)
canvas.create_image(400, 200, image=train_img)
canvas.grid(row=0, column=0, columnspan=2)

# labels

train_dim_title_label = Label(text="Train Dimensions", font=("Arial", 20))
train_dim_title_label.grid(row=1, column=0, sticky=W)

end_windows_outer_width_label = Label(text="End windows' outer width", font=("Arial", 16))
end_windows_outer_width_label.grid(row=2, column=0)

outer_windows_inner_width_label = Label(text="End windows' inner width", font=("Arial", 16))
outer_windows_inner_width_label.grid(row=3, column=0)

centre_windows_outer_width_label = Label(text="Centre windows' outer width", font=("Arial", 16))
centre_windows_outer_width_label.grid(row=4, column=0)

fire_title_label = Label(text="Fire Properties", font=("Arial", 20))
fire_title_label.grid(row=6, column=0, sticky=W)

# entries

end_windows_outer_width_entry = Entry(font=("Arial", 16))
end_windows_outer_width_entry.grid(row=2, column=1, sticky=W)

end_windows_inner_width_entry = Entry(font=("Arial", 16))
end_windows_inner_width_entry.grid(row=3, column=1, sticky=W)

centre_windows_outer_width_entry = Entry(font=("Arial", 16))
centre_windows_outer_width_entry.grid(row=4, column=1, sticky=W)

window.mainloop()