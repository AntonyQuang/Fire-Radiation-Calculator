import os


txt_quantity = 0
methodology_text = []
text_dir = "methodology text"

for path in os.listdir(text_dir):
    if os.path.isfile(os.path.join(text_dir, path)):
        txt_quantity += 1

for i in range(1, txt_quantity+1):
    with open(f"{text_dir}/part_{i}.txt", mode='r', encoding='utf8') as file:
        text = file.read()
        methodology_text.append(text)


equation_quantity = 0
methodology_equations = []
equation_dir = "methodology equations"
for path in os.listdir(equation_dir):
    if os.path.isfile(os.path.join(equation_dir, path)):
        equation_quantity += 1

for i in range(1, equation_quantity+1):
    equation_file_name = f"{equation_dir}/equation {i}.png"
    methodology_equations.append(equation_file_name)
