import pandas as pd

def load_candidates():
    return pd.read_csv(r"E:\recruitment-data-pipeline\data\raw\candidates.csv")
def load_interviews():
    return pd.read_csv(r"E:\recruitment-data-pipeline\data\raw\interviews.csv")