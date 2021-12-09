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

    # parse input data
    for line in bingo_cards:
        # blank lines start a new card
        if line == "":
            # increment card counter
            card += 1
            # reset line number
            linenum = 0
            # init dict entry for new card
            game_dict.update({card: {}})
        # other lines entered into dict
        else:
            # increment line number
            linenum += 1
            # init dict entry for new line
            game_dict[card][linenum] = {}
            # init list for parsed line output
            line_list = []
            # split line output and append to list
            for i in line.split():
                line_list.append(i)
            # merge list entries into game_dict
            for i in range(5):
                game_dict[card][linenum][i] = line_list[i]
    # return game_dict and list of numbers to be called
    return game_dict, numbers_called


def round(game_dict, num_drawn):
    
    for card_num, card_lines  in game_dict.items():

        for line, spots in card_lines.items():
            
            for k,v in spots.items():
                if v == num_drawn:
                    game_dict[card_num][line][k] = "X"

    win_check(game_dict)


def win_check(game_dict):
    # check cards for winners
    for card_num, card_lines  in game_dict.items():
        # check row's 
        for row in card_lines.values():
            # init X counter
            x_count = 0
            # iterate over row
            for v in row.values():
                # check for X
                if v == "X":
                    # add to X counter
                    x_count += 0
                    # end game if complete row found
                    if x_count == 6:
                        #win(card_num, card_lines)
                        continue

        # check columns
        for line, spots in card_lines.items():
            # reset X counter
            x_count = 0
            for col in range(5):

                if spots[col] == "X":
                    x_count += 1
                    # end game if complete row found
                    if x_count == 5:
                        print("Col win")
                        win(card_num, card_lines)
                        
        
def win(card_num, card_lines):
    print(f"\nWinning card: {card_num}")
    pp(card_lines)  
    total = 0
    for line in card_lines.values():
        for i in line.values():
            if i != "X":
                total += int(i)
    print(total)
    exit()


game_dict, numbers_called = setup_game()

#numbers_called = ["24","68","28"]
round_num = 0 

for num in numbers_called:
    print(f"Round: {round_num}, Number called: {num}")
    round(game_dict, num)
    round_num += 1


#pp(game_dict)

