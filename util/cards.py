import os
import shutil
import random
from PIL import Image, ImageDraw, ImageFont

def generate_cards(text, index, colour):
    width = 1024 // 5
    height = 768 // 5
    if colour == "black":
        color = (0, 0, 0)
    elif colour == "red":
        color = (255, 87, 51)
    elif colour == "blue":
        color = (51, 85, 255)
    elif colour == "neutral":
        color = (173, 174, 136)
    card = Image.new(mode='RGB', size=(width, height), color=color)
    font = ImageFont.truetype("arial.ttf", 25)
    d = ImageDraw.Draw(card)
    w = card.width // 2
    h = card.height // 2
    d.text(xy=(w, h), text=text, font=font, fill=(255, 255, 255, 128), anchor="mm")
    card.save(f"./images/answer-{index}-{colour}.png", "PNG")

def generate_prompt(text, index):
    width = 1024 // 5
    height = 768 // 5
    card = Image.new(mode='RGB', size=(width, height), color=(246, 247, 212))
    font = ImageFont.truetype("arial.ttf", 25)
    d = ImageDraw.Draw(card)
    w = card.width // 2
    h = card.height // 2
    d.text(xy=(w, h), text=text, font=font, fill=(0, 0, 0, 128), anchor="mm")
    card.save(f"./images/prompt-{index}.png", "PNG")

def assign_cards():
    words = []
    assigned = {}
    with open("./codenames.txt") as f:
        code = f.read()
        for word in code.split("\n"):
            words.append(word)
        teams = ["red", "blue"]
        random.shuffle(teams)
        starting_team = teams[0]
        other_team = teams[1]
        random.shuffle(words)
        for i, word in enumerate(words):
            if (i == 0):
                assigned.update({word: [i, "black"]})
            elif (i < 10):
                assigned.update({word: [i, starting_team]})
            elif (i < 18):
                assigned.update({word: [i, other_team]})
            elif (i < 25):
                assigned.update({word: [i, "neutral"]})
            else:
                break
        for index, (word, detail) in enumerate(assigned.items()):
            color = detail[1]
            # print(f"{index}: {word}, {color} ")
            generate_cards(text=word, index=index, colour=color)
            generate_prompt(text=word, index=index)
        return starting_team, other_team, assigned

def open_image(path):
    cards = []
    for _, _, files in os.walk(path):
        for file in files:
            cards.append(file)
    return cards

def save_pic(list, type, background, width, height):
    w = 0
    h = 0
    for i in range(5):
        for j in range(5):
            background.paste(list[5*i+j], (w, h))
            w += width
        background.paste(list[i], (w, h))
        h += height
        w = 0
    background.save(f"{type}.png", "PNG")
    return background

def show_pic(pic):
    with Image.open(f"./{pic}") as p:
        p.show()

def merge_cards():
    cards = open_image("./images/")
    width = 0
    height = 0
    with Image.open(f"./images/{cards[0]}") as ref:
        width = ref.width
        height = ref.height
    bg = Image.new(mode="RGB", size=(5*width, 5*height), color=(0, 0, 0))
    types = ["answer", "prompt"]
    z = []
    for type in types:
        images = [Image.open(f"./images/{card}").convert("RGBA") for card in cards if type in card]
        z.append(images)
    zipped = list(zip(z[0], z[1]))
    random.shuffle(zipped)
    answer, prompt = zip(*zipped)
    save_pic(list=answer, type="answer", background=bg, width=width, height=height)
    save_pic(list=prompt, type="prompt", background=bg, width=width, height=height)
    return prompt

def clear_directory():
    for root, dirs, files in os.walk('./images/'):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))

def flip_cards(flipped, init):
    # i need a function that shows the color of the card passed in the argument and show it in a 5x5 grid along with all unflipped cards
    # Use the index of words to differentiate if the card is flipped, and merging an image tgt again and then show; Btw forgive me for the mess i'm not use to object-orientated coding
    cards = open_image("./images/")
    width = 0
    height = 0
    with Image.open(f"./images/{cards[0]}") as ref:
        width = ref.width
        height = ref.height
    bg = Image.new(mode="RGB", size=(5*width, 5*height), color=(0, 0, 0))
    # all_cards = [Image.open(f"./images/{card}").convert("RGBA") for card in cards if "prompt" in card]
    init_list = list(init)
    for index in flipped:
        for card in cards:  
            temp_card = card.split("-")[1]
            if (temp_card == str(index) and "answer" in card):
                # print(index)
                prompt_card = Image.open(f"./images/prompt-{index}.png").convert("RGBA")
                # print(prompt_card)
                position = init_list.index(prompt_card)
                init_list[position] = Image.open(f"./images/{card}").convert("RGBA")
    save_pic(list=init_list, type="flipped", background=bg, width=width, height=height)
        
