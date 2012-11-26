from math import pow

def p9():
    m = 2
    a, b, c = 0, 0, 0
    
    while a+b+c != 1000:
        for n in range(1, m):
            g = int(pow(m,2))
            h = 2*int(pow(n,2))
            i = 2*m*n
            
            a = g+i
            b = h+i
            c = g+h+i
             
            if a+b+c == 1000:
                print 'Result: ',a*b*c
                return
        m+=1
                
if __name__ == '__main__':
    p9()
