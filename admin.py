import os
from flask_admin import Admin
from models import db, User, People, Planets, Starships, Favorite_people, Favorite_planets, Favorite_starships
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(People, db.session))
    admin.add_view(ModelView(Planets, db.session))
    admin.add_view(ModelView(Starships, db.session))
    admin.add_view(ModelView(Favorite_people, db.session))
    admin.add_view(ModelView(Favorite_planets, db.session))
    admin.add_view(ModelView(Favorite_starships, db.session))
