
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[2]:


get_ipython().run_line_magic('sql', 'postgresql://postgres@psql:5432/postgres')


# Find the country whose GDP has grown the most over time and plot the level of education on the x axis and the life expectancy on the y axis. Do the same thing for the country whose GDP has grown the least over time

# In[8]:


get_ipython().run_cell_magic('sql', '', 'drop view max;\ncreate view max as\nselect location, max(time) as time from gdp group by location')


# In[10]:


get_ipython().run_cell_magic('sql', '', 'drop view min;\ncreate view min as\nselect location, min(time) as time from gdp group by location')


# In[12]:


get_ipython().run_cell_magic('sql', '', 'drop view maxexp;\ncreate view maxexp as\nselect location, avg(value) from max join gdp using(location, time) group by location order by location asc')


# In[14]:


get_ipython().run_cell_magic('sql', '', 'drop view minexp;\ncreate view minexp as\nselect location, avg(value) from min join gdp using(location, time) group by location order by location asc')


# In[16]:


get_ipython().run_cell_magic('sql', '', 'drop view growth;\ncreate view growth as\nselect location, (maxexp.avg-minexp.avg)/minexp.avg*100 as gro from minexp join maxexp using (location) order by gro asc')


# To find out the average 

# In[80]:


get_ipython().run_cell_magic('sql', '', 'select * from growth')


# In[17]:


get_ipython().run_cell_magic('sql', '', 'create view maxlife as\nselect location, max(time) as time from life where location = 4 group by location')


# In[18]:


get_ipython().run_cell_magic('sql', '', 'create view bralife as\nselect location, time, avg(value) as value from life\nwhere life.location = 4\ngroup by time, location\norder by time asc')


# In[19]:


get_ipython().run_cell_magic('sql', '', 'create view brasilian as\nselect education. location, education.time, avg(education.value) as eduscore, avg(bralife.value) as lifeexp from education\njoin bralife using(time)\nwhere education.location = 4\ngroup by education.time, education.location\norder by education.time asc')


# In[20]:


import matplotlib.pyplot as plt


# In[21]:


result = get_ipython().run_line_magic('sql', 'select eduscore, lifeexp from brasilian')


# In[22]:


list1, list2 = zip(*result)
plt.scatter(list1,list2)
plt.show


# In[23]:


get_ipython().run_cell_magic('sql', '', 'create view minlife as\nselect location, max(time) as time from life where location = 28 group by location')


# In[24]:


get_ipython().run_cell_magic('sql', '', 'create view kolife as\nselect location, time, avg(value) as value from life\nwhere life.location = 28\ngroup by time, location\norder by time asc')


# In[26]:


get_ipython().run_cell_magic('sql', '', 'create view korea as\nselect education. location, education.time, avg(education.value) as eduscore, avg(kolife.value) as lifeexp from education\njoin kolife using(time)\nwhere education.location = 28\ngroup by education.time, education.location\norder by education.time asc')


# In[27]:


result = get_ipython().run_line_magic('sql', 'select eduscore, lifeexp from korea')


# In[28]:


list1, list2 = zip(*result)
plt.scatter(list1,list2)
plt.show

