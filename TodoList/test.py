import sys
import os
import time

def priority_selection():
    try:
        priority = int(input('Приоритет задачи от 1 до ..: '))
        if type(priority) == int:
            return priority
    except ValueError:
        print('Введите число')
        for i in range(1,4):
            print(i)
            time.sleep(1)
        priority_selection()


test = []
for task in sys.stdin:
    task = task.strip()
    if len(task) > 1:
        test.append((task,priority_selection()))
    else:
        break
        
    #
        
print(test)