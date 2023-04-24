from django.contrib.auth.hashers import make_password

from users.models import Users
from users.serializer import UserSerializer


class UserService:
    def get_all(self):
        users = Users.objects.all()
        return users

    def get(self, nr):
        user = Users.objects.get(pk=nr)
        return user

    def encrypt(self, user: UserSerializer):
        db_password = make_password(user.data.get("password"))
        Users.objects.filter(email=user.data.get("email")).update(password=db_password)

    def delete(self, user_id):
        user = self.get(nr=user_id)
        user.is_active = False
        user.save()
