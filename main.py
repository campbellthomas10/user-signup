from flask import Flask, request, redirect, render_template
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def index():
    return render_template('signup.html', title='Signup')




def is_valid(username):
    if len(username) >= 3 and len(username) <= 20:
        for letter in username:
            if letter == ' ':
                return False
        return True
        

@app.route('/signup', methods=['POST'])
def checks():
    username = request.form['username']
    password = request.form['password']
    verified = request.form['verified']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verification_error = ''
    email_error = ''



    #Checks if username is valid
    if not is_valid(username):
        username_error = "Username is invalid!"
        username = ''



    #Checks if password is valid
    if not is_valid(password):
        password_error = "Password is invalid!"



    #Checks if the password and its verification are the same
    if password != verified:
        verification_error = "Passwords must match!"



    #Checks if the email is valid (if there is one)
    if len(email) != 0:
        if email.find('@') != -1:
            if email.find('.') == -1:
                email_error = "Email is invalid"
                email = ''
        else:
            email_error = "Email is invalid!"
            email = ''



    #Checks if all fields are valid, resets invalid fields
    if not username_error and not password_error and not verification_error and not email_error:
        return redirect('/signed-up?username={0}'.format(username))
    else:
        return render_template('signup.html', title='Signup',
        username_error=username_error, 
        password_error=password_error, 
        verification_error=verification_error, 
        email_error=email_error, 
        username=username,
        email=email)



#What shows up when all is valid
@app.route('/signed-up')
def signed_up():
    username = request.args.get('username')
    return '<h1>Welcome, {0}!</h1>'.format(username)


    

app.run()