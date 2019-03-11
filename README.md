# Chinese Word2vect
在going through 這個實作之前，之乎上的這邊文章(https://zhuanlan.zhihu.com/p/31023929)有提到史丹佛的glove word vector 跟google word2vect的差異，會事先提起這件事是因為之後R-net的使用上，R-net是使用glove的。不過這當然不是種點啦，這篇git主要是紀錄一下我在word2vect實作中使用到的一些東西以及程式碼，讓自己之後不會忘記而已。
除此之外，想要使用Chinese word embedding的不妨直接造訪(https://github.com/Embedding/Chinese-Word-Vectors)，這裡有北京師範大學學者所開源的詞向量，以及中文analogue test 的資料及CA8。well done!

以下就進入Chinese word2vect實作的部分
step1: text pasing 請點texr parsing 資料夾，裡面主要使用了中研院的斷詞系統以及subsampling
step2: 帶入google 已經寫好的tensorflow code
