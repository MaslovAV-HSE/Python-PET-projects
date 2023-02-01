from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont


def CreatePDF(text):
    canvas = Canvas("results.pdf", pagesize=A4)
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))

    canvas.setFont('FreeSans', 16)
    canvas.drawString(1 * inch, 11 * inch, "Возможные результаты через 10 лет")
    canvas.drawString(1 * inch, 10 * inch, text)

    canvas.drawImage("result.png", 10, 10, mask="auto", width=600, height=300)
    canvas.save()

