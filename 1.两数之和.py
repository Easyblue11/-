# Author: EasyBlue
# Time: 2022.3.20-20:50
# Topic: 快速查找List中两数的和为Target的两数的索引
import time
import random
InitList = [random.randint(0,30) for i in range(1000)]
InitList.insert(random.randint(0,999),23)
InitList.insert(random.randint(0,999),30)
List = InitList
Target = 53


# My Way

def MyFunc():
    global List,Target
    lenth = len(List)
    for i in range(lenth):
        for j in range(i,lenth):
            if List[i] + List[j] == Target:
                return [i,j]

# Other Way
def OtherFunc():
    global List,Target
    Dict = dict()
    for index,value in enumerate(List):
        Sub = Target - value
        if Sub in Dict:
            return [Dict[Sub],index]
        else:
            Dict[value] = index


TempTime = time.time()
Result = MyFunc()
print("My Way   :",time.time() - TempTime,"s",Result)

TempTime = time.time()
Result = OtherFunc()
print("Other Way:",time.time() - TempTime,"s",Result)