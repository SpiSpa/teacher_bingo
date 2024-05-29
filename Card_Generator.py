# This was a quick project I threw together to help celebrate teachera appreciation week at our school
#the following code creates 5x5 bingo cards with 25 randomized images.  
#the first 5 cards are winners after 12 predetermind bingo images are called.  the remaining cards are losers.  

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
#from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 

def checkForWinners(winnerArray):
    winner = False
    sumsArray1 = winnerArray.sum(axis=0)
    sumsArray2 = winnerArray.sum(axis=1)
    sumDiagonal1 = winnerArray[0][0] + winnerArray[1][1] + winnerArray[2][2] + winnerArray[3][3] + winnerArray[4][4]
    sumDiagonal2 = winnerArray[0][4] + winnerArray[1][3] + winnerArray[2][2] + winnerArray[3][1] + winnerArray[4][0]

    print(sumsArray1)
    print(sumsArray2)
    print(sumDiagonal1)
    print(sumDiagonal2)

    if sumsArray1[0] == 5 or sumsArray1[1] == 5 or sumsArray1[2] == 5 or sumsArray1[3] == 5 or sumsArray1[4] == 5:
        print("found a vertical win")
        winner = True 
    elif sumsArray2[0] == 5 or sumsArray2[1] == 5 or sumsArray2[2] == 5 or sumsArray2[3] == 5 or sumsArray2[4] == 5:
        print("found a horizontal win")
        winner = True 
    elif sumDiagonal1 == 5 or sumDiagonal2 == 5:
        print("found a diagonal win")
        winner = True
    else:
        winner = False

    return(winner)

myArray = np.array([('apple.jpg', 1), ('ball.jpg', 1), ('books.png', 1), ('brain.jpg', 1), ('bus.jpg', 1),
                    ('chalkboard.png', 1), ('computer.jpg', 1), ('crayons.jpg', 1), ('globe.jpg', 1), ('heart.jpg', 0),
                    ('lightbulb.jpg', 1), ('mug.jpg', 0), ('musicnote.jpg', 1), ('paint.jpg', 0), ('paperclip.jpg', 0), 
                    ('pencil.jpg', 1), ('raisedhand.jpg', 0), ('ruler.jpg', 0), ('school.jpg', 1), ('scissors.png', 0),
                    ('notebook.jpg', 0), ('slide.jpg', 0), ('students.jpg', 1), ('teacher.jpg', 1), ('teacherm.jpg', 0)])

cwd = '/Users/sarabellus/Desktop/Personal Code Projects/BrookParkBingo/images/'

fileName = 'myfile.pdf'
docTitle = 'My File'
title = 'Brook Park BINGO'
subTitle = 'Instructions go here!'

pdf = canvas.Canvas(fileName)

winCardNum = int(input("Enter the number of winning cards you would like."))
for i in range(winCardNum):
    winner = False

    while winner == False:
        np.random.shuffle(myArray)

        imageList = []
        for i in range(25):
            imageList.append(myArray[i][0])

        winnerList = []
        for i in range(25):
            winnerList.append(int(myArray[i][1]))

        imageArray = np.array(imageList).reshape(5, 5)
        winnerArray = np.array(winnerList).reshape(5, 5)

        print(imageArray)
        print(winnerArray)

        winner = checkForWinners(winnerArray)
        if winner == False:
            print("Winner NOT found, regenerating card")

    pdf.setTitle(docTitle)

    pdfmetrics.registerFont(TTFont('abc', 'vera.ttf'))
                        
    pdf.setFont('abc', 36)
    pdf.drawCentredString(300, 770, title)

    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290, 720, subTitle)

    pdf.line(30, 710, 550, 710)
    #text = pdf.beginText(40, 680)
    #text.setFont("Courier", 18)
    #text.setFillColor(colors.red)

    image1 = cwd + imageArray[0][0]
    image2 = cwd + imageArray[0][1]
    image3 = cwd + imageArray[0][2]
    image4 = cwd + imageArray[0][3]
    image5 = cwd + imageArray[0][4]
    image6 = cwd + imageArray[1][0]
    image7 = cwd + imageArray[1][1]
    image8 = cwd + imageArray[1][2]
    image9 = cwd + imageArray[1][3]
    image10 = cwd + imageArray[1][4]
    image11 = cwd + imageArray[2][0]
    image12 = cwd + imageArray[2][1]
    image13 = cwd + imageArray[2][2]
    image14 = cwd + imageArray[2][3]
    image15 = cwd + imageArray[2][4]
    image16 = cwd + imageArray[3][0]
    image17 = cwd + imageArray[3][1]
    image18 = cwd + imageArray[3][2]
    image19 = cwd + imageArray[3][3]
    image20 = cwd + imageArray[3][4]
    image21 = cwd + imageArray[4][0]
    image22 = cwd + imageArray[4][1]
    image23 = cwd + imageArray[4][2]
    image24 = cwd + imageArray[4][3]
    image25 = cwd + imageArray[4][4]
    

    pdf.drawImage(image1, 60, 160, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image2, 160, 160, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image3, 260, 160, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image4, 360, 160, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image5, 460, 160, width=80, height=80, preserveAspectRatio=True)

    pdf.drawImage(image6, 60, 260, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image7, 160, 260, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image8, 260, 260, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image9, 360, 260, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image10, 460, 260, width=80, height=80, preserveAspectRatio=True)

    pdf.drawImage(image11, 60, 360, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image12, 160, 360, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image13, 260, 360, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image14, 360, 360, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image15, 460, 360, width=80, height=80, preserveAspectRatio=True)

    pdf.drawImage(image16, 60, 460, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image17, 160, 460, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image18, 260, 460, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image19, 360, 460, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image20, 460, 460, width=80, height=80, preserveAspectRatio=True)

    pdf.drawImage(image21, 60, 560, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image22, 160, 560, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image23, 260, 560, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image24, 360, 560, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image25, 460, 560, width=80, height=80, preserveAspectRatio=True)
    

    pdf.setLineWidth(6)
    pdf.rect(50, 150, 500, 500)
    pdf.setLineWidth(3)
    pdf.line(50, 250, 550, 250)
    pdf.line(50, 350, 550, 350)
    pdf.line(50, 450, 550, 450)
    pdf.line(50, 550, 550, 550)
    pdf.line(150, 150, 150, 650)
    pdf.line(250, 150, 250, 650)
    pdf.line(350, 150, 350, 650)
    pdf.line(450, 150, 450, 650)

    pdf.showPage()

for i in range(95):
    winner = True

    while winner == True:
        np.random.shuffle(myArray)

        imageList = []
        for i in range(25):
            imageList.append(myArray[i][0])

        winnerList = []
        for i in range(25):
            winnerList.append(int(myArray[i][1]))

        imageArray = np.array(imageList).reshape(5, 5)
        winnerArray = np.array(winnerList).reshape(5, 5)

        print(imageArray)
        print(winnerArray)

        winner = checkForWinners(winnerArray)
        if winner == True:
            print("Winner was found, regenerating card")

    pdf.setTitle(docTitle)

    pdfmetrics.registerFont(TTFont('abc', 'vera.ttf'))
                        
    pdf.setFont('abc', 36)
    pdf.drawCentredString(300, 770, title)

    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290, 720, subTitle)

    pdf.line(30, 710, 550, 710)
    #text = pdf.beginText(40, 680)
    #text.setFont("Courier", 18)
    #text.setFillColor(colors.red)

    image1 = cwd + imageArray[0][0]
    image2 = cwd + imageArray[0][1]
    image3 = cwd + imageArray[0][2]
    image4 = cwd + imageArray[0][3]
    image5 = cwd + imageArray[0][4]
    image6 = cwd + imageArray[1][0]
    image7 = cwd + imageArray[1][1]
    image8 = cwd + imageArray[1][2]
    image9 = cwd + imageArray[1][3]
    image10 = cwd + imageArray[1][4]
    image11 = cwd + imageArray[2][0]
    image12 = cwd + imageArray[2][1]
    image13 = cwd + imageArray[2][2]
    image14 = cwd + imageArray[2][3]
    image15 = cwd + imageArray[2][4]
    image16 = cwd + imageArray[3][0]
    image17 = cwd + imageArray[3][1]
    image18 = cwd + imageArray[3][2]
    image19 = cwd + imageArray[3][3]
    image20 = cwd + imageArray[3][4]
    image21 = cwd + imageArray[4][0]
    image22 = cwd + imageArray[4][1]
    image23 = cwd + imageArray[4][2]
    image24 = cwd + imageArray[4][3]
    image25 = cwd + imageArray[4][4]
    

    pdf.drawImage(image1, 60, 160, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image2, 160, 160, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image3, 260, 160, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image4, 360, 160, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image5, 460, 160, width=80, height=80, preserveAspectRatio=True)

    pdf.drawImage(image6, 60, 260, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image7, 160, 260, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image8, 260, 260, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image9, 360, 260, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image10, 460, 260, width=80, height=80, preserveAspectRatio=True)

    pdf.drawImage(image11, 60, 360, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image12, 160, 360, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image13, 260, 360, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image14, 360, 360, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image15, 460, 360, width=80, height=80, preserveAspectRatio=True)

    pdf.drawImage(image16, 60, 460, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image17, 160, 460, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image18, 260, 460, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image19, 360, 460, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image20, 460, 460, width=80, height=80, preserveAspectRatio=True)

    pdf.drawImage(image21, 60, 560, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image22, 160, 560, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image23, 260, 560, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image24, 360, 560, width=80, height=80, preserveAspectRatio=True)
    pdf.drawImage(image25, 460, 560, width=80, height=80, preserveAspectRatio=True)
    

    pdf.setLineWidth(6)
    pdf.rect(50, 150, 500, 500)
    pdf.setLineWidth(3)
    pdf.line(50, 250, 550, 250)
    pdf.line(50, 350, 550, 350)
    pdf.line(50, 450, 550, 450)
    pdf.line(50, 550, 550, 550)
    pdf.line(150, 150, 150, 650)
    pdf.line(250, 150, 250, 650)
    pdf.line(350, 150, 350, 650)
    pdf.line(450, 150, 450, 650)

    pdf.showPage()


pdf.save()