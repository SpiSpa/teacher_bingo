from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
#from PIL import Image
import numpy as np

myArray = np.array([[0, 1, 2, 3, 4],
                    [5, 6, 7, 8, 9],
                    [10, 11, 12, 13, 14], 
                    [15, 16, 17, 18, 19],
                    [20, 21, 22, 23, 24]])

cwd = '/Users/sarabellus/Desktop/Personal Code Projects/BrookParkBingo/images/'

fileName = 'myfile.pdf'
docTitle = 'My File'
title = 'Brook Park BINGO'
subTitle = 'Instructions go here!'
textLines = ['hello,', "I'm here,", "I'm waiting!."]

apple = cwd + "apple.jpg"

pdf = canvas.Canvas(fileName)

for i in range(5):

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

    pdf.drawImage(apple, 50, 150, width=80, height=80, preserveAspectRatio=True)

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