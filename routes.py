from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User, Place
from forms import SignupForm, LoginForm, AddressForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///learningflask'
db.init_app(app)
app.secret_key = 

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
	if 'email' in session:
		return redirect(url_for('home'))

	form = SignupForm()
	if request.method == 'POST':
		if form.validate() == False:
			return render_template("signup.html", form = form)
		else:
			#if not db.session.query(User).filter(User.email == form.email.data).count():
			newUser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
			db.session.add(newUser)
			db.session.commit()

			session['email'] = newUser.email
			return redirect(url_for('home'))
	elif request.method == 'GET':
		return render_template("signup.html", form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
	if 'email' in session:
		return redirect(url_for('home'))

	form = LoginForm()
	if request.method == 'POST':
		if form.validate() == False:
			return render_template("login.html", form = form)
		else:
			#user = User(form.email.data)
			email = form.email.data
			password = form.password.data
			user_from_table = User.query.filter_by(email = email).first()
			if user_from_table is not None and user_from_table.check_password(password):
				session['email'] = user_from_table.email
				return redirect(url_for('home'))
			else:
				return redirect(url_for('login'))

	elif request.method == 'GET':
		return render_template("login.html", form = form)

@app.route("/logout")
def signout():
	session.pop('email', None)
	return redirect(url_for('index'))

@app.route("/home", methods = ['GET', 'POST'])
def home():
	if 'email' not in session:
		return redirect(url_for('login'))

	form = AddressForm()
	places = []
	coordinates = (37.122, -122.084)

	if request.method == 'POST':
		if form.validate ==  False:
			return render_template("home.html", form = form)
		else:
			address = form.address.data
			p = Place()
			coordinates = p.address_to_latlng(address)
			places = p.query(address)
			return render_template("home.html", form = form, coordinates = coordinates, places = places)

	elif request.method == 'GET':
		return render_template("home.html", form = form, coordinates = coordinates, places = places)

if __name__ == "__main__":
	app.run(debug = True)