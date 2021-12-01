with open("1-data.txt") as file:
    depth_chart = file.readlines()
    depth_chart = [line.rstrip() for line in depth_chart]

count = 0
prev_depth = "0"

for current_depth in depth_chart:

    if current_depth > prev_depth:
        print(f"{current_depth} increased")
        count += 1
    prev_depth = current_depth

print(count)
