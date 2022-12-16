class ListNode:

    def __init__(self,val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0,val)


    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index > self.size:
            return
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add =  ListNode(val)
        to_add.next = pred.next
        pred.next = to_add
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        p = self.head
        pre = self.head
        for _ in range(index):
            pre = p
            p = p.next
        pre.next = p.next
        p = None
        self.size -= 1

linkedList = MyLinkedList()
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   #链表变为1-> 2-> 3
linkedList.get(1);            #返回2
linkedList.deleteAtIndex(1);  #现在链表是1-> 3
linkedList.get(1);            #返回3