import esgrammar
import os


def clear_console():
    os.system("clear")


words_analyzed = []

while True:
    clear_console()
    print(
        """++++Menu++++
1) Enter a words.
2) Show words with type.
3) Exit.""")
    try:
        option = int(input("> "))
    except:
        option = 0

    if option == 1:
        clear_console()
        print("Enter a words splited by space:")
        words = input().split(" ")

        words_analyzed = esgrammar.analyze(words)

    if option == 2:
        clear_console()

        for i, itm in enumerate(words_analyzed):
            type = ""
            word = words[i]

            if itm["type"] == 1:
                type = "Aguda"
            elif itm["type"] == 2:
                type = "Grave"
            elif itm["type"] == 3:
                type = "Esdrújula"
            elif itm["type"] == 4:
                type = "Sobrésdrujula"

            print(f"""Word: {word}
Syllables: {itm["syllables"]}
Tone syllable: {itm["tone_syllable"]}
Vowels: {itm["vowels"]}
Consonants: {itm["consonants"]}
Type: {type}""")
            print("----------------------")

        input()

    elif option == 3:
        exit()

    elif option == 4:
        print(words_analyzed)
        input()

    else:
        pass
