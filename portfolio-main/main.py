#Импорт
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

@app.route('/form', methods=['POST'])
def save_form():
    if request.method == 'POST':
        email = request.form.get('email')
        text = request.form.get('text')
        
        form = Form(email=email, text=text)
        db.session.add(form)
        db.session.commit()
    return redirect('/')    

#Запуск страницы с контентом
@app.route('/')
def index():
    entries = Form.query.all()
    return render_template('index.html', entries=entries)

@app.route('/feedback')
def feedback():
    entries = Form.query.all()
    return render_template('feedback.html', entries=entries)

#Динамичные скиллы
@app.route('/process_form', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python,
                           button_discord=button_discord,
                           button_html=button_html,
                           button_db=button_db)


if __name__ == "__main__":
    app.run(debug=True)