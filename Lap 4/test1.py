


def main():

    c = input("Please enter a phrase: ")
    b = list(c)
    a = 0
    for x in b:
        a = a + len(x.split())
    print("Your phrase has ", a, "words")

main()
