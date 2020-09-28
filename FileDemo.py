
def main():
    file = open("Silly.txt", 'r')
    all_of_file = file.readlines()
    print(all_of_file)

def reverser():
    rev_file = open("Reversable.txt", 'r')
    all_lines = rev_file.readlines()
    to_insert = all_lines[0]
    print(f"welcome to {to_insert}, Fantastic Student")

def slice():
    question1a = "go to the store"
    question1b = "Sufferin' Succotash!"
    answer1b = question1b.replace("S", "Th")
    print(answer1b)
    answer1a = question1a[:10] + question1a[11:]
    print(answer1a)

# main()
#reverser()
slice()