import pygame as pg
import copy 
import sys
from time import*
from Global import*
from random import*

class FiveChess(object):
    Turn=0#落子顺序
    Flag=0#结束标志
    isAi=0#是否人机
    xAi=0#Ai最后落子位置
    yAi=0
    xNow=0#用户最后落子位置
    yNow=0
    lButton=0#左侧按钮控制量
    rButton=0#右侧按钮控制量
    sButton=0#设置菜单按钮
    board=[[] for _ in range(18)]#棋盘数据
    Map=[[] for _ in range(18)]#棋盘权值
    tempPos=[0,0]
    Timer:int=0#倒计时
    lastTime=0
    limTime=30
    sec=0
    isLoad=False
    isLoad1=False

    #构造方法
    def __init__(self,username:str):
        self.userName=username
        pg.mixer.init()

    #设置菜单用户交互
    def settingUserDo(self):
        eventList1=pg.event.get()
        for event in eventList1:
            if event.type==32787:
                 pg.quit()
                 sys.exit()
            pos=pg.mouse.get_pos()

            #背景音乐
            if pos[0]>0 and pos[0]<385 and pos[1]>97 and pos[1]<262:
                self.sButton=1
                if event.type==pg.MOUSEBUTTONDOWN:
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/ChessDown.mp3')
                        pg.mixer.Sound.play(chessSound)
                    return 1 
                return 0
            
            #游戏音效
            elif pos[0]>0 and pos[0]<385 and pos[1]>302 and pos[1]<467:
                self.sButton=2
                if event.type==pg.MOUSEBUTTONDOWN:
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/ChessDown.mp3')
                        pg.mixer.Sound.play(chessSound)
                    return 1 
                return 0
            
            #调短时限
            elif pos[0]>580 and pos[0]<615 and pos[1]>380 and pos[1]<425:
                self.sButton=3
                if event.type==pg.MOUSEBUTTONDOWN:
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/ChessDown.mp3')
                        pg.mixer.Sound.play(chessSound)
                    return 1 
                return 0
            
            #调长时限
            elif pos[0]>720 and pos[0]<755 and pos[1]>380 and pos[1]<425:
                self.sButton=4
                if event.type==pg.MOUSEBUTTONDOWN:
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/ChessDown.mp3')
                        pg.mixer.Sound.play(chessSound)
                    return 1 
                return 0
            
            #返回
            elif pos[0]>15 and pos[0]<90 and pos[1]>25 and pos[1]<85:
                self.sButton=5
                if event.type==pg.MOUSEBUTTONDOWN:
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/ChessDown.mp3')
                        pg.mixer.Sound.play(chessSound)
                    return 1 
                return 0
            
            #主菜单
            elif pos[0]>790 and pos[0]<960 and pos[1]>490 and pos[1]<540:
                self.sButton=6
                if event.type==pg.MOUSEBUTTONDOWN:
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/ChessDown.mp3')
                        pg.mixer.Sound.play(chessSound)
                    return 1 
                return 0
            
            #无操作
            else:
                self.sButton=0
                return 0

    #设置菜单
    def settingMenu(self,screen)->int:
        global musicFlag
        global soundFlag
        if self.isLoad1==False:
            setitngBg=pg.image.load("FiveChess/FiveChessSetting.png").convert_alpha()
            goMainMenu=pg.image.load("FiveChess/MainMenu.png").convert_alpha()
            BGM=pg.image.load("FiveChess/BGM.png").convert_alpha()
            BGM1=pg.image.load("FiveChess/BGM1.png").convert_alpha()
            gameSound=pg.image.load("FiveChess/Sound.png").convert_alpha()
            gameSound1=pg.image.load("FiveChess/Sound1.png").convert_alpha()
            blueS=pg.image.load("FiveChess/Blue.png").convert_alpha()
            redS=pg.image.load("FiveChess/Red.png").convert_alpha()
            buttonOn=pg.image.load("FiveChess/ButtonOn.png").convert_alpha()
            buttonOff=pg.image.load("FiveChess/ButtonOff.png").convert_alpha()
            chessTime=[pg.image.load("FiveChess/Time0.png").convert_alpha(),pg.image.load("FiveChess/Time1.png").convert_alpha(),pg.image.load("FiveChess/Time2.png").convert_alpha(),pg.image.load("FiveChess/Time3.png").convert_alpha()]
            Left1=pg.image.load("FiveChess/Left1.png").convert_alpha()
            Right1=pg.image.load("FiveChess/Right1.png").convert_alpha()
            goback=pg.image.load("FiveChess/GoBack_glow.png").convert_alpha()

        while True:
            status1=self.settingUserDo()
            screen.blit(setitngBg,(0,0))
            screen.blit(goMainMenu,(791,491))
            screen.blit(chessTime[int(self.limTime/15)-1],(645,391))
            
            #游戏音乐
            if self.sButton==1:
                if musicFlag==1:
                    screen.blit(blueS,(0,97))
                else:
                    screen.blit(redS,(0,97))
                if status1==1:
                    if musicFlag==1:
                        musicFlag=0
                        playMusic(0)
                    else:
                        musicFlag=1
                        playMusic(1)
                    
            #游戏音效
            elif self.sButton==2:
                if soundFlag==1:
                    screen.blit(blueS,(0,302))
                else:
                    screen.blit(redS,(0,302))
                if status1==1:
                    if soundFlag==1:
                        soundFlag=0
                    else:
                        soundFlag=1

            #调短时限
            elif self.sButton==3:
                screen.blit(Left1,(583,382))
                if status1==1:
                    if self.limTime>15:
                        self.limTime-=15

            #调长时限
            elif self.sButton==4:
                screen.blit(Right1,(723,382))
                if status1==1:
                    if self.limTime<60:
                        self.limTime+=15

            #返回游戏
            elif self.sButton==5:
                screen.blit(goback,(19,26))
                if status1==1:
                    return 1
                
            #返回主菜单
            elif self.sButton==6:
                if status1==1:
                    return -1

            if musicFlag==1:
                screen.blit(BGM,(28,161))
                screen.blit(buttonOn,(311,161))
            else:
                screen.blit(BGM1,(28,161))
                screen.blit(buttonOff,(311,161))

            if soundFlag==1:
                screen.blit(gameSound,(28,363))
                screen.blit(buttonOn,(311,363))
            else:
                screen.blit(gameSound1,(28,363))
                screen.blit(buttonOff,(311,363))

            pg.display.update()  
    
    #落子实现
    def drawChess(self,m:int,n:int):
        x=int(abs(m-70)/30+1)
        y=int(abs(n-10)/30+1)
        if self.board[x][y]!=0:
            return 
        
        list = copy.deepcopy(self.board[x])
        list[y] = self.Turn + 1
        self.board[x] = copy.deepcopy(list)

        self.xNow=x
        self.yNow=y

        if self.Turn==0:
            self.Turn=1
        elif self.Turn==1 and self.isAi==0:
            self.Turn=0
        self.sec=0
        self.Timer=0

    #用户交互
    def chessUserdo(self):
        eventList1=pg.event.get()
        for event in eventList1:
            if event.type==32787:
                 pg.quit()
                 sys.exit()
            pos=pg.mouse.get_pos()

            #落子判断
            if self.Flag!=1 and pos[0]>40 and pos[0]<570 and pos[1]>1 and pos[1]<530 and event.type==pg.MOUSEBUTTONDOWN:
                if self.isAi==0 or (self.isAi==1 and self.Turn==0):
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/ChessDown.mp3')
                        pg.mixer.Sound.play(chessSound)
                    self.drawChess(pos[0],pos[1])
                return 0
            
            #悔棋
            elif pos[0]>696 and pos[0]<920 and pos[1]>130 and pos[1]<190:
                self.rButton=1
                if self.Flag!=1 and event.type==pg.MOUSEBUTTONDOWN:
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/ChessDown.mp3')
                        pg.mixer.Sound.play(chessSound)
                    return 1
                return 0
            
            #清空棋盘
            elif pos[0]>696 and pos[0]<920 and pos[1]>205 and pos[1]<265:
                self.rButton=2
                if event.type==pg.MOUSEBUTTONDOWN:
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/ChessDown.mp3')
                        pg.mixer.Sound.play(chessSound)
                    return 1
                return 0
            
            #AI对战
            elif pos[0]>696 and pos[0]<920 and pos[1]>280 and pos[1]<345:
                self.rButton=3
                if event.type==pg.MOUSEBUTTONDOWN:
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/ChessDown.mp3')
                        pg.mixer.Sound.play(chessSound)
                    return 1
                return 0
            
            #游戏设置
            elif pos[0]>696 and pos[0]<920 and pos[1]>360 and pos[1]<425:
                self.rButton=4
                if event.type==pg.MOUSEBUTTONDOWN:
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/ChessDown.mp3')
                        pg.mixer.Sound.play(chessSound)
                    return 1
                return 0
            
            #返回主菜单
            elif pos[0]>696 and pos[0]<920 and pos[1]>440 and pos[1]<505:
                self.rButton=5
                if event.type==pg.MOUSEBUTTONDOWN:
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/ChessDown.mp3')
                        pg.mixer.Sound.play(chessSound)
                    return 1
                return 0
            
            #无操作
            else:
                self.rButton=0
                return 0
            
    #判断输赢
    def checkWin(self,x:int,y:int):
        cnt=0
        
        if self.board[x][y]==0:
            return False
        
        #纵向判断
        if x>=6:
            start=x-5
        else:
            start=1
        for i in range(start,min(x+5,16)+1):
            if self.board[i][y]==self.board[x][y]:
                cnt+=1
            else:
                cnt=0
            if  cnt==5 and self.Turn==1:
                if i<min(x+5,16) and self.board[i+1][y]==self.board[x][y]:
                    self.Turn=0
                    return True
            if cnt>=5:
                return True
            
        #横向判断
        cnt=0
        if y>=6:
            start=y-5
        else:
            start=1
        for i in range(start,min(y+5,16)+1):
            if self.board[x][i]==self.board[x][y]:
                cnt+=1
            else:
                cnt=0
            if  cnt==5 and self.Turn==1:
                if i<min(y+5,16) and self.board[x][i+1]==self.board[x][y]:
                    self.Turn=0
                    return True
            if cnt>=5:
                return True
            
        #右下判断
        cnt=0
        start=0
        start1=0
        if x>=6 and y>=6:
            start=x-5
            start1=y-5
        else:
            if x>y:
                start=x-y+1
                start1=1
            else:
                start=1
                start1=y-x+1
        
        for i in range(start,min(x+5,16)+1):
            if start1>16 or start1>y+5:
                break
            if self.board[i][start1]==self.board[x][y]:
                cnt+=1
            else:
                cnt=0
            if  cnt==5 and self.Turn==1:
                if i<min(x+5,16) and start1<min(y+5,16) and self.board[i+1][start1+1]==self.board[x][y]:
                    self.Turn=0
                    return True
            if cnt>=5:
                return True
            start1+=1

        #左下判断
        cnt=0
        start=0
        start1=0
        if x>=6 and y<=12:
            start=x-5
            start1=y+5
        else:
            if x>16-y:
                start=x-(16-y)
                start1=16
            else:
                start=1
                start1=y+x-1
        
        for i in range(start,min(x+5,16)+1):
            if start1<1 or start1<y-5:
                break
            if self.board[i][start1]==self.board[x][y]:
                cnt+=1
            else:
                cnt=0
            if  cnt==5 and self.Turn==1:
                if i<min(x+5,16) and start1>max(y-5,1) and self.board[i+1][start1-1]==self.board[x][y]:
                    self.Turn=0
                    return True
            if cnt>=5:
                return True
            start1-=1
        return False

    #Ai走棋
    def aiDrawChess(self):
        self.calWorth()
        posArr=[]
        maxWorth:int=0
        arrlen=0
        for i in range(1,18):
            for j in range(1,18):
                if self.board[i][j]==0:
                    if self.Map[i][j]>maxWorth:
                        maxWorth=self.Map[i][j]
                        arrlen=0
                        posArr=[]
                        posArr.append([i,j])
                        arrlen+=1
                    elif self.Map[i][j]==maxWorth:
                        posArr.append([i,j])
                        arrlen+=1
        index=randint(0,len(posArr)-1>0)
        temp = copy.deepcopy(self.board[posArr[index][0]])
        temp[posArr[index][1]] = 2
        self.board[posArr[index][0]] = copy.deepcopy(temp)
        # list = copy.deepcopy(self.board[posArr[index][0]])
        # list[posArr[index][1]] = 2
        # self.board[posArr[index][0]] = copy.deepcopy(list)
        self.xAi=posArr[index][0]
        self.yAi=posArr[index][1]
        self.sec=0

    #计算权值
    def calWorth(self):
        blaNum=0#黑方连子
        whiNum=0#白方连子
        empNum=0#空白数

        for i in range(18):
            for j in range(18):
                self.Map[i].append(0)

        #对棋盘的每一个点计算权值
        for row in range(1,18):
            for col in range(1,18):
                if self.board[row][col]!=0:
                    continue
            
                for y in range(-1,1):
                    for x in range(-1,2):
                        if (y==0 and x==0) or (y==0 and x!=1):
                            continue
                        blaNum=0
                        whiNum=0
                        empNum=0

                        #正向计算
                        for i in range(1,5):
                            curRow=row+i*y
                            curCol=col+i*x

                            if curRow>=1 and curRow<18 and curCol>=1 and curCol<18 and self.board[curRow][curCol]==1:
                                blaNum+=1
                            elif curRow>=1 and curRow<18 and curCol>=1 and curCol<18 and self.board[curRow][curCol]==0:
                                empNum+=1
                                break
                            elif curRow>=1 and curRow<18 and curCol>=1 and curCol<18 and self.board[curRow][curCol]==2:
                                break

                        #反向计算                    
                        for i in range(1,5):
                            curRow=row-i*y
                            curCol=col-i*x

                            if curRow>=1 and curRow<18 and curCol>=1 and curCol<18 and self.board[curRow][curCol]==1:
                                blaNum+=1
                            elif curRow>=1 and curRow<18 and curCol>=1 and curCol<18 and self.board[curRow][curCol]==0:
                                empNum+=1
                                break
                            elif curRow>=1 and curRow<18 and curCol>=1 and curCol<18 and self.board[curRow][curCol]==2:
                                break
                        
                        #连二
                        if blaNum==1:
                            self.Map[row][col]+=10

                        #连三
                        elif blaNum==2:
                            if empNum==1:
                                self.Map[row][col]+=30
                            elif empNum==2:
                                self.Map[row][col]+=40

                        #连四
                        elif blaNum==3:
                            if empNum==1:
                                self.Map[row][col]+=60
                            elif empNum==2:
                                self.Map[row][col]+=200

                        #连五
                        elif blaNum>=4:
                            self.Map[row][col]+=20000

                        empNum=0

                        #正向计算(白棋)
                        for i in range(1,5):
                            curRow=row+i*y
                            curCol=col+i*x

                            if curRow>=1 and curRow<18 and curCol>=1 and curCol<18 and self.board[curRow][curCol]==2:
                                whiNum+=1
                            elif curRow>=1 and curRow<18 and curCol>=1 and curCol<18 and self.board[curRow][curCol]==0:
                                empNum+=1
                                break
                            elif curRow>=1 and curRow<18 and curCol>=1 and curCol<18 and self.board[curRow][curCol]==1:
                                break

                        #反向计算                    
                        for i in range(1,5):
                            curRow=row-i*y
                            curCol=col-i*x

                            if curRow>=1 and curRow<18 and curCol>=1 and curCol<18 and self.board[curRow][curCol]==2:
                                whiNum+=1
                            elif curRow>=1 and curRow<18 and curCol>=1 and curCol<18 and self.board[curRow][curCol]==0:
                                empNum+=1
                                break
                            elif curRow>=1 and curRow<18 and curCol>=1 and curCol<18 and self.board[curRow][curCol]==1:
                                break
                        
                        #单子
                        if whiNum==0:
                            self.Map[row][col]+=5

                        #连二
                        if whiNum==1:
                            self.Map[row][col]+=10

                        #连三
                        elif whiNum==2:
                            if empNum==1:
                                self.Map[row][col]+=25
                            elif empNum==2:
                                self.Map[row][col]+=50

                        #连四
                        elif whiNum==3:
                            if empNum==1:
                                self.Map[row][col]+=55
                            elif empNum==2:
                                self.Map[row][col]+=10000

                        #连五
                        elif whiNum>=4:
                            self.Map[row][col]+=30000

    #计算帧时差
    def getDelay(self)->int:
        curTime=pg.time.get_ticks()
        if self.lastTime==0:
            self.lastTime=curTime
            return 0
        else:
            ret:int=curTime-self.lastTime
            self.lastTime=curTime
            return ret

    #运行游戏
    def runGame(self,screen):
        global musicFlag
        global soundFlag
        myFont=pg.font.Font(None,50)
        white=255,255,255
        self.board=[[0]*18]*18
        for i in range(18):
            self.Map[i].clear()
        for i in range(18):
            for j in range(18):
                self.Map[i].append(0)
        self.Turn=0
        self.Flag=0
        self.xAi=0
        self.xNow=0
        self.yAi=0
        self.yNow=0
        self.Timer=0
        self.sec=0
        if self.isLoad==False:
            bg=pg.image.load("FiveChess/FiveChessMenu.png").convert_alpha()
            clearBoard=pg.image.load("FiveChess/ClearBoard.png").convert_alpha()
            clearBoard1=pg.image.load("FiveChess/ClearBoard_glow.png").convert_alpha()
            retract=pg.image.load("FiveChess/Retract.png").convert_alpha()
            retract1=pg.image.load("FiveChess/Retract_glow.png").convert_alpha()
            setting=pg.image.load("FiveChess/GameSettings.png").convert_alpha()
            setting1=pg.image.load("FiveChess/GameSettings_glow.png").convert_alpha()
            blaC=pg.image.load("FiveChess/Black.png").convert_alpha()
            whiC=pg.image.load("FiveChess/White.png").convert_alpha()
            mainMenu=pg.image.load("FiveChess/GoMainMenu.png").convert_alpha()
            mainMenu1=pg.image.load("FiveChess/GoMainMenu_glow.png").convert_alpha()
            whiWin=pg.image.load("FiveChess/WhiteWin.png").convert_alpha()
            blaWin=pg.image.load("FiveChess/BlackWin.png").convert_alpha()
            pointC=pg.image.load("FiveChess/Point.png").convert_alpha()
            chessBoard=pg.image.load("FiveChess/BoardBlue.png").convert_alpha()
            timePic=pg.image.load("FiveChess/Timer.png").convert_alpha()

        if self.isAi==0:
            Ai=pg.image.load("FiveChess/AI.png").convert_alpha()
            Ai1=pg.image.load("FiveChess/AI_glow.png").convert_alpha()
        else:
            Ai=pg.image.load("FiveChess/VSPlayer.png").convert_alpha()
            Ai1=pg.image.load("FiveChess/VSPlayer_glow.png").convert_alpha()

        while True:
            self.Timer+=self.getDelay()
            if int(self.Timer/1000)!=0:
                self.sec+=1
                self.Timer=0
            if self.Flag!=1:
                showTime=self.limTime-self.sec
            if showTime<0:
                self.Flag=1
                showTime=0
            textImage=myFont.render(("%2d"%showTime),True,white)
            #赢棋后不再判断
            if self.Flag==0:
                if self.checkWin(self.xNow,self.yNow):
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/Win.mp3')
                        pg.mixer.Sound.play(chessSound)
                    self.Flag=1

                if self.isAi==1 and self.checkWin(self.xAi,self.yAi):
                    if soundFlag==1:
                        chessSound = pg.mixer.Sound('FiveChess/Win.mp3')
                        pg.mixer.Sound.play(chessSound)
                    self.Flag=1

            status=self.chessUserdo()

            #Ai落子
            if self.isAi==1 and self.Turn==1 and self.checkWin(self.xNow,self.yNow)==False:
                for i in range(1,18):
                    for j in range(1,18):
                        if self.board[i][j]==1:
                            screen.blit(blaC,(70+(i-1)*30,10+(j-1)*30))
                        elif self.board[i][j]==2:
                            screen.blit(whiC,(70+(i-1)*30,10+(j-1)*30))
                        #sleep(200)
                self.aiDrawChess()
                self.Turn=0

            screen.blit(bg,(0,0))
            screen.blit(chessBoard,(44,1))
            screen.blit(retract,(696,127))
            screen.blit(clearBoard,(696,205))
            screen.blit(Ai,(696,283))
            screen.blit(setting,(696,361))
            screen.blit(mainMenu,(696,439))
            screen.blit(timePic,(612,54))
            screen.blit(textImage,(621,264))

            #悔棋
            if self.rButton==1:
                screen.blit(retract1,(696,127))
                if status==1 and self.board[self.xNow][self.yNow]!=0:
                    if self.isAi==0:
                        self.board[self.xNow][self.yNow]=0
                        if self.Turn==1:
                            self.Turn=0
                        else:
                            self.Turn=1
                        self.xNow=0
                        self.yNow=0
                        self.xAi=0
                        self.yAi=0
                    elif self.isAi==1 and not(self.xNow==self.xAi and self.yNow==self.yAi):
                        self.board[self.xNow][self.yNow]=0
                        self.board[self.xAi][self.yAi]=0
                        self.Turn=0
                        self.xNow=0
                        self.yNow=0
                        self.xAi=0
                        self.yAi=0
                    self.Timer=0
                    self.sec=0

            #清空棋盘
            elif self.rButton==2:
                screen.blit(clearBoard1,(696,205))
                if status==1:
                    self.board=[[0]*18]*18
                    #self.Map=[[0]*18]*18
                    for i in range(18):
                        self.Map[i].clear()
                    for i in range(18):
                        for j in range(18):
                            self.Map[i].append(0)
                    self.Flag=0
                    self.Turn=0
                    self.xNow=0
                    self.xAi=0
                    self.yAi=0
                    self.yNow=0
                    self.sec=0
                    self.Timer=0

            #Ai对战
            elif self.rButton==3:
                screen.blit(Ai1,(696,283))
                if status==1:
                    if self.isAi==0:
                        self.isAi=1
                    else:
                        self.isAi=0
                        pg.display.update()
                    self.runGame(screen)
                    return

            #游戏设置
            elif self.rButton==4:
                screen.blit(setting1,(696,361))
                if status==1:
                    settingChoice=self.settingMenu(screen)
                    if settingChoice==-1:
                        self.board=[[0]*18]*18
                        for i in range(18):
                            for j in range(18):
                                self.Map[i].append(0)
                        self.Flag=0
                        self.Turn=0
                        self.xNow=0
                        self.xAi=0
                        self.yAi=0
                        self.yNow=0
                        self.isAi=0
                        return
                
            #返回主菜单
            elif self.rButton==5:
                screen.blit(mainMenu1,(696,439))
                if status==1:
                    self.board=[[0]*18]*18
                    #self.Map=[[0]*18]*18
                    for i in range(18):
                        for j in range(18):
                            self.Map[i].append(0)
                    self.Flag=0
                    self.Turn=0
                    self.xNow=0
                    self.xAi=0
                    self.yAi=0
                    self.yNow=0
                    self.isAi=0
                    return
                            
            #打印棋子
            for i in range(1,18):
                for j in range(1,18):
                    if self.board[i][j]==1:
                        screen.blit(blaC,(70+(i-1)*30,10+(j-1)*30))
                    elif self.board[i][j]==2:
                        screen.blit(whiC,(70+(i-1)*30,10+(j-1)*30))

            #打印提示点
            if self.board[self.xNow]!=0 and self.board[self.yNow]!=0:
                if self.isAi==0:
                    screen.blit(pointC,(50+self.xNow*30,self.yNow*30-11))
                if self.isAi==1:
                    screen.blit(pointC,(50+self.xAi*30,self.yAi*30-11))

            #胜负输出
            if self.Flag==1:
                if self.Turn==1:
                    screen.blit(blaWin,(100,300))
                else:
                    screen.blit(whiWin,(100,300))

            pg.display.update()