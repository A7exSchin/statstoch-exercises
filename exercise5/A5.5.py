"""
application for solving Exercise 5.5
"""
import math
import scipy.stats

import pandas


def main(filepath, datasetname):
    """
    main application
    """
    dataframe = pandas.read_csv(filepath)
    dataframe["FLOPS"] = dataframe["FLOPS"].apply(lambda x: math.log10(x))
    print(f"\n=== Exercise a) {datasetname} ===")
    correlation_efficiency, p_value = scipy.stats.pearsonr(dataframe["Jahr"], dataframe["FLOPS"])
    print(f"Korrelationseffizient: {correlation_efficiency}")


if __name__ == "__main__":
    main("./data/GrosseKisten.csv", "Große Kisten")
    main("./data/Prozessoren.csv", "Prozessoren")
