![](E:\笔记\蓝桥杯\图片\day2.1.png)

```python
class MyHashSet:

    def __init__(self):
        self.mod = 1000 #设置哈希函数空间
        self.bucket = [[] for i in range(self.mod)] #初始化哈希函数


    def add(self, key: int) -> None:
        k = key % self.mod #求key所在哈希函数的位置
        if key not in self.bucket[k]: #判断key是否已经在k位置上
            self.bucket[k].append(key) 


    def remove(self, key: int) -> None:
        k = key % self.mod 
        if key in self.bucket[k]: #判断k位置上是否有key的值，有则删除
            self.bucket[k].remove(key)


    def contains(self, key: int) -> bool:
        k = key % self.mod
        return key in self.bucket[k] #返回key是否在k的位置上


```

