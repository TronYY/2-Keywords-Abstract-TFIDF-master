# @Time         : 20190221
# @First Author : Richer
# @Mod by       : Jin Yang

本项目采用TF-IDF算法完成从中文文本中提取关键字
## 1. 将《微信公众号采集某个月份前所有文章采集方法记录》中2得到的excel保存至目录“2 Keywords-Abstract-TFIDF-master”下，比如将名字命名为“contents.xlsx”

## 2. 对于一批全新刚采集的文章，要将 train_data/tf_idf_input和 data/idf_out两个目录下的文件删除

## 3. train_data目录下的stop_words.txt存放了停用词，可以根据需要自己添加或删除，使用默认的也可以

## 4. 找到train.py文件

    if __name__ == '__main__':
    	run = MAIN('/contents.xlsx')#将内容excel第一列附上key(1,2,3...),
    	run.main()        

###   MAIN() 的参数,填入1中保存的名字。运行后train_data/tf_idf_input会出现若干txt文档，是由1中的excel每一单元格的文章内容转化而来

## 5. 得到单篇测试txt文章的关键词
### 找到runSingle.py,当在目录“2 Keywords-Abstract-TFIDF-master”下已有单篇测试txt文章时，运行该程序两次（第一次是用于得到逆文本频率指数（即data/idf_out下的文件），第二次用于得到单篇测试txt文章的关键词）
if __name__ == '__main__':
    run = MAIN('tf-idf', 'test1.txt')
    keywords = run.main()
    print(keywords)
### MAIN()两个参数，第二个参数为测试文章txt名

## 6. 得到1中excel中每篇文章的关键词
### 找到runMulti.py，
if __name__ == '__main__':
    excelName = '/contents.xlsx'#excel名
### excelName写的是1中excel的文件名
### runMulti.py文件最后的wb.save('contents_keywords.xlsx')的参数是最后导出excel文件名。最后的关键词即在该文件中