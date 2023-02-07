import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_para_suspender(data):
    df = pd.read_csv(data)
    df = df.dropna()
    mean_grades = df.groupby("NAME").mean()["NOTES"]
    mean_grades.plot(kind="bar")
    plt.xlabel("ALUMNAT")
    plt.ylabel("NOTES")
    plt.title("MITJA NOTA ALUMNAT CICLE LEONEL RUIZ")
    plt.show()


if __name__ == "__main__":
    plot_para_suspender("llistat.csv")


