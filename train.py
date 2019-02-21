# -*- coding: utf-8 -*-
# @Time         : 20190221
# @First Author : Richer
# @Mod by       : Jin Yang


import os,sys
import xlrd


class MAIN():
    def __init__(self, excel = ''):

        self.base_path = os.getcwd()
        self.excel = self.base_path + excel


    def main(self):
        data = xlrd.open_workbook(self.excel)  # excel不能单独一列，会有keyError
        sheets = data.sheets()  # 查询工作表
        sheet_1_by_name = data.sheet_by_name(u'Sheet 1')
        # 通过工作表的属性获得行数和列数。
        n_of_rows = sheet_1_by_name.nrows
        n_of_cols = sheet_1_by_name.ncols

        for i in range(1, n_of_rows):
            f = open(self.base_path + '/train_data/tf_idf_input/' + 'test' + str(i) + '.txt', "wb")
            tmp = ""
            tmp = str(sheet_1_by_name.cell(i, 1))#内容在第1列（列号从0开始）
            f.write(tmp.encode('utf8'))

if __name__ == '__main__':
    run = MAIN('/contents.xlsx')#将内容excel第一列附上key(1,2,3...),
    run.main()
