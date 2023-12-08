import numpy as np
import pandas as pd
import tensorflow as tf
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    try:
        df = pd.read_csv("../backend/Datasets/COALINDIA.csv")
        plot = sns.pairplot(df)
        plt.savefig('pairplot.png')
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    main()
