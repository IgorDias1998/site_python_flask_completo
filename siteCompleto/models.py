from siteCompleto import bancodedados, loginmanager
from datetime import datetime
from flask_login import UserMixin

@loginmanager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(bancodedados.Model, UserMixin):
    id = bancodedados.Column(bancodedados.Integer, primary_key = True)
    username = bancodedados.Column(bancodedados.String, nullable=False)
    email = bancodedados.Column(bancodedados.String, nullable=False, unique=True)
    senha = bancodedados.Column(bancodedados.String, nullable=False)
    foto_perfil = bancodedados.Column(bancodedados.String, default='default.jpg')
    posts = bancodedados.relationship('Post', backref='Autor', lazy=True)
    cursos = bancodedados.Column(bancodedados.String, nullable=False, default='Não informado')

    def contar_posts(self):
        return len(self.posts)

class Post(bancodedados.Model):
    id = bancodedados.Column(bancodedados.Integer, primary_key=True)
    titulo = bancodedados.Column(bancodedados.String, nullable=False)
    corpo = bancodedados.Column(bancodedados.Text, nullable=False)
    data_criacao = bancodedados.Column(bancodedados.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = bancodedados.Column(bancodedados.Integer, bancodedados.ForeignKey('usuario.id'), nullable=False)