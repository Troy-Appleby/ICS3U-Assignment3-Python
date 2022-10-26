# Copyright (c) 2022 Troy Appleby All rights reserved.
#
# Created by: Troy Appleby
# Created on: October 2022
# This program sees if the shape is a square


def main():

    # input and variables

    length = int(input("input the length of your shape: "))
    width = int(input("input the width of your shape: "))

    # process and output
    if length == width:
        print("\nThe shape is a square.")
    elif length != width:
        print("\nThe shape is a rectangle.".format(length))

    print("\nDone.")


if __name__ == "__main__":
    main()
