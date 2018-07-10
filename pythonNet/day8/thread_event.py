import threading 
from time import sleep 

msg = None 

#创建事件对象
e = threading.Event()

def bar():
    print("呼叫foo")
    global msg 
    msg = "天王盖地虎"

def foo():
    print("等待口令")
    sleep(2)
    if msg == "天王盖地虎":
        print("宝塔镇河妖,自己人,哈哈哈")
    else:
        print("口令错误,打死他")
    e.set()

def fun(): 
    print("呵呵....内奸出现")
    sleep(1)
    e.wait()
    global msg
    msg = "小鸡炖蘑菇" 

t1 = threading.Thread(target = bar)
t2 = threading.Thread(target = foo)
t3 = threading.Thread(target = fun)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()