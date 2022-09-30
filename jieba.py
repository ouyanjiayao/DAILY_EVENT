#!/usr/bin/env python
# coding: utf-8


# In[1]:


import  jieba


# In[2]:


text='切段+清洗'


# In[3]:


seq_list=jieba.cut(text,cut_all=False)


# In[4]:


print(seq_list) #<generator object Tokenizer.cut at 0x0000026EB6F0CD58>
print(list(seq_list))


# In[6]:


import pymysql


# In[7]:


import re


# In[8]:


conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='dhxs_new', charset='utf8',port=3306)   


# In[9]:


cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


# In[10]:


cursor.execute("select `name` from tbl_goods_attr_item where attr_id = 2")
item_names = cursor.fetchall()


# In[11]:


item_names


# In[12]:


item_list = []


# In[13]:


for i in item_names:
    jieba.load_userdict('G:/book/自定义词典.txt')
    sep_list=jieba.lcut(i['name'])
    item_list.append(sep_list)
#     print('userdict>>>',sep_list)
#     seq_list=jieba.cut(i['name'],cut_all=False)
#     print(list(seq_list))


# In[14]:


item_list


# In[15]:


import numpy as np


# In[16]:


np.unique(item_list)


# In[17]:


b = []
a = open(r"G:/book/停用词.txt",'rb').read()
text= jieba.cut(a)
for i in text:
    b.append("".join(i))


# In[ ]:


b


# In[ ]:


f = []
for k in item_names:

    if k['name'] not in b:
        print(k)
#         f.append(k)


# In[ ]:


f





