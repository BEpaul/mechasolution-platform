import time

import pandas
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
import pandas as pd

word_dict = ["여행", "운동", "캠핑", "패션"]
category = []


def bow(document1, document2):
    document1 = str(document1)
    document2 = str(document2)

    doc_tokenized = document1.split(' ')
    doc_tokenized += document2.split(' ')

    temp = [0, 0, 0, 0]

    for word in doc_tokenized:

        if word_dict[0] in word:
            temp[0] += 1
        if word_dict[1] in word:
            temp[1] += 1
        if word_dict[2] in word:
            temp[2] += 1
        if word_dict[3] in word:
            temp[3] += 1

    return temp


#excel_data_df = pandas.read_excel('train.xlsx', sheet_name='Sheet1')
# 1510 data of accounts that are found by searching '여행'

#excel_data_df = pandas.read_excel('train_1.xlsx', sheet_name='Sheet1')
excel_data_df = pandas.read_excel('train2.xlsx', sheet_name='Sheet1')

names = []
bios = []
texts = []

feature = []
target = []

names = excel_data_df['account_id'].tolist()
bios = excel_data_df['소개글'].tolist()
texts = excel_data_df['게시글 본문'].tolist()

for bio, text in zip(bios, texts):
    bow_t = bow(bio, text)
    feature.append(bow_t)

    val = 1
    max = bow_t[0]

    for i in range(0, 4):
        if bow_t[i] > max:
            max = bow_t[i]
            val = i + 1  # labeling each account
    target.append(val)

labels = {1: '여행', 2: '운동', 3: '캠핑', 4: '패션'}

#for name, bagofword, labeling in zip(names, feature, target):
    #print(f"name: {name} / bow: {bagofword} / label: {labels[labeling]}")

feature = MinMaxScaler().fit_transform(feature)

x_train, x_test, y_train, y_test = train_test_split(feature, target, random_state=30)

range_k = range(3, 15)

scores = {}
scores_list = []
highest = 3
temp = 0

for k in range_k:
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(x_train, y_train)

    y_pred = classifier.predict(x_test)

    scores[k] = metrics.accuracy_score(y_test, y_pred)
    if scores[k] > temp:
        temp = scores[k]
        highest = k
        print(f"The highest accuracy is {round(temp * 100, 2)}% when k is {highest}")
    scores_list.append(metrics.accuracy_score(y_test, y_pred))

result1 = metrics.classification_report(y_test, y_pred)
print("Classification Report:", )
print(result1)

import matplotlib.pyplot as plt

plt.plot(range_k, scores_list)
plt.xlabel("Value of K")
plt.ylabel("Accuracy")

#print(f"The highest accuracy is {round(temp*100, 2)}% when k is {highest}")

#plt.show()

#excel_data_df = pandas.read_excel('test.xlsx', sheet_name='Sheet1')
excel_data_df = pandas.read_excel('bert.xlsx', sheet_name='Sheet1')

testnames = []
testbios = []
testtexts = []

testcase = []

testnames = excel_data_df['account_id'].tolist()
testbios = excel_data_df['소개글'].tolist()
testtexts = excel_data_df['게시글 본문'].tolist()

for name, bio, text in zip(testnames, testbios, testtexts):
    testcase.append(bow(bio, text))

testcase = MinMaxScaler().fit_transform(testcase)

classifier = KNeighborsClassifier(n_neighbors=highest)
classifier.fit(feature, target)

predictions = classifier.predict(testcase)

KNeighborsClassifier(
    algorithm='auto', leaf_size=30, metric='minkowski',
    metric_params=None, n_jobs=None, n_neighbors=3, p=2,
    weights='uniform'
)
classes = {1: '여행', 2: '운동', 3: '캠핑', 4: '패션'}

for testcas, name, prediction in zip(testcase, testnames, predictions):
    #print(f"{name} belongs in {classes[prediction]}")
    category.append(classes[prediction])

column = ['카테고리']
df = pd.DataFrame(category, columns = column)
df.to_excel("카테고리.xlsx")
