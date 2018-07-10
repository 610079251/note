# 1. 输入一个字符串，打印如下内容
#   1) 打印这个字符串的第一个字符
#   2) 打印这个字符串的最后一个字符
#   3) 如果这个字符串长度是奇数，打印中间这个字符
#   (注: 求字符串长度的函数是 len(s))

s = input("请输入字符串: ")

print("第一个字符是:", s[0])
print("最后一个字符是:", s[-1])
length = len(s)  # 用length 表示长度
if length % 2 == 1:
    center_index = length // 2
    print("中间的字符是:", s[center_index])



