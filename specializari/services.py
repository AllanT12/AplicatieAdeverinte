from specializari.models import Specializari
from specializari.serializer import SpecializariSerializer


class SpecializariService:
    def get_all(self):
        users = Specializari.objects.all()
        return users

    def get(self, nr):
        user = Specializari.objects.get(pk=nr)
        return user



