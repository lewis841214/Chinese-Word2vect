
step1: 
Parsing a xml's text and remain a text file
裡面使用了繁轉簡的函式庫，網址為:http://www.bkjia.com/Pythonjc/440646.html

step2:
使用中研院中文斷詞系統， http://ckipsvr.iis.sinica.edu.tw/ckipws/reg.php 
在該子目錄下 在cmd中打指令
CKIPWSTester     ws.ini    test\sample.txt  test\sample.tag
即可得到斷詞後的檔案，不過這個步驟其實花很多時間，要注意的是，他的斷詞系統要安裝32位元的python3 才能執行

step3:
這邊開始做原始word2vect中的subsampling，subsampling可以不只做一次，我自己是認為做多次一點，或者更乾脆把stop word拿掉，會更好，不過我在網路上有看到別人的文章說把stop word拿掉對整體word vector的精確度是沒有影響的，這道有點出乎我的意料之外。大家如果有時間可以試試看比較一下(拿北京師範大學的CA8資料庫來測試一下)





