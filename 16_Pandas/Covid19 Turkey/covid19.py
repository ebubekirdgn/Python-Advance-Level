import pandas as pd
import numpy as np

confirmed_df = pd.read_csv("worldometer_coronavirus_daily_data.csv")
confirmed_df = confirmed_df.groupby(["country"]).aggregate(np.sum).T
confirmed_df.index.name ="date"
confirmed_df.

print(confirmed_df.head())