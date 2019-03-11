
# coding: utf-8

# In[ ]:


# -*- coding：utf-8 -*-
from langconv import *
def read_data(content):
    #intab定義了把不要的東西
    #outlab定義了把不要的東西變成什麼
    #str.maketrans 把兩個東西合併成一個dictionary
    #在for 迴圈的第一行 把content 的內容translate 
    #
    intab = "�‘’－'*；＝:）Обществоγῆγίψυχήγο《》（-%”[x{X&]#=}）μαθηματικός/;,abc|def\"X<>ghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWSYZ_()、「.1234567890：」?？※“ 『』〈〉，。\n！"
    outtab ="                                                                                                                                                  "
    #print(len(intab))
    #print(len(outtab))
    trantab = str.maketrans(intab, outtab)
    #print(content.translate(trantab))
    #print(content.translate(trantab).split(' '))
    #print(type(content.translate(trantab).split(' ')))
    words=[]
    vocabulary=[]
    #print(type(words))
    for word in content.translate(trantab).split(' '):
        if word!='' and word!='\u3000' and word!='\ufeff':
            #print(word.strip('　'))
            if(len(word.strip('　'))!=1 and word.strip('　')!='刪除守則' and word.strip('　')!='根據維基的'  and word.strip('　')!='粗體文字'  and word.strip('　')!='此處插入公式'  and word.strip('　')!='請點擊下麵網址連接' and word.strip('　')!='內容為' and word.strip('　')!='斜體文字' and word.strip('　')!='鏈接標題' and word.strip('　')!='侵犯了版權' and word.strip('　')!='版權聲明文章作者'):
            # or word.strip('　')!='根據維基的'  or word.strip('　')!='粗體文字'  or word.strip('　')!='此處插入公式'  or word.strip('　')!='請點擊下麵網址連接'
                vocabulary.append(word.strip('　'))
    return vocabulary
inf = open('zhwiki-latest-pages-articles.xml',encoding="utf8")
c=0
#do not change the file below which will lead to data cancelling
file = open("wiki_text.txt", "w",encoding="utf8")
for line in inf:
    line = Converter('zh-hant').convert(line)
    line=read_data(line)
    del line[0:4]
    if(len(line) != 0):
        del line[-1]
    if(len(line)>2):
        del(line[1])
    print(line)
    for i in line:
        file.write(i)
        file.write('\n')
    
file.close()

