#!/usr/bin/env python
# coding: utf-8

# In[24]:


# -*- coding:utf-8 -*-

import codecs
import imgkit
import pandas as pd
import pdfkit as pdfkit


class ExcelToImage:
    def __init__(self):
        super(ExcelToImage, self).__init__()
        self.config = imgkit.config(wkhtmltoimage='G:/pdf/wkhtmltopdf/bin/wkhtmltoimage.exe')
        self.html_head = """<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                <title>Document</title>
                            </head>
                            <body>"""

        self.html_end = """</body>
                            </html>"""
        

    def excel_html(self, excel_path, html_path):
        """
        excel to html
        :param excel_path: excel 路径
        :param html_path: html 存放 路径
        :return: html 路径集合
        """
        html_paths = []

        excel_obj = pd.ExcelFile(excel_path)  # excel 文件对象

        excel_sheets = excel_obj.sheet_names  # 获取 excel 所有单元

        # 将每个单元转换为 html 文件
        for index, sheet in enumerate(excel_sheets):
            html_path_own = html_path + sheet + ".html"
            print()

            # 获取本单元 excel 信息
            excel_data = excel_obj.parse(excel_obj.sheet_names[index])

            with codecs.open(html_path_own, 'w', 'utf-8') as html:
                # 加上头尾部, 防止中文乱码
                html_data = self.html_head + excel_data.to_html(header=True, index=True) + self.html_end

                html.write(html_data)

            html_paths.append(html_path_own)

        return html_paths

#     @staticmethod
#     def html_pdf(html_paths, pdf_path, config):
#         """
#         html to pdf
#         :param html_paths: html 路径
#         :param pdf_path: pdf 存放 结果 路径
#         :return:
#         """

#         for index, html_path in enumerate(html_paths):
#             pdf_obj = pdf_path + str(index) + ".pdf"
#             with open(html_path, "r", encoding="utf-8") as html_file:
#                 pdfkit.from_file(html_file, pdf_obj,config=config)

#     @staticmethod
    def html_image(self,html_paths, image_path):
        """
        html to image
        :param html_paths: html 路径
        :param image_path: image 存放 结果 路径
        :return:
        """
        for index, html_path in enumerate(html_paths):
            img_obj = image_path + str(index) + ".png"
            with open(html_path, "r", encoding="utf-8") as html_file:
                imgkit.from_file(html_file, img_obj,config=self.config)


if __name__ == '__main__':
    ReportImage = ExcelToImage()
    config = imgkit.config(wkhtmltoimage='G:/pdf/wkhtmltopdf/bin/wkhtmltoimage.exe')
    # excel 转 html
    html_paths = ReportImage.excel_html("D:/GoodsStatistics/2020-10-14_detail_morning_1602644318.xls", "D:/GoodsStatistics/html/")
    # html 转 pdf
#     ReportImage.html_pdf(html_paths, "D:/GoodsStatistics/pdf/",config)
    # html 转 image
    ReportImage.html_image(html_paths, "D:/GoodsStatistics/image/")



# In[2]:

config = imgkit.config(wkhtmltoimage='G:/pdf/wkhtmltopdf/bin/wkhtmltoimage.exe')

imgkit.from_string(html_string, output_file, config=config)

self.wkhtmltoimage = subprocess.Popen(['which', 'wkhtmltoimage'], stdout=subprocess.PIPE).communicate()[0].strip()






