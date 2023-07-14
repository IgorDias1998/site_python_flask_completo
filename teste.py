from siteCompleto import bancodedados, app

with app.app_context():
    bancodedados.create_all()
