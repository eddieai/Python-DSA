"""
约瑟夫问题  或 热土豆问题
参加游戏一群人，每次传递num次停下的人除去 继续传直到只剩一个人
"""

from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    queue = Queue()
    for name in namelist:
        queue.enqueue(name)

    time = 0
    while queue.size() > 1:
        holding_potato = queue.dequeue()
        queue.enqueue(holding_potato)
        time += 1
        if time % num == 0:
            queue.dequeue()

    return queue.dequeue()

print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
