"""
1. 有如下文件，a1.txt，里面的内容为：

老男孩是最好的学校，
全心全意为学生服务，
只为学生未来，不为牟利。
我说的都是真的。哈哈

分别完成以下的功能：
a.将原文件全部读出来并打印。
b,在原文件后面追加一行内容：信不信由你，反正我信了。
c,将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。
d,将原文件全部清空，换成下面的内容：

每天坚持一点，
每天努力一点，
每天多思考一点，
慢慢你会发现，
你的进步越来越大。
"""

# a.将原文件全部读出来并打印。
# with open("a1.txt", encoding="utf-8") as f:
#     for i in f:
#         print(i.strip())


# b,在原文件后面追加一行内容：信不信由你，反正我信了。
# with open("a1.txt", mode="a", encoding="utf-8") as f:
#     f.write("\n")
#     f.write("信不信由你，反正我信了。")

# c,将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。
# with open("a1.txt", mode="r", encoding="utf-8") as f1, open("a1.txt", mode="a", encoding="utf-8") as f2:
#     for i in f1:
#         print(i.strip())
#     f2.write("\n信不信由你，反正我信了。")

# d,将原文件全部清空，换成下面的内容：

str = """
每天坚持一点，
每天努力一点，
每天多思考一点，
慢慢你会发现，
你的进步越来越大。
"""
for i in str:
    print(i, end="")
with open("a1.txt", mode="w", encoding="utf-8") as f:
    for i in str:
        f.write(i)