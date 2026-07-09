from util import *
n = int(input())
lst = []

for i in range(n):
    command = input().split()

    if command[0] == "insert":
        insert_no(lst, int(command[1]), int(command[2]))
    elif command[0] == "append":
        append_no(lst, int(command[1]))
    elif command[0] == "remove":
        remove_no(lst, int(command[1]))
    elif command[0] == "sort":
        sort_list(lst)
    elif command[0] == "pop":
        pop_no(lst)
    elif command[0] == "reverse":
        reverse_list(lst)
    elif command[0] == "print":
        print_list(lst)
    else:
        print("Not a valid command")
