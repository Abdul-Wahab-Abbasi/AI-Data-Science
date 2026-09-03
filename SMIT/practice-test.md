# Practice Test — NumPy & Pandas

**Topics:** NumPy (numerical analysis, probability) • Pandas (Series, DataFrame)

> Try to solve every question first **without** running code. Then check the
> **Answer Key** at the bottom and verify by running the snippets in a notebook.

---

## Section A — NumPy: Numerical Analysis

**A1.** Create a NumPy array of the numbers 10 to 50 (inclusive) and print its
`shape`, `size`, `ndim`, and `dtype`.

**A2.** Given `a = np.array([4, 8, 15, 16, 23, 42])`, compute the **sum**,
**mean**, **median**, **standard deviation**, and **variance**.

**A3.** What is the difference between `np.sum(m, axis=0)` and
`np.sum(m, axis=1)` for a 2-D array `m`? Give the output shape for a `(3, 4)`
array.

**A4.** Given `arr = np.array([3, 1, 7, 2, 9, 4])`, find:
(a) the index of the maximum value, (b) the index of the minimum value,
(c) the array sorted in ascending order.

**A5.** Use `np.cumsum` and `np.diff` on `np.array([2, 5, 9, 14])`. What does
each return, and why does `diff` have one fewer element?

**A6.** Reshape `np.arange(12)` into a `(3, 4)` matrix, then compute the
**mean of each column** and the **max of each row**.

**A7.** From `data = np.array([12, 7, 22, 3, 18, 9])`, use **boolean masking**
to (a) select all values greater than 10, and (b) count how many values are
even.

**A8.** Explain **broadcasting**. What is the result of
`np.array([1, 2, 3]) * 10`? And of `np.array([[1], [2], [3]]) + np.array([10, 20, 30])`?

**A9.** Create a 3×3 identity matrix and a 3×3 matrix of all sevens without
typing the numbers manually.

**A10.** Given monthly sales `s = np.array([120, 90, 200, 175, 60, 145])`,
compute the **total**, the **average**, and the **percentage each month
contributes** to the total.

---

## Section B — NumPy: Probability

**B1.** What does `np.random.seed(0)` do, and why is it useful when testing
probability code?

**B2.** Generate 5 random integers between 1 and 6 (inclusive) to simulate
dice rolls.

**B3.** Generate a `(2, 3)` array of random floats between 0 and 1 using
`np.random.rand`.

**B4.** Use `np.random.choice` to pick 10 random samples from
`['red', 'green', 'blue']`. How would you make `red` twice as likely as the
others?

**B5.** Simulate rolling a die **1000 times**. Estimate the probability of
rolling a 6 and compare it to the theoretical value (1/6).

**B6.** What is the difference between `np.random.rand`, `np.random.randn`, and
`np.random.randint`?

**B7.** Simulate flipping a fair coin 1000 times (0 = tails, 1 = heads) and
report the proportion of heads.

**B8.** Generate 10,000 samples from a **normal distribution** with mean 50 and
standard deviation 5. Report the sample mean and std — are they close to 50 and 5?

**B9.** You roll two dice. Using simulation (100,000 trials), estimate the
probability that the **sum equals 7**.

**B10.** From `np.random.randint(0, 100, 20)`, estimate the probability that a
value drawn is greater than 75.

---

## Section C — Pandas: Series

**C1.** Create a Pandas Series from the list `[10, 20, 30, 40]` with custom
index labels `['a', 'b', 'c', 'd']`.

**C2.** Given `s = pd.Series([5, 15, 25], index=['x', 'y', 'z'])`, how do you
access the value at label `'y'` and the value at position `0`?

**C3.** What is the difference between a Pandas **Series** and a NumPy 1-D array?

**C4.** Create a Series from the dictionary `{'Mon': 100, 'Tue': 80, 'Wed': 120}`.
What becomes the index?

**C5.** Given `s = pd.Series([3, 8, 1, 9, 4])`, use a boolean condition to
select all values greater than 4.

**C6.** For `s = pd.Series([10, 20, 30])`, what does `s * 2` return? What about
`s + pd.Series([1, 2, 3])`?

**C7.** How do you find the `sum`, `mean`, `max`, and `min` of a Series? How do
you get all descriptive statistics at once?

---

## Section D — Pandas: DataFrame

**D1.** Create a DataFrame from this dictionary and print it:
```python
{'Name': ['Tom', 'Nick', 'Krish'], 'Age': [20, 21, 19]}
```

**D2.** What is the difference between `df.head()`, `df.tail()`, `df.shape`,
and `df.info()`?

**D3.** Given a DataFrame `df` with columns `Name` and `Age`, how do you select
(a) just the `Age` column, and (b) both columns?

**D4.** How do you read a CSV file into a DataFrame? How do you read only the
first 5 rows after loading?

**D5.** For a DataFrame `df`, how do you filter all rows where `Age > 20`?

**D6.** How do you add a new column `Passed` that is `True` when `Marks >= 50`
and `False` otherwise?

**D7.** What does `df.describe()` return, and which column types does it
summarize by default?

**D8.** Given the DataFrame below, compute the average `Age` and find the name
of the oldest person:
```python
{'Name': ['A', 'B', 'C'], 'Age': [30, 25, 40]}
```

---

## ✅ Answer Key

### Section A — NumPy Numerical Analysis
```python
import numpy as np

# A1
a = np.arange(10, 51)
print(a.shape, a.size, a.ndim, a.dtype)   # (41,) 41 1 int64

# A2
a = np.array([4, 8, 15, 16, 23, 42])
a.sum(), a.mean(), np.median(a), a.std(), a.var()
# 108, 18.0, 15.5, 12.30..., 151.33...

# A3  axis=0 -> collapses rows (per-column), shape (4,)
#     axis=1 -> collapses cols (per-row),  shape (3,)

# A4
arr = np.array([3, 1, 7, 2, 9, 4])
arr.argmax()      # 4  (value 9)
arr.argmin()      # 1  (value 1)
np.sort(arr)      # [1 2 3 4 7 9]

# A5
np.cumsum([2, 5, 9, 14])   # [ 2  7 16 30]  running total
np.diff([2, 5, 9, 14])     # [3 4 5]  differences; n-1 because it pairs neighbours

# A6
m = np.arange(12).reshape(3, 4)
m.mean(axis=0)    # column means -> [4. 5. 6. 7.]
m.max(axis=1)     # row maxes    -> [ 3  7 11]

# A7
data = np.array([12, 7, 22, 3, 18, 9])
data[data > 10]           # [12 22 18]
np.sum(data % 2 == 0)     # 2  (12 and 22... and 18) -> actually 3: 12,22,18

# A8  Broadcasting stretches smaller shapes to match:
np.array([1, 2, 3]) * 10                       # [10 20 30]
np.array([[1],[2],[3]]) + np.array([10,20,30]) # 3x3 grid of sums

# A9
np.eye(3)          # identity
np.full((3, 3), 7) # all sevens

# A10
s = np.array([120, 90, 200, 175, 60, 145])
s.sum()                  # 790
s.mean()                 # 131.66...
s / s.sum() * 100        # percentage contribution of each month
```
> Note A7(b): 12, 22, and 18 are even → the count is **3**.

### Section B — NumPy Probability
```python
# B1  Fixes the random generator so results are reproducible (same output every run).

# B2
np.random.randint(1, 7, 5)          # e.g. [3 6 1 4 2]  (high is exclusive -> use 7)

# B3
np.random.rand(2, 3)                 # 2x3 floats in [0, 1)

# B4
np.random.choice(['red','green','blue'], 10)
np.random.choice(['red','green','blue'], 10, p=[0.5, 0.25, 0.25])  # red twice as likely

# B5
rolls = np.random.randint(1, 7, 1000)
np.mean(rolls == 6)                  # ~0.16, close to 1/6 = 0.1667

# B6  rand -> uniform [0,1);  randn -> standard normal (mean 0, std 1);
#     randint -> random integers in a range.

# B7
flips = np.random.randint(0, 2, 1000)
flips.mean()                         # ~0.5

# B8
x = np.random.normal(50, 5, 10000)
x.mean(), x.std()                    # ~50 and ~5

# B9
d1 = np.random.randint(1, 7, 100000)
d2 = np.random.randint(1, 7, 100000)
np.mean(d1 + d2 == 7)                # ~0.1667 (6/36)

# B10
vals = np.random.randint(0, 100, 20)
np.mean(vals > 75)                   # proportion above 75
```

### Section C — Pandas Series
```python
import pandas as pd

# C1
pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# C2
s = pd.Series([5, 15, 25], index=['x', 'y', 'z'])
s['y']      # 15  (label-based)
s.iloc[0]   # 5   (position-based)

# C3  A Series has an *index* (labels) and can hold a name; a NumPy array is
#     just raw values with positions. Series is built on top of a NumPy array.

# C4
pd.Series({'Mon': 100, 'Tue': 80, 'Wed': 120})   # dict keys become the index

# C5
s = pd.Series([3, 8, 1, 9, 4])
s[s > 4]                                          # 8 and 9

# C6
pd.Series([10, 20, 30]) * 2                       # [20 40 60]
pd.Series([10, 20, 30]) + pd.Series([1, 2, 3])    # aligns by index -> [11 22 33]

# C7
s.sum(); s.mean(); s.max(); s.min()
s.describe()                                      # count, mean, std, min, quartiles, max
```

### Section D — Pandas DataFrame
```python
# D1
df = pd.DataFrame({'Name': ['Tom', 'Nick', 'Krish'], 'Age': [20, 21, 19]})

# D2  head() -> first 5 rows; tail() -> last 5 rows;
#     shape -> (rows, cols) tuple; info() -> columns, dtypes, non-null counts.

# D3
df['Age']            # (a) single column -> a Series
df[['Name', 'Age']]  # (b) list of columns -> a DataFrame

# D4
df = pd.read_csv('data.csv')
df.head()            # first 5 rows

# D5
df[df['Age'] > 20]

# D6
df['Passed'] = df['Marks'] >= 50

# D7  describe() -> count, mean, std, min, 25%, 50%, 75%, max for numeric columns.

# D8
df = pd.DataFrame({'Name': ['A', 'B', 'C'], 'Age': [30, 25, 40]})
df['Age'].mean()                    # 31.67
df.loc[df['Age'].idxmax(), 'Name']  # 'C'  (oldest)
```

### Section E — Missed Concepts (from class quiz)
```python
# E1  "evenly spaced" -> linspace (NOT random.rand)
np.linspace(0, 1, 5)      # [0.  , 0.25, 0.5 , 0.75, 1.  ]
np.linspace(0, 100, 6)    # [  0.,  20.,  40.,  60.,  80., 100.]

# E2  a 1-D array's shape is a one-element tuple
np.array([1, 2, 3]).shape     # (3,)      <- 1-D
np.array([[1, 2, 3]]).shape   # (1, 3)    <- 2-D row (extra brackets)

# E3  select a column with brackets; there is no .column()
df = pd.DataFrame({'Name': ['A', 'B'], 'Age': [30, 25]})
df['Age']     # bracket notation -> Series
df.Age        # attribute notation -> same Series

# E4  Pandas sorts with sort_values / sort_index (NOT plain sort)
df = pd.DataFrame({'Name': ['A', 'B', 'C'], 'Age': [30, 25, 40]})
df.sort_values(by='Age')   # rows reordered 25, 30, 40
df.sort_index()            # back to original row order

# E5  dtypes = types per column (attribute);  columns = the names
df.dtypes     # Name: object, Age: int64
df.columns    # Index(['Name', 'Age'], dtype='object')

# E6  drop_duplicates removes rows; unique() is for ONE Series
df = pd.DataFrame({'Name': ['A', 'B', 'A'], 'Age': [30, 25, 30]})
df.drop_duplicates()   # drops the repeated ('A', 30) row
df['Name'].unique()    # ['A' 'B']  (distinct values of one column)
```
> Memory hook: `linspace`=evenly spaced • 1-D shape=`(n,)` • `df['col']` not `df.column()`
> • `sort_values` not `sort` • `dtypes` not `columns.dtype` • `drop_duplicates` (rows) vs `unique` (Series).

---

**Study tip:** Re-do each coding answer from a blank cell without looking. If you
can reproduce A2, A4, A6, B5, B9, C5, D5–D6, and **all of Section E** from memory,
you're in good shape. Good luck! 🎯
