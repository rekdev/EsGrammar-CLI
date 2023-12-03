import esgrammar
import os


def clear_console():
    os.system("clear")


words_analyzed = []

while True:
    clear_console()
    print(
        """
++++Menu++++
1) Enter a words.
2) Show words with type.
3) Exit.""")
    option = int(input("> "))

    if option == 1:
        clear_console()
        print("Enter a words splited by space:")
        words = input()

        words_analyzed = esgrammar.analyze(words)

    if option == 2:
        clear_console()

        for itm in words_analyzed:
            type = ""

            if itm["type"] == 1:
                type = "Aguda"
            elif itm["type"] == 2:
                type = "Grave"
            elif itm["type"] == 3:
                type = "Esdrújula"
            elif itm["type"] == 4:
                type = "Sobrésdrujula"

            print("----------------------")
            print(
                f"""Palabra: {itm["syllables"]}
Silaba tonica: {itm["tone_syllable"]}
Tipo: {type}""")

        input()

    elif option == 3:
        exit()
