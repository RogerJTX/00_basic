'''
据说著名犹太历史学家Josephus有过以下的故事：在罗马人占领乔塔帕特后，39 个犹太人与Josephus及他的朋友躲到一个洞中，
39个犹太人决定宁愿死也不要被敌人抓到，于是决定了一个自杀方式，41个人排成一个圆圈，由第1个人开始报数，
每报数到第3人该人就必须自杀，然后再由下一个重新报数，直到所有人都自杀身亡为止。然而Josephus 和他的朋友并不想遵从。
首先从一个人开始，越过k-2个人（因为第一个人已经被越过），并杀掉第k个人。接着，再越过k-1个人，并杀掉第k个人。
这个过程沿着圆圈一直进行，直到最终只剩下一个人留下，这个人就可以继续活着。问题是，给定了和，一开始要站在什么地方才能避免被处决。
Josephus要他的朋友先假装遵从，他将朋友与自己安排在第16个与第31个位置，于是逃过了这场死亡游戏。
'''


#循环链表解决约瑟夫问题
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LoopLinkedList:
    def __init__(self):
        self.root = None

    # 在循环链表尾部添加节点，尾部即头结点上一个
    def addNode(self, data):
        newNode = Node(data)
        if self.root==None:
            self.root = newNode
        else:
            cursor = self.root
            while cursor.next!= self.root:
                cursor = cursor.next
            cursor.next = newNode
        newNode.next=self.root      #链接成环

    #链表长度
    def size(self):
        if self.root == None:
            return 0
        cursor = self.root
        i=1
        while cursor.next != self.root:
            i+=1
            cursor = cursor.next
        return i

#约瑟夫问题仿真函数
def circle(num,nameList):
    linkedList=LoopLinkedList()
    for i in range(len(nameList)):
        linkedList.addNode(nameList[i])
    i = 1
    pre = linkedList.root
    cursor = linkedList.root
    while linkedList.size() != 1:
        if i != num:
            pre=cursor
            cursor=cursor.next
            i += 1
        else :
            print('删除节点:', pre.next.data)
            pre.next=cursor.next    #删除当前节点需要用上一个节点连接下一个节点
            cursor=pre.next

            linkedList.root=cursor  #重新选择头结点是为了计算链表长度
            i = 1
    return cursor.data

#主函数
if __name__=='__main__':
    nameList=["Bill","David","Susan","Jane","Kent","Brad"]
    print(circle(7,nameList))
#输出结果
#Kent