#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymysql


# In[2]:


import json


# In[3]:


import pandas as pd


# In[4]:


import re


# In[5]:


conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='local_db', charset='utf8',port=3306)  


# In[6]:


conn


# In[7]:


cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


# In[8]:


cursor.execute("select * from order where order_state>1 and order_num is not null and delivery_start_time BETWEEN 1662787860 AND 1662825600 order by id asc ")
purchase = cursor.fetchall()


# In[9]:


purchase


# In[10]:


data=purchase.copy()


# In[11]:


len(data)


# In[12]:


inserts = []
for i in data:
    o = i.get('order_data')
    if o:
        order_data = json.loads(o)
    for m in order_data['details']:
        #         print(m)
        if m.get('type') == 1 and (m.get('dp_id',0)!=''):

            sku_properties_name = ''
            tag = ''
            if m.get('tag_id','None') != 'None':
                cursor.execute("select name from goods_tag where id=%s", m['tag_id'])
                tag = cursor.fetchone()
                if tag:
                    tag = tag['name']
                else:
                    tag = '未分类'
            else:
                tag = '未分类'
            handle = []
            attr = []
            handle5 = ''
            attr5 = ''
            if m.get('sku_properties_name'):
                for l in m['sku_properties_name']:
                    sku_properties_name += l['k'] + ':' + l['v']
                    if l['k'] == '加工方式':
                        handle.append(l['k'] + ':' + l['v'])
                    else:
                        attr.append(l['k'] + ':' + l['v'])
                    attr5 = ','.join(attr)
                    handle5 = ','.join(handle)
            inserts.append((m['dp_id'], m['title'], m['sku_ids'], attr5, handle5, m['weight'], m['count'], tag, m.get('tag_id','None')))

    for j in order_data['cp_config']:
        for k in j['dp_config']:
            #             print(k)
            handle1 = []
            attr1 = []
            handle3 = ''
            attr3 = ''
            tag_names = ''
            if k.get('dp_id', 0) != '':
                if k['tag_id'] != 'None':
                    cursor.execute("select name from goods_tag where id=%s", k['tag_id'])
                    tag_names = cursor.fetchone()
                    if tag_names:
                        tag_names = tag_names['name']
                    else:
                        tag_names = '未分类'
                else:
                    tag_names = '未分类'
                if k.get('desc'):
                    for d in k['desc'].split(','):
                        if d.find('加工方式') >= 0:
                            handle1.append(d)
                        else:
                            attr1.append(d)
                        attr3 = ','.join(attr1)
                        handle3 = ','.join(handle1)
                inserts.append((k['dp_id'], k['dp_name'], k['sku_ids'], attr3, handle3, k['weight'], k['count'], tag_names, k['tag_id']))

    for n in order_data['tc_config']:
        for tc in n['tc_config']:
            for dp_config in tc['dp_config']:
                tc_tag = ''
                if dp_config.get('dp_id',0)!='':
                    if dp_config['tag_id'] != 'None':
                        cursor.execute("select name from goods_tag where id=%s", dp_config['tag_id'])
                        tc_tag = cursor.fetchone()
                        if tc_tag:
                            tc_tag = tc_tag['name']
                        else:
                            tc_tag = '未分类'
                    else:
                        tc_tag = '未分类'
                    handle2 = []
                    attr2 = []
                    handle4 = ''
                    attr4 = ''
                    if dp_config.get('desc'):
                        for des in dp_config['desc'].split(','):
                            if des.find('加工方式') >= 0:
                                handle2.append(des)
                            else:
                                attr2.append(des)
                            attr4 = ','.join(attr2)
                            handle4 = ','.join(handle2)

                    inserts.append((dp_config['dp_id'], dp_config['dp_name'], dp_config['sku_ids'], attr4, handle4, dp_config['weight'], dp_config['count'], tc_tag, dp_config['tag_id']))
if len(inserts) > 0:
    cursor.executemany("insert into bill_dp_on(dp_goods_id,dp_name,sku_id,sku_name,handle,weight,count,tag_name,tag) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", inserts)
    conn.commit()


# In[29]:


cursor.close()


# In[13]:

# 格式转换
file_name = 'D:/20220910004.csv'
data = pd.read_csv(file_name, encoding='gbk')
rows = data.shape[0]  # 获取行数 shape[1]获取列数
goods_list = []
data.columns = ['商品名称', '规格','加工方式', '重量', '累计重量','累计数量', '分类']
data.fillna('', inplace=True)
x = data.copy()
for i in range(rows):
    if x.iloc[i, 6] == '':
        x.iloc[i, 6] = '未分类'
    temp = x.iloc[i, 6]
    if temp not in goods_list:  # 防止重复
        goods_list.append(temp)  # 将分类存在一个列表中
n = len(goods_list)  # 商品数
df_list = []
df_data = {}
for i in range(n):
    df_data[i] = pd.DataFrame()
    df_list.append(df_data[i])

for categories in range(n):
    for i in range(0, rows):
        if x.iloc[i, 6] == goods_list[categories]:
            df_list[categories] = pd.concat([df_list[categories], x.iloc[[i], :]], axis=0, ignore_index=True)

re_file_name = file_name.replace(".csv", ".xlsx")
writer = pd.ExcelWriter(re_file_name)  # 利用pd.ExcelWriter()存多张sheets
for i in range(n):
    df_list[i].to_excel(writer, sheet_name=str(goods_list[i]), index=False, encoding='utf_8_sig')  # 注意加上index=FALSE 去掉index列
writer.save()


# In[117]:


import zmail

def send_email_to(subject,content_text,attachments,receivers,cc):
    mail_content = {
        'subject': subject,
        'content_text': content_text,
        'attachments': attachments
    }

    server = zmail.server('abcd@163.com', '123456')
    server.send_mail(receivers, mail_content, cc)
    print('send success')


# In[121]:


subject = '单品统计20210211上午'
content_text = '单品统计20210210上午'
attachments = ['D:/20210211.xlsx']
cc = []

receivers = ['abcd@efgh.com']
send_email_to(subject, content_text, attachments, receivers, cc)


# In[ ]:




