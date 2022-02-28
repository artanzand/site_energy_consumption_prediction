#!/usr/bin/env python
# coding: utf-8

# # EDA on R
# ## Data Import
# 
# For basic data profile, please check out [Profile Report]('ProfileReport_mini.html')

# In[1]:


library(tidyverse)
library(ggplot2)


# In[2]:


train_df = read_csv('data/widsdatathon2022/train.csv')
head(train_df)


# In[ ]:




