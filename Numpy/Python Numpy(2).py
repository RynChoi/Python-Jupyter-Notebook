#!/usr/bin/env python
# coding: utf-8

# 인덱싱 - 파이썬 리스트와 동일한 개념으로 사용, ,를 사용하여 각 차원의 인덱스에 접근 가능

# In[1]:


import numpy as np


# 1차원 벡터 인덱싱

# In[2]:


x = np.arange(10)
print(x)


# In[5]:


print(x[3])
print(x[5])


# 2차원 행렬 인덱싱

# In[29]:


x = np.arange(10).reshape(2, 5)
print(x) #[[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]


# In[32]:


print(x[0]) #[0, 1, 2, 3, 4]
print(x[0,2]) #2
print(x[1, -1]) #9


# 3차원 텐서 인덱싱

# In[37]:


x = np.arange(36).reshape(3, 4, 3)
print(x)


# In[41]:


print(x[0]) #4행 3열 012 345 678 91011
print(x[1,3]) # 21 22 23
print(x[2,2,1]) #31


# 슬라이싱 - 리스트, 문자열 slicing과 동일한 개념으로 사용, ,를 사용하여 각 차원 별로 슬라이싱 가능

# 1차원 벡터 슬라이싱

# In[44]:


x = np.arange(10)
print(x)


# In[45]:


x [1:7]


# 2차원 행렬 슬라이싱

# In[46]:


x = np.arange(10).reshape(2,5)
print(x)


# In[54]:


print(x[:, 1:4]) #123 678
print(x[:, :2]) #01 56
print(x[0, :3]) #012 벡터 (인덱싱으로 차원이 하나 줄음)
print(x[1, :3]) #567 벡터 (인덱싱으로 차원이 하나 줄음)
print(x[:1, :3]) #012 행렬 (차원이 안줄음)


# 3차원 텐서 슬라이싱

# In[57]:


x = np.arange(54).reshape(2, 9, 3)
print(x)


# In[63]:


print(x[:1, :2, :]) #012 345 행렬
print(x[0, :2, :]) #012 345 벡터
# :는 전체를 의미


# 1. ndarray shape 변경하기

# ravel - 다차원 배열을 1차원으로 변경, 'order' 파라미터 *'C' - row우선 변경, 'F' - column 우선 변경

# In[65]:


x = np.arange(15).reshape(3,5)
print(x)


# In[70]:


temp = x.ravel() #np.ravel(x)

print(temp)


# In[71]:


temp[0] = 100
print(temp)
print(x) #x도 temp로 인해 바뀐다


# In[78]:


np.ravel(x, order='F') #행기준으로 펴진다, 기본값은 C


# flatten - 다차원 배열을 1차원으로 변경 , ravel과 다르게 원본이 아닌 복사본 반환, 'order' 파라미터

# In[68]:


y = np.arange(15).reshape(3,5)
print(y)


# In[73]:


temp2 = y.flatten()

print(temp2)


# In[76]:


temp2[0] = 100
print(temp2)
print(y) #y는 바뀌지 않는다


# In[80]:


x = np.arange(30).reshape(2, 3, 5)
print(x)


# In[84]:


x.ravel() #한차원 행렬 출력후 다음차원 행렬 출력


# reshae 함수 - array의 shape을 다른차원으로 변경, 주의할점은 rehape한 후의 결과의 전체 원소 개수와 이전 개수가 같아야 가능
# 
# 사용 예) 이미지 데이터 벡터화 - 이미지는 기본적으로 2차원 혹은 3차원(RGB)이나 트레이닝을 위해 1차원으로 변경하여 사용 됨

# In[87]:


x = np.arange(36)
print(x)
print(x.shape)
print(x.ndim) #차원을 나타냄


# In[93]:


y = x.reshape(6, 6) #x.reshape(6, -1) -1할시에 와야할 수가 알아서 온다
#곱이 안맞으면 출력이 안된다
print(y.shape) #(6,6)
print(y.ndim) #2


# In[94]:


k = x.reshape(3, 3, 4)
print(k)
print(k.shape) # (3,3,4)
print(k.ndim) #3


# ndarray 기본 함수 사용하기

# 연산함수 - add, substract, mulitply, divide

# In[95]:


x = np.arange(15).reshape(3, 5)
y = np.random.rand(15).reshape(3, 5)
print(x)
print(y)


# In[103]:


np.add(x, y) #더하기 (행렬이 같을때만) x+y


# In[104]:


np.divide(x, y) #나누기 x/y


# 통계함수 - 평균, 분산, 중앙, 최대, 최소값 등등 통계 관련된 함수가 내장

# In[105]:


print(y)


# In[108]:


print(np.mean(y)) #y.mean() 평균
print(np.max(y)) #가장 큰 값 가져오기
print(np.argmax(y)) #가장 큰 값의 순서
# var: 분신, median: 중간값, std: 표준편차


# 집계함수 - 합계(sum), 누적합계(vumsum) 등등 계산 가능

# In[109]:


y


# In[111]:


np.sum(y) #행렬 전체 수의 합


# In[113]:


np.cumsum(y) #리스트 출력 뒤의원소는 바로 앞의 원소와 합으로 만들어진다


# any, all 함수
# 
# any: 특정 조건을 만족하는 것이 하나라도 있으면 True, 아니면 False
# 
# all: 모든 원소가 특정 조건을 만족한다면 True, 아니면 False

# In[114]:


z = np.random.randn(10)
print(z)


# In[118]:


np.any(z>0) #조건이 하나라도 맞으면 TRUE


# In[117]:


np.all(z > 0) #모든 조건이 맞아야 TRUE


# where 함수 - 조건에 따라 선별적으로 값을 선택 가능
# 
# 사용 예) 음수인경우는 0, 나머지는 그대로 값을 쓰는 경우

# In[119]:


z = np.random.randn(10)
print(z)


# In[122]:


np.where(z > 0, z, 0) #z가 0위일떄만 출력하고 나머지 z는 0으로 출력


# In[ ]:





# In[ ]:




