import pyfiglet
from termcolor import colored

text = "Byte Boosters"
ascii_banner = pyfiglet.figlet_format(text, font="straight")
colored_ascii_art = colored(ascii_banner, color="red")
print(colored_ascii_art)

# Print all available fonts
print("\nAvailable fonts:")
fonts = pyfiglet.FigletFont.getFonts()
print(fonts)

# Print all available colors
print("\nAvailable colors:")
colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
print(colors)

your_text = input("Enter the text : ")
font_style = input("Choose a font style from the available fonts : ")
color = input("Choose a color from the available colors : ")
print("Your banner will look like : ")

if font_style not in fonts:
    font_style = "slant"

if color not in colors:
    color = "white"

banner = pyfiglet.figlet_format(your_text, font=font_style)
colored_banner = colored(banner, color=color)
print(colored_banner)

create_file = input("\nDo you want to create a banner.py file for the above configuration? (Y/n) : ")
if create_file in ["Y", "y", ""]:
    with open(your_text+".py", "w") as f:
        f.writelines(["import pyfiglet",
                      "\nfrom termcolor import colored",
                      "\ncolored_banner = colored(pyfiglet.figlet_format(\""+your_text+"\", font=\""+font_style+"\"), color=\""+color+"\")",
                      "\nprint(colored_banner)"
                      ])
    print("banner.py - File created successfully")
