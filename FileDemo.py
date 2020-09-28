
def main():
    file = open("Silly.txt", 'r')
    all_of_file = file.readlines()
    print(all_of_file)

def reverser():
    rev_file = open("Reversable.txt", 'r')
    all_lines = rev_file.readlines()
    to_insert = all_lines[0]
    print(f"welcome to {to_insert}, Fantastic Student")


reverser()