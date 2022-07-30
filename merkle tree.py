import hashlib  #导入哈希模块

def cal_hash(data): #计算数据块的哈希值，其中哈希函数使用的是sha256（）
    data = data.encode('utf-8')  #编码字符串
    hash_value=hashlib.sha256(data)
    return hash_value.hexdigest()  #返回摘要，作为16进制数据字符串值

def Tree(lst): #对lst构造merkle tree
    n=0  #merkle tree的高度
    lst1 = []
    for i in lst:
        lst1.append(cal_hash(i)) #计算每个数据的hash值，存放在lst1中
    length=len(lst1)
    
    if length>=2:  #有多个数据块时
        
        tmp=lst1  #tmp用于存放当前层的hash值
        tmp2=[]  #tmp2用于存放上一层的，即当前层每两个hash值计算出的新hash值
        while True:
            print(tmp)
            length2=len(tmp)
            if length2<2:  #当前层hash值只有1个时，即为根结点时，无需再计算
                break
            a=length2 // 2  
            b=length2 % 2
            for i in range(a):
                index=i*2
                tmp2.append(cal_hash(tmp[index]+tmp[index+1]))
            if b!=0:
                tmp2.append(tmp[length2-1])  #如果当前层hash值个数不是2的倍数，新一层的hash值应该加上该层的最后一个
                
            tmp=tmp2  
            tmp2=[]
            n+=1
    else:
        print("只有一个数据块")
        print(lst1)
    return n+1  #返回merkle tree的高度
    
    
l = ['a', 'b','c','d','e']
print(Tree(l))
