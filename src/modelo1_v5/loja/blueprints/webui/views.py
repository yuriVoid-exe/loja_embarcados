from flask import render_template, request, redirect, url_for, session, flash
from loja.ext.database import db
from loja.model import Product, User


def index():
    products = db.session.execute(
        db.select(Product).order_by(Product.description)
    ).scalars()
    return render_template("products.html", products=products)


def product(product_id):
    product = db.session.execute(
        db.select(Product).filter_by(id=product_id)
    ).scalar()
    return render_template("product.html", product=product)


def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        # Validações básicas de entrada
        if not username or not password:
            flash("Preencha todos os campos.", "warning")
            return render_template("register.html")

        if password != confirm_password:
            flash("As senhas não coincidem.", "danger")
            return render_template("register.html")

        # Verifica se o usuário já existe
        if User.query.filter_by(username=username).first():
            flash("Nome de usuário já cadastrado. Escolha outro.", "danger")
            return render_template("register.html")

        # Criação do novo usuário (por padrão is_admin=False)
        new_user = User(username=username, is_admin=False)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash("Cadastro realizado com sucesso! Faça seu login.", "success")
        return redirect(url_for("webui.login"))

    return render_template("register.html")


def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session["user_id"] = user.id
            session["username"] = user.username
            session["is_admin"] = user.is_admin
            flash("Login realizado com sucesso!", "success")

            next_page = request.args.get("next") or url_for("webui.index")
            return redirect(next_page)

        flash("Usuário ou senha inválidos.", "danger")

    return render_template("login.html")


def logout():
    session.clear()
    flash("Sessão encerrada com sucesso.", "info")
    return redirect(url_for("webui.index"))
