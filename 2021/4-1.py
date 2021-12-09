from pprint import pprint as pp

def setup_game():
    # read game data input, strip whitespace
    with open("4-data.txt") as file:
        bingo_cards = file.readlines()
        bingo_cards = [line.rstrip() for line in bingo_cards]

    # create a list of numbers to be drawn
    numbers_called = bingo_cards.pop(0).split(",")

    # init game dictionary and counters
    game_dict = {}
    card = 0

    for line in bingo_cards:
        
        if line == "":
            card += 1
            linenum = 0
            game_dict.update({card: {}})
        
        else:
            linenum += 1

            game_dict[card][linenum] = {}

            line_list = []

            for i in line.split():
                line_list.append(i)

            for i in range(5):
                game_dict[card][linenum][i] = line_list[i]

    return game_dict, numbers_called


def scan_row(row, num_drawn):
    winning_column = ""
    row = row.split()
    
    for num in range(len(row)):
        if row[num] == num_drawn:
            winning_column = num

    return winning_column

def round(bingo_card):
    
    num_drawn = numbers_called.pop(0)

    #print(num_drawn + "\n---")
    
    for row in bingo_card:
        scan_row(row, num_drawn)

game_dict, numbers_called = setup_game()
pp(game_dict)
#round(bingo_card)
