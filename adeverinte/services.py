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