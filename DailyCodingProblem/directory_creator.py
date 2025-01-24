import os, argparse
import sys


def main(date_arg: str):
    if not date_arg:
        raise ValueError("Date can not be null.")
    if not len(date_arg) == 8:
        raise ValueError("Date must be of 8 characters")
    if not all(i.isdigit() for i in date_arg):
        raise ValueError("Date must be all digits")

    func(date_arg)


def func(date_str: str) -> None:
    dcp_dir_path = os.path.dirname(__file__)
    date_dir_path = os.path.join(dcp_dir_path, date_str)
    if os.path.exists(date_dir_path):
        print(f"Directory named |{date_str}| already exists. Ignoring.")
        sys.exit(0)

    # create base date directory
    os.mkdir(date_dir_path)

    # create IO directories
    input_files_dir_path = os.path.join(date_dir_path, "inputs")
    output_files_dir_path = os.path.join(date_dir_path, "outputs")
    os.mkdir(input_files_dir_path)
    os.mkdir(output_files_dir_path)

    # create main code file and sample IO files
    for file_path in map(
        lambda x: os.path.join(*x),
        [
            [date_dir_path, f"{date_str}.py"],
            [input_files_dir_path, "000.txt"],
            [output_files_dir_path, "000.txt"],
        ],
    ):
        with open(file_path, "w") as fp:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("date")
    args = parser.parse_args()
    main(args.date)
