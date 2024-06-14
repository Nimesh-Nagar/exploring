from flask import Flask , render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd1b00e9e2053b397c892a26bf72e365c'

# dummy data 
posts = [
    {
        "author" : "Nimesh Nagar",
        "title" : "Blog Post 1",
        "content" : "my first post",
        "date_posted" : "May 18 , 2024"
    },
    {
        "author" : "Mahendra Nagar",
        "title" : "Blog Post 2",
        "content" : "my second post",
        "date_posted" : "May 19 , 2024"
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

# Registration page routing
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    #validatoin of info filled in form and creat a message accrdingly using "flash "
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html', title='Register', form=form)

#  Login page routing
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        #check is user is register? than allow her to home page
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been Logined in ! ", 'success')
            return redirect(url_for('home'))
        else:
            flash("Login Not Allowed. Please Check you email or password", 'danger')
        
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)