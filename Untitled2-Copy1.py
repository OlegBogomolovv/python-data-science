#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = np.array([[1, 6], [2, 8], [3, 11], [3, 10], [1, 7]])


# In[3]:


import numpy as np


# In[7]:


a.shape


# In[8]:


a


# In[15]:


mean_a = np.mean(a, axis = 0)


# In[16]:


mean_a


# 

# In[18]:


a


# In[20]:


a_centered = a - mean_a


# In[21]:


a_centered


# In[24]:


a.dot


# In[30]:


a_centered_sp = (-1) * 0 * 1 * 1 * (-1) + (-2.4) * (-0.4) * 2.6 * 1.6 * (-1.4)


# In[31]:


a_centered_sp


# In[32]:


a_centered_sp / (5-1)


# In[ ]:




