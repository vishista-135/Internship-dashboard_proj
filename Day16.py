import pandas as pd


df = pd.read_csv('Salaries.csv')

type(df)

df.shape

df.head()

df.tail(2)

df.sample(3)

df['rank']

df['salary']

#df('rank')

df[['rank','salary']]

df['rank'].unique()

df['rank'].value_counts(normalize = True)


df['sex'].unique()

df['salary'].max()
df['salary'].min()
df['salary'].mean()

