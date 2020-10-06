import random

def main():
    file = open("Silly.txt", 'r')
    all_of_file = file.readlines()
    random_line = random.choice(all_of_file)
    print(random_line)

def reverser():
    rev_file = open("Reversable.txt", 'r')
    all_lines = rev_file.readlines()
    to_reverse = all_lines[1]
    backwards = ""
    for char in to_reverse:
        backwards = f"{char}{backwards}"
    print(f"Reversing string gives you {backwards}")

def slice():
    question1a = "go to the store"
    question1b = "Sufferin' Succotash!"
    answer1b = question1b.replace("S", "Th")
    print(answer1b)
    answer1a = question1a[:10] + question1a[11:]
    print(answer1a)
    # could have also done print(question1a.replace("s", ""))

def list():
    mylist = ["apples", "bananas", "pears", "oranges", "peaches"]
    print(mylist)
    slice1 = mylist[1] + ", " + mylist[2]
    print(slice1)
    for item in mylist:
        print(f"Eat {slice1} this year")

def string_formatting():
    result = 100/3
    formatted_number = "{:5.3f}".format(result)
    print(f"the result is {formatted_number}")

def statement():
    file = open("Silly.txt", 'r')
    all_of_file = file.readlines()
    counter = 1
    for line in all_of_file:
        if counter%2 == 1:
            print(line)
        else:
            pass
        counter += 1

#statement()
#main()
reverser()
#slice()
#list()
#string_formatting()