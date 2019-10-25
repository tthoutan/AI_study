import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

## assign current directory to read lottery.csv file
cur_dir = os.getcwd()

## read lotter.csv file and then assign to df variable (DataFrame Object)
df = pd.read_csv(f'{cur_dir}/lottery.csv')

## this variable is DataFrame object that I am going to use as feature of KMeans
feature_first = df[['first', 'fifth']]

## Make KMenas Model Object, the number of clusters is six (because the count of lottery number to win is six)
model_first = KMeans(n_clusters=6, algorithm='auto')

## KMeans model learn The lottery number datas in My feature DataFrame 
model_first.fit(feature_first)

## based on learned data, assign clustering labeled number(0 to 5 because n_clusters is 6)
predict_first = pd.DataFrame(model_first.predict(feature_first))

## column name of clustering labeled number is predict
predict_first.columns=['predict']

## to visualize, execute concat function of pandas. to concatenate to DataFrame(data of each feature and predict value)
result = pd.concat([feature_first, predict_first], axis=1)

## draw a graph
plt.scatter(result['first'],result['fifth'],c=result['predict'],alpha=0.5)

## prepare centroid value to mark centroid into my graph
centers = pd.DataFrame(model_first.cluster_centers_,columns=['first','fifth'])
center_x = centers['first']
center_y = centers['fifth']

plt.scatter(center_x, center_y,s=50,marker='*',c='r')

print(center_x)
print(center_y)

## graph show
plt.show()
