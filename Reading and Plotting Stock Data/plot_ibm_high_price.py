"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/IBM.csv")
    plt.plot(df["High"])
    plt.title("IBH High Price")
    # TODO: Your code here
    plt.axis([0,3300,20,220])
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()
