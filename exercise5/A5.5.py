"""
application for solving Exercise 5.5
"""
import math

import pandas


def main():
    """
    main application
    """
    computer = pandas.read_csv("./data/GrosseKisten.csv")
    processor = pandas.read_csv("./data/Prozessoren.csv")
    computer["FLOPS"] = computer["FLOPS"].apply(lambda x: math.log10(x))
    processor["FLOPS"] = processor["FLOPS"].apply(lambda x: math.log10(x))
    print(computer)
    print(processor)


if __name__ == "__main__":
    main()
