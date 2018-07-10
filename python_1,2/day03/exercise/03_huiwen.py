# 2. 输入任意一个字符串，判断这个字符串是否是回文
# 　　回文是指中心对称的文字
#   如:
#     上海自来水来自海上
#     ABCCBA

s = input("请输入字符串: ")

reverse_string = s[::-1]  # 把字符串反过来
print(reverse_string)

# 比较反过来的字符串和原字符串是否相同
if s == reverse_string:
    print(s, "是回文")
else:
    print(s, "不是回文")

