
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

# class NodeList:
#     Node_List = []
#     node = [Node(None,None,None,None) for i in range(1000)]
#     def __init__(self,Node_List):
#         for i in Node_List:
#             count = 0
#             if i==0:
#                 node[i].val = Node_List[i]
#                 node[i].prev = None
#                 node[i].next = Node_List[i + 1]
#             else:
#                 Node[i].val = Node_List[i]
#                 Node[i].prev = Node_List[i - 1]
#                 Node[i].next = Node_List[i + 1]
#             if Node_List[i] == None:
#                 count += 1
#             if Node_List[i] == None & Node_List[i+1] != 0:
#                 Node[count-1].child = Node_List[i+1]
#                 Node[i+1].pre=Node[count-1]
#                 Node[count-1].next=Node[i+1]
#             if i == (Node_List.lenth-1):
#                 Node[i].next = None

# """节点类"""
# class Node(object):
#     def __init__(self, data=None):
#         self.data = data
#         self.pre = None
#         self.next = None
#         self.child = None
#
# """初始化双向链表"""
#
#     def __init__(self):
#         """
#         设置头尾，操作比较容易
#         头－－（next）－－》尾
#         尾－－（pre）－－》头
#         :return:
#         """
#         head = Node()
#         tail = Node()
#         self.head = head
#         self.tail = tail
#         self.head.next = self.tail
#         self.tail.pre = self.head
#
#     def append(self, data):
#         """
#         :param data:
#         :return:
#         """
#         node = Node(data)
#         pre = self.tail.pre
#         pre.next = node
#         node.pre = pre
#         self.tail.pre = node
#         node.next = self.tail
#         return node


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node: "Node") -> "Node":
            cur = node  # 记录链表的最后一个节点
            last = None

            while cur:
                nxt = cur.next
                # 如果有子节点，那么首先处理子节点
                if cur.child:
                    child_last = dfs(cur.child)

                    nxt = cur.next
                    # 将node与child相连
                    cur.next = cur.child
                    cur.child.prev = cur

                    # 如果nxt不为空，就将last与nxt相连
                    if nxt:
                        child_last.next = nxt
                        nxt.prev = child_last

                    # 将chiLd置为空
                    cur.child = None
                    last = child_last

                else:
                    last = cur
                cur = nxt

            return last

        dfs(head)
        return head

