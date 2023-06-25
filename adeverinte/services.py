import datetime
import io

from django.http import FileResponse
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.rl_settings import defaultPageSize

from adeverinte.models import Adeverinta
from specializari.models import Specializari
from users.models import Users
from users.serializer import UserSerializer


class AdeverintaService:
    nr = 1
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

    def createPDF(self, nr, user_id):
        adeverinta = self.get(nr)
        subsemnat = Users.objects.get(email=adeverinta.subsemnatul)
        decan = Users.objects.get(email=adeverinta.decan)
        secS = Users.objects.get(email=adeverinta.secretar_sef)
        sec = Users.objects.get(email=adeverinta.secretar)
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        pdfmetrics.registerFont(TTFont("TNR", "times.ttf"))
        pdfmetrics.registerFont(TTFont("TNRB", "timesbd.ttf"))
        p.setFont("TNR", 20)
        p.drawCentredString(300, 700, "ADEVERINTA")
        p.setFont("TNR", 14)
        p.drawString(50, 650, f"Subsemnatul(a) {subsemnat.first_name} {subsemnat.last_name} este inscris(a) in anul universitar 2022/2023")
        p.drawString(30, 635, "în anul 4 de studii, program/ domeniu de studii - licenta:")
        form = p.acroForm
        spec = Specializari.objects.all()
        y= 610
        id_list = [item['id'] for item in subsemnat.specializare.values("id")]
        for i in spec :
            c = False
            for j in id_list:
                if i.id == j:
                    c = True
            form.checkbox(x=40, y=y, checked=c, buttonStyle='check',
                      name="program",
                      tooltip="program",
                      relative=True,
                      size=12)
            p.drawString(55, y, i.nume)
            y -= 15
        y -= 15
        p.drawString(30, y, "forma de invatamant IF, regim: fara taxa.")
        y -= 15
        p.drawString(50, y, f"Adeverinta se elibereaza pentru a-i servi la ..{adeverinta.motivatie}..")
        y -= 30
        p.drawString(70, y, "DECAN,")
        p.drawCentredString(300, y, "SECRETAR SEF,")
        p.drawString(450, y, "SECRETARIAT,")
        y -= 15
        p.drawString(70, y, decan.first_name + " " + decan.last_name)
        p.drawString(300, y, secS.first_name + " " + secS.last_name)
        p.drawString(450, y, sec.first_name + " " + sec.last_name)

        p.drawString(430, 750, f"Nr {adeverinta.nr}/FIESC/{adeverinta.data}")
        p.setFont("TNR", 12)
        p.drawString(30, 790, "UNIVERSITATEA STEFAN CEL MARE DIN SUCEAVA")
        p.drawString(30, 775, "FACULTATEA DE INGINERIE ELECTRICA SI STIINTA CALCULATOARELOR")
        p.showPage()
        p.save()
        buffer.seek(0)
        return buffer

    def create(self, data, user_id):
        subsemnat = Users.objects.get(pk=user_id)
        data["subsemnatul"] = subsemnat.id
        decan = Users.objects.get(role=4)
        sec = Users.objects.get(role=1)
        sec_sef = Users.objects.get(role=3)
        data["decan"] = decan.id
        data["secretar"] = sec.id
        data["secretar_sef"] = sec_sef.id
        id_list = [item['id'] for item in subsemnat.specializare.values("id")]
        data["specilizare"] = id_list
        data["acord_decan"] = False
        data["acord_secretar"] = False
        data["acord_secretar_sef"] = False
        data["nr"] = self.nr
        self.nr += 1
        data["numar_de_inregistrare_comun"] = self.nr
        data["data"] = datetime.date.today()
        return data

    def Accept(self, id,user_id):
        subsemnat = Users.objects.get(pk=user_id)
        adev = Adeverinta.objects.get(pk=id)
        if subsemnat.role == 1:
            adev.acord_secretar = True
        elif subsemnat.role == 3:
            adev.acord_secretar_sef = True
        elif subsemnat.role == 4:
            adev.acord_decan = True
        if adev.acord_decan and adev.acord_secretar and adev.acord_secretar_sef:
            adev.stare = 1
        adev.save()

    def Deny(self, id,user_id):
        adev = Adeverinta.objects.get(pk=id)
        adev.stare = 2
        adev.save()

    def getOnlyAccepted(self):
        adev = Adeverinta.objects.filter(stare=1)
        return adev