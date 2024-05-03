from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
#from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 

myArray = np.array(['apple.jpg', 'ball.jpg', 'books.png', 'brain.jpg', 'bus.jpg',
                    'chalkboard.png', 'computer.jpg', 'crayons.jpg', 'globe.jpg', 'heart.jpg',
                    'lightbulb.jpg', 'mug.jpg', 'musicnote.jpg', 'paint.jpg', 'paperclip.jpg', 
                    'pencil.jpg', 'raisedhand.jpg', 'ruler.jpg', 'school.jpg', 'scissors.png',
                    'notebook.jpg', 'slide.jpg', 'students.jpg', 'teacher.jpg', 'teacherm.jpg'])

cwd = '/Users/sarabellus/Desktop/Personal Code Projects/BrookParkBingo/images/'

fileName = 'myfile.pdf'
docTitle = 'My File'
title = 'Brook Park BINGO'
subTitle = 'Instructions go here!'

pdf = canvas.Canvas(fileName)

for i in range(5):

    np.random.shuffle(myArray)

    sb = myArray.reshape(5, 5)  # sb means shuffled board

    print(sb)

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

    image1 = cwd + sb[0][0]
    image2 = cwd + sb[0][1]
    image3 = cwd + sb[0][2]
    image4 = cwd + sb[0][3]
    image5 = cwd + sb[0][4]
    image6 = cwd + sb[1][0]
    image7 = cwd + sb[1][1]
    image8 = cwd + sb[1][2]
    image9 = cwd + sb[1][3]
    image10 = cwd + sb[1][4]
    image11 = cwd + sb[2][0]
    image12 = cwd + sb[2][1]
    image13 = cwd + sb[2][2]
    image14 = cwd + sb[2][3]
    image15 = cwd + sb[2][4]
    image16 = cwd + sb[3][0]
    image17 = cwd + sb[3][1]
    image18 = cwd + sb[3][2]
    image19 = cwd + sb[3][3]
    image20 = cwd + sb[3][4]
    image21 = cwd + sb[4][0]
    image22 = cwd + sb[4][1]
    image23 = cwd + sb[4][2]
    image24 = cwd + sb[4][3]
    image25 = cwd + sb[4][4]
    

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