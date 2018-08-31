# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp
data = []
with open('../../data/car.txt', 'r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))
data = np.array(data).T
x = []
for row in range(len(data)):
    encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])
x = np.array(x).T
model = se.RandomForestClassifier(
    max_depth=9, n_estimators=150, random_state=7)
train_sizes = np.linspace(0.1, 1, 10)
train_sizes, train_scores, test_scores = \
    ms.learning_curve(
        model, x, y, train_sizes=train_sizes, cv=5)
train_means = train_scores.mean(axis=1)
train_stds = train_scores.std(axis=1)
test_means = test_scores.mean(axis=1)
test_stds = test_scores.std(axis=1)
mp.figure('Learning Curve', facecolor='lightgray')
mp.title('Learning Curve', fontsize=20)
mp.xlabel('Train Size', fontsize=14)
mp.ylabel('Score', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.fill_between(train_sizes,
                train_means - train_stds,
                train_means + train_stds,
                color='dodgerblue', alpha=0.25)
mp.fill_between(train_sizes,
                test_means - test_stds,
                test_means + test_stds,
                color='orangered', alpha=0.25)
mp.plot(train_sizes, train_means, 'o-',
        c='dodgerblue', label='Training')
mp.plot(train_sizes, test_means, 'o-',
        c='orangered', label='Testing')
mp.legend()
mp.show()
