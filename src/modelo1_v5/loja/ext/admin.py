from flask import session, redirect, url_for, request
from flask_babel import Babel
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from loja.ext.database import db
from loja.model import Product, User


class ProtectedModelView(ModelView):
    def is_accessible(self):
        return session.get("is_admin") is True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("webui.login", next=request.url))


class ProtectedAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return session.get("is_admin") is True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("webui.login", next=request.url))


def init_app(app):
    babel = Babel(app)
    admin = Admin(
        app,
        name="Painel Architech",
        index_view=ProtectedAdminIndexView()
    )

    admin.add_view(ProtectedModelView(Product, db.session))
    admin.add_view(ProtectedModelView(User, db.session))
