from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
# from ew import User

app = Flask(__name__)
app.secret_key = "qwe"
bcrypt = Bcrypt(app)


app.config["MONGO_URI"] = "mongodb+srv://admin:12341234@cluster0.1ddpj.mongodb.net/MyMa_db?retryWrites=true&w=majority"
mongo = PyMongo(app)
dbs = mongo.db.users
checker=False



class User:
    is_registered = False

    def __init__(self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password

    def get_info(self):
        return {"name": self.name,
                "mail": self.mail,
                "password": self.password
                }


@app.route('/', methods=['POST', 'GET'])
def main_page():
    if "user" not in session:
        if request.method == "POST":
            new_user = User(mail=request.form['mail'],
                            name=request.form['mail'].split("@")[0],
                            password=bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
                            )
            try:
                if bcrypt.check_password_hash(
                        dbs.find_one({"mail": request.form['mail']})["password"],
                        request.form['password']):

                    session["user"] = new_user.name.capitalize()
                    flash("Please choose which item tracker you want")
                    return render_template("chosing.html", session=session, checker=True, myname=session["user"])
                else:
                    flash(new_user.name.capitalize() + ", Please check your Password and try again")
                    return render_template("index.html", session=None)

            except:
                flash("Username or Password is incorrect. Please try again")
                return render_template("index.html", session=None)


        else:
            if User.is_registered:
                return render_template("index.html", checker=True, session=None)
            else:
                return render_template("index.html")
    else:
        return render_template("chosing.html", myname=session["user"])



@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if "user" not in session:
        if request.method == "POST":
            new_user = User(mail=request.form['mail'],
                            name=request.form['name'],
                            password=bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
                            )

            if dbs.find_one({"mail": new_user.mail}):
                flash("The account already exists")
                return render_template("SignUp.html", session=None)
            else:
                dbs.insert_one(new_user.get_info())
                flash("You Have Registered Successfully, Please Login ")
                User.is_registered=True
                return redirect(url_for("main_page", session=None))
        else:
            return render_template("SignUp.html", session=None)

    else:
        return render_template("chosing.html", session=None)




@app.route('/chosing')
def chosing():
    if "user" not in session:
        flash("Please Register First")
        return redirect(url_for("signup"))
    else:
        return render_template("chosing.html")




@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("main_page"))

if __name__ == "__main__":
    app.run(debug=True)


