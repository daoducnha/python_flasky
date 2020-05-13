from .app import db

from .app.models import User, Role



admin_role = Role.query.filter_by(name='Administrator').first()
default_role = Role.query.filter_by(default=True).first()

for u in User.query.all():
    if u.role is None:
        if u.email == 'daoducnha2949301@gmail.com':
            u.role = admin_role
        else:
            u.role = default_role

db.session.commit()