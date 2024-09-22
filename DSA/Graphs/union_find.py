class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, u: int):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u: int, v: int):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.parents[pv] = pu
            self.rank[pu] += self.rank[pv]
        else:
            self.parents[pu] = pv
            self.rank[pv] += self.rank[pu]

        return True
