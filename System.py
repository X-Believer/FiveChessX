import pygame as pg
from Global import*


class System(object):
    #构造方法
    def __init__(self,username:str):
        self.userName=username
        
    userName="Admin"#当前用户名
    music_flag=True#控制音乐播放
    button_flag=0#用户交互状态

    #用户交互
    def userDo(self)->int:
        pos=pg.mouse.get_pos()
        eventList=pg.event.get()
        for event in eventList:
            if event.type==32787:
                return -1
            #五子棋
            if pos[0]>540 and pos[0]<900 and pos[1]>70 and pos[1]<350:
                self.button_flag=1
                if event.type==pg.MOUSEBUTTONDOWN:
                    return 1
            
            else:
                self.button_flag=0
                return 0
        return 0
        

    #显示主菜单
    def showMenu(self,screen)->int:
        if self.music_flag:
            menu=pg.image.load("MainMenu/MainMenu.png").convert_alpha()
            glow=pg.image.load("MainMenu/FiveChess_glow.png").convert_alpha()
        
        while True:
            status=self.userDo()
            screen.blit(menu,(0,0))

            #用户退出系统
            if status==-1:
                return -1
            
            #五子棋
            if self.button_flag==1:
                screen.blit(glow,(563,69))
                if status==1:
                    return 1
                
            pg.display.update()    
        






