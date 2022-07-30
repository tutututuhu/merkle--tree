# merkle--tree
   Merkle tree是一个在密码学中常使用的树形结构，适用于解决数据完整性问题。 它的结构功能异常简单，通常我们用二叉树的形式来表示一棵 Merkle树， 它存在的作用是数据分组并保证数据在存储中的完整性。

   Merkle tree的存在性和不存在性证明：
  
   在整棵树尚未完整下载的情况下，仅通过下载的部分数据来进行完整性校验，快速判断某数据小组是否在其应处的位置。仅需知晓4个哈希值即可证明该数据块是否存在。即：相邻数据块的哈希值，相邻分组的联合哈希值，相邻分支的哈希值以及根节点的哈希值。 

  Merkle tree的简单实现：
  
   （1）对data blocks分别计算哈希值（采用sha256算法）；

   （2）每层两两计算获得哈希值，并将每一层的hash值从左到右存放在一个列表中。

   （3）直至计算至最上一层，得到根节点。

  本实验中使用的数据为‘a’,‘b’，‘c’，‘d’,‘e’,下图中的第一个列表表示最低层的hash值，最后一个列表表示根节点的hash值。（相当于一个倒的merkle tree）
  
  <img width="404" alt="image" src="https://user-images.githubusercontent.com/110089380/181920837-2b752e07-d9e0-4974-a894-39b048afbb40.png">

  一些问题和局限：
  
本次实验只是使用python语言简单实现merkle tree，体会一下merkle tree的实现思想。与现实应用中的merkle tree存在非常大的差距。

  参考文献：

https://ethbook.abyteahead.com/ch4/merkle.html
