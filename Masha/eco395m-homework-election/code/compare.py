import os

import pandas as pd

REPORT_PATH = os.path.join("artifacts", "election_report.csv")
PANDAS_REPORT_PATH = os.path.join("artifacts", "election_report_pandas.csv")

if __name__ == "__main__":

    df = pd.read_csv(REPORT_PATH)
    pd_df = pd.read_csv(PANDAS_REPORT_PATH)

    print(df.equals(pd_df))
