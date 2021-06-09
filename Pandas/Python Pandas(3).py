#!/usr/bin/env python
# coding: utf-8

# Dataframe data 살펴보기

# *Series가 1차원이라면 DataFrame은 2차원으로 확대된 버젼

# *Excel spreadsheet이라고 생각하면 이해하기 쉬움

# *2치원이기 때문에 인덱스가 row, colunm로 구성됨 - row는 각 개별데이터, column은 개별 속성을 의미

# *Data Analysis, Machine Learning에서 data 변형을 위해 가장 많이 사용

# In[40]:


import pandas as pd
import numpy as np


# In[3]:


train_data = pd.read_csv('C:\/train.csv')


# head, tail 함수

# *데이터 전체가 아닌, 일부를 간단히 보기 위한 함수

# In[5]:


train_data.head(n=3)


# In[6]:


train_data.tail()


# dataframe 데이터 파악하기

# *shape 속성(row, column)

# *describe 함수 - 숫자형 데이터의 통계치 계산

# *info 함수 - 데이터 타입, 각 아이템의 개수 등 출력

# In[7]:


train_data.shape


# In[8]:


train_data.describe()


# In[9]:


train_data.info()


# 인덱스(index)

# *index 속성

# *각 아이템을 특정할 수 있는 고유의 값을 저장

# *복잡한 데이터의 경우, 멀티 인덱스로 표현 가능

# In[10]:


train_data.index


# 컬럼(column)

# *columns 속성

# *각각의 특성(feature)을 나타냄

# *복잡한 데이터의 경우, 멀티 컬럼으로 표현 가능

# In[11]:


train_data.columns


# DataFrame 생성하기

# *일반적으로 분석을 위한 데이터는 다른 데이터 소스(database, 외부파일)을 통해 dataframe을 생성

# *여기서는 실습을 통해, dummy 데이터를 생성하는 방법을 다룰 예정

# dictionary로 부터 생성하기

# *dict의 key -> colunm

# In[14]:


data = {'a' : [1, 2, 3], 'b' : [4, 5, 6], 'c' : [10, 11, 12]}
pd.DataFrame(data, index=['x', 'y', 'z'])


# Series로 부터 생성하기

# *각 Series의 인덱스 -> column

# In[16]:


a = pd.Series([100, 200, 300], ['a', 'b', 'c'])
b = pd.Series([101, 201, 301], ['a', 'b', 'c'])
c = pd.Series([110, 210, 310], ['a', 'b', 'c'])

pd.DataFrame([a, b, c], index=[1, 2, 3])


# csv 데이터로 부터 Dataframe 생성

# *데이터 분석을 위해, dataframe을 생성하는 가장 일반적인 방법

# *데이터 소스로부터 추출된 csv(comma separated values) 파일로부터 생성

# *pandas.read_csv 함수 사용

# read_csv 함수 파라미터

# *sep - 각 데이터 값을 구별하기 위한 구분자(separator) 설정

# *header - header를 무시할 경우, None 설정

# *index_col - index로 사용할 column 설정

# *usercols - 실제로 dataframe에 로딩할 columns만 설정

# In[27]:


train_data = pd.read_csv('C:\/train.csv', index_col='PassengerId', usecols=['PassengerId', 'Survived', 'Pclass', 'Name'])
train_data


# In[24]:


train_data.columns


# column 선택하기

# *기본적으로 [ ]는 column울 추출

# *컬럼 인덱스일 경우 인덱스의 리스트 사용 가능

# *리스트를 전달할 경우 결과는 Dataframe

# *하나의 컬럼명을 전달할 경우 결과는 Series

# In[28]:


train_data = pd.read_csv('C:\/train.csv')


# 하나의 컬럼 선택하기

# In[30]:


train_data['Survived'] #컬럼


# 복수의 컬럼 선택하기

# In[32]:


train_data[['Survived', 'Name', 'Age']] #리스트


# dataframe slicing

# *dataframe의 경우 기본적으로 [ ]연산자가 column 선택에 사용

# *하지만, slicing은 row 레벨로 지원

# In[34]:


train_data[7:10]


# row 선택하기

# *Series의 경우 [ ]로 row선택이 가능하나, Dataframe의 경우는 기본적으로 column을 선택하도록 설계

# *.loc, .lioc로 row 선택 가능

# loc - 인덱스 자체를 사용, lioc - 0 based index로 사용

# *이 두함수는 ,를 사용하여 column 선택도 가능

# In[36]:


train_data.info()


# In[42]:


train_data.index = np.arange(100, 991)


# In[44]:


train_data.head()


# In[45]:


train_data.loc[986]


# In[46]:


train_data.loc[[100, 547, 658]]


# In[48]:


train_data.iloc[0]


# In[49]:


train_data.iloc[[0, 100, 200, 2]]


# row, column 동시에 선택하기

# *loc, iloc 속성을 이용할 때, 콤마를 이용하여 둘 다 명시 가능

# In[50]:


train_data.loc[[986, 100, 110, 990], ['Survived', 'Name', 'Sex', 'Age']]


# In[51]:


train_data.iloc[[101, 100, 110, 102], [1, 4, 5]]


# boolean selection으로 row 선택하기

# *numpy에서와 동일한 방식으로 해당 조건에 맞는 row만 선택

# - 30대이면서 1등석에 탄 사람 선택하기

# In[55]:


train_data.index = np.arange(0, 891)
train_data.head()


# In[59]:


class_ = train_data['Pclass'] == 1
age_ = (train_data['Age'] >= 30) & (train_data['Age'] < 40)

train_data[class_ & age_]


# 새 column 추가하기

# *[ ] 사용하여 추가하기

# *insert 함수 사용하며 원하는 위치에 추가하기

# In[63]:


train_data['Age_double'] = train_data['Age'] *2
train_data.head()


# In[64]:


train_data['Age_tripple'] = train_data['Age_double'] + train_data['Age']
train_data.head()


# In[65]:


train_data.insert(3, 'Fare10', train_data['Fare']/10)
train_data.head()


# column 삭제하기

# *drop 함수 사용하여 삭제 - 리스트를 사용하여 멀티풀 삭제 가능

# In[67]:


train_data.drop('Age_tripple', axis = 1) #복사본 반환
train_data.head()


# In[69]:


train_data.drop(['Age_double', 'Age_tripple'], axis = 1)


# In[70]:


train_data.drop(['Age_double', 'Age_tripple'], axis = 1, inplace=True) #inplace는 원본에서 삭제
train_data


# In[71]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[72]:


train_data = pd.read_csv('C:\/train.csv')


# 변수(column) 사이의 상관계수(correlation)

# *corr함수를 통해 상관계수 연산 (-1, 1사이의 결과)

# *연속성(숫자형) 데이터에 대해서만 연산, 인과관계를 의미하진 않음

# In[74]:


train_data.corr() #대각선 값은 항상 1


# In[76]:


plt.matshow(train_data.corr()) #색깔이 다를수록 관계가 더 깊다


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




