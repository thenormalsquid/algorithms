from uf import QuickFind, QuickUnion


class UFSimulator(object):

    def set_algo(self, obj):
        self.obj = obj

    def simulate(self):
        with open('test.txt', 'r') as f:
            n = int(f.readline())
            uf_obj = self.obj(n)
            print ('------------> Started Algo: ' + str(uf_obj) + '\n')
            for line in f.readlines():
                l = line.split(' ')
                p, q = (int(l[0]), int(l[1]))
                if (uf_obj.connected(p, q)):
                    print '%s is connected with %s' % (p, q)
                else:
                    uf_obj.union(p, q)
                    print ' connections: %s %s' % (p, q)
            print '%s components \n' % uf_obj.count()


if __name__ == '__main__':
#create instances of the classes here and test with a text file
    algos = [QuickUnion, QuickFind]
    ufsimulator = UFSimulator()

    for algo in algos:
        ufsimulator.set_algo(algo)
        ufsimulator.simulate()
    
        
            
        
        
    
    