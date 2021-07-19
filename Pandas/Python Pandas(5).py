#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# group by

# - 아래의 세 단계를 적용하여 데이터를 그룹화(SQL의 group by 와 개념적으로는 동일, 사용법 유사)

# - 데이터 분할, operation 적용, 데이터 병합

# In[4]:


df = pd.read_csv('C:\/train.csv')
df.head()


# GroupBy groups 속성

# - 각 그룹과 그룹에 속한 index를 dict 형태로 표현

# In[5]:


class_group = df.groupby('Pclass')
class_group


# In[6]:


class_group.groups


# In[7]:


gender_group = df.groupby('Sex')
gender_group.groups


# groupping 함수

# * 그룹 데이터에 적용 가능한 통계 함수(NaN은 제외하여 연산)

# - count - 데이터 개수

# - sum = 데이터의 합

# - mean, std, var - 평균, 표준편차, 분산

# - min, max - 최소, 최대값

# In[8]:


class_group.count()


# In[9]:


class_group.mean()['Survived']


# 성별에 따른 생존율 구해보기

# In[17]:


df.groupby(['Pclass', 'Sex']).mean()['Survived']


# 복수 columns로 groupping 하기

# - grouby에 colunm 리스트를 전달

# - 통계함수를 적용한 결과는 multiindex를 갖는 dataframe

# 
# 클래스와 성별에 따른 생존률 구해보기

# In[13]:


df.groupby(['Pclass', 'Sex']).mean().index


# In[15]:


df.groupby(['Pclass', 'Sex']).mean()


# In[14]:


df.groupby(['Pclass', 'Sex']).mean().loc[(2, 'female')]


# Index를 이용한 group by

# *Index가 있는 경우, group by 함수에 level 사용 가능
# 
# *level은 index의 depth를 의미하며, 가장 왼쪽부터 0부터 증가

# set_index 함수

# * column 데이터를 index 레벨로 변경

# reset_index 함수

# * 인덱스 초기화

# In[18]:


df.head()


# In[22]:


df.set_index(['Pclass', 'Sex']).reset_index()


# In[23]:


df.set_index('Age').groupby(level=0).mean()


# ### 나이대별로 생존율 구하기

# In[25]:


import math
def age_cate(age):
    if math.isnan(age):
        return -1
    return math.floor(age/10) * 10


# In[27]:


df.set_index('Age').groupby(age_cate).mean()['Survived']


# #### MultiIndex를 이용한 groupping

# In[32]:


df.set_index(['Pclass', 'Sex']).groupby(level=[0,1]).mean()['Age']


# #### aggregate(집계) 함수 사용하기

# * group by 결과에 집계함수를 적용하여 그룹별 데이터 확인 가능

# In[33]:


df.set_index(['Pclass', 'Sex']).groupby(level=[0,1]).aggregate([np.mean, np.sum, np.max])


# ## transform 함수

# * group by 후 transform 함수를 사용하면 원래의 index를 유지한 상태로 통계함수를 적용
# * 전체 데이터의 집계가 아닌 각 그룹에서의 집계를 계산
# * 따라서 새로 생성된 데이터를 원본 dataframe과 합치기 쉬움

# In[34]:


df.groupby('Pclass').mean()


# In[35]:


df.groupby('Pclass').transform(np.mean)


# In[36]:


df['Age2'] = df.groupby('Pclass').transform(np.mean)['Age']
df


# In[37]:


df.groupby(['Pclass', 'Sex']).mean()


# In[38]:


df.groupby(['Pclass', 'Sex']).transform(np.mean)


# In[40]:


df = pd.DataFrame({
    '지역' : ['서울', '서울', '서울', '경기', '경기', '부산', '서울', '서울', '부산', '경기', '경기', '경기'],
    '요일' : ['월요일', '화요일', '수요일', '월요일', '화요일', '월요일', '목요일', '금요일', '화요일', '수요일', '목요일', '금요일'],
    '강수량' : [100, 80, 1000, 200, 200, 100, 50, 100, 200, 100, 50, 100],
    '강수확률' : [80, 70, 90, 10, 20, 30, 50, 90, 20, 80, 50, 10] 
})
df


# ### pivot
# * dataframe의 형태를 변경
# * 인덱스, 컬럼, 데이터로 사용할 컬럼을 명시

# In[41]:


df.pivot('지역', '요일')


# In[43]:


df.pivot('요일', '지역', '강수량')


# ### pivot_table
# * 기능적으로 pivot과 동일
# * pivot과의 차이점 (중복되는 모호한 값이 있을 경우, aggregation 함수 사용하여 값을 채움)

# In[46]:


pd.pivot_table(df, index='요일', columns='지역', aggfunc=np.mean)


# ### stack & unstack
# 
# * stack : 컬럼 레벨에서 인덱스 레벨로 dataframe 변경 (즉, 데이터를 쌓아 올리는 개념)
# * unstack : 인덱스 레벨에서 컬럼 레벨로 dataframe 변경 (stack의 반대 operation)
# * 둘은 역의 관계에 있다

# In[49]:


new_df = df.set_index(['지역', '요일'])
new_df


# In[50]:


new_df.unstack(0)


# In[51]:


new_df.unstack(1)


# In[52]:


new_df.unstack(0).stack(0)


# In[53]:


new_df.unstack(0).stack(1)


# ### concat 함수 사용하여 dataframe 병합하기
# * pandas.concat 함수
# * 축을 따라 dataframe을 병합 가능(기본 axis = 0-> 행단위 병합)

# In[ ]:





# In[ ]:





# * column명이 같은 경우

# In[55]:


df1 = pd.DataFrame({'key1': np.arange(10), 'value1' : np.random.randn(10)})


# In[56]:


df2 = pd.DataFrame({'key1': np.arange(10), 'value1' : np.random.randn(10)})


# In[58]:


df1


# In[60]:


pd.concat([df1, df2] ,ignore_index=True)


# In[63]:


pd.concat([df1, df2], axis=1)


# * column 명이 다른 경우

# In[57]:


df3 = pd.DataFrame({'key2': np.arange(10), 'value2' : np.random.randn(10)})


# In[65]:


pd.concat([df1, df3], axis=1)


# ### dataframe merge
# ##### SQL의  join처럼 특정한 column을 기준으로 병합
# * join 방식 : how 파라미터를 통해 명시
#  - inner : 기본값, 일치하는 값이 있는 경우
#  - left : left outer join
#  - right : right outer join
#  - outer : full outer join
# * pandas.merge 함수가 사용됨

# In[67]:


customer = pd.DataFrame({'customer_id' : np.arange(6),
                        'name' : ['철수'"", '영희', '길동', '영수', '수민', '동건'],
                         '나이' : [40, 20, 21, 30, 31, 18]})
customer


# In[68]:


orders = pd.DataFrame({'customer_id' : [1, 1, 2, 2, 2, 3, 3, 1, 4, 9],
                      'item' : ['치약', '칫솔', '이어폰', '헤드셋', '수건', '생수', '수건', '치약', '생수', '케이스'],
                       'quantity' : [1, 2, 1, 1, 3, 2, 2, 3, 2, 1]})
orders.head()


# * on
#  - join 대상이 되는 coulmn 명시

# In[70]:


pd.merge(customer, orders, on='customer_id', how='inner')


# In[71]:


pd.merge(customer, orders, on='customer_id', how='left')


# In[73]:


pd.merge(customer, orders, on='customer_id', how='right')


# In[74]:


pd.merge(customer, orders, on='customer_id', how='outer')


# - index 기준으로 join 하기

# In[75]:


cust1 = customer.set_index('customer_id')
order1 = orders.set_index('customer_id')


# In[76]:


cust1


# In[77]:


order1


# In[78]:


pd.merge(cust1, order1, left_index=True, right_index=True)


# 1. 가장 많이 팔린 아이템은?

# In[82]:


pd.merge(customer, orders, on='customer_id').groupby('item').sum().sort_values(by='quantity', ascending=False)


# 2. 영희가 가장 많이 구매한 아이템은?

# In[86]:


pd.merge(customer, orders, on='customer_id').groupby(['name', 'item']).sum().loc['영희', 'quantity']


# ### join 함수
# * 내부적으로 pandas.merge 함수 사용
# * 기본적으로 index를 사용하여 left join

# In[88]:


cust1.join(order1, how='inner')


# In[ ]:




