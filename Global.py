import pygame as pg

musicFlag=1#音乐控制
soundFlag=1#音效控制
isInit=False

#音乐播放
def playMusic(flag):
    global isInit
    global musicFlag
    global soundFlag
    if isInit==False:
        pg.mixer.init()
        pg.mixer.music.load("MainMenu/Theme.mp3")
        pg.mixer.music.play(-1)
        isInit=True
        return
    if flag==1:
        pg.mixer.music.unpause()
    else:
        pg.mixer.music.pause()
