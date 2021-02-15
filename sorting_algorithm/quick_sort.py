'''
descroption:快速排序 及 时间复杂度
https://www.cnblogs.com/sfencs-hcy/p/10602598.html
'''

def quick_sort(s):
    """快速排序，s为列表"""
    # 结束条件
    if len(s) < 2:
        return
    # 从列表取出一个元素作为基准值
    p = s[0]
    L = [] # 小于
    E = [] # 等于
    R = [] # 大于
    # 把s里的元素放入3个队列
    while len(s) > 0:
        if s[-1] < p:
            L.append(s.pop())
        elif s[-1] == p:
            E.append(s.pop())
        else:
            R.append(s.pop())

    quick_sort(L)
    quick_sort(R)
    s.extend(L)
    s.extend(E)
    s.extend(R)


# TODO 就地快速排序
def inplace_quick_sort(s,a,b):
    """列表的就地快速排序，s为列表，a为起始索引，b为终止索引"""
    if a >= b:
        return
    # s[b]作为基准值
    p = s[b]
    # left和right相当于指向
    left = a
    right = b-1
    # 把除了s[b]d 其他元素按照以s[b]为基准分割
    while left <= right:

        while left <= right and s[left] < p:
            left += 1

        while left <= right and p < s[right]:
            right -=1

        if left <= right:
            s[left],s[right] = s[right],s[left]
            left,right = left+1,right-1

    s[left],s[b] = s[b],s[left]
    inplace_quick_sort(s,a,left-1)
    inplace_quick_sort(s,left+1,b)


# TODO 分而治之+递归
def quick_sort2(data):
    """快速排序"""
    if len(data) >= 2:  # 递归入口及出口
        mid = data[len(data) // 2]  # 选取基准值，也可以选取第一个或最后一个元素
        left, right = [], []  # 定义基准值左右两侧的列表
        data.remove(mid)  # 从原始数组中移除基准值
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


if __name__ == '__main__':
    s = [1, 7, 3, 5, 4]
    quick_sort(s)
    print(s)