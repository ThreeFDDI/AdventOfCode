with open("2-data.txt") as file:
    navigation = file.readlines()
    navigation = [line.rstrip() for line in navigation]

horizontal = 0
depth = 0
aim = 0

for i in navigation:
    distance = i.split()[1]
    #print(distance)

    if "down" in i:
        aim += int(distance)

    if "up" in i:
        aim -= int(distance)

    if "forward" in i:
        horizontal += int(distance)
        depth += int(distance) * aim

    #print(aim)

print(horizontal)    
print(depth)

print(horizontal * depth)
