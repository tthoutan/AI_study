import pandas as pd
import os
import operator

cur_dir = os.getcwd()

df = pd.read_csv(f'{cur_dir}/lottery.csv')

result_dic = dict()

for i in range(1, 46):
        count = 0
        for row in df.values:
                for n in range(2,9):
                        if row[n] is i:
                                count+=1
        result_dic[i]=count

result_dic = sorted(result_dic.items(), key=operator.itemgetter(1), reverse=True)

for item in result_dic:
    print(f'{item[0]} -> {item[1]} times')




