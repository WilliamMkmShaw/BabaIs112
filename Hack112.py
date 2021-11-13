#Members (andrewID): wmshaw, bingchel, qingyanc, zmansoor
#Members (names): William Shaw, Christine Li, Qingyang Cao, Zara Mansoor
#Team: 112 is US
#Project Name: BABA IS 112

from cmu_112_graphics import *

def appStarted(app):
    app.mode = 'menuMode'

    #in game Mode
    app.level = 0
    resetAll(app)

##########################################
# Menu Mode
##########################################

def menuMode_redrawAll(app, canvas):
    canvas.create_image(app.margin, app.margin, anchor = NW, image=ImageTk.PhotoImage(app.imageMenu))

def menuMode_mousePressed(app, event):
    #when click start

    r = app.fullScreenRatio #r is ratio
    m = app.margin
    #when click levels
    if (265*r+m < event.x < 765*r+m and 460*r+m < event.y < 610*r+m):
        app.mode = 'levelMode'
    #when click Demo
    elif(265*r+m < event.x < 765*r+m and 640*r+m < event.y < 780*r+m):
        app.mode = 'gameMode'
        #hardcoded level 0
        app.level = 0
        resetAll(app)
    #when click Credit
    elif(690*r+m < event.x < 935*r+m and 870*r+m < event.y < 950*r+m):
        app.mode = 'creditMode'
    #when click help
    elif(70*r+m < event.x < 315*r+m and 870*r+m < event.y < 950*r+m):
        app.mode = 'helpMode'

##########################################
# Level Mode
##########################################

def levelMode_redrawAll(app, canvas):
    canvas.create_image(app.margin, app.margin, anchor = NW, image=ImageTk.PhotoImage(app.imageLevel))

def levelMode_mousePressed(app, event):
    r = app.fullScreenRatio #r is ratio
    m = app.margin
    
    #click back
    if (690*r+m < event.x < 935*r+m and 865*r+m < event.y < 945*r+m):
        app.mode = 'menuMode'
    #level 1
    elif (20*r+m < event.x < 470*r+m and 350*r+m < event.y < 500*r+m):
        app.mode = 'gameMode'
        app.level = 1
        resetAll(app)
    #level 2
    elif (515*r+m < event.x < 970*r+m and 350*r+m < event.y < 500*r+m):
        app.mode = 'gameMode'
        app.level = 2
        resetAll(app)
    #level 3
    elif (20*r+m < event.x < 470*r+m and 540*r+m < event.y < 685*r+m):
        app.mode = 'gameMode'
        app.level = 3
        resetAll(app)
    #level 4
    elif (515*r+m < event.x < 970*r+m and 540*r+m < event.y < 685*r+m):
        app.mode = 'gameMode'
        app.level = 4
        resetAll(app)

def levelMode_keyPressed(app, event):
    if event.key == "m":
            app.mode = "menuMode"
            

##########################################
# Credit Mode
##########################################

def creditMode_redrawAll(app, canvas):
    canvas.create_image(app.margin, app.margin, anchor = NW, image=ImageTk.PhotoImage(app.imageCredit))

def creditMode_mousePressed(app, event):
    r = app.fullScreenRatio #r is ratio
    m = app.margin
    
    #click back
    if (705*r+m < event.x < 945*r+m and 890*r+m < event.y < 975*r+m):
        app.mode = 'menuMode'

def creditMode_keyPressed(app, event):
    if event.key == "m":
            app.mode = "menuMode"

##########################################
# Help Mode
##########################################

def helpMode_redrawAll(app, canvas):
    canvas.create_image(app.margin, app.margin, anchor = NW, image=ImageTk.PhotoImage(app.imageHelp))

def helpMode_mousePressed(app, event):
    r = app.fullScreenRatio #r is ratio
    m = app.margin
    
    #click back
    if (695*r+m < event.x < 935*r+m and 870*r+m < event.y < 950*r+m):
        app.mode = 'menuMode'

def helpMode_keyPressed(app, event):
    if event.key == "m":
            app.mode = "menuMode"

##########################################
# Game Mode
##########################################

#------------------ Helper ------------------
# copied from 2d list class notes
def print2dList(a):
    if (a == []): print([]); return
    rows, cols = len(a), len(a[0])
    colWidths = [0] * cols
    for col in range(cols):
        colWidths[col] = max([len(str(a[row][col])) for row in range(rows)])
    print('[')
    for row in range(rows):
        print(' [ ', end='')
        for col in range(cols):
            if (col > 0): print(', ', end='')
            print(str(a[row][col]).ljust(colWidths[col]), end='')
        print(' ]')
    print(']')

#------------------ __init__ ------------------
# from Tetris of Homework6
def getDimensions():
    rows = 21
    cols = 21
    cellSize = 30
    margin = 10
    return (rows, cols, cellSize, margin)

def generateBoardDemo(app):
    board = [[0] * app.cols for row in range(app.rows)]
    
    for row in range(app.rows):
        for col in range(app.cols):
            board[row][col] = set()

    board[3][3].add('babaT')
    board[3][4].add('is')
    board[3][5].add('youA')
    board[3][-6].add('flagT')
    board[3][-5].add('is')
    board[3][-4].add('winA')
    board[4][-4].add("dieA")

    board[10][5].add('baba')
    board[10][-6].add('flag')

    for col in range(3, 18):
        board[8][col].add("wall")
        board[12][col].add("wall")
    
    for row in range(9, 12):
        board[row][9].add('rock')
    
    board[-4][3].add('wallT')
    board[-4][4].add('is')
    board[-4][5].add('stopA')
    board[-4][-6].add('rockT')
    board[-4][-5].add('is')
    board[-4][-4].add('pushA')
    
    return board

def generateBoardLevel1(app):
    board = [[0] * app.cols for row in range(app.rows)]
    
    for row in range(app.rows):
        for col in range(app.cols):
            board[row][col] = set()
    
    for col in range(9, 17):
        board[3][col].add("wall")
        board[12][col].add("wall")
        board[18][col].add("wall")
    
    for col in range(4, 10):
        board[8][col].add("wall")
        board[12][col].add("wall")
    
    for row in range(8, 13):
        board[row][4].add("wall")
    
    for row in range(3, 18):
        board[row][16].add("wall")
        if not (9 <= row <= 12):
            board[row][9].add("wall")
    
    board[14][6].add('babaT')
    board[15][6].add('is')
    board[16][6].add('youA')
    board[14][11].add('wallT')
    board[15][11].add('is')
    board[16][11].add('stopA')

    board[5][11].add('is')
    board[10][11].add('flag')
    board[10][6].add('flagT')
    board[8][14].add('winA')
    board[15][14].add('baba')

    return board

def generateBoardLevel2(app):
    board = [[0] * app.cols for row in range(app.rows)]
    
    for row in range(app.rows):
        for col in range(app.cols):
            board[row][col] = set()
    
    for col in range(9, 17):
        board[3][col].add("flag")
        board[12][col].add("flag")
        board[18][col].add("flag")
    
    for col in range(4, 10):
        board[8][col].add("flag")
        board[12][col].add("flag")
    
    for row in range(8, 13):
        board[row][4].add("flag")
    
    for row in range(3, 18):
        board[row][16].add("flag")
        if not (9 <= row <= 12):
            board[row][9].add("flag")
    
    board[14][6].add('wallT')
    board[15][6].add('is')
    board[16][6].add('youA')
    board[14][11].add('flagT')
    board[15][11].add('is')
    board[16][11].add('stopA')

    board[5][11].add('is')
    board[10][11].add('baba')
    board[10][6].add('flagT')
    board[8][14].add('winA')
    board[15][14].add('wall')

    return board

def generateBoardLevel3(app):
    board = [[0] * app.cols for row in range(app.rows)]
    
    for row in range(app.rows):
        for col in range(app.cols):
            board[row][col] = set()
    
    # set all the walls
    for row in range(4):
        for col in range(7,14):
            board[row][col].add("wall")

    # set "target" flag and "wall is stop"
    board[0][10] = {"flag"}
    board[1][9] = {"wallT"}
    board[1][10] = {"is"}
    board[1][11] = {"dieA"}

    # set two 1's rocks
    for row in range(6, 11):
        board[row][5].add("rock")
        board[row][9].add("rock")

    # set 2 rocks
    for col in range(13, 16):
        board[6][col].add("rock")
        board[8][col].add("rock")
        board[10][col].add("rock")

    board[7][15].add("rock")
    board[9][13].add("rock")

    # set "baba is you"
    board[16][3].add('babaT')
    board[16][4].add('is')
    board[16][5].add('youA')

    # set other rules
    board[16][15].add('flagT')
    board[16][16].add('is')
    board[16][17].add('winA')
    board[17][15].add('rockT')
    board[17][16].add('is')
    board[17][17].add('pushA')

    # place baba
    board[16][10].add("baba")
    
    return board

def generateBoardLevel4(app):
    board = [[0] * app.cols for row in range(app.rows)]
    
    for row in range(app.rows):
        for col in range(app.cols):
            board[row][col] = set()
    
    # set all the walls
    for col in range(9, 19):
        board[5][col].add("wall")
        board[17][col].add("wall")
    
    for row in range(5, 18):
        board[row][9].add("wall")
        board[row][18].add("wall")

    for col in range(0, 4):
        board[1][col].add("wall")
    
    for col in range(-1, -5, -1):
        board[1][col].add("wall")
    
    board[0][3].add("wall")
    board[0][-4].add("wall")

    # set rock and baba
    board[11][2].add('baba')
    board[9][1].add('rock')
    board[13][6].add('rock')
    board[11][5].add('rock')
    board[17][5].add('rock')
    board[16][2].add('rock')
    board[7][4].add('rock')
        
    # set "flag is win" (fixed in the corner)
    board[0][0].add('flagT')
    board[0][1].add('is')
    board[0][2].add('winA')

    # set "wall is die"
    board[7][11].add('wallT')
    board[8][11].add('is')
    board[9][11].add('dieA')

    # set "rock is push"
    board[19][-4].add("rockT")
    board[19][-3].add("is")
    board[19][-2].add("pushA")

    # set "baba is you"
    board[0][-3].add('babaT')
    board[0][-2].add('is')
    board[0][-1].add('youA')

    # set target flag
    board[11][16].add('flag')

    return board

def resetAll(app):
    app.rows, app.cols, app.cellSize, app.margin = getDimensions()
    
    if app.level == 0:
        app.board = generateBoardDemo(app)
    elif app.level == 1:
        app.board = generateBoardLevel1(app)
    elif app.level == 2:
        app.board = generateBoardLevel2(app)
    elif app.level == 3:
        app.board = generateBoardLevel3(app)
    elif app.level == 4:
        app.board = generateBoardLevel4(app)

    app.bgcolor = 'black'
    app.picRatio = app.cellSize/76
    app.fullScreenRatio = app.rows*app.cellSize/1000

    # initialize all dictionaries
    resetAttributeDict(app)
    resetAttributeDictTrans(app)
    app.modifierList = {'babaT', 'wallT', 'flagT', 'rockT',
                        'youA', 'winA', 'stopA', 'pushA', 'dieA',
                        'is'
                        }
    readStatement(app)
    transDict(app)
    genBoardAttributes(app)

    # game state
    app.isDie = False
    app.isWin = False
    app.direction = (0, 0)

    # load images
    app.imageBaba = app.scaleImage(app.loadImage('images/baba.png'),app.picRatio)
    app.imageWall = app.scaleImage(app.loadImage('images/wall.png'),app.picRatio)
    app.imageFlag = app.scaleImage(app.loadImage('images/flag.png'),app.picRatio)
    app.imageRock = app.scaleImage(app.loadImage('images/rock.png'),app.picRatio)
    app.imageBabaT = app.scaleImage(app.loadImage('images/babaT.png'),app.picRatio)
    app.imageWallT = app.scaleImage(app.loadImage('images/wallT.png'),app.picRatio)
    app.imageFlagT = app.scaleImage(app.loadImage('images/flagT.png'),app.picRatio)
    app.imageRockT = app.scaleImage(app.loadImage('images/rockT.png'),app.picRatio)
    app.imageYouA = app.scaleImage(app.loadImage('images/youA.png'),app.picRatio)
    app.imageWinA = app.scaleImage(app.loadImage('images/winA.png'),app.picRatio)
    app.imageStopA = app.scaleImage(app.loadImage('images/stopA.png'),app.picRatio)
    app.imagePushA = app.scaleImage(app.loadImage('images/pushA.png'),app.picRatio)
    app.imageDieA = app.scaleImage(app.loadImage('images/dieA.png'),app.picRatio)
    app.imageIs = app.scaleImage(app.loadImage('images/is.png'),app.picRatio)
    app.imageWin = app.scaleImage(app.loadImage('images/winImage.png'),app.fullScreenRatio)
    app.imageLose = app.scaleImage(app.loadImage('images/loseImage.png'),app.fullScreenRatio)
    app.imageMenu = app.scaleImage(app.loadImage('images/menu.png'),app.fullScreenRatio)
    app.imageLevel = app.scaleImage(app.loadImage('images/level.png'),app.fullScreenRatio)
    app.imageCredit = app.scaleImage(app.loadImage('images/credit.png'),app.fullScreenRatio)
    app.imageHelp = app.scaleImage(app.loadImage('images/help.png'),app.fullScreenRatio)

#Generate 2D list of empty sets:
def generate2DListSet(rows, cols):
    return [[set()]*cols for row in range(rows)]

# from classnotes https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def getCellBounds(app, row, col):
    gridWidth = app.width-app.margin*2
    gridHeight = app.height-app.margin*2
    cellWidth = gridWidth/app.cols
    cellHeight = gridHeight/app.rows
    x0 = app.margin + col*cellWidth
    x1 = app.margin + (col+1)*cellWidth
    y0 = app.margin + row*cellHeight
    y1 = app.margin + (row+1)*cellHeight
    return (x0, y0, x1, y1)

def drawCell(app, canvas, row, col):
    x0, y0, x1, y1 = getCellBounds(app, row, col)
    canvas.create_rectangle(x0, y0, x1, y1, fill=app.bgcolor)

def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, canvas, row, col)

def drawBaba(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imageBaba))

def drawWall(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imageWall))

def drawFlag(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imageFlag))

def drawRock(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imageRock))

def drawBabaT(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imageBabaT))

def drawWallT(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imageWallT))

def drawFlagT(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imageFlagT))

def drawRockT(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imageRockT))

def drawYouA(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imageYouA))

def drawWinA(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imageWinA))

def drawStopA(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imageStopA))

def drawPushA(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imagePushA))

def drawDieA(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imageDieA))

def drawIs(app, canvas, x0, y0):
    canvas.create_image(x0, y0, anchor = NW, image=ImageTk.PhotoImage(app.imageIs))

def drawElements(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            x0, y0, x1, y1 = getCellBounds(app, row, col)
            position = app.board[row][col] 
            if "wall" in position:
                drawWall(app, canvas, x0, y0)
            if "rock" in position:
                drawRock(app, canvas, x0, y0)
            if "flag" in position:
                drawFlag(app, canvas, x0, y0)
            if "babaT" in position:
                drawBabaT(app, canvas, x0, y0)
            if "wallT" in position:
                drawWallT(app, canvas, x0, y0)
            if "flagT" in position:
                drawFlagT(app, canvas, x0, y0)
            if "rockT" in position:
                drawRockT(app, canvas, x0, y0)
            if "youA" in position:
                drawYouA(app, canvas, x0, y0)
            if "winA" in position:
                drawWinA(app, canvas, x0, y0)
            if "stopA" in position:
                drawStopA(app, canvas, x0, y0)
            if "pushA" in position:
                drawPushA(app, canvas, x0, y0)
            if "dieA" in position:
                drawDieA(app, canvas, x0, y0)
            if "is" in position:
                drawIs(app, canvas, x0, y0)
            if "baba" in position:
                drawBaba(app, canvas, x0, y0)

#------------------ Attributes ------------------
#Empty app.attributeDict:
def resetAttributeDict(app):
    app.attributeDict = {'baba':set(), 'wall':set(), 'flag':set(), 'rock':set()}

#Empty app.attributeDictTrans:
def resetAttributeDictTrans(app):
    app.attributeDictTrans = {'youA':set(),'winA':set(), 'stopA':set(), 
                              'pushA':set(), 'dieA':set()}

#Takes app.attributeDict and adds key(object) with value(attribute)
def updateAttributeDict(app, object, attribute):
    app.attributeDict[object].add(attribute)

#Generate list of attributes given board
#Use this to create a board of attribute vals for checking.
def genBoardAttributes(app):
    rows, cols = len(app.board), len(app.board[0])
    app.attributeBoard = generate2DListSet(rows, cols)
    #Iterate through each coord in board:
    for row in range(rows):
        for col in range(cols):
            #For each object in pos, add attributes to the other board.
            for object in app.board[row][col]:
                if object in app.attributeDict:
                    app.attributeBoard[row][col] = app.attributeBoard[row][col].union(
                                                        app.attributeDict[object])
                elif object in app.modifierList:
                    app.attributeBoard[row][col] = {"modifier"}

                        
    return None #app.attributeBoard is changed
    
#Creates a transpose of the app.attributeDict()
def transDict(app):
    resetAttributeDictTrans(app)
    for objectName in app.attributeDict:
        attributeSet = app.attributeDict[objectName]
        for attribute in attributeSet:
            app.attributeDictTrans[attribute].add(objectName)

# Update the app.attributeDict based on current board
def readStatement(app):
    resetAttributeDict(app)
    rows, cols = len(app.board), len(app.board[0])
    for row in range(rows):
        for col in range(cols):
            # iterate through each cell
            # find the corresponding item set
            itemSet = app.board[row][col]
            if "is" in itemSet:
                # when we find a is -- wordSearch around it
                statementSearch(app, row, col)
    app.attributeDict 

# inspired by 112 wordSearch
def statementSearch(app, row, col):
    # "is" location -- row, col
    # check the cell around
    for drow, dcol in [(-1, 0), (0, -1), (+1, 0), (0, +1)]:
        rowCheck, colCheck = row + drow, col + dcol
        if isOnBoard(app, rowCheck, colCheck):
            # if the cell is on board
            # get itemSet of that cell -- check whether it's an object
            itemSetOfCellCheck = app.board[rowCheck][colCheck]
            for item in itemSetOfCellCheck:
                # if item is an object text representations (end with "T")
                if item.endswith("T"):
                    # check the opposite cell
                    oppRow, oppCol = row - drow, col - dcol
                    if isOnBoard(app, oppRow, oppCol):
                        itemSetOfOppCell = app.board[oppRow][oppCol]
                        for oppItem in itemSetOfOppCell:
                            if oppItem.endswith("A"):
                                # key: item[:-1] | value: oppItem
                                updateAttributeDict(app, item[:-1], oppItem)

# Helper function: check whether certain cell is on board
def isOnBoard(app, row, col):
    rows, cols = len(app.board), len(app.board[0])
    return not (row < 0 or row >= rows or col < 0 or col >= cols)

# Takes app.attributeDict and adds key(object) with value(attribute)
def updateAttributeDict(app, object, attribute):
    app.attributeDict[object].add(attribute)

#------------------ Game States ------------------
#Checks if game is won:
#CHANGE THE LAST TO CHANGE GAME STATE
def isWonOrDie(app):
    rows, cols = len(app.attributeBoard), len(app.attributeBoard[0])
    for row in range(rows):
        for col in range(cols):
            attriList = app.attributeBoard[row][col]
            if 'youA' in attriList and 'winA' in attriList:
                app.isWin = True
                print('WINNER')
            elif 'youA' in attriList and 'dieA' in attriList:
                app.isDie = True
                print('DEAD')

#------------------ Movement ------------------
def gameMode_keyPressed(app, event):
    if event.key == "m":
        app.mode = "menuMode"
        return

    # waiting for restart
    if event.key == "r":
        resetAll(app)
        return
    
    if app.isWin or app.isDie:
        return
    
    if app.isDie == False:
        # Takes app.direction from keypressed
        # sets direction and passes to make move
        if (event.key == 'Up'):   
            app.direction = (-1, 0)
            for row in range(app.rows):
                for col in range(app.cols):
                    makeMove(app, row, col)
        elif (event.key == 'Down'): 
            app.direction = (+1, 0)
            for row in range(app.rows-1, -1, -1):
                for col in range(app.cols):
                    makeMove(app, row, col)
        elif (event.key == 'Left'):  
            app.direction = (0, -1)
            for col in range(app.cols):
                for row in range(app.rows):
                    makeMove(app, row, col)
        elif (event.key == 'Right'): 
            app.direction = (0, +1)
            for col in range(app.cols-1, -1, -1):
                for row in range(app.rows):
                    makeMove(app, row, col)

# makeMove takes in row and col -- make the move if legal
def makeMove(app, row, col):
    # check if "youA" in attribute list of current cell
    attributeListCurr = app.attributeBoard[row][col]

    if "youA" not in attributeListCurr: return

    # move the object with attribute "youA"
    drow, dcol = app.direction
    nextRow, nextCol = row + drow, col + dcol
    if isOnBoard(app, nextRow, nextCol):
        # check attribute in next cell
        attributeListNext = app.attributeBoard[nextRow][nextCol]

        # just return when there is "stopA"
        if "stopA" in attributeListNext: return

        # push everything in pushList except for "youA"
        if "pushA" in attributeListNext or "modifier" in attributeListNext:
            # get a list of pushable items and endCondition
            pushList, endCondition = getPushList(app, nextRow, nextCol)
            # if the item after endList is "stop" -- we cannot push into it
            if endCondition == "stop":
                return
            else:
                # else -- we push each item one by one
                # note: pushList is ordered
                for itemRow, itemCol in pushList:
                    movePushableItem(app, itemRow, itemCol)
                    genBoardAttributes(app)
        
        # update first once after move all the pushable items
        readStatement(app)
        transDict(app)
        genBoardAttributes(app)

        # move all the items that has "youA"
        if "stopA" not in attributeListNext:
            currObjectSet = app.board[row][col]
            tempObjectSet = copy.copy(currObjectSet)
            # only move the object that has "youA" in currObjectSet
            for currObject in tempObjectSet:
                if currObject in app.attributeDictTrans["youA"]:
                    tempNextAttriList = app.attributeBoard[nextRow][nextCol]
                    if "pushA" not in tempNextAttriList and "modifier" not in tempNextAttriList:
                        app.board[nextRow][nextCol].add(currObject)
                        app.board[row][col].remove(currObject)
    
    # After we make move, get the updated version of all the dictionaries
    # including: app.attributeDict, app.attributeDictTrans, app.attributeBoard
    readStatement(app)
    transDict(app)
    genBoardAttributes(app)

    # Also check app.isDie stage -- update
    isWonOrDie(app)

# Return a list of pushable and endCondtion items based on the direction
# starting from given row and col
def getPushList(app, row, col):
    pushList = [[row, col]]
    drow, dcol = app.direction
    currRow, currCol = row, col
    endCondition = ""

    # check whether nextRow and nextCol is on broad
    while isOnBoard(app, currRow + drow, currCol + dcol):
        nextRow, nextCol = currRow + drow, currCol + dcol
        nextAttriSet = app.attributeBoard[nextRow][nextCol]

        # if the next item is pushable -- insert it into the list
        if "pushA" in nextAttriSet or "modifier" in nextAttriSet:
            pushList.insert(0, [nextRow, nextCol])
            currRow, currCol = nextRow, nextCol
        else:
            # if the next item is stop -- mark it
            if "stopA" in nextAttriSet:
                endCondition = "stop"
            break
    
    # return a 2d list of pushable items locations and endConditon
    # endCondition: stop or not
    return pushList, endCondition

# Move pushable items based on the given row and col
# -- similar to how we move "youA"
def movePushableItem(app, row, col):
    drow, dcol = app.direction
    nextRow, nextCol = row + drow, col + dcol

    # if the next position is on board
    if isOnBoard(app, nextRow, nextCol):
        currObjectSet = app.board[row][col]
        tempObjectSet = copy.copy(currObjectSet)

        # only move the objects that has "pushA" attribute
        # or is in app.modifierList -- pushable
        for currObject in tempObjectSet:
            if (currObject in app.attributeDictTrans["pushA"] 
                    or currObject in app.modifierList):
                tempNextAttriList = app.attributeBoard[nextRow][nextCol]
                if "pushA" not in tempNextAttriList and "modifier" not in tempNextAttriList:
                    app.board[nextRow][nextCol].add(currObject)
                    app.board[row][col].remove(currObject)

def gameMode_redrawAll(app, canvas):
    drawBoard(app, canvas)
    drawElements(app, canvas)
    if app.isWin == True:
        # draw the win screen
        canvas.create_image(app.margin, app.margin, anchor = NW, image=ImageTk.PhotoImage(app.imageWin))
    if app.isDie == True:
        # draw the lose screen
        canvas.create_image(app.margin, app.margin, anchor = NW, image=ImageTk.PhotoImage(app.imageLose))

def playBaba():
    rows, cols, cellSize, margin = getDimensions()
    width = cols*cellSize+margin*2
    height = rows*cellSize+margin*2
    runApp(width=width, height=height)

playBaba()
