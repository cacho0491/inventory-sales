import os
import random
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import textobject
from reportlab.platypus import *
from controlador import get_date_records


def create_report(start_date, end_date):
       registros = get_date_records(start_date, end_date)
       id = random.randint(1, 1000)
       file_path = os.path.dirname(os.path.realpath("__file__")) + "/reporte-{0}.pdf".format(id)
       doc = SimpleDocTemplate(file_path, pagesize=letter)
       styleSheet = getSampleStyleSheet()

       # container for the 'Flowable' objects
       elements = []
       # c = canvas.Canvas(file_path, pagesize=landscape(letter))


       P1 = Paragraph('''<para autoLeading="off" fontSize=25 align=center>
                     <p>Bazar y Papeleria Fiorella</p><br/><br/></para>''',
       styleSheet["BodyText"])

       P4 = Paragraph('''<para autoLeading="off" fontSize=10 align=center>
                                   <p>RUC: 1102916648001</p><br/><br/></para>''',
                      styleSheet["BodyText"])

       P5 = Paragraph('''<para autoLeading="off" fontSize=10 align=center>
                            <p>Febres Cordero y Mariano Samaniego</p><br/><br/></para>''',
                      styleSheet["BodyText"])

       P6 = Paragraph('''<para autoLeading="off" fontSize=10 align=center>
                                   <p>Cariamanga</p><br/><br/></para>''',
                      styleSheet["BodyText"])
       P7 = Paragraph('''<para autoLeading="off" fontSize=10 align=center>
                                   <p>Telf. (07) 2 687460 / (07) 2 687 034</p><br/><br/></para>''',
                      styleSheet["BodyText"])



       P3 = Paragraph('''<para autoLeading="off" fontSize=15 align=left>
                     <p>Desde: {0} Hasta: {1}</p><br/><br/></para>'''.format(start_date, end_date),
       styleSheet["BodyText"])



       data= [['ID', 'Nombre del Producto', 'Precio Unitario', 'Cantidad', 'Total'],]

       for registro in registros:
           data.append(registro)

       data.append([' ', ' ', ' ', ' ', ' '])
       data.append(['', '', '', 'Total', calcular_total(registros)])
       t=Table(data)
       t.setStyle(TableStyle([
                            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                            ('TEXTCOLOR',(0,0),(1,-1),colors.red)
                            ]))
       elements.append(P1)
       elements.append(P4)
       elements.append(P5)
       elements.append(P6)
       elements.append(P7)
       elements.append(P3)
       elements.append(t)

       # write the document to disk
       doc.build(elements)
       dirname = os.path.dirname(__file__)
       filename = os.path.join(dirname, file_path)
       os.startfile(filename)


def calcular_total(registros):
    total = 0
    for registro in registros:
        total = total + registro[4]

    return total
