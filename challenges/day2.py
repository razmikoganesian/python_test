from encodings import utf_8
from fileinput import filename
import textwrap

name = input("Enter your name:  ").strip()
profession = input("What is your profession:  ").strip()
passion = input("What is your passion: ").strip()
emoji = input("Favourite emoji:  ").strip()
website = input("Do you have a website? Please indicate : ").strip()

print("\n Choose yoor style: ")
print("1 - Simple lines ")
print("2 - Vertical flair")
print("3 - Emoji sandwich ")

style = input("Enter 1 or 2 or 3 to choose a style  ").strip()


def bio_generator(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n ✅. {passion} \n {website}"
    elif style == "2":
        return f"{emoji} {name} 😎 | {profession} \n {passion} \n {website}"
    elif style == "3":
        return f"{emoji*3} {name} 😜 | {profession} \n {passion} \n {website} \n favourite emoji {emoji}"
    
bio = bio_generator(style)
print(f"Your stylish bio {bio}")
print("*" * 40)
print(textwrap.dedent(bio))
print("*" * 40)

save = input("Do you want to save this bio into text? (y/n):  ").lower()

if save == "y":
    filename = f"{name.lower().replace(" ", "_")}_bio.txt"
    with open(filename, "w", encoding="utf_8") as f:
        f.write(bio)
    print("File saved!")

