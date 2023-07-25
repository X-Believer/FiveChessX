from System import*
from Global import*
import sys
from FiveChessX import*
import pygame as pg

pg.init()
pg.display.init()
going=True#控制游戏退出

#新建游戏窗口
Wid=960
Hei=540
screen=pg.display.set_mode((Wid,Hei))
pg.display.set_caption("游戏启动器")
playMusic(1)
clock=pg.time.Clock()#帧率控制
element=[]#游戏内元素列表

#导入System类并创建类对象
NowUser=System("X-Believer")

while True:

    choice=NowUser.showMenu(screen)

    #用户选择退出
    if choice==-1:
        pg.quit()
        sys.exit()

    #用户选择五子棋
    elif choice==1:
        player=FiveChess("X-Believer")
        player.runGame(screen)
