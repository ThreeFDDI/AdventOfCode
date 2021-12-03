with open("3-data.txt") as file:
    diag_logs = file.readlines()
    diag_logs = [line.rstrip() for line in diag_logs]

bit_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
gamma = ""
epsilon = ""

for entry in diag_logs:
    for x in range(len(entry)):
        bit_counts[x] = bit_counts.get(x) + int(entry[x])


for i in range(len(bit_counts)):
    if bit_counts[i] > len(diag_logs)/2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))
