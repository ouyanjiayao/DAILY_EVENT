#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install PyPDF2


# In[9]:


import pdfkit


# In[10]:


from apscheduler.schedulers.blocking import BlockingScheduler


# In[20]:


pip install apscheduler


# In[11]:


def task(s):
    print(s)


# In[19]:


if __name__ == '__main__':
    # 初始化调度器
    blocking_scheduler = BlockingScheduler()

    # 添加任务作业，args()中最后一个参数后面要有一个逗号，本任务设置在每天凌晨1:00:00执行
    scheduler.add_job(task, 'cron', hour='17', minute='45', second='0', args=("hello",))

    # 启动调度器，到点task就会被执行啦
    scheduler.start()


# In[16]:


from apscheduler.schedulers.blocking import BlockingScheduler


# In[17]:


import sys


# In[18]:


sys.path.append('../')


# In[15]:


import util.Reader as Reader


# In[14]:


pip install util


# In[1]:


import difflib
import sys
import argparse
import os
import pandas as pd


# In[2]:


def read_file(file_name):
    try:
        file_desc = open(file_name, 'r',encoding='gbk')
        # 读取后按行分割
        text = file_desc.read().splitlines()
        file_desc.close()
        return text
    except IOError as error:
        print ("Read input file Error: {0}".format(error))
        sys.exit()


# In[3]:


# 比较两个文件并把结果生成一份html文本
def compare_file(file1, file2):
    if file1 == "" or file2 == "":
        print('文件路径不能为空：第一个文件的路径：{0}, 第二个文件的路径：{1} .'.format(file1, file2))
        sys.exit()
    else:
        print("正在比较文件{0} 和 {1}".format(file1, file2))
    text1_lines = read_file(file1)
    text2_lines = read_file(file2)
    diff = difflib.HtmlDiff()    # 创建HtmlDiff 对象
    result = diff.make_file(text1_lines, text2_lines)  # 通过make_file 方法输出 html 格式的对比结果
    print(result)
    # 将结果写入到result_comparation.html文件中
    try:
        with open('D:/result_comparation.html', 'w',encoding='gbk') as result_file:
            result_file.write(result)
            print ("0==}==========> Successfully Finished\n")
    except IOError as error:
        print ('写入html文件错误：{0}'.format(error))


# In[4]:


file1 = 'D:/GoodsDetail/20210625.csv'
file2 = 'D:/GoodsDetail/20210725.csv'

compare_file(file1, file2)


# In[10]:


file1 = 'D:/26mon/2020-02-26morning.csv'
file2 = 'D:/26night/2020-02-26_night_total.csv'

compare_file(file1, file2)


# In[5]:


get_ipython().run_line_magic('tb', '')


# In[6]:


file2


# In[7]:


import hashlib
def get_file_md5(filename):
    '''可以比较两个文件的md5值，来比较文件内容。未使用'''
    md5 = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        md5.update(b)
    f.close()
    return md5.hexdigest()


# In[8]:


import filecmp
# true if 2 files are the same
result = filecmp.cmp(file1, file2)


# In[9]:


result


# In[1]:


pip install cacheout


# In[1]:


pip install --upgrade pip


# In[10]:


from cacheout import Cache


# In[11]:


cache = Cache()


# In[12]:


cache.set('a',45)


# In[13]:


cache.get('a')


# In[14]:


dir


# In[15]:


import os
os.getcwd()


# In[ ]:





# In[ ]:




