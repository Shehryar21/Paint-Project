#basicPaint.py
from random import *
from pygame import *
from tkinter import *
from math import *
#mixer.init()
root=Tk()
root.withdraw() #hiding the extra window
####Defining Colours
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
size=(1800,1000)
####
screen = display.set_mode(size)

####Defining tools
tool="no tool"
xtool="no tool"
mtool="no tool"
bgtool="no tool"
et=0
col=BLACK
rad=10 #thickness for eraser
omx,omy=300,300 #old mx, my. Becomes mx, my at the end
pos=0 #counter for the background list. increases/decreases when toggled right or left to see different backgrounds

#song loading
mixer.pre_init(44100,-16,1,512)
init()
mixer.init()
mixer.music.load("music/music.mp3")#loads the song
#mixer.music.play(-1)


thickness=4 #rectangle
thickness2=1#pencil
thickness3=4#line
thickness4=10#spray
thickness5=4#ellipse
thickness6=10#marker
thickness7=4#polygon
thickness8=25#background eraser thickness
showthickness= "N/A" #thickness which is shown on screen. Each of the above thickness becomes show thickness when the tool of that thickness is selected

####counters that are used for different purposes
n=0 #changes and has a diffent value when mx, my collides with a rect. Used so that a new rect can be made around the tool when we select or hover over that tool
m=0 #used for color picker tool
k=0 
g=0
s=0 #for polygon
f=4 #list counter for backgrounds drop down menu
d=0 #counter for the background list
mm=0 #for music
ss=0
bt=2 #brush transparency
gxlist=[] #lists for polygon tool to have store the points when clicked
gylist=[]
undo=[]#lists to hold the screens for undo/redo
redo=[]

#for showing the title SPACEPAINT on screen. It is blitted at the end of the program
font.init()
arialFont=font.SysFont("Comic Sans MS",150)
myText=arialFont.render("SpacePaint",True,WHITE)
                #width height
infoBar=Surface((1000,200),SRCALPHA)


#For showing stamp title. blitted at the end of the program on screen
stampFont=font.SysFont("Comic Sans MS",40)
stampText=stampFont.render("Stamps",True,BLACK)
stampBar=Surface((500,100),SRCALPHA)
stampBar.blit(stampText,(200,0))#writing SHEHRYAR on the infoBAr surface
#for showing background title
bgFont=font.SysFont("Comic Sans MS",40)
bgText=bgFont.render("Backgrounds",True,BLACK)
bgBar=Surface((500,100),SRCALPHA)
bgBar.blit(bgText,(40,0))





######load ALL pictures
backpic=image.load("images/space.jpg")
pencilpic=image.load("images/pencil.gif")
eraserpic=image.load("images/eraser.png")
colourpic=image.load("images/color.png")
markerpic=image.load("images/brush.jpg")
clearpic=image.load("images/clear.png")
savepic=image.load("images/save.png")
openpic=image.load("images/open.png")
linepic=image.load("images/line.png")
rectpic=image.load("images/rect.png")
spraypic=image.load("images/spray.jpg")
frectpic=image.load("images/frectangle.png")
ellipsepic=image.load("images/ellipse.png")
polygonpic=image.load("images/polygon.png")
undopic=image.load("images/undo.jpg")
redopic=image.load("images/redo.png")
leftpic=image.load("images/left.png")
rightpic=image.load("images/right.png")
bgleftpic=image.load("images/left.png")
bgrightpic=image.load("images/right.png")
jupiterpic=image.load("images/jupiter.png")
myjupiter=image.load("stamps/jupiter.png")
marspic=image.load("stamps/mars.png")
saturnpic=image.load("stamps/saturn.png")
venuspic=image.load("stamps/venus.gif")
playpic=image.load("images/play.png")
pausepic=image.load("images/pause.png")
neptunepic=image.load("images/neptune.png")
uranuspic=image.load("images/uranus.png")
earthpic=image.load("images/earth.png")
planetpic=image.load("images/planet.png")
mercurypic=image.load("images/mercury.png")
sunpic=image.load("images/sun.png")
pickerpic=image.load("images/colorpicker.png")
alphabrushpic=image.load("images/fill.png")
spacebg1=image.load("images/spacebg.png")
spacebg2=image.load("images/spacebg2.jpg")
spacebg3=image.load("images/spacebg3.jpg")
spacebg4=image.load("images/spacebg4.jpg")
spacebg5=image.load("images/spacebg5.jpg")
spacebg6=image.load("images/spacebg6.jpg")
spacebg7=image.load("images/spacebg7.jpg")

############# RESIZING STAMPS AND PICTURES AND BACKGROUNDS ##############

jupiterSmall=transform.scale(jupiterpic,(150,150))#resizing the picture
jupiterstampSmall=transform.scale(myjupiter,(300,300))#resizing the picture
marsSmall=transform.scale(marspic,(150,150))#resizing the picture
marsstampSmall=transform.scale(marspic,(300,300))#resizing the picture
saturnSmall=transform.scale(saturnpic,(150,150))#resizing the picture
saturnstampSmall=transform.scale(saturnpic,(300,300))#resizing the picture
venusSmall=transform.scale(venuspic,(150,150))#resizing the picture
venusstampSmall=transform.scale(venuspic,(300,300))#resizing the picture
neptunepic=transform.scale(neptunepic,(150,150))#resizing the picture
neptunestamp=transform.scale(neptunepic,(300,300))#resizing the picture
uranuspic=transform.scale(uranuspic,(150,150))#resizing the picture
uranusstamp=transform.scale(uranuspic,(300,300))#resizing the picture
earthpic=transform.scale(earthpic,(135,135))#resizing the picture
earthstamp=transform.scale(earthpic,(300,300))#resizing the picture
planetpic=transform.scale(planetpic,(130,130))#resizing the picture
planetstamp=transform.scale(planetpic,(300,300))#resizing the picture
mercurypic=transform.scale(mercurypic,(150,150))#resizing the picture
mercurystamp=transform.scale(mercurypic,(300,300))#resizing the picture
sunpic=transform.scale(sunpic,(150,150))#resizing the picture
sunstamp=transform.scale(sunpic,(300,300))#resizing the picture
pickerpic=transform.scale(pickerpic,(120,120))#resizing the picture
spacebgg1=transform.scale(spacebg1,(200,140))#resizing the picture
spacebgg2=transform.scale(spacebg2,(200,140))#resizing the picture
spacebgg3=transform.scale(spacebg3,(200,140))#resizing the picture
spacebgg4=transform.scale(spacebg4,(200,140))#resizing the picture
spacebgg5=transform.scale(spacebg5,(200,140))#resizing the picture
spacebgg6=transform.scale(spacebg6,(200,140))#resizing the picture
spacebgg7=transform.scale(spacebg7,(200,140))#resizing the picture
playpic=transform.scale(playpic,(60,60))#resizing the picture
pausepic=transform.scale(pausepic,(60,60))#resizing the picture

############## LISTS FOR THE STAMPS AND BACKGROUNDS ################
bggList=[spacebgg1,spacebgg2,spacebgg3,spacebgg4,spacebgg5,spacebgg6,spacebgg7] #for backgrounds same size as canvas
bgList=[spacebg1,spacebg2,spacebg3,spacebg4,spacebg5,spacebg6,spacebg7] #for smaller pic of backgrounds
stampsList=[jupiterSmall,marsSmall,saturnSmall,venusSmall,neptunepic,uranuspic,earthpic,planetpic,mercurypic,sunpic]


##############################defining all RECTS
canvasRect=Rect(300,200,1000,600)
borderRect=Rect(295,195,1008,610)
pencilRect=Rect(20,80,120,120)
eraserRect=Rect(160,80,120,120)
markerRect=Rect(20,220,120,120)
lineRect=Rect(160,220,120,120)
sprayRect=Rect(20,360,120,120)
rectangleRect=Rect(160,360,120,120)
frectangleRect=Rect(20,500,120,120)
ellipseRect=Rect(160,500,120,120)
fellipseRect=Rect(20,640,120,120)
flellipseRect=Rect(40,660,80,80)
polygonRect=Rect(160,640,120,120)
pickerRect=Rect(20,780,120,120)
alphabrushRect=Rect(160,780,120,120)
stampRect=Rect(320,820,200,80)
stampsRect=Rect(540,820,760,150)
stampspicRect=Rect(540,820,770,150)
leftRect=Rect(540,820,100,150)
rightRect=Rect(1200,820,100,150)
firstRect=Rect(650,820,150,150)
secondRect=Rect(830,820,150,150)
thirdRect=Rect(1010,820,150,150)
bgRect=Rect(1400,700,280,80)
bgsRect=Rect(1350,800,400,180)
bgleftRect=Rect(1353,820,100,180)
bgrightRect=Rect(1647,820,100,180)
bgiRect=Rect(1450,825,200,140)
bggsRect=Rect(1345,795,410,190)


showRect=Rect(1350,40,400,180)
frectRect=Rect(20,535,120,60)
rectRect=Rect(160,390,120,60)
wheelRect=Rect(770,80,183,184)
backRect=Rect(0,0,1800,1000)
colourRect=Rect(1350,300,400,300)
zoomRect=Rect(1350,615,60,60)
clearRect=Rect(1460,620,100,50)
undoRect=Rect(1600,620,50,50)
redoRect=Rect(1670,620,50,50)
saveRect=Rect(20,10,120,60)
openRect=Rect(160,10,120,60)

playRect=Rect(320,920,60,60)
pauseRect=Rect(400,920,60,60)


############################################


screen.blit(backpic,backRect)#blitting the background

sub = screen.subsurface(stampspicRect) #copying the area of stamps Rect when stamps tool is selected so that when some other tool is selected,
#the drop down menu of stamps closes, and the copied pic blits onto that stampsRect area
spic=sub.copy()

#same thing for background. Copying the background area when background is selected. This pic is blitted when some other tool is selected
subbg = screen.subsurface(bggsRect)
bgspic=subbg.copy()


draw.rect(screen,WHITE,canvasRect)#drawing the canvas BEFORE the loop

undo.append(screen.subsurface(canvasRect).copy()) #the blank canvas screen is added to the undo list


canvas=screen.subsurface(canvasRect) #creating a subsurface of the canvas

running=True
while running:
    
    
    click=False #changes to true when clicking
    #print(tool)
    for evt in event.get(): 
        if evt.type == QUIT: 
            running = False
        if evt.type==MOUSEBUTTONDOWN:
            click=True
            #print(567)
            sx,sy=mouse.get_pos() #capturing the point when mouse button is down
            fx,fy=mouse.get_pos() #same as above
            canvasPic=screen.copy()#screen capture (screenshot)
            screen.blit(canvasPic,(0,0)) #blitting canvas pic
        
        if evt.type==MOUSEBUTTONUP and n==10 and canvasRect.collidepoint(mx,my): #for the polygon tool. n equals to 10 when polygon tool is selected  
            gx,gy=mouse.get_pos() #point captured when mouse button releases or up
            if evt.button==1:
                gxlist.append(gx)#appending those point to the list. x coordinates in x list
                gylist.append(gy) #appending those point to the list. y coordinates in y list
                print(gxlist,gylist)
                print(len(gxlist))
            if len(gxlist)>=2: # has to be greater than 2 because we need to points from the user to draw the first line of polygon
                tool="polygon"
                screen.blit(canvasPic,(0,0))
                if s in range(len(gxlist)): #whenever user clicks, s increases by 1. it has to be in range with gxlist, because if becomes greater than length of gxlist, error would occur
                    if mb[0]==1: #when clicked
                        draw.line(screen,col,(gxlist[s],gylist[s]),(gxlist[s+1],gylist[s+1]),thickness7) #draw the line between the points. First. s is 0, but increases after every click
                        s+=1
                if mb[2]==1: #right click to enclose the polygon
                    draw.line(screen,col,(gxlist[len(gxlist)-1],gylist[len(gylist)-1]),(gxlist[0],gylist[0]),thickness7) #line between last point and the first point of the list
                    #draw.line(screen,col,(gxlist[len(gxlist)-1],gylist[len(gylist)-1]),(gxlist[1],gylist[1]),thickness7)
                    gxlist=[] #both list become emptied so that the user can make new polygon, and s also becomes s.
                    gylist=[]
                    s=0
        if evt.type == MOUSEBUTTONUP:
            
            if canvasRect.collidepoint(mx,my):
                undo.append(screen.subsurface(canvasRect).copy())# appending the screenshot of the canvasRect subsurface whenever mouse button is up and a change has occured on the canvas
                redo=[] #emptying the redo list
        
        if evt.type==KEYDOWN: #when key is pressed
                #print("scrolling up")
            ######### THICKNESSES FOR DIFFERENT TOOLS AND CHANGES WHEN THAT TOOL IS SELECTED. SHOWTHICKNESS BECOMES THE THICKNESS OF THE SELECTED TOOL ######
            if evt.key==K_UP: #hwhen up arrow key is pressed
                if thickness<60 and tool=="rectangle":
                    thickness+=1
                    showthickness=thickness #showthickness becomes the thickness of that tool because showthickness is whats going to be shown on screen to the user
                    
                if thickness2<3 and tool=="pencil":
                    thickness2+=1
                    showthickness=thickness2 
                    
                if thickness3<60 and tool=="line":
                    thickness3+=1
                    showthickness=thickness3
                    
                if thickness4<60 and tool=="spray":
                    thickness4+=1
                    showthickness=thickness4
                    
                if thickness5<60 and tool=="ellipse":
                    thickness5+=1
                    showthickness=thickness5
                    
                if thickness6<60 and tool=="marker":
                    thickness6+=1
                    showthickness=thickness6
                    
                if thickness7<5 and tool=="polygon":
                    thickness7+=1
                    showthickness=thickness7
                    
                if thickness8<70 and tool=="transparent brush":
                    thickness8+=1
                    showthickness=thickness8
                    
                if rad<70 and tool=="eraser":
                    rad+=1
                    showthickness=rad
                    
            if evt.key==K_RIGHT: #when right arrow key is pressed
                if bt<20 and tool=="transparent brush":
                    bt+=1 #transparency increases. max it can go is 20
                    print(bt)
            if evt.key==K_LEFT: #when left arrow key is pressed
                if bt>0 and tool=="transparent brush": 
                    bt-=1 #decreases bt which is the transparency of the brush
                    print(bt)

            ######### DECREASESES THICKNESS ########   
            if evt.key==K_DOWN: #when down arrow key is pressed
                if thickness>1 and tool=="rectangle":
                    thickness-=1
                    showthickness=thickness
                    
                if thickness2>1 and tool=="pencil":
                    thickness2-=1
                    showthickness=thickness2
                    
                if thickness3>1 and tool=="line":
                    thickness3-=1
                    showthickness=thickness3
                    
                if thickness4>1 and tool=="spray":
                    thickness4-=1
                    showthickness=thickness4
                    
                if thickness5>1 and tool=="ellipse":
                    thickness5-=1
                    showthickness=thickness5
                    
                if thickness6>1 and tool=="marker":
                    thickness6-=1
                    showthickness=thickness6
                if thickness7>1 and tool=="polygon":
                    thickness7-=1
                    showthickness=thickness7
                if thickness8>1 and tool=="transparent brush":
                    thickness8-=1
                    showthickness=thickness8
                if rad>1 and tool=="eraser":
                    rad-=1
                    showthickness=rad
                    
    mx,my=mouse.get_pos() #getting mouse position
    mb=mouse.get_pressed() ###mb --- mouse button###if mb[0]==1:
    #print(mx,my)

    ########drawing the tools
    draw.rect(screen,WHITE,pencilRect)
    draw.rect(screen,WHITE,eraserRect)
    draw.rect(screen,WHITE,markerRect)
    draw.rect(screen,WHITE,lineRect)
    draw.rect(screen,WHITE,sprayRect)
    draw.rect(screen,WHITE,rectangleRect)
    draw.rect(screen,BLACK,borderRect,5)
    draw.rect(screen,WHITE,clearRect)
    draw.rect(screen,WHITE,frectangleRect)
    draw.rect(screen,WHITE,ellipseRect)
    draw.rect(screen,WHITE,fellipseRect)
    draw.rect(screen,WHITE,polygonRect)
    draw.rect(screen,WHITE,showRect)
    draw.rect(screen,WHITE,pickerRect)
    draw.rect(screen,WHITE,alphabrushRect)
    draw.rect(screen,WHITE,stampRect)
    draw.rect(screen,WHITE,playRect)
    draw.rect(screen,WHITE,pauseRect)
    draw.rect(screen,WHITE,bgRect)
    
    #######BLITTING THE PICTURES OF THE TOOLS#########
    screen.blit(pencilpic,pencilRect)
    screen.blit(eraserpic,eraserRect)
    screen.blit(colourpic,colourRect)
    screen.blit(markerpic,markerRect)
    screen.blit(clearpic,clearRect)
    screen.blit(savepic,saveRect)
    screen.blit(openpic,openRect)
    screen.blit(linepic,lineRect)
    screen.blit(rectpic,rectRect)
    screen.blit(spraypic,sprayRect)
    screen.blit(frectpic,frectRect)
    screen.blit(ellipsepic,ellipseRect)
    screen.blit(polygonpic,polygonRect)
    screen.blit(undopic,undoRect)
    screen.blit(redopic,redoRect)
    screen.blit(playpic,playRect)
    screen.blit(pausepic,pauseRect)
    screen.blit(pickerpic,pickerRect)
    screen.blit(alphabrushpic,alphabrushRect)
    ###############################################

    ################ DRAWING BORDER FOR THE TOOLS##############
    draw.rect(screen,(0, 0, 153),pencilRect,5)
    draw.rect(screen,(0, 0, 153),eraserRect,5)
    draw.rect(screen,(0, 0, 153),markerRect,5)
    draw.rect(screen,(0, 0, 153),lineRect,5)
    draw.rect(screen,(0, 0, 153),sprayRect,5)
    draw.rect(screen,(0, 0, 153),rectangleRect,5)
    draw.rect(screen,(0, 0, 153),frectangleRect,5)
    draw.rect(screen,(0, 0, 153),ellipseRect,5)
    draw.rect(screen,(0, 0, 153),fellipseRect,5)
    draw.rect(screen,(0, 0, 153),polygonRect,5)
    draw.rect(screen,(0, 0, 153),pickerRect,5)
    draw.rect(screen,(0, 0, 153),alphabrushRect,5)
    draw.rect(screen,(0, 0, 153),stampRect,5)
    draw.rect(screen,(0, 0, 153),playRect,5)
    draw.rect(screen,(0, 0, 153),pauseRect,5)
    draw.rect(screen,(0, 0, 153),bgRect,5)
    draw.rect(screen,(0, 0, 153),(1460,619,102,52),6)#border for clear
    draw.rect(screen,(0, 0, 153),(22,10,116,58),6)#border for save
    draw.rect(screen,(0, 0, 153),(162,10,116,58),6)#border for open
    draw.rect(screen,(0, 0, 153),(1597,617,56,56),6)#border for undo
    draw.rect(screen,(0, 0, 153),(1667,617,56,56),6)#border for redo
    draw.rect(screen,(0, 0, 153),(1348,38,404,184),6)#border for showing tools selected
    ###########################################
    
    draw.ellipse(screen, BLACK,flellipseRect) #ELLIPSE DRAWN TO SHOW THE ELLIPSE TOOL. INSTEAD OF BLITTING A CIRCLE PIC TO SHOW THE USER, I JUST DREW AN ELLIPSE IN THAT AREA

    ############### DRAWING THE WHITE BORDER WHEN MOUSE IS HOVERED OVER THE SELECTED TOOL##############
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,pencilRect,4)
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,eraserRect,4)
    if markerRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,markerRect,4)
    if rectangleRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,rectangleRect,4)
    if frectangleRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,frectangleRect,4)
    if ellipseRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,ellipseRect,4)
    if fellipseRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,fellipseRect,4)
    if lineRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,lineRect,4)
    if sprayRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,sprayRect,4)
    if polygonRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,polygonRect,4)
    if pickerRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,pickerRect,4)
    if alphabrushRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,alphabrushRect,4)
    if stampRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,stampRect,4)
    if bgRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,bgRect,4)
    #############################################

        
    #####selecting the tools
    if mb[0]==1:#checking left click
        ####### CHANGING THE TOOL WHEN THE RECT OF THAT TOOL IS CLICKED##### n changes and is used to draw background when n equals to what rect the user pressed to 
        if pencilRect.collidepoint(mx,my):
            tool="pencil"
            n=1
        elif eraserRect.collidepoint(mx,my):
            tool="eraser"
            n=2
        elif markerRect.collidepoint(mx,my):
            tool="marker"
            n=3
        elif rectangleRect.collidepoint(mx,my):
            tool="rectangle"
            n=4
            f=4
        elif lineRect.collidepoint(mx,my):
            tool="line"
            n=5
        elif sprayRect.collidepoint(mx,my):
            tool="spray"
            n=6
        elif frectangleRect.collidepoint(mx,my):
            tool="frectangle"
            n=7
        elif ellipseRect.collidepoint(mx,my):
            tool="ellipse"
            n=8
        elif fellipseRect.collidepoint(mx,my):
            tool="fellipse"
            n=9
        elif polygonRect.collidepoint(mx,my):
            tool="polygon"
            
            n=10
        elif pickerRect.collidepoint(mx,my):
            tool="colorpicker"
            n=11
        elif alphabrushRect.collidepoint(mx,my):
            tool="transparent brush"
            
            n=12
        elif stampRect.collidepoint(mx,my):
            tool="stamp"
            n=13
            draw.rect(screen,WHITE,stampsRect) #drop down menu opens
            
            screen.blit(rightpic,rightRect) #blits the right and left pictures for user to toggle in stamps menu
            screen.blit(leftpic,leftRect)

        elif firstRect.collidepoint(mx,my): # There are three rects in stamps drop down menu where different stamps are blitted according to the ss value.
            #                                first rect is  the position of the first stamp, and the second rect for second stamp to show and so on.
            xtool="firststamp"              #xtool changes when first, second, or third rect is pressed. 
            
        elif secondRect.collidepoint(mx,my):
            xtool="secondstamp"
            
        elif thirdRect.collidepoint(mx,my):
            xtool="thirdstamp"
            
        elif rightRect.collidepoint(mx,my):
            mtool="right" #mtool is if right or left pic/rect is pressed. According to that, ss value changes.
            xtool="no tool"
            tool="stamp"
            
            
        elif leftRect.collidepoint(mx,my):
            mtool="left"
            xtool="no tool"
            tool="stamp"
            
        elif bgrightRect.collidepoint(mx,my): # for the background when right pic is clicked
            tool="backgrounds"
            
        elif bgleftRect.collidepoint(mx,my): # for the background when left pic is clicked
            tool="backgrounds"
    
        elif playRect.collidepoint(mx,my) and mm==0: #plays the music when play button is pressed first time and mm becomes 1 
            mixer.music.play(-1)
            mm=1
            draw.rect(screen,RED,playRect,4)
        elif playRect.collidepoint(mx,my) and mm==1: #mm has already became one, so if play is presses after the first time, music would start to play again
            mixer.music.unpause()
            draw.rect(screen,RED,playRect,4)
        elif pauseRect.collidepoint(mx,my): #pauses the music when pause button is pressed
            mixer.music.pause()
            draw.rect(screen,RED,pauseRect,4)
            
        elif bgRect.collidepoint(mx,my): #this is when the user clicks on backgrounds
            tool="backgrounds"
            g=2
            draw.rect(screen,WHITE,bgsRect) #new drop down menu opens
            draw.rect(screen,(0, 0, 153),bgsRect,5) #border around that drop down menu
            screen.blit(bgrightpic,bgrightRect) #blitting the right/ left pic on that drop down menu
            screen.blit(bgleftpic,bgleftRect)
            draw.rect(screen,BLACK,bgiRect,3) #area where the smaller version of the background is shown to the user
            n=17
        elif bgiRect.collidepoint(mx,my):
            bgtool="bg" #when the area where the smaller of version of background is shown, the bgtool becomes bg, and is used after for blitting the background on the canvas

        elif undoRect.collidepoint(mx,my): #when undo is pressed 
        #draw.rect(screen,(255,0,0),undoRect,2)
            if click: #only when clicked. only does it ones
                try:
                    redo.append(undo[-1])#the last screenshot in the undo list is appended to the redo list
                    del(undo[-1]) #the last element in the undo list is deleted
                    screen.blit(undo[-1],(300,200)) #the last screenshot is then blitted on the canvas
                except:
                    pass
        
        ######SAME THING FOR REDO########            
        elif redoRect.collidepoint(mx,my):
            if click:
                try:
                    undo.append(redo[-1])
                    del(redo[-1])
                    screen.blit(redo[-1],(300,200))
                except:
                    pass
        
            
                
    if bgrightRect.collidepoint(mx,my) and click==True and g==2 and tool=="backgrounds": #when right pic is pressed
        #stamp3=stampsRect.copy()#screen capture (screenshot)
        if d<(len(bggList)-1): #if d is one less than the length of bggList.
            d+=1 #d increaes
        bgtool="no tool" #bgtool become no tool, so that the user has to press on the bgiRect again (where the background is shown) to blit that background on the canvas. Later in the program
        if pos<6: #as my last background in the list is just white, so the pos variable just checks whether the user that white background is selected or not
                    #because if its selected, then the eraser that has to be used is the normal one, not the blitting one
            pos+=1 
        
        print(pos)

    ##### SAME THING FOR WHEN THE USER CLICKS ON LEFT PIC ON THE BACKGROUND DROP DOWN MENU ######
    if bgleftRect.collidepoint(mx,my) and click==True and g==2 and tool=="backgrounds": 
        if d>0:
            d-=1
        bgtool="no tool" 
        if pos>0:
            pos-=1
    if tool=="backgrounds" and g==2:
        k=2
        screen.blit(bggList[d],bgiRect) #d starts from 0, and when right pic clicked it increases, when left, it decreases, d brings the item from bgglist to blit on bgiRect
                                        #ex. if d = 0, the first background from bgglist would be blitted on the backgrounds drop down menu. if its one, the second background would be blitted

    ###### SAME THING FOR THE RIGHT/LEFT PIC CLICK, BUT THIS IT IS FOR THE STAMPS DROP DOWN MENU, NOT THE BACKGROUND ONE#####
    if rightRect.collidepoint(mx,my) and click==True and n==13:
        #stamp3=stampsRect.copy()#screen capture (screenshot)
        if ss<(len(stampsList)-3): #as three stamps were shown at the same time. One at firstRect, second at secondRect, third at third Rect, the ss had to be three less than the lenght of the stamps list 
            ss+=1 #increases
        
        #screen.blit(stamp3,(540,820)
        #print(ss)

    if leftRect.collidepoint(mx,my) and click==True and n==13:
        if ss>0:
            ss-=1
        
    if tool=="stamp" and n==13: #when stamps is pressed and tool is stamps
        draw.rect(screen,WHITE,firstRect) #rect drawn on each of the three rect so that when the ss changes and new stamp blits, the previous one hides by this white rect
        draw.rect(screen,WHITE,secondRect)
        draw.rect(screen,WHITE,thirdRect)
        screen.blit(stampsList[ss],firstRect) #ss start from 0, when ss is 0, the first stamp is blitted on first Rect, second on second Rect, third on third
        screen.blit(stampsList[ss+1],secondRect) #so when ss increases or decreases by 1, the stamps are blitted according to that from the list
        screen.blit(stampsList[ss+2],thirdRect)        
        print(ss)
        
     
        
    ######### PREVIOUSLY N WAS CHANGED ACCORDING TO THE RECT PRESSES, SO NOW THE FOLLOWING CODE IS USED TO HAVE BACKGROUND AROUND THAT TOOL, WHEN USER SELECTS THAT TOOL#####        
    if n==1:
        draw.rect(screen,RED,pencilRect,4)
        showthickness=thickness2
    elif n==2:
        draw.rect(screen,RED,eraserRect,4)
        showthickness=rad
    elif n==3:
        draw.rect(screen,RED,markerRect,4)
        showthickness=thickness6
    elif n==4:
        draw.rect(screen,RED,rectangleRect,4)
        showthickness=thickness
    elif n==5:
        draw.rect(screen,RED,lineRect,4)
        showthickness=thickness3
    elif n==6:
        draw.rect(screen,RED,sprayRect,4)
        showthickness=thickness4
    elif n==7:
        draw.rect(screen,RED,frectangleRect,4)
    elif n==8:
        draw.rect(screen,RED,ellipseRect,4)
        showthickness=thickness5
    elif n==9:
        draw.rect(screen,RED,fellipseRect,4)
    elif n==10:
        draw.rect(screen,RED,polygonRect,4)
        showthickness=thickness7
    elif n==11:
        draw.rect(screen,RED,pickerRect,4)
    elif n==12:
        draw.rect(screen,RED,alphabrushRect,4)
    elif n==13:
        draw.rect(screen,RED,stampRect,4)
    elif n==17:
        draw.rect(screen,RED,bgRect,4)
        
    if pos==6: #when pos = 6, or the white background is selected by the user, as explained before
        k=3 #used when seeing which eraser to use. Normal one or blitting bakcgrounds one

    if canvasRect.collidepoint(mx,my):
        #########TO GET THE MOUSE POSITION ON THE CANVAS AND SHOW IT ON THE SCREEN##########
        tx,ty=mouse.get_pos()
        mxFont=font.SysFont("Comic Sans MS",20)
        mxText=mxFont.render("Current Mouse Position: "+str(tx-300)+", "+str(ty-200),True,BLACK)
        mxBar=Surface((500,100),SRCALPHA)#infoBar is our "sticky note"
        mxBar.blit(mxText,(40,0))#writing CURRENT MOUSE POSITION on the infoBAr surface
        screen.blit(mxBar,(1320,140))#blitting the sticky note on the
        
    
    print(k)
    ######using the selected tool

    
    if mb[0]==1:
        if canvasRect.collidepoint(mx,my):#clicked on canvas
            screen.set_clip(canvasRect)#only allows the CANVAS to be modified
            if tool=="pencil":
                draw.line(screen,col,(omx,omy),(mx,my),thickness2) #drawing line between old mx, my to new one.
                showthickness= thickness2
            elif tool=="eraser" and k!=2:
                dx=mx-omx #horizontal distance
                dy=my-omy #vertical distance
                dist=int(sqrt(dx**2+dy**2)) #hypotenues distance
                if dist==0: #if there is not distance, meaning the user is not moving the cursoe, then, erase that tiny bit by drawing white circle
                    draw.circle(screen,WHITE,(mx,my),rad)
                for i in range(1,dist+1): #checking i if its in the range of dist. i would start from 1, and would increase until it reaches the value of dist. 
                    xc=int(omx+i*dx//dist) #we are basically checking how far we went from omx to the newer spot. this is is how far we went horizontally. we are checking every time until i is not in range of dist
                    yc=int(omy+i*dy/dist) #this is how far we went vertically
                    draw.circle(screen,WHITE,(xc,yc),rad) #drawing a circle at that point with the same radius
                showthickness= rad
                #draw.circle(screen,WHITE,(mx,my),rad)

            elif tool=="eraser" and k==2 and pos!=6: #this is the eraser tool for the different backgrounds
                
                try:
                    samplePic=bgList[pos].subsurface((mx-300,my-200,rad,rad)) #a subsurface has been created for the background with the width and length of the radius
                    screen.blit(samplePic,(mx,my)) #blitted that where the cursor is pressed.
                    
                except:
                    pass
                
                
            elif tool=="marker":
                
                #####SAME IDEA AS THE ERASER ########
                dx=mx-omx #horizontal distance
                dy=my-omy #vertical distance
                dist=int(sqrt(dx**2+dy**2))
                
                for i in range(1,dist+1):
                    xc=int(omx+i*dx//dist)
                    yc=int(omy+i*dy/dist)
                    draw.circle(screen,col,(xc,yc),thickness6)
                showthickness= thickness6
                #draw.line(screen,col,(omx,omy),(mx,my),10)

                
            elif tool=="rectangle":
                
                screen.blit(canvasPic,(0,0))
                
                f=thickness/2 #i knew that the problem was occuring because if we have higher thickness, the line start from that particular pixel, and
                                #there is an area which remains unfilled. so then i also knew that the point if half of that thickness, so thats what i did here
                l=f-1

                ########## FOUR CASES ################
                if mx>sx and my>sy: #first one when you are making it right to left going bottom
                    
                    draw.line(screen,col,(sx-l,sy),(sx,sy),thickness)
                    draw.line(screen,col,(sx,sy),(sx,my+f),thickness) #i added f which is half of the thickness to the lines. For some cases, adding f was a bit more
                    draw.line(screen,col,(sx,sy),(mx+f,sy),thickness) #so i tried by adding f-1, which is l to some lines and it worked. Then after that i just worked
                    draw.line(screen,col,(mx,sy),(mx,my),thickness) #with the numbers, and it worked after a while.
                    draw.line(screen,col,(sx,my),(mx+f,my),thickness)
                    
                elif mx<sx and my>sy: #second one when you are making it left to right going bottom
                    draw.line(screen,col,(sx,sy),(sx+f,sy),thickness)
                    draw.line(screen,col,(sx,sy),(sx,my+f),thickness)
                    draw.line(screen,col,(sx,sy),(mx-l,sy),thickness)
                    draw.line(screen,col,(mx,sy),(mx,my),thickness)
                    draw.line(screen,col,(sx,my),(mx-l,my),thickness)
                elif mx<sx and sy>my: #third one when you are making it left to right going up
                    draw.line(screen,col,(sx,sy),(sx+f,sy),thickness)
                    draw.line(screen,col,(sx,sy),(sx,my-l),thickness)
                    draw.line(screen,col,(sx,sy),(mx-l,sy),thickness)
                    draw.line(screen,col,(mx,sy),(mx,my),thickness)
                    draw.line(screen,col,(sx,my),(mx-l,my),thickness)
                elif mx>sx and sy>my:#fourth one when you are making it rigth to left going up
                    draw.line(screen,col,(sx-l,sy),(sx,sy),thickness)
                    draw.line(screen,col,(sx,sy),(sx,my-l),thickness)
                    draw.line(screen,col,(sx,sy),(mx+f,sy),thickness)
                    draw.line(screen,col,(mx,sy),(mx,my),thickness)
                    draw.line(screen,col,(sx,my),(mx+f,my),thickness)

                    
            elif tool=="frectangle":
                screen.blit(canvasPic,(0,0))
                draw.rect(screen,col,[sx,sy,mx-sx,my-sy]) # as it was filled, i did not have the problem that i had with unfilled, so i just made a simple rect
                
            elif tool=="line":
                screen.blit(canvasPic,(0,0))
                #                       start   current
                draw.line(screen,col,(sx,sy),(mx,my),thickness3) #sx,sy is the position saved when mouse button down, so just making a line from that point to current 
            
            elif tool=="spray":
                for i in range(40): #making 40 circles randomly in the diameter of the thickness
                    fx=randint(-thickness4,thickness4) #randomly getting fx from the diameter
                    fy=randint(-thickness4,thickness4) ##randomly getting fy from the diameter
                    h=int(sqrt(fx**2+fy**2)) #getting hypoteneuse
                    if h<=thickness4: #has to be less, because if its not, it would go outside the circle of the thickness
                        draw.circle(screen,col,(mx+fx,my+fy),0) #making a small filled circle at that point


            elif tool=="ellipse":
                screen.blit(canvasPic,(0,0))
                ellRect=Rect( sx,sy,mx-sx,my-sy) #need to have rect at four starting points, so that the small holes can be filled and taken up by other ellipse
                ellRect.normalize()
                eellRect=Rect( sx+1,sy,mx-sx,my-sy)#starting one right to the original
                esllRect=Rect( sx-1,sy,mx-sx,my-sy)#starting one left to the original 
                efllRect=Rect( sx,sy+1,mx-sx,my-sy)#starting one up to the original
                edllRect=Rect( sx,sy-1,mx-sx,my-sy)#starting one down to the original
                eellRect.normalize() #normalize makes it works for negative value
                esllRect.normalize()
                efllRect.normalize()
                edllRect.normalize()
                try:
                    
                    #drawing ellipses on all those rects
                    draw.ellipse(screen,col,ellRect,thickness5)
                    draw.ellipse(screen,col,eellRect,thickness5)
                    draw.ellipse(screen,col,esllRect,thickness5)
                    draw.ellipse(screen,col,efllRect,thickness5)
                    draw.ellipse(screen,col,edllRect,thickness5)
                    
                except:
                    pass
                
            elif tool=="fellipse":
                screen.blit(canvasPic,(0,0))
                ellRect=Rect( sx,sy,mx-sx,my-sy) #only need one because it is filled, and there would be no holes of its only one
                ellRect.normalize()
                try:
                    
                    draw.ellipse(screen,col,ellRect,)
                except:
                    pass

            elif tool=="transparent brush":
                ###### SAME IDEA AS THE BRUSH AND THE ERASER, BUT THIS TIME THE BRUSH IS TRANSPARENT#########
                dx=mx-omx #horizontal distance
                dy=my-omy #vertical distance
                cover = Surface((thickness8,thickness8),SRCALPHA) #transparent surface
                dist=int(sqrt(dx**2+dy**2))
                if dist==0:
                    draw.circle(cover,(col[0],col[1],col[2],bt),(10,10),10) #as col has three values (r,g,b), we can take those values for r,g,b,a where a is bt
                    screen.blit(cover,(mx,my)) #when cursor is not moving just clicked
                for i in range(1,dist+1):
                    xc=int(omx+i*dx//dist)
                    yc=int(omy+i*dy/dist)
                    
                    draw.circle(cover,(col[0],col[1],col[2],bt),(thickness8,thickness8),thickness8) #drawing a cicrle on cover surface, not the screen
                    screen.blit(cover,(xc,yc)) #then that surface is blitted on the screen
                showthickness= thickness8
                
                
                        

            #######this was explained before what ss does, and when xtool changes and its purpose######
                
            elif tool=="stamp":
                if xtool=="firststamp":
                    screen.blit(canvasPic,(0,0))
                    screen.blit(stampsList[ss],(mx-75,my-75))# blit the stamp when the cursor is on first rect, as explained before, and clicks on canvas rect
                elif xtool=="secondstamp":
                    screen.blit(canvasPic,(0,0))
                    screen.blit(stampsList[ss+1],(mx-75,my-75)) #same thing as above, the only difference is that the user has to click on second rect for the xtool to beocme second stamp
                elif xtool=="thirdstamp":
                    screen.blit(canvasPic,(0,0))
                    screen.blit(stampsList[ss+2],(mx-75,my-75))

          
            screen.set_clip(None)#EVERYTHING can be modified
        #print(mx,my)
    
    if tool=="backgrounds" and bgtool!="bg":
        k=0
    if tool=="transparent brush":
        #showing transparency ahd how to change it on screen#####
        transparencyFont=font.SysFont("Comic Sans MS",20)
        transparencyText=transparencyFont.render("Current Transparency: "+str(bt) ,True,BLACK) #showing current transparency when transparent tool is chosen.
        transparencyBar=Surface((600,100),SRCALPHA)
        transparencyBar.blit(transparencyText,(200,0))
        screen.blit(transparencyBar,(1160,170))
        ttFont=font.SysFont("Comic Sans MS",20)
        ttText=ttFont.render("Change from right/left arrows" ,True,BLACK)
        ttBar=Surface((600,100),SRCALPHA)
        ttBar.blit(ttText,(200,0))
        screen.blit(ttBar,(1160,190))
        showthickness=thickness8
            
    if tool=="colorpicker" and mb[0]==1: #choosing colour from the colour picker tool
        c=screen.get_at((mx,my))
        col=c
        print(col)
        m=1
        draw.rect(screen,col,zoomRect) #this is the preview box where you can see what colour have you picked
                
    if tool=="backgrounds" and bgtool=="bg" and g==2:
        screen.blit(bgList[d],(300,200)) #this blits the background on canvaas
        k=2
                
    if tool!="stamp":
        screen.blit(spic,(530,820)) #spic was the screenshot of subsurface where stamps drop down menu was, so when the user is not using stamps, that drop down menu
                                    #is replaced by this pic. Same for backgrounds
    if tool!="backgrounds":
        screen.blit(bgspic,(1345,795))
        bgtool="no tool"

    ####changing the colour
    
    if mb[0]==1:
        if colourRect.collidepoint(mx,my):
            col=screen.get_at((mx,my))
            draw.rect(screen,col,zoomRect) #preview box to see the colour that you have picked
            m=1 #Once you change the colour, m=1, because when m is 1, the preview box shows that black col is chosen
    if m!=1:
        draw.rect(screen,BLACK,zoomRect) #at the start it should show that black colour is chosen

    #1-step tool
    if click==True:#left mouse click (button down)
        if clearRect.collidepoint(mx,my):
            draw.rect(screen,WHITE,canvasRect) #drawing a white rect on canvas
            k=3
            print("clearing the screen")
        if saveRect.collidepoint(mx,my): #saving the canvas
            try:
                fname=filedialog.asksaveasfilename(defaultextension=".png")
                #asks the user to input file name they would like to save
                if fname!="":
                    image.save(screen.subsurface(canvasRect),fname)
                #SAving the picture

                #make sure the program is not trying to save a picture if the user does not enter a name
                #to save a picture if the user does not enter a name
            except:
                print("Saving Error")
        if openRect.collidepoint(mx,my):
            try:
                fname=filedialog.askopenfilename()
                newpic=image.load(fname)
                newsmall=transform.scale(newpic,(1000,600))#resizing the picture
                screen.blit(newsmall,canvasRect)

            except:
                print("Loading error")
        
    omx=mx
    omy=my

    ######## THIS SET OF CODE IS JUST TO SHOW THE USER WHAT TOOL THEY HAVE SELECTED, THE THICKNESS, AND HOW TO CHANGE IT ON SCREEN############
    comicFont=font.SysFont("Comic Sans MS",20)
    radiusFont=font.SysFont("Comic Sans MS",20)
    changeFont=font.SysFont("Comic Sans MS",20)
    #maxFont=font.SysFont("Comic Sans MS",20)
    toolText=comicFont.render("Current tool: "+tool,True,BLACK)
    toolBar=Surface((500,100),SRCALPHA)#infoBar is our "sticky note"
    toolBar.blit(toolText,(200,0))
    radiusText=radiusFont.render("Current radius / thickness: "+str(showthickness),True,BLACK)
    radiusBar=Surface((500,100),SRCALPHA)#infoBar is our "sticky note"
    radiusBar.blit(radiusText,(200,0))
    changeText=changeFont.render("Use up/down arrows to change thickness ",True,BLACK)
    changeBar=Surface((800,100),SRCALPHA)#infoBar is our "sticky note"
    changeBar.blit(changeText,(200,0))
    screen.blit(infoBar,(230,0))#blitting the sticky note on the screen
    infoBar.blit(myText,(200,0))
    screen.blit(toolBar,(1160,50))#blitting the sticky note on the scr

    screen.blit(radiusBar,(1160,80))#blitting the sticky note on the scr
    screen.blit(changeBar,(1160,110))#blitting the sticky note on the scr
    

    screen.blit(stampBar,(150,830))#blitting the sticky note on the screen

    screen.blit(bgBar,(1380,710))#blitting the sticky note on the screen
    
    display.flip()
    

quit() #

