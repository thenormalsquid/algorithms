#classes representing the different algorithms used in lecture 1
#usage: from uf import QuickFind, ...

#read 1.5 and view lectures 1.1 to understand how
#this works

class  UF(object):
    
    def __init__(self, n):
        self.ct = n
        self.id = range(n)

    def count(self):
        return self.ct

    def find(self, p):
        pass

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pass
    

class QuickFind(UF):
    
    def __str__(self):
        return 'QuickFind'

    def find(self,  p):
        return self.id[p]

    def union(self, p, q):
        #place p and q into the same component
        idp = self.find(p)
        idq = self.find(q)

        if (idp == idq):
            return
        else:
            for i in xrange(len(self.id)):
                if(self.id[i] == idp):
                    self.id[i] = idq
    
        self.ct -= 1


class QuickUnion(UF):

    def __str__(self):
        return 'QuickUnion'

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return
        self.id[p_root] = q_root

        self.ct -= 1


class WeightedQuickUnion(UF):

    def __str__(self):
        return 'WeightedQuickUnion'

    def __init__(self, n):
        self.sz = range(n)
        super(WeightedQuickUnion, self).__init__(n)

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)

        if i == j:
            return

        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

        self.ct -= 1
        