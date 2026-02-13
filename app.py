from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_super_secreta"

DEFAULT_USER = "user"
DEFAULT_PASS = "2508"

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        u = (request.form.get("username") or "").strip()
        p = (request.form.get("password") or "").strip()

        if u == DEFAULT_USER and p == DEFAULT_PASS:
            session["auth"] = True
            return redirect(url_for("flower"))
        else:
            error = "Usuario o contraseña incorrectos."

    return render_template("login.html", error=error)

@app.route("/flower")
def flower():
    if not session.get("auth"):
        return redirect(url_for("login"))
    return render_template("flower.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
