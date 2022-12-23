#%%
from turtle import distance
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, f1_score
from sqlalchemy import create_engine 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsRegressor
from sklearn import svm
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from statsmodels.datasets.longley import load_pandas
import seaborn as sns
import lightgbm as lgb

load_dotenv()

def min_max_normalize(lst):
    normalized = []
    
    for value in lst:
        normalized_num = (value - min(lst)) / (max(lst) - min(lst))
        normalized.append(normalized_num)
    
    return normalized

#engine = create_engine(f"mysql+pymysql://{os.getenv('dbus')}:{os.getenv('dbpw')}@{os.getenv('dbip')}/{os.getenv('dbnm')}")

#conn = engine.connect()

'''figs_df = pd.read_sql("SELECT * FROM RawInfo;",conn)
target = pd.read_sql("SELECT * FROM ProcessedInfo;",conn)
figs_df.drop('Username', axis=1, inplace=True)
#figs_df.drop('KeywordID', axis=1, inplace=True)
figs_df.drop('CategoryID', axis=1, inplace=True)
figs_df.drop(labels=range(792, 801), inplace=True)
target_df = target[['Real_Influence']]'''
#print(figs_df)
#print(target_df)


df = pd.read_excel("testinput2.xlsx", names=['id', 'follower', 'following', 'likes', 'comments', 'ER', 'f/f', 'c/l', 'l/f', 'c/f', 'score', 'roundscore'])
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.drop('id', axis=1, inplace=True)

print(df)


figs_df = df.drop('score', axis=1)
figs_df = df.drop('roundscore', axis=1)
#figs_df.drop('f/f', axis=1, inplace=True)
figs_df.drop('l/f', axis=1, inplace=True)
figs_df.drop('c/f', axis=1, inplace=True)
#figs_df.drop('c/l', axis=1, inplace=True)
#figs_df.drop('ER', axis=1, inplace=True)
figs_df.drop('following', axis=1, inplace=True)


figs_df = StandardScaler().fit_transform(figs_df)
pca = PCA(n_components=1) # 주성분을 몇개로 할지 결정
printcipalComponents = pca.fit_transform(figs_df)
figs_df = pd.DataFrame(data=printcipalComponents, columns = ['principal component1'])

print(figs_df)

target_df = df[['score']]
#target_df.dropna(inplace=True)

print(target_df)

#다중공선성 분석
'''df = pd.concat([figs_df, target_df], axis=1)

sns.pairplot(figs_df)
plt.show()'''

'''cmap = sns.light_palette("black", as_cmap=True)
sns.heatmap(figs_df.corr(), annot=True, fmt='3.1f', cmap=cmap)
plt.show()'''
#print(figs_df)

training_data, validation_data , training_labels, validation_labels = train_test_split(figs_df, target_df, test_size = 0.2, random_state=100)


#LGBM
'''params = {
    'task': 'train', 
    'boosting': 'gbdt',
    'objective': 'regression',
    'num_leaves': 10,
    'learnnig_rage': 0.05,
    'metric': {'l2','l1'},
    'verbose': -1
}

model = lgb.train(params,
                 train_set=training_data,
                 valid_sets=training_labels,
                 early_stopping_rounds=30)

y_pred = model.predict(validation_data)
print("Validation F1 score: ", f1_score(y_pred, validation_labels, average='macro'))'''
 


#회귀모델

gb = GradientBoostingRegressor(n_estimators=16, max_depth=4)
gb.fit(training_data, np.ravel(training_labels))
gb_score = gb.score(validation_data, np.ravel(validation_labels))
gb_mabe = mean_absolute_error(validation_data, validation_labels)
gb_r2 = r2_score(validation_data.astype(int), validation_labels.astype(int))
gb_msqe = mean_squared_error(validation_data, validation_labels)
print(f"mabe: {gb_mabe}")
print(f"r2: {gb_r2}")
print(f"msqe: {gb_msqe}")
print(f"boosting score: {gb_score}")
l = LinearRegression()
l.fit(training_data, training_labels)
l_score = l.score(validation_data, validation_labels)
print(f"linear score: {l_score}")

'''
knn = KNeighborsRegressor(n_neighbors = 17, weights="distance")
knn.fit(training_data, training_labels)
knn_score = knn.score(validation_data, np.ravel(validation_labels))
print(f"knn score: {knn_score}")

lasso = Lasso()
lasso.fit(training_data, training_labels)
lasso_score = lasso.score(validation_data, validation_labels)
print(f"lasso score: {lasso_score}")

svm = svm.SVR()
svm.fit(training_data, training_labels)
svm_score = svm.score(validation_data, validation_labels)
print(f"svm score: {svm_score}")'''

'''fr = RandomForestRegressor()
fr.fit(training_data, np.ravel(training_labels))
fr_score = fr.score(validation_data, np.ravel(validation_labels))
print(f"forest score: {fr_score}")'''


'''x = np.arange(4)
plt.bar(x, score_board)
plt.xticks(x, regressions)
plt.show()'''

'''machine = fr #gb

#하이퍼파리미터튜닝
params = {
    'n_estimators': [10, 20, 30, 40],
    'max_depth': [2, 3, 4, 5],
    'min_samples_leaf': [8, 12, 18],
    'min_samples_split': [8, 16, 20],
    #'learning_rate': [0.001, 0.01, 0.1] 
}

grid_cv = GridSearchCV(machine, param_grid=params, cv=2, verbose=1)
grid_cv.fit(training_data, np.ravel(training_labels))

print("Optimal parameters: ", grid_cv.best_params_)
print("Higest score: ", grid_cv.best_score_)
op_score = grid_cv.score(validation_data, np.ravel(validation_labels))
print(f"optimal score: {op_score}")'''


'''
train_acc = []
test_acc = []
#gradient boosting n_estimators 선택
params = #np.linspace(0.1, 1.0, 10, endpoint=True) #range(2,40,2)#
for param in params:
    accu = GradientBoostingRegressor(n_estimators=param)
    accu.fit(training_data, training_labels)
    #train_acc.append(accu.score(validation_data,validation_labels))
    test_acc.append(accu.score(validation_data,validation_labels))

plt.figure(figsize = (20,10))
plt.plot(params, test_acc, label="test", marker='o')
plt.ylabel('accuracy')
plt.xlabel('max_depth')
plt.show()'''

# %%
