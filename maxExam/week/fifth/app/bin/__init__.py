# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: __init__.py
# @datatime: 2023/5/6 下午1:03

# import asyncio
#
# async def get_url():
#     reader,writer = await asyncio.open_connection('www.baidu.com',80)
#     writer.write(b'GET / HTTP/1.1\r\nHOST:www.baidu.com\r\nConnection:close\r\n\r\n')
#     all_lines = []
#     async for line in reader:
#         data = line.decode()
#         all_lines.append(data)
#     html = '\n'.join(all_lines)
#     return html
#
# async def main():
#     tasks = []
#     for url in range(20):
#         tasks.append(asyncio.ensure_future(get_url()))
#     for res in asyncio.as_completed(tasks):
#         result = await res
#         print(result)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())  # 处理一个任务
#     loop.run_until_complete(asyncio.wait([main()]))  # 处理多个任务
#
#     task = loop.create_task(main())  # 使用create_task获取返回值
#     loop.run_until_complete(task)
#     loop.run_until_complete(asyncio.wait([task]))


num = 100
print(divmod(num, 15))

a, b = divmod(num, 15)
c = a + 1

print(a, b, c)
l = []
