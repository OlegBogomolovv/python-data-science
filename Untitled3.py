#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[4]:


import pandas as pd


# In[8]:


authors = pd.DataFrame({'author_id':[1, 2, 3], 'author_name':['Тургеньев', 'Чехов', 'Островский']}, columns=['author_id', 'author_name'])


# In[9]:


authors


# In[17]:


book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3], 'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий',
             'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 'price':[450, 300, 350, 500, 450, 370, 290]}, columns=['author_id', 'book_title', 'price'])


# In[18]:


book


# In[21]:


authors_price = pd.merge(authors, book, on = 'author_id', how = 'inner')


# In[22]:


authors_price


# In[24]:


top5 = authors_price.nlargest(5, 'price')


# In[25]:


top5


# In[ ]:


aut

