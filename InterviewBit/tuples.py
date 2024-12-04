def main():
    tuple1 = tuple(("one", "two", "three"))
    tuple2 = tuple(("1", "2", "3"))

    # change value at index 0 of both tuple to string "number"
    # Your code goes here
    tuple1 = ("number",) + tuple1[1:]
    tuple2 = ("number",) + tuple2[1:]

    print(tuple1)
    print(tuple2)

    return 0


if __name__ == "__main__":
    main()
