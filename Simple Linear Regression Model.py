#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os 
import pandas as pd
import numpy as np
import statsmodels.api as sm


# In[7]:


#현재경로 확인
os.getcwd()


# In[9]:


#데이터 불러오기
boston = pd.read_csv("./Boston_house.csv")


# In[10]:


boston.head()


# In[11]:


#target 제외한 데이터만 뽑기
boston_data = boston.drop(['Target'],axis=1)


# In[12]:


boston_data.describe()
#data 통계 뽑아보기


# In[13]:


'''
타겟 데이터
1978 보스턴 주택 가격
506개 타운의 주택 가격 중앙값 (단위 1,000 달러)

특징 데이터
CRIM: 범죄율
INDUS: 비소매상업지역 면적 비율
NOX: 일산화질소 농도
RM: 주택당 방 수
LSTAT: 인구 중 하위 계층 비율
B: 인구 중 흑인 비율
PTRATIO: 학생/교사 비율
ZN: 25,000 평방피트를 초과 거주지역 비율
CHAS: 찰스강의 경계에 위치한 경우는 1, 아니면 0
AGE: 1940년 이전에 건축된 주택의 비율
RAD: 방사형 고속도로까지의 거리
DIS: 직업센터의 거리
TAX: 재산세율'''


# ## crim/rm/lstat 세게의 변수로 각각 단순 선형 회귀 분석하기

# In[35]:


## 변수 설정 target/crim/rm/lstat
target = boston[['Target']]
crim = boston[['CRIM']]
rm = boston[['RM']]
lstat = boston[['LSTAT']]


# ## target ~ crim 선형회귀분석

# In[38]:


# crim변수에 상수항추가하기
crim1=sm.add_constant(crim,has_constant="add")


# In[39]:


# sm.OLS 적합시키기 
model1 = sm.OLS(target,crim1)
fitted_model1 = model1.fit()


# In[40]:


# summary함수통해 결과출력
fitted_model1.summary()


# In[41]:


## 회귀 계수 출력
fitted_model1.params


# ### y_hat=beta0 + beta1 * X 계산해보기

# In[42]:


#회귀 계수 x 데이터(X)
np.dot(crim1,fitted_model1.params)


# In[45]:


## predict함수를 통해 yhat구하기 
pred1 = fitted_model1.predict(crim1)


# In[46]:


## 직접구한 yhat과 predict함수를 통해 구한 yhat차이 
np.dot(crim1,fitted_model1.params) - pred1


# ## 적합시킨 직선 시각화 

# In[47]:


import matplotlib.pyplot as plt
plt.yticks(fontname = "Arial") #
plt.scatter(crim,target,label="data")
plt.plot(crim,pred1,label="result")
plt.legend()
plt.show()


# In[48]:


plt.scatter(target,pred1)
plt.xlabel("real_value")
plt.ylabel("pred_value")
plt.show()


# In[49]:


## residual 시각화 
fitted_model1.resid.plot()
plt.xlabel("residual_number")
plt.show()


# In[51]:


##잔차의 합계산해보기
np.sum(fitted_model1.resid)


# ## 위와 동일하게 rm변수와 lstat 변수로 각각 단순선형회귀분석 적합시켜보기 

# In[55]:


# 상수항추가
rm1=sm.add_constant(rm,has_constant="add")
lstat1=sm.add_constant(lstat,has_constant="add")


# In[56]:


# 회귀모델 적합
model2 = sm.OLS(target,rm1)
fitted_model2 = model2.fit()

model3 = sm.OLS(target,lstat1)
fitted_model3 = model3.fit()


# In[57]:


# rm모델 결과 출력
fitted_model2.summary()


# In[58]:


# lstat모델 결과 출력 
fitted_model3.summary()


# In[61]:


## 각각 yhat_예측하기 
pred2 = fitted_model2.predict(rm1)

pred3 = fitted_model3.predict(lstat1)


# In[62]:


## rm모델 시각화
import matplotlib.pyplot as plt
plt.scatter(rm,target,label="data")
plt.plot(rm,pred2,label="result")
plt.legend()
plt.show()


# In[63]:


## lstat모델 직선 시각화
import matplotlib.pyplot as plt
plt.scatter(lstat,target,label="data")
plt.plot(lstat,pred3,label="result")
plt.legend()
plt.show()


# In[64]:


# rm모델 reisidual 시각화 
fitted_model2.resid.plot()
plt.xlabel("residual_number")
plt.show()


# In[65]:


# lstat모델 residual시각화
fitted_model3.resid.plot()
plt.xlabel("residual_number")
plt.show()


# In[66]:


## 세모델의 residual비교 
fitted_model1.resid.plot(label="crim")
fitted_model2.resid.plot(label="rm")
fitted_model3.resid.plot(label="lstat")
plt.legend()


# In[ ]:





# In[ ]:





# In[ ]:




