import io

from django.http import FileResponse
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.rl_settings import defaultPageSize

from adeverinte.models import Adeverinta


class AdeverintaService:
    def get_all(self):
        users = Adeverinta.objects.all()
        return users

    def get(self, nr):
        user = Adeverinta.objects.get(pk=nr)
        return user

    def delete(self, user_id):
        user = self.get(nr=user_id)
        user.is_active = False
        user.save()

    def createPDF(self, nr):
        adeverinta = self.get(nr)
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        pdfmetrics.registerFont(TTFont("TNR", "times.ttf"))
        pdfmetrics.registerFont(TTFont("TNRB", "timesbd.ttf"))
        p.setFont("TNR", 20)
        p.drawCentredString(300, 700, "ADEVERINȚĂ")
        p.setFont("TNR", 14)
        p.drawString(50, 650, "Subsemnatul(a) {Nume Complet Student} este înscris(ă) în anul universitar 2022/2023")
        p.drawString(30, 635, "în anul {anul de studiu} de studii, program/ domeniu de studii - licență:")
        form = p.acroForm
        form.checkbox(x=40, y=610, checked=False, buttonStyle='check',
                      name="program",
                      tooltip="program",
                      relative=True,
                      size=12)
        p.drawString(55, 610, "Calculatoare")
        p.drawString(30, 595, "formă de învățământ IF, regim: {cu taxă/ fără taxă}.")
        p.drawString(50, 580, f"Adeverința se eliberează pentru a-i servi la ..{adeverinta.motivatie}..")
        p.drawString(70, 550, "DECAN,")
        p.drawCentredString(300, 550, "SECRETAR ȘEF,")
        p.drawString(450, 550, "SECRETARIAT,")
        p.drawString(430, 750, "Nr..../FIESC/....")
        p.setFont("TNR", 12)
        p.drawString(30, 790, "UNIVERSITATEA „ȘTEFAN CEL MARE” DIN SUCEAVA")
        p.drawString(30, 775, "FACULTATEA DE INGINERIE ELECTRICĂ ȘI ȘTIINȚA CALCULATOARELOR")
        p.showPage()
        p.save()
        buffer.seek(0)
        return buffer
