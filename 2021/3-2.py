with open("3-data.txt") as file:
    diag_logs = file.readlines()
    diag_logs = [line.rstrip() for line in diag_logs]


def bit_counter(diag_logs, matched):

    bit_counts = {}

    for i in range(len(diag_logs[0])):
        bit_counts[int(i)] = 0
    
    for entry in diag_logs:
        if entry.startswith(matched['most']):
            for x in range(len(entry)):
                bit_counts[x] = bit_counts.get(x) + int(entry[x])

    return bit_counts


def bit_calc(diag_logs, matched):

    most_common = ""
    least_common = ""
    
    bit_counts = bit_counter(diag_logs, matched)

    for i in range(len(bit_counts)):
        if bit_counts[i] > len(diag_logs)/2:
            most_common += "1"
            least_common += "0"
        else:
            most_common += "0"
            least_common += "1"

        matched["most"] = most_common
        matched["least"] = least_common
        print(len(matched["match"]))
        print(matched["match"])
        matched["match"] = matched["match"] + most_common[len(matched["match"])]
    print(f"most common {most_common}")
    print(f"least common {least_common}")
    return most_common, least_common, matched, bit_counts


def tally_bit(diag_logs, matched, bit_place):

    most_common = ""
    least_common = ""
    
    bit_counts = bit_counter(diag_logs, matched)

    if bit_counts[bit_place] > len(diag_logs)/2:
        most_common += "1"
        least_common += "0"
    else:
        most_common += "0"
        least_common += "1"

    matched["most"] = most_common
    matched["least"] = least_common
    #print(len(matched["match"]))
    #print(matched["match"])
    #matched["match"] = matched["match"] + most_common[len(matched["match"])]
        
    print(f"most common {most_common}")
    print(f"least common {least_common}")
    return most_common, least_common, matched, bit_counts


matched = {"most": "", "least": "", "match": ""}

#parsed_logs = bit_calc(diag_logs, matched)

for i in range(len(diag_logs[0])):
    parsed_logs = tally_bit(diag_logs, matched, 0)

print(int(parsed_logs[0], 2) * int(parsed_logs[1], 2))

if 3633500 == int(parsed_logs[0], 2) * int(parsed_logs[1], 2):
        print("Part 1 working")
else: 
    print("You broke shit.")

print(parsed_logs[3])

print(f"{'*'*100}\n")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



print(matched)

bit_counts = bit_counter(diag_logs, matched)

print(bit_counts)


if bit_counts[0] >= 500:
    oxygen = "1"
    co2 = "0"
else:
    oxygen = "0"
    co2 = "1"

print(oxygen, co2)

#for i in range(len(bit_counts)):
#    if i[0] == 