
class UserLogin:

    def __init__(self, usuario, passw):
        self.usuario = usuario
        self.passw = passw

    def to_dict(self):
        return {
            "usuario": self.usuario,
            "pass": self.passw
        }