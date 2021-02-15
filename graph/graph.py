'''
description: python 图的基本代码
date: 2020-12-10
author: jtx
url: https://blog.csdn.net/qq_39422642/article/details/79473289
     https://blog.csdn.net/qq_29681777/article/details/84202039
keyword:
    1.邻接矩阵
    2.邻接表



'''




class Graph:
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("参数错误")
        self._mat = [mat[i][:] for i in range(vnum)]  # 做拷贝
        self._unconn = unconn
        self._vnum = vnum

    # 顶点个数
    def vertex_num(self):
        return self._vnum

    # 顶点是否无效
    def _invalid(self, v):
        return v < 0 or v >= self._vnum

    # 添加边
    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + "不是有效的顶点")
        self._mat[vi][vj] = val

    # 获取边的值
    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + "不是有效的顶点")
        return self._mat[vi][vj]

    # 获得一个顶点的各条出边
    def out_edges(self, vi):
        if self._invalid(vi):
            raise ValueError(str(vi) + "不是有效的顶点")
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edegs = []
        for i in range(len(row)):
            if row[i] != unconn:
                edegs.append((i, row[i]))
        return edegs

    def __str__(self):
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]" + "\nUnconnected: " + str(self._unconn)



class GraphAL(Graph):
    def __init__(self, mat=[], unconn=0):
        super().__init__(mat)
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("参数错误")
        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum

    # 添加顶点
    # 返回该顶点编号
    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    # 添加边
    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise ValueError("不能向空图添加边")
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + "不是有效的顶点")

        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj, val)  # 如果原来有到vj的边，修改mat[vi][vj]的值
                return
            if row[i][0] > vj:  # 原来没有到vj的边，退出循环后加入边
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    # 获取边的值
    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + "不是有效的顶点")
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    # 获得一个顶点的各条出边
    def out_edges(self, vi):
        if self._invalid(vi):
            raise ValueError(str(vi) + "不是有效的顶点")
        return self._mat[vi]


a, b, c, d, e, f, g, h = range(8)
N = [
[b, c, d],
[a, e, g],
[d, g, h],
]
#print(N)
g = GraphAL(N, 0)
print(b)
print(g.out_edges(b))
