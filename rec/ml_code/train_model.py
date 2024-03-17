import numpy as np
import pandas as pd
import re
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score
from .extract_text import *
import pickle



df = pd.read_csv('UpdatedResumeDataSet.csv')
df['Resume'] = df['Resume'].apply(lambda x: clean_text(x))

le = LabelEncoder()
le.fit(df['Category'])
df['Category'] = le.transform(df['Category'])

tfidf = TfidfVectorizer(stop_words='english')
tfidf.fit(df['Resume'])
requredTaxt  = tfidf.transform(df['Resume'])

X_train, X_test, y_train, y_test = train_test_split(requredTaxt, df['Category'], test_size=0.2, random_state=42)


clf = OneVsRestClassifier(KNeighborsClassifier())
clf.fit(X_train,y_train)
ypred = clf.predict(X_test)
print(accuracy_score(y_test,ypred))



pickle.dump(tfidf,open('tfidf.pkl','wb'))
pickle.dump(clf, open('clf.pkl', 'wb'))