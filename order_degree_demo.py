#!/usr/bin/env python
# coding: utf-8

# In[181]:


import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


list1 = [(10, 20, 30),
 (10, 10, 20),
 (10, 10, 30),
 (10, 20, 10),
 (10, 20, 20),
 (10, 20, 30),
 (10, 30, 10),
 (10, 30, 20),
 (10, 30, 30),
 (20, 10, 10),
 (20, 10, 20),
 (20, 10, 30),
 (20, 20, 10),
 (20, 20, 20),
 (20, 20, 30),
 (20, 30, 10),
 (20, 30, 20),
 (20, 30, 30),
 (30, 10, 10),
 (30, 10, 20),
 (30, 10, 30),
 (30, 20, 10),
 (30, 20, 20),
 (30, 20, 30),
 (30, 30, 10),
 (30, 30, 20),
 (30, 30, 30)]
list2 = [0.0,0.25,0.5,0.75,1,1.25,1.5,1.75]
list3 = [1,2,3]
list4 = [1,0.1]


# In[4]:


list1 = ['近','远']
list2 = ['相同','不同']
list3 = ['多','少']


# In[5]:


def list_of_groups(list_info, per_list_len):
    '''
    :param list_info:   列表
    :param per_list_len:  每个小列表的长度
    :return:
    '''
    list_of_group = zip(*(iter(list_info),) *per_list_len) 
    end_list = [list(i) for i in list_of_group] # i is a tuple
    count = len(list_info) % per_list_len
    end_list.append(list_info[-count:]) if count !=0 else end_list
    return end_list

if __name__ == '__main__':
    list_info = list1
    ret = list_of_groups(list_info,1)
    print(ret)


# In[6]:


b=[]
for l1 in list1:
    a= []
    all_list = [l1,list2,list3,list4]
    a.extend(itertools.product(*all_list))
    b.extend(a)


# In[7]:


all_list


# In[8]:


len(b)


# In[9]:


len(a)


# In[182]:


data = pd.DataFrame(data) 


# In[183]:


data.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)


# In[184]:


data['azimuth']


# In[74]:


data[['azimuth']] = data[['azimuth']].astype(float)


# In[108]:


weight =  pd.DataFrame(pd.Series([2,1],index=['distance','goods_num'],name=0))


# In[109]:


weight


# In[110]:


data * weight[0]


# In[111]:


data.dot(weight)


# In[112]:


data['weighted_sum'] = data.dot(weight)


# In[185]:


data2 = data.sort_values(by='weighted_sum',ascending=False)


# In[77]:


data2 = data2.drop_duplicates()


# In[186]:


data.to_excel (r'D:\GoodsDetail\word_count7.xlsx', index =True, header=True)


# In[115]:


data2


# In[167]:


weight[0].to_excel (r'D:\GoodsDetail\word_count2.xlsx', index =True, header=True)


# In[88]:


data.to_excel (r'D:\GoodsDetail\word_count2.xlsx', index =True, header=True)


# In[204]:


distin_list1 = [10,20,30]


# In[205]:


distin_list2 = [10,20,30]


# In[206]:


distin_list3 = [10,20,30]


# In[207]:


all_dis_list =  [distin_list1,distin_list2,distin_list3]


# In[208]:


all_dis_list = list(itertools.product(*all_dis_list))


# In[209]:


all_dis_list


# In[3]:


print(getDegree(lat1, lon1, lat2, lon2))


# In[15]:


import math
lon1 = 116.73629442108817
lat1 = 23.37958171359216
lon2 = 116.74480264697759
lat2 = 23.36759474635962


# In[16]:


def getDegree(latA, lonA, latB, lonB):

    """

    Args:

    point p1(latA, lonA)

    point p2(latB, lonB)

    Returns:

    bearing between the two GPS points,

    default: the basis of heading direction is north

    """

    radLatA = math.radians(latA)

    radLonA = math.radians(lonA)

    radLatB = math.radians(latB)

    radLonB = math.radians(lonB)

    dLon = radLonB - radLonA

    y = math.sin(dLon) * math.cos(radLatB)

    x = math.cos(radLatA) * math.sin(radLatB) - math.sin(radLatA) * math.cos(radLatB) * math.cos(dLon)

    brng = math.degrees(math.atan2(y, x))

    brng = (brng + 360) % 360

    return brng


# In[17]:


print(getDegree(lat1, lon1, lat2, lon2))


# In[ ]:





# In[37]:


orign = list(data['方向'][0:100])


# In[38]:


dis = list(data['距离'][0:100])


# In[39]:


import matplotlib.pyplot as plt
import numpy as np

theta = np.array(orign)
r = dis

plt.polar(theta*np.pi,r,"ro",lw=2)
# plt.fill(theta*np.pi,r,'r',alpha=0.75)
plt.ylim(0,30)
plt.show()


# In[147]:


orign


# In[148]:


dis


# In[42]:


data.reindex([])


# In[50]:


random.shuffle(data)


# In[24]:


type(data['azimuth']).tolist()


# In[187]:


radiu = 30
level = 3
# a = [0,15,24,12,20,30,182,183,190,200,202,205,215,152,90,180,150,210,300,87,97,360]
a = data['azimuth'].tolist()

a.sort()
def group_direction(a,radiu,level):
    if not level:
        return a
    b = c = []
    for i in a:
        if not b:
            b = [i]
        else:
            if (i - b[-1] < radiu):
                b.append(i)
            else:
                c.append(b)
                b = [i]
            
    c.append(b)
    if level>1:
        tmp = []
        for i in c:
            tmp.extend(group_direction(i,math.sqrt(radiu),level-1))
        c = tmp
    
    return c


# In[188]:


d = group_direction(a,radiu,level)
import math


# In[189]:


d


# In[64]:


len(d)


# In[65]:


e = d[len(d)-1].extend(list(map(function_tmp, d[0])))


# In[66]:


d


# In[55]:


d[len(d)-1]


# In[58]:


def function_tmp(x):
    x+=360
    return x


# In[59]:


list(map(function_tmp, d[0]))


# In[60]:


d[0]


# In[71]:


f = group_direction(d[len(d)-1],radiu,level)


# In[72]:


f

