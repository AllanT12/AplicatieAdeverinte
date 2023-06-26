from setari.models import Setari


class SetariService:

    def get_all(self):
        setari = Setari.objects.all()
        return setari