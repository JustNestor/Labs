english_letters = "abcdefghijklmnopqrstuvwxyz"
ukr_letters = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя"


def main():
    text = input("Введіть текст: ").lower()
    runtype = input("Виберіть як запустити програму(*1*/2): ")

    chars = ""

    if runtype in "1 ":
        lang = input("Виберіть мову(*us*/ua): ")
        chardict = dict()

        if lang in "us1 ":
            chars = english_letters
        elif lang in "ua2":
            chars = ukr_letters
        else:
            print("Така мова не підтримується!")
            main()

        print(f"\nКількість символів: {len(text)}\n")

        for char in chars.lower():
            chardict[char] = 0

        for char in text:
            if char in chars:
                chardict[char] += 1

        for key, value in chardict.items():
            print(f"Кількість букв '{key}': {value}")

    elif runtype == "2":
        words = text.split(" ")

        dictlist = [word.lower() for word in words if len(word) > 3]
        dictlist = sorted(set(dictlist))

        print(dictlist)

        for num, word in enumerate(dictlist):
            print(f"{num+1}. {word}")

    else:
        print("Не правильний режим!")
        main()


if __name__ == "__main__":
    main()

"""
а
програма рахує загальну кількість символів, показує скільки яких букв
б
зробити словник слів(посортувати в алфавітному порядку)(слово >3)(англ укр)
"""
