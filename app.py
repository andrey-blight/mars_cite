import os.path
import os
from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route("/")
@app.route('/index/<title>')
def index(title="Начальная страница"):
    return render_template('base.html', title=title)


@app.route("/training/<prof>")
def training(prof: str):
    css_href = url_for('static', filename="/css/center.css")
    header, img = "Научные симуляторы", url_for('static', filename='images/spaceship_science.jpg')
    if "инженер" in prof.lower() or "строитель" in prof.lower():
        header, img = "Инженерные тренажеры", url_for('static', filename='images/spaceship_engineer.jpg')
    return render_template('training.html', header=header, img_href=img, css_href=css_href)


@app.route("/list_prof/<list_style>")
def list_prof(list_style):
    css_href = url_for('static', filename="/css/center.css")
    profs = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "инжинер по терраформированию",
             "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер жизнеобеспечения",
             "метеороог", "оператор марсохода", "киберинженер", "штурман", "пилот дронов"]
    return render_template("list.html", css_href=css_href, type=list_style, profs=profs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
