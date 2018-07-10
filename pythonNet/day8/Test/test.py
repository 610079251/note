#计算密集

def count(x,y):
    c = 0
    while c < 6000000:
        c += 1
        x += 1
        y += 1

#IO密集
def write():
    f = open('test.txt','w')
    for x in range(1000000):
        f.write("比利时加油\n")
    f.close()

def read():
    f = open('test.txt')
    lines = f.readlines()
    f.close()
