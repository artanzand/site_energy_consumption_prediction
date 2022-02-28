#!/usr/bin/env python
# coding: utf-8

# # EDA on Python
# ## Data Import
# For basic data profile, please check out [Profile Report]('ProfileReport_mini.html')

# In[1]:


import pandas as pd
import altair as alt
from altair_saver import save
alt.data_transformers.disable_max_rows();
alt.data_transformers.enable('data_server');
alt.renderers.enable('mimetype');
alt.renderers.enable('altair_saver', fmts=['vega-lite', 'svg']);


# In[2]:


train_df = pd.read_csv('data/widsdatathon2022/train.csv')
train_df.head()


# ## EDA
# ### Facility type
# - Commercial buildings has higher Energy Use Intensity (EUI) than residential building in general.

# In[3]:


train_df.groupby(['facility_type', 'building_class']).mean()['site_eui'].sort_values(ascending = False).head(10)


# In[4]:


sorted_mean = train_df.groupby('facility_type').mean('site_eui').sort_values('site_eui', ascending = False).index
alt.Chart(train_df).mark_boxplot(extent="min-max").encode(
    x=alt.X(
        "facility_type",
        sort=list(sorted_mean)
    ),
    y="site_eui:Q",
    color="building_class",
)


# ### Energy star rating 
# - Energy star rating is highly correlated to EUI

# In[5]:


alt.Chart(train_df).mark_boxplot(extent="min-max").encode(
    x=alt.X(
        "energy_star_rating",
    ),
    y="site_eui:Q",
    color="building_class",
).properties(width=1000)


# ### Elevation
# - Elevation does not correlate much with EUI.
# - How can we make use of this data?

# In[6]:


## Do a Binning
alt.Chart(train_df).mark_boxplot(extent="min-max").encode(
    x=alt.X(
        "ELEVATION",
         bin=alt.Bin(maxbins=50)
    ),
    y="site_eui:Q",
    color="building_class",
    tooltip=["count()"],
    facet=alt.Facet('building_class:N', columns=1),
).properties(height= 150, width=800)


# ### Built year
# - Residential buildings are less vary than Commercial Building.
# - New residential buildings built after 2000 has obvious EUI drop

# In[7]:


## Do facat

alt.Chart(train_df.query('year_built >= 1840')).mark_boxplot(extent="min-max").encode(
    x=alt.X(
        "year_built",
        scale=alt.Scale(domain=[1840, 2020])
    ),
    y="site_eui:Q",
    color="building_class:N",
    facet=alt.Facet('building_class:N', columns=1)
).properties(width=1000)#.configure_mark(
  #  opacity=0.8,
#)


# In[ ]:




