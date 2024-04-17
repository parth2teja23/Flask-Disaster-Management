from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", text="testing")


@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstname) < 3:
            flash('Name must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) > 8:
            flash('Password should be greater than 7 characters.', category='error')
        else:
            #add user to database
            flash('User aded sucessfuly!', category='success')
            pass
        
        
        
    return render_template("sign_up.html", method=['GET', 'POST'])