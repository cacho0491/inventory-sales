from reportlab.pdfgen import canvas

def hello(c):
    c.drawString(100, 100, "Hello world")
    c.canvas.Canvas("/Users/carloscorrea91/Desktop/inventario/" + "hello.pdf")
    hello(c)
    c.showPage()
    c.save()