# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    'audi', 'ford', 'audi', 'toyota',
    'ford', 'bmw', 'toyota', 'ford'])
print(raw_samples)
lbe = sp.LabelEncoder()
lbe_samples = lbe.fit_transform(raw_samples)
print(lbe_samples)
new_sample = np.array(['bmw', 'audi', 'toyota'])
lbe_sample = lbe.transform(new_sample)
print(lbe_sample)
raw_sample = lbe.inverse_transform(lbe_sample)
print(raw_sample)
