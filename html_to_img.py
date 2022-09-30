#!/usr/bin/env python
# coding: utf-8

# In[6]:


def html_image(html_paths, image_path, config, image_name):
    """
    html to image
    :param html_paths: html
    :param image_path: image
    :return:
    """
    for index, html_path in enumerate(html_paths):
        img_obj = image_path + image_name + ".jpg"
        with open(html_path, "r", encoding="utf-8") as html_file:
            imgkit.from_file(html_file, img_obj, config=config)


# In[7]:


def to_one_image(excel_name=None, image_name=None):
    if not excel_name:
        return
    ReportImage = ExcelToImage()
    # self.wkhtmltoimage = subprocess.Popen(['which', 'wkhtmltoimage'], stdout=subprocess.PIPE).communicate()[0].strip()
    config = imgkit.config(wkhtmltoimage=self.default_config['to_image']['image_config_path'])
    # excel 转 html
    html_paths = ReportImage.excel_html(excel_name, self.default_config['to_image']['html_path'])
    # html 转 image
    ReportImage.html_image(html_paths, self.default_config['to_image']['image_path'], config, image_name)


# In[18]:


config = imgkit.config(wkhtmltoimage='G:/pdf/wkhtmltopdf/bin/wkhtmltoimage.exe')


# In[31]:


html_image(['E:/DeskTop/timeline.html'], 'F:/php-project/new/', config, '210215')


# In[15]:


import pdfkit as pdfkit


# In[16]:


import imgkit


# In[ ]:




