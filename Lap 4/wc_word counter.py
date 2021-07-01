#
#       Sergio Munguia
#
#
#       Data.txt file word counter


def main():

    text = open ("data.txt", 'r')
    lines = list(text)
    text.close()
    words_all = 0
    for line in lines:
        words_all = words_all + len(line.split())
    print ("Total words:   ", words_all)

main()
