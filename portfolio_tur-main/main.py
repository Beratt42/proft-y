# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    berat = request.form.get("button_discord")
    hetemele = request.form.get("button_html")
    debe = request.form.get("button_db")
    meyil = request.form.get("email")
    yazi = request.form.get("text")

    with open("e.txt","a",encoding = "utf-8") as Q:
        if meyil:

            Q.write(f'meyil: {meyil}\n')
            Q.write(f'yazi: {yazi}\n')
            Q.write(f'-----------\n')


    return render_template('index.html', button_python=button_python, berat = berat, hetemele = hetemele, debe = debe)



if __name__ == "__main__":
    app.run(debug=True)
