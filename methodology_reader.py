import os
txt_quantity = 0
dir = "methodology text"
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        txt_quantity += 1
print(txt_quantity)

for i in range(1, txt_quantity+1):
    with open(f"{dir}/part_{i}.txt", mode='r', encoding='utf8') as file:
        text = file.read()
