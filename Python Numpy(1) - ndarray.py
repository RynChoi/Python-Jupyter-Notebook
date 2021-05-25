#!/usr/bin/env python
# coding: utf-8

# Numpy&ndarray

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


x = np.array([1, 2, 3])
y = np.array([2, 4, 6])

plt.plot(x, y)


# In[7]:


x = np.array([1, 2, 3, 4])
print(x)

y = np.array([[2, 3, 4], [1, 2, 5]])
print(y)

print(type(y))


# np.arrange 함수로 생성하기

# In[9]:


np.arange(10)


# In[10]:


np.arange(1, 10)


# In[11]:


np.arange(1, 10, 2)


# In[12]:


np.arange(5, 101, 5)


# np.ones, np.zero로 생성하기

# In[13]:


np.ones((4, 5))
#1로된 행렬


# In[14]:


np.ones((2, 3, 4))
#3, 4행 행렬이 2개있다


# In[17]:


np.zeros((2, 3, 8 , 8))
#0으로된 행렬


# np.empty, np.full로 생성하기

# In[21]:


np.empty((3, 4))
#초기화된 수로 행렬 생성


# In[20]:


np.full((3, 4), 7)
#원하는 수로 행렬 이루기


# np.eye로 생성하기 - 단위 행렬 생성

# In[23]:


np.eye(5)
#5행 5열에 대각선은 모두 1


# np.linspace로 생성하기

# In[24]:


np.linspace(1, 10, 3)
#(시장, 끝, 나누는 수) 시작과 끝 사이의 전체수가 3개가 되도록 균일 하게 나누기


# In[26]:


np.linspace(1, 10, 4)


# In[27]:


np.linspace(1, 10, 5)


# reshape 함수 활용 - ndarray의 형태, 차원을 바꾸기 위해 사용

# In[33]:


x = np.arange(1, 16)
print(x)

x.shape

x.reshape(5, 3, 1)
#숫자에 가능한 행렬만 돌아감, 2개는 2차원 3개는 3차원


# random 서브모듈

# rand 함수 - 0, 1사이의 분포로 랜덤한 ndarray 생성

# In[42]:


np.random.rand(2, 3)


# randn 함수 - n:정규분포 약자, 정규분포로 샘플링된 랜덤 ndarray 생성

# In[60]:


np.random.randn(3,4)
#음수도 나온다


# randint 함수 - 특정 정수 사이에서 랜덤하게 샘플링

# In[62]:


np.random.randint(1, 100, size=(3, 5))
#1부터 100사이 3,5 행렬 생성


# seed 함수 - 랜덤한 값을 동일하게 다시 생성하고자 할때 사용

# In[73]:


np.random.randn(3,4)


# In[72]:


np.random.seed(100) #숫자는 상관 없음
#seed 호출후 랜덤 함수 돌리면 동일하게 나옴


# choice - 주어진 1차원 ndarray로 부터 랜덤으로 샘플링, 정수가 주어진 경우, np.arange(해당숫자)로 간주

# In[74]:


np.random.choice(100, size=(3, 4))


# In[107]:


x = np.array([1, 2, 3, 1.5, 2.6, 4.9])
np.random.choice(x, size=(2, 2), replace=False)
#주어진 x중에서 뽑아 행렬을 만든다, replace=Falsw 하면 중복 허용x


# 확률분포에 따른 ndarray 생성 - uniform, normal 등등

# In[108]:


np.random.uniform(1.0, 3.0, size=(4, 5))


# In[112]:


np.random.normal(size=(3, 4)) #randn과 같은 기능


# In[ ]:




