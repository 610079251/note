# 1. 写一个函数myfun, 此函数用显示两个参数的相关信息
#    函数:
#      def myfun(a, b):
#          此处自己实现
#   此函数给定两个参数，打印关于两个参数的信息:
#       1) 打印两个参数的最大值
#       2) 打印两个参数的和
#       3) 打印两个参数的积(相乘)
#       4) 打印从a开始到b结束的所有偶数:
#   如:
#     myfun(3, 10)
#   打印如下:
#     最大值是: 10
#     和是: 13
#     积是: 30
#     3到10之间的偶数是: 4 6 8 
#   myfun(10, 20)
#   打印...



def myfun(a, b):
    # 1) 打印两个参数的最大值
    print("最大值是:", max(a, b))
    # 2) 打印两个参数的和
    print("和是:", a + b)
    # 3) 打印两个参数的积(相乘)
    print("积是:", a * b)
    # 4) 打印从a开始到b结束的所有偶数:
    i = a
    while i < b:
        if i % 2 == 0:  # 是偶数 
            print(i)
        i += 1
    

myfun(3, 10)
#   打印如下:
#     最大值是: 10
#     和是: 13
#     积是: 30
#     3到10之间的偶数是: 4 6 8 
#   myfun(10, 20)
#   打印...