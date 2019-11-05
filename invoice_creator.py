import os
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import textobject
from reportlab.platypus import *
from controlador import *


def create_invoice(factura_id):
       registros = get_invoice_records(factura_id)
       factura = get_invoice(factura_id)
       iva = factura[4]
       subtotal = factura[3]
       total = factura[2]
       full_name = ""
       address = ""
       if factura[5] is not None:
          cliente = search_client_id(factura[5])
          full_name = cliente[1] + " " + cliente[2]
          address = cliente[5]
       fecha = factura[1]
       file_path = os.path.dirname(os.path.realpath("__file__")) + "/factura-{0}.pdf".format(factura_id)
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

       P2 = Paragraph('''<para autoLeading="off" fontSize=15 align=left>
                     <p>Nombre del cliente: {0}</p><br/><br/></para>'''.format(full_name),
       styleSheet["BodyText"])

       P8 = Paragraph('''<para autoLeading="off" fontSize=15 align=left>
                         <p>Direccion del cliente: {0}</p><br/><br/></para>'''.format(address),
                      styleSheet["BodyText"])


       P3 = Paragraph('''<para autoLeading="off" fontSize=15 align=left>
                     <p>Fecha: {0}</p><br/><br/></para>'''.format(fecha),
       styleSheet["BodyText"])



       data= [['ID', 'Nombre del Producto', 'Precio Unitario', 'Cantidad', 'Total'],]

       for registro in registros:
              data.append(registro)

       data.append(['', '', '', 'Subtotal', subtotal])
       data.append(['', '', '', 'IVA', iva])
       data.append(['', '', '', 'Total', total])
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
       elements.append(P8)
       elements.append(P2)
       elements.append(t)

       # write the document to disk
       doc.build(elements)
       dirname = os.path.dirname(__file__)
       filename = os.path.join(dirname, file_path)
       os.startfile(filename)
