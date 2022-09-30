#!/usr/bin/env python
# coding: utf-8
# pip install pywin32
# pip install pdfkit

from win32com.client import gencache
from win32com.client import constants, gencache

def createPdf(wordPath, pdfPath):
    """
    word转pdf
    :param wordPath: word文件路径
    :param pdfPath:  生成pdf文件路径
    """
    word = gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(wordPath, ReadOnly=1)
    doc.ExportAsFixedFormat(pdfPath,
                            constants.wdExportFormatPDF,
                            Item=constants.wdExportDocumentWithMarkup,
                            CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
    word.Quit(constants.wdDoNotSaveChanges)

if __name__ == '__main__':
    createPdf('E:/DeskTop/总结.docx','E:/DeskTop/qqq.pdf')

