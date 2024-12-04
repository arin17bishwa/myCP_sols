import numpy as np


def main():
    arr = [1, 3, 2, 2, 5, 3, 8, 2]

    # Convert the above array into ndarray
    arr = np.array(arr)

    print(type(arr))

    # Use where to find all the indexes of 2
    x = np.where(arr == 2)

    print(x)
    return 0


if __name__ == "__main__":
    main()
