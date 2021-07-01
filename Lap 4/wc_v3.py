#
#
#   wc_v3
#
#   counting lines, words, characters
#
#
#
#

def main():
    

    fname = open("data.txt", "r")

    num_lines = 0
    num_words = 0
    num_chars = 0

    with open(fname, 'r') as f:
        for line in f:
            words = line.split()

    num_lines += 1
    num_words += len(words)
    num_chars += len(line)

    print("The number of lines: ", num_lines)
    print("The number of words: ", num_words)
    print("The number of characters: ", num_chars)

    data.close()

main()
