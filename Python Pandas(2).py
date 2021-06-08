#!/usr/bin/env python
# coding: utf-8

# Series 함수 활용하여 데이터 분석하기

# In[1]:


import numpy as np
import pandas as pd


# Series size, shape, unique, count, valus_counts 함수

# *size: 개수 반환

# *shape: 튜플형태로 shape 반환

# *uniqe: 유일한 값만 ndarray로 반환

# *count: NaN을 제외한 개수를 반환

# *mean: NaN을 제외한 평균

# *value_counts: NaN을 제외하고 각 값들의 빈도를 반환

# In[3]:


s = pd.Series([1, 1, 2, 1, 2, 2, 2, 1, 1, 3, 3, 4, 5, 5, 7, np.NaN])
s


# In[4]:


len(s)


# In[5]:


s.size


# In[7]:


s.shape #튜플형태


# In[8]:


s.unique()


# In[9]:


s.count()


# In[13]:


a = np.array([2, 2, 2, 2, np.NaN]) #NaN 무시못함
a.mean()

b = pd.Series(a)#NaN 무시하고 평균 구함
b.mean()


# In[16]:


s.mean()


# In[17]:


s.value_counts()


# index를 활용하여 멀티풀한 값에 접근

# In[23]:


s[[5, 7, 8, 10]].value_counts()


# head, tail 함수

# *head: 상위 n개 출력 기본 5개

# *tail: 하위 n개 출력 기본 5개

# In[24]:


s.head()


# In[25]:


s.tail()


# index를 기준으로 연산

# In[27]:


s1 = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
s2 = pd.Series([6, 3, 2, 1], ['d', 'c', 'b', 'a'])

s1


# In[28]:


s2


# In[29]:


s1 + s2


# 산술연산

# *Series의 경우에도 스칼라와의 연산은 각 원소별로 스칼라와의 연산이 적용

# *Series와의 연산은 각 인덱스에 맞는 값끼리 연산이 적용 - 이떄, 인덱스의 pair가 맞지않으면, 결과느 NaN

# In[30]:


s1 ** 2


# In[31]:


s1 ** s2


# index pair가 맞지 않는 경우

# 해당 index에 대해선 NaN 값 생성

# In[32]:


s1['k'] = 7
s2['e'] = 9


# In[33]:


s1


# In[34]:


s2


# In[36]:


s1 + s2 #페어가 맞지 않아서 e와k에 NaN 출력


# Boolean selection

# *boolean Series가 []와 함께 사용되면 True값에 해당하는 값만 새로 반환되는 Series객체에 포함됨

# *다중조건의 경우,&(and), |(or)를 사용하여 연결기능

# In[37]:


s = pd.Series(np.arange(10), np.arange(10)+1)
s


# In[38]:


s > 5


# In[39]:


s[s>5]


# In[42]:


s[s % 2 ==0]


# In[44]:


s.index > 5


# In[45]:


s[s.index > 5]


# In[47]:


s[(s > 5) & (s < 8)]


# In[48]:


(s >= 7).sum()


# In[50]:


(s[s>=7]).sum()


# Series 값 변경

# *추가 및 업데이트: 인덱스를 이욜

# *삭제: drop함수 이용

# In[51]:


s = pd.Series(np.arange(100, 105), ['a', 'b', 'c', 'd', 'e'])
s


# In[52]:


s['a'] = 200
s


# In[53]:


s['k'] = 300
s


# In[56]:


s.drop('k') #결과만 삭제하고 원래 s의 k는 사라지지 않는다
#inplace를 True로 설정하면 s객체에서도 k를 삭제할 수 있다.


# In[55]:


s


# In[59]:


s[['a', 'b']] = [300, 900]
s


# In[ ]:





# Slicing

# *리스트, ndarray와 동일하게 적용

# In[61]:


s1 = pd.Series(np.arange(100, 105))
s1


# In[63]:


s1[1:3]


# In[67]:


s2 = pd.Series(np.arange(100, 105), ['a', 'c', 'b', 'd', 'e'])
s2


# In[68]:


s2[1:3]


# In[69]:


s2['c':'d']


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




