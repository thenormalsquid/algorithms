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

    def union(self, p, q):
        pass
    

class QuickFind(UF):
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)

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



