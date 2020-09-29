import random

def main():
    file = open("Silly.txt", 'r')
    all_of_file = file.readlines()
    random_line = random.choice(all_of_file)
    print(random_line)

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

def list():
    mylist = ["apples", "bananas", "pears", "oranges", "peaches"]
    print(mylist)
    slice1 = mylist[1] + ", " + mylist[2]
    print(slice1)
    for item in mylist:
        print(f"Eat {item} this year")

main()
#reverser()
#slice()
#list()