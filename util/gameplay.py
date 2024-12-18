import sys
import cards

cards.clear_directory()

def game_over():
    cards.show_pic("./answer.png")
    sys.exit(0)    

start_team, other_team, words = cards.assign_cards()
initial = cards.merge_cards()
cards.show_pic("./prompt.png")

start_cards = 9
other_cards = 8

start = {"team": start_team, "cards": start_cards}
other = {"team": other_team, "cards": other_cards}

current = start
next = other

guessed_words = []
flipped_cards = []

while True:
    print(f"{current['team']} has {current['cards']} cards left\n{next['team']} has {next['cards']} cards left")
    word = input(f"enter word for {current['team']} team: ")
    word = word.upper()
    color = ""
    if word in words.keys():
        color = words.get(word)[1]
        guessed_words.append(word)
        flipped_cards.append(words.get(word)[0]) # store index of guessed card
        words.pop(word)
        remaining_picks = 3
        cards.flip_cards(flipped_cards, initial)
        cards.show_pic("./flipped.png")
        while (remaining_picks > 0):
            if remaining_picks < 3:
                cards.flip_cards(flipped_cards, initial)
                cards.show_pic("./flipped.png")
            if color == current["team"]:
                remaining_picks -= 1
                current["cards"] -= 1
                print(f"{word} is a {color} team word!") 
                if current["cards"] == 0:
                    print(f"{current['team']} won!")
                    game_over()
                print(f"{current['team']} has {remaining_picks} picks left")
                if remaining_picks == 0:
                    print(f"{next['team']}\'s turn")
                    temp = current
                    current = next
                    next = temp
                    break
                while True:
                    print(f"{current['team']} has {current['cards']} cards left\n{next['team']} has {next['cards']} cards left")
                    word = input(f"enter word for {current['team']} team: ")
                    word = word.upper()
                    color = ""
                    if word in words.keys():
                        color = words.get(word)[1]
                        guessed_words.append(word)
                        flipped_cards.append(words.get(word)[0]) # store index of guessed card
                        words.pop(word)
                        break
                    elif word in guessed_words:
                        print("word already guessed!")
                    else:
                        print("not a valid input!")
                    continue
            elif color == next["team"]:
                next["cards"] -= 1
                print(f"{word} is a {color} team word!")
                if next["cards"] == 0:
                    print(f"{next['team']} won!")
                    game_over()
                print(f"{next['team']}\'s turn")
                temp = current
                current = next
                next = temp
                break
            elif color == "neutral":
                print(f"{word} is a neutral word!")
                print(f"{next['team']}\'s turn")
                temp = current
                current = next
                next = temp
                break
            elif color == "black":
                print(f"{current['team']} loses!")
                game_over()
            elif color == "":
                word = input(f"enter word for {current['team']} team: ")
                if word in words.keys():
                    color = words.get(word)[1]
                    continue
                else:
                    print(f"not a valid input!")
                    print(f"{next['team']}\'s turn")
                    break
    elif word in guessed_words:
        print("word already guessed!")
    else:
        print("not a valid input!") 