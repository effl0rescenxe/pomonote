from flask import Flask, render_template, request, redirect, url_for, session
# render_template : get code from template its css
# request = flask something
# redirect = tells the browser to go visit another route
# url_for = generates the exact path for a route
# session = memory of who you are so you can access your data 

app = Flask(__name__) # is the main file being run?
app.secret_key = "babo"

notes = [] # list that stores the notes - later needs to be in database

users = {
    "skibidi": "12345678",   # username: password
}

@app.route("/", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
    return render_template("home.html", notes=notes)

@app.route("/delete/<int:index>", methods=["POST"])
def delete_note(index):
    if 0 <= index < len(notes):
        notes.pop(index)
    return redirect(url_for("home"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if users.get(username) == password:
            session["user"] = username
            return redirect(url_for("home"))
        else:
            return "Invalid credentials"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)