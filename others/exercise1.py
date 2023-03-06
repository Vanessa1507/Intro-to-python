import numpy as np
import pandas as pd

# Series
s = pd.Series([1,2,3, np.nan, 6, 8])
print(s)
"""
0    1.0
1    2.0
2    3.0
3    NaN
4    6.0
5    8.0
"""

# Dates
"""
date_range(): Let us to label the columns
"""
dates = pd.date_range("20130101", periods=6)
# print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))
print(df)

# Dictionary
"""
  Dictionaries can be converted into a series-like:
  The key is going to be the name of each column
  An the values of each key will be the values on each row
"""
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

# Data frame 
print(df2)
"""
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""
print(df2.dtypes)
"""
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
"""

# print(df.head())
# print(df.tail(3))
# print(df.index)
# print(df.columns)
# print(df.to_numpy())
# print(df.describe())