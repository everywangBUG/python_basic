f = open("model_list.txt", mode="r", encoding="utf-8")
for line in f:
    line = line.split()
    print(line)
    height = int(line[2])
    weight = int(line[3])
    if weight <= 50 and height >= 170:
        print(line)