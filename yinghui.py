#!/usr/bin/python

import time 
ticks = time.time()

month = time.strftime('%m',time.localtime())
month = str(int(month))
day = time.strftime('%m',time.localtime())
day = str(int(day)+1)


if __name__ == '__main__':
    print('颖辉会在%s月%s日请我喝奶茶' %(month,day))
    
    