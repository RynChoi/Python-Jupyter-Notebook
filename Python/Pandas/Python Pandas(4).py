#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np


# In[3]:


train_data = pd.read_csv('C:\/train.csv')


# NaN 값 확인

# *info 함수를 통하여 개수 확인

# *isna 함수를 통해 boolean 타입으로 확인

# In[4]:


train_data.info()


# In[5]:


train_data.isna()


# In[6]:


train_data['Age'].isna()


# NaN 처리방법

# *데이터에서 삭제 - dronpa 함수

# *다른 값으로 치환 - fillna 함수

# -NaN 데이터 삭제하기

# In[7]:


train_data.dropna()


# In[8]:


train_data.dropna(subset=['Age']) #Age가 NaN


# In[9]:


train_data.dropna(axis=1) #NaN이 있는column을 제거


# *NaN 값 대체하기 - 평균으로 대체하기, 생존자/사망자 별 평균으로 대체하기

# In[11]:


train_data['Age'].fillna(train_data['Age'].mean())


# In[13]:


#생존자 나이 평균
mean1 = train_data[train_data['Survived']==1]['Age'].mean()

#사망자 나이 평균
mean2 = train_data[train_data['Survived']==0]['Age'].mean()

print(mean1, mean2)


# In[15]:


#NaN 값에 평균 값 넣기
train_data[train_data['Survived']==1]['Age'].fillna(mean1)
train_data[train_data['Survived']==0]['Age'].fillna(mean2)


# In[17]:


train_data.loc[train_data['Survived']==1,'Age'] = train_data[train_data['Survived']==1]['Age'].fillna(mean1)
train_data.loc[train_data['Survived']==0,'Age'] = train_data[train_data['Survived']==0]['Age'].fillna(mean2)


# In[19]:


train_data[train_data['Age'] == 28.343689655172415]


# In[20]:


train_data = pd.read_csv('C:\/train.csv')


# info함수로 각 변수의 데이터 타입 확인

# *타입 변경은 astype함수를 사용

# In[22]:


train_data.info()


# 숫자형(Numerical Type) 데이터

# *연속성을 띄는 숫자로 이루어진 데이터 ex)Age, Fare 등

# 범주형(Categorical Type) 데이터

# *연속적이지 않은 값(대부분의 경우 숫자를 제외한 나머지 값)을 갖는 데이터를 의미

# ex) Name, Sex, Ticket, Cabin, Embarked

# *어떤 경우, 숫자형 타입이라 할지라도 개념적으로 범주형으러 처리해야할 경우가 있음

# ex) Pclass

# Pclass 변수 변환하기

# *astype 사용하여 간단히 타입만 변환

# In[25]:


train_data['Pclass'] = train_data['Pclass'].astype(str)


# In[26]:


train_data.info()


# Age 변수 변환하기

# *변환 로직을 함수로 만든 후, apply 함수로 적용

# In[27]:


import math


# In[31]:


def age_cat(age):
    if math.isnan(age):
        return -1
    return math.floor(age/10)*10


# In[40]:


train_data['Age'].apply(age_cat)


# In[41]:


train_data


# One-hot encoding

# *범주형 데이터는 분석단계에서 계산이 어렵기 때문에 숫자형으로 변경이 필요함

# *범주형 데이터의 각 범주를 column 레벨로 변경

# *해당 범주에 해당하면 1, 아니면 0으로 채우는 인코딩 기법

# *pandas.get_dummies 함수 사용

# *drop_first: 첫번째 카테고리 값은 사용하지 않음

# In[42]:


train_data = pd.read_csv('C:\/train.csv')


# In[45]:


pd.get_dummies(train_data, columns=['Pclass','Sex','Embarked'], drop_first=True)


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




