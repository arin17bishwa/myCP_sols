def main():
    my_list = [["a", "b"], ["cc", "dd", ["eee", "fff"]], ["g", "h"]]

    # insert a new list [1, 2, 3] at the end of my_list
    # Your code goes here
    my_list.append([1, 2, 3])

    print(my_list)

    # Delete 'eee' from the list
    # Your code goes here
    my_list[1][2].remove("eee")

    print(my_list)
    return 0


if __name__ == "__main__":
    main()
