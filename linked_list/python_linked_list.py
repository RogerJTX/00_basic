class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


if __name__ == '__main__':
    head = None
    for n in range(1, 6):
        head = Node(n, head)

    while head != None:
        print(head.data)
        head = head.next