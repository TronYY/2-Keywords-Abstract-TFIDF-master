# -*- coding: utf-8 -*-
# @Time        : 2019/02/21 17:22
# @FirstAuthor : Richer
# @Mod By      : Jin Yang


import os,sys
import xlrd                           #导入模块
from xlutils.copy import copy
from lib.tf_idf.get_idf import IDF
from bin.tfidf import TFIDF
excel = os.getcwd()



class MAIN():
    def __init__(self, model='tf-idf', file = ''):
        self.model = model
        self.base_path = os.getcwd()
        self.idf_file = self.base_path + '/data/idf_out/idf.txt'
        self.file = self.base_path + '/train_data/tf_idf_input/' + file
        #self.excel = self.base_path + '/train_data/tf_idf_input/' + excel


    def main(self):
        keywords = []
        if self.model == 'tf-idf':
            if not os.path.isfile(self.idf_file):
                idfObj = IDF()
                idfObj.idf()
            else:
                main = TFIDF(self.file)
                keywords = main.key_abstract()
        else:
            # 还有一种方式
            keywords = ''

        return keywords
if __name__ == '__main__':
    excelName = '/contents.xlsx'#excel名
    excelPath = excel + excelName
    data = xlrd.open_workbook(excelPath)  # excel不能单独一列，会有keyError
    sheets = data.sheets()  # 查询工作表
    sheet_1_by_name = data.sheet_by_name(u'Sheet 1')

    # 通过工作表的属性获得行数和列数。
    n_of_rows = sheet_1_by_name.nrows
    n_of_cols = sheet_1_by_name.ncols

    wb = copy(data)#写excel  利用xlutils.copy下的copy函数复制
    ws = wb.get_sheet(0)  # 获取表单0

    for i in range(1, n_of_rows):
        run = MAIN('tf-idf', 'test'+str(i)+'.txt')
        keywords = ""
        keywords = run.main()
        printKeywords = ','.join(str(n) for n in keywords)
        ws.write(i, 2, printKeywords)
        print(i, printKeywords)

    wb.save('contents_keywords.xlsx')



