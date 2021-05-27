#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# axis 이해하기
# 
# *몇몇 함수에는 axis kwyword 파라미터가 존재
# 
# *axis값이 없는 경우에는 전체 데이터에 대해 적용
# 
# *axis값이 있는 경우에는, 해당 axis를 따라서 연산적용

# **axis를 파라미터로 갖는 함수를 이용하기
# 
# *거의 대부분이 연산 함수들이 axis 파라미터를 사용
# 
# *이 경우, 해당 값이 주어졌을 때, 해당 axis를 따라서 연산이 적용
# 
# *예)np.sum, np.mean, np.any 등등

# In[2]:


x = np.arange(15)
print(x)


# In[3]:


np.sum(x, axis=0) #105
#1차원 데이터에 적용


# In[7]:


y = x.reshape(3, 5)
print(y)

np.sum(y, axis=0) #행방향
# [15, 18, 21, 24, 27]
#행렬에 적용


# In[8]:


y = x.reshape(3, 5)
print(y)

np.sum(y, axis=1) #열방향
# 1[0, 35, 60]
#행렬에 적용


# In[12]:


z = np.arange(36).reshape(3, 4, 3)
print(z)
#3차원 텐서에 적용
np.sum(z, axis=0) #각 행렬들의 위치로 더함
#[[36, 39, 42],
#   [45, 48, 51],
#   [54, 57, 60],
#   [63, 66, 69]]


# In[14]:


z = np.arange(36).reshape(3, 4, 3)

#3차원 텐서에 적용
np.sum(z, axis=1) #각 행렬의 행더하기
#array([[ 18,  22,  26],
#       [ 66,  70,  74],
#       [114, 118, 122]])


# In[15]:


z = np.arange(36).reshape(3, 4, 3)

#3차원 텐서에 적용
np.sum(z, axis=2) #열 더하서 하나의 행으로 만들기 
#array([[  3,  12,  21,  30],
#       [ 39,  48,  57,  66],
#       [ 75,  84,  93, 102]])


# axis의 값이 튜플일 경우
# 
# *해당 튜플에 명시된 모든 axis에 대해서 연산

# In[20]:


np.sum(z, axis=(0, 2)) #2가지 축을 이용


# 브로드캐스팅
# 
# *Shape이 같은 두 ndarray에 대한 연산은 각 원소별로 진행
# 
# *연산되는 두 ndarray가 다른 shape을 갖는 경우 브로드 캐스틴(Shape을 맞춤)후 진행

# In[22]:


#shape이 같은 경우의 연산
x = np.arange(15).reshape(3, 5)
y = np.arange(15).reshape(3, 5)
print(x)
print(y)
x+y


# In[23]:


#Scalar(상수)와의 연산
x+2


# In[30]:


#Shape이 다른 경우 연산
a = np.arange(12).reshape(4, 3)
b = np.arange(100, 103)
c = np.arange(1000, 10003) #a + c는 연산이 안됨, 브로드캐스팅은 뒷차원부터 비교!
d = b.reshape(1, 3)

print(a)
print(b)
a + b


# Boolean indexing
# 
# *ndarry 인덱싱 시, bool 리스트를 전달하여 True인 경우만 필터링
# 
# *브로드캐스팅을 활용하여 ndarray로 부터 bool list 얻기 예) 짝수인 경우만 찾아보기

# In[33]:


x = np.random.randint(1, 100, size=10)
print(x)


# In[35]:


even_mask = x % 2 == 0


# In[37]:


x[even_mask] #bool 리스트를 인덱스로 전달


# In[38]:


x[x % 2 == 0] #바로 받아오기 (참인 값만 출력)


# 다중조건 사용하기
# 
# *파이썬 논리 연산지인 and, or, not 키워드 사용 불가
# 
# *& - and,  | - or

# In[41]:


x[(x % 2 == 0) & (x < 30)]


# In[43]:


x[(x < 30) | (x > 70)]


# linalg 서브모듈 함수 활용여 선형대수 연산하기

# np.linalg.inv
# 
# *역행렬을 구할 때 사용, 모든 차원의 값이 같아야 함

# In[44]:


x = np.random.rand(3, 3) #행과 열의 수가 같은 경우에만 구할 수 있다

print(x)

x @ np.linalg.inv(x)


# np.linalg.solve
# 
# *Ax = B 형태의 선형대수식 솔루션을 제공
# 
# *예) 호랑이와 홍합의 합 : 25 호랑이 다리와 홍합 다리의 합은 64
# 
# x+y=25 , 2x + 4y = 64

# In[48]:


A = np.array([[1, 1], [2, 4]])
B = np.array([25, 64])

x = np.linalg.solve(A, B)
print(x)

np.allclose(A@x, B) # 답 맞는지 확인 과정


# In[ ]:





# In[ ]:




