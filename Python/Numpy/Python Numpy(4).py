#!/usr/bin/env python
# coding: utf-8

# matplotlib 모듈 이용하여 그래프 표현하기

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# 그래프 데이터 생성

# In[2]:


x = np.linspace(0, 10, 11)
y = x ** 2 + x + 2 + np.random.randn(11)

print(x)
print(y)


# 그래프 출력하기
# 
# plot함수 (선 그래프), scatter(점 그래프), hist(히스토그램)등 사용
# 
# *함수의 parameter 혹은 plt의 다른 함구로 그래프 형태 및 설정을 변경 가능
# 
# *기본적으로 x, y에 해당하는 값이 필요

# In[3]:


plt.plot(x, y)


# In[4]:


plt.scatter(x,y)


# 그래프에 주석 추가
# 
# *x,y 축 및 타이틀

# In[8]:


plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('X-Y relation')
plt.plot(x,y)


# grid 추가

# In[9]:


plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('X-Y relation')
plt.grid(True)
plt.plot(x,y)


# x, y축 범위 지정

# In[10]:


plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('X-Y relation')
plt.grid(True)

plt.xlim(0, 20)
plt.ylim(0, 200)

plt.plot(x,y)


# plot 함수 parameters
# 
# *그래프의 형태에 대한 제어가능, plot함수 도큐먼트
# 
# 그래프의 색상변경

# In[11]:


plt.plot(x, y, 'r')


# 그래프의 선스타일 변경

# In[13]:


plt.plot(x, y, '-.') 


# In[14]:


plt.plot(x, y, 'g^')


# 그래프 두께 변경
# 
# *linewidth 명시

# In[15]:


plt.plot(x, y, 'm:', linewidth=9)


# keyword parameter 이용하여 모든 속성 설정
# 
# *color, linestyle, marker, markerfacecolor, markersize 등등

# In[17]:


plt.plot(x, y, color='black', linestyle='--', marker='^', 
         markerfacecolor='blue', markersize='6')


# subplot으로 여러 그래프 출력하기
# 
# *subplot 함수로 구획을 구별하여 각각의 subplot에 그래프 출력

# In[19]:


plt.subplot(2, 2, 1)
plt.plot(x, y, 'r')

plt.subplot(2, 2, 2)
plt.plot(x, y, 'g')

plt.subplot(2, 2, 3)
plt.plot(y, x, 'k')

plt.subplot(2, 2, 4)
plt.plot(x, np.exp(x), 'b')


# hist 함수 사용
# 
# *histogram 생성, bins로 historgram 개수 설정

# In[20]:


data = np.random.randint(1, 100, size=200)
print(data)


# In[24]:


plt.hist(data, bins=20, alpha=0.3)
plt.xlabel('값')
plt.ylabel('개수')
plt.grid(True)


# 1.로또 번호 자동 생성기(함수로) 만들기

# In[25]:


import numpy as np


# In[40]:


def generate_lotto_nums():
    return np.random.choice(np.arange(1, 46), size=6, replace=False)

generate_lotto_nums()


# 2. numpy를 이용하여 pi(원주율) 값을 계산하기 *몬테 카를로 방법 이용하기

# In[52]:


total = int(1e7)
points = np.random.rand(total, 2)
4 * np.sum(np.sum(points ** 2, axis=1) < 1)/ total


# In[ ]:




