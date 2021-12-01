with open("1-data.txt") as file:
    depth_chart = file.readlines()
    depth_chart = [line.rstrip() for line in depth_chart]

count = 0
window_size = 3
prev_window = 0

for i in range(len(depth_chart) - window_size + 1):
    
    total = 0 
    
    for window in depth_chart[i: i + window_size]:
        total += int(window)
    
    if total > prev_window and prev_window != 0:
        count += 1
    
    prev_window = total 

print(count)
