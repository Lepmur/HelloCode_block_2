# file = open('file.txt', 'r', encoding='utf-8')
#
# resultData = list()
# for line in file.readlines():
#     resultData.append(tuple(line.split('\n')[0].split(';')))
#
# file.close()
#
# print(resultData)

'''
a - added
w - write
r - read
'''

from flask import Flask, render_template
from LoginForm import Lf
from AuthForm import Af

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwerty123'

# @app.route('/')
# def main():
#     with open('file.txt', 'r', encoding='utf-8') as file:
#         resultData = list()
#         for line in file.readlines():
#             resultData.append(tuple(line.split('\n')[0].split(';')))
#     return render_template('base.html', data=resultData)
#
# @app.route('/about')
# def about():
#     return render_template('about.html')

@app.route('/')
def main():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def reg():
    form = Lf()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title="Registration", form=form,
                                   message="Password mismatch!")
        with open('file.txt', 'a', encoding='utf-8') as file:
            file.write(f'{form.name.data};{form.email.data};{form.password.data}\n')
        return render_template('register.html', message="Registration successful!")
    return render_template('register.html', title="Authorisation", form=form)

@app.route('/log', methods=['GET', 'POST'])
def log():
    form = Af()
    if form.validate_on_submit():
        with open('file.txt', 'r', encoding='utf-8') as file:
            data = ' '.join(file.readlines())
        if form.email.data not in data:
            return render_template('login.html', form=form, message="You are not registred!")
        else:
            for i in data.split():
                if form.email.data in i:
                    if i.split(';')[-1] == form.password.data:
                        return render_template('login.html', form=form, message="You are login successful!")
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run()
