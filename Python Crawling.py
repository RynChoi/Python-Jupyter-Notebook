#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time


# In[9]:


chrome_driver = 'C:\chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(chrome_driver)

driver.get('https://www.python.org')

search = driver.find_element_by_id('id-search-field')

search.clear()
time.sleep(3)

search.send_keys('lambda')

time.sleep(3)
search.send_keys(Keys.RETURN)

time.sleep(3)



driver.close()


# In[13]:


chrome_driver = 'C:\chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)

url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=103&oid=011&aid=0003913994'
driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.u_cbox_info_txt')))

src = driver.page_source
soup = BeautifulSoup(src)

driver.close()

comment = soup.select_one('span.u_cbox_info_txt')
comment.get_text()


# In[15]:


import requests
from bs4 import BeautifulSoup


# In[22]:


def get_daum_news_title(news_id):
    url = 'https://news.v.daum.net/v/{}'.format(news_id)
    resp = requests.get(url)
    
    soup = BeautifulSoup(resp.text)
    


# In[17]:


get_daum_news_title('20190728165812603')


# In[18]:


get_daum_news_title('20210524230140392')


# In[24]:


def get_daum_news_content(news_id):
    url = 'https://news.v.daum.net/v/{}'.format(news_id)
    resp = requests.get(url)
    
    soup = BeautifulSoup(resp.text)
    
    content = ''
    for p in soup.select('div#harmonyContainer p'):
        content += p.get_text()
    return content


# In[25]:


get_daum_news_content('20190728165812603')


# In[26]:


get_daum_news_content('20210524230140392')


# In[27]:


url = 'https://comment.daum.net/apis/v1/posts/133493400/comments?parentId=0&offset=3&limit=10&sort=POPULAR&isInitial=false&hasNext=true&randomSeed=1621868803'

requests.get(url)


# In[ ]:




