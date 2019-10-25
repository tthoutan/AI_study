import pandas as pd
import random
import os

cur_dir = os.getcwd()

df = pd.read_csv(f'{cur_dir}/lottery.csv')

df['win']=0
df['winner_count']=0
df['avr_age']=0

l = len(df)

df['win'] = [random.randrange(0,2) for i in range(0, l)]
df['winner_count'] = [random.randrange(1, 10) for i in range(0, l)]
df['avr_age'] = [random.randrange(20,50) for i in range(0,l)]

print(df.head(20))

df.to_csv('new_col.csv')
