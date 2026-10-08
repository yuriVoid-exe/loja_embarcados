from flask import Blueprint
from .views import index, product, login, logout

bp = Blueprint(
    'webui',
    __name__,
    template_folder='templates',
    url_prefix="/main/v1"
)

bp.add_url_rule("/", view_func=index, endpoint="index")
bp.add_url_rule(
    "/product/<product_id>",
    view_func=product,
    endpoint="productview"
)
bp.add_url_rule("/login", view_func=login, methods=["GET", "POST"], endpoint="login")
bp.add_url_rule("/logout", view_func=logout, endpoint="logout")


def init_app(app):
    app.register_blueprint(bp)
