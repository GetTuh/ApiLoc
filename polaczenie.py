from flask import Flask,render_template,request
from lokalizacja import funkcja_szer_dlug

app = Flask(__name__,template_folder='Strona')

@app.route('/wynik',methods=['POST'])
def wynik():
    szerokosc = request.form['szerokosc']
    dlugosc = request.form['dlugosc']
    zasieg = request.form['zasieg']

    return funkcja_szer_dlug(szerokosc,dlugosc,zasieg)


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
