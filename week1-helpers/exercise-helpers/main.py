from uf import UF, QuickFind

if __name__ == '__main__':
#create instances of the classes here and test with a text file 
    with open('test.txt', 'r') as f:
        n = int(f.readline())

        qf = QuickFind(n)

        for line in f.readlines():
            l = line.split(' ')
            p, q = (int(l[0]), int(l[1]))
            if (qf.connected(p, q)):
                print '%s is connected with %s' % (p, q)
            else:
                qf.union(p, q)
                print ' connections: %s %s' % (p, q)
            
        print '%s components' % qf.count()
        
        
    
    