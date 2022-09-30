#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install Image


# In[33]:


from PIL import Image, ImageFont, ImageFile
import shutil 
import os 
ImageFile.LOAD_TRUNCATED_IMAGES = True


# In[34]:


path = "D:/uploads/0405/"
path2 = "D:/uploads/0405_100/"
path3 = "D:/uploads/0405_250/"
dirs = os.listdir(path)


# In[35]:


dirs


# In[36]:


x = dirs[0].split('.',1)


# In[37]:


def fixed_size(infile, outfile, width, height): 
    im = Image.open(infile) 
    out = im.resize((width, height),Image.ANTIALIAS) 
    out.save(outfile) 


# In[7]:


for i in dirs:
    x = '' 
    x = i.split(".", 1)
    fixed_size(path+i,path3+x[0]+'_250x0.'+x[1], 250, 250)


# In[39]:


for i in dirs:
    x = '' 
    x = i.split(".", 1)
    fixed_size(path+i,path2+x[0]+'_100x0.'+x[1], 80, 80)


# In[ ]:




