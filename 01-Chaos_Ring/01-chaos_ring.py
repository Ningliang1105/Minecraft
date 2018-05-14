#import library引入库
import ministack

i = 20

#create a chaos ring that goes to player position every second
#每秒创建一个不断缩小的混乱圆环
while i > 0:
    #update player position更新位置
    pos = ministack.getPlayerPosition("Ningliang")
    #random block type随机砖块种类
    block = ministack.randomNumber()
    ministack.drawCircle(pos.x, pos.y, pos.z, i, block)
    i = i - 1
    ministack.wait(1)

'''
低难度版本：
选定一个材料，建造一系列从小到大的圆环
import ministack

pos = ministack.getPlayerPosition("Ningliang")
while i < 20:
    ministack.drawCircle(pos.x, pos.y, pos.z, i, 46)
    i = i + 1
    ministack.wait(1)
'''
