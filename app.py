import os.path
import os
from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return "Миссия Колонизация Марса"


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route("/promotion_image")
def promo():
    return f"""<html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/promo_style.css')}" />
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src="{url_for('static', filename='images/mars.jpg')}" alt="Марс">
            <div class="alert alert-primary" role="alert">
                <p><strong>Человечество вырастает из детства.</strong></p>
            </div>
            <div class="alert alert-secondary" role="alert">
                <p><strong>Человечеству мала одна планета.</strong></p>
            </div>
            <div class="alert alert-success" role="alert">
                <p><strong>Мы сделаем обитаемыми безжизненные пока планеты.</strong></p>
            </div>
            <div class="alert alert-danger" role="alert">
                <p><strong>И начнем с Марса!</strong></p>
            </div>
            <div class="alert alert-warning" role="alert">
                <p><strong>Присоединяйся!</strong></p>
            </div>
        </body>
    </html>"""


@app.route("/astronaut_selection", methods=["GET", "POST"])
def selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename="/css/form_style.css")}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <div>
                                    <h1 class="heading">Анкета претиндента</h1>
                                    <h2 class="heading">На участие в мисии</h2>
                                </div>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <input class="form-control" placeholder="Введите фамилию" name="surname">
                                        <input class="form-control" placeholder="Введите имя" name="name">
                                        <input type="email" class="form-control email" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у Вас образование?</label>
                                            <select class="form-select" id="education" name="education">
                                              <option>Начальное</option>
                                              <option>Основное</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                            </select>
                                        </div>
                                        <div class="form-group block">
                                            <label for="classSelect">Какие у Вас есть профессии?</label>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="prof" value="investigator">
                                                <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="prof" value="builder">
                                                <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="prof" value="pilot">
                                                <label class="form-check-label" for="acceptRules">Пилот</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="prof" value="meteorologist">
                                                <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="prof" value="life_support">
                                                <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="prof" value="chemical_protection">
                                                <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="prof" value="Doctor">
                                                <label class="form-check-label" for="acceptRules">Врач</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="prof" value="Exobiologist">
                                                <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                            </div>
                                        </div>
                                        <div class="form-group block">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group block">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="ans" rows="3" name="ans"></textarea>
                                        </div>
                                        <div class="form-group block">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group form-check block">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    else:
        return "Форма отправлена"


@app.route("/choice/<planet_name>")
def choice_planet(planet_name):
    if planet_name == "Меркурий":
        return f"""<html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
            <title>Варианты выбора</title>
        </head>
        <body>
            <h1>Мое предложение: {planet_name}</h1>
            <div class="alert alert-primary" role="alert">
                <p><strong>Меркурий — самая маленькая и самая близкая к Солнцу планета.</strong></p>
            </div>
            <div class="alert alert-secondary" role="alert">
                <p><strong>C помощью обычного телескопа можно увидеть эту удивительную планету.</strong></p>
            </div>
            <div class="alert alert-success" role="alert">
                <p><strong>Меркурий известен с античных времен и представляет собой «странствующую звезду».</strong></p>
            </div>
            <div class="alert alert-danger" role="alert">
                <p><strong>Первые люди наблюдали Меркурий невооруженным взглядом примерно 5 тысяч лет назад.</strong></p>
            </div>
            <div class="alert alert-warning" role="alert">
                <p><strong>Первым астрономом, который наблюдал за Меркурием, был Галилео Галилей.</strong></p>
            </div>
        </body>
    </html>"""
    elif planet_name == "Венера":
        return f"""<html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                crossorigin="anonymous">
                <title>Варианты выбора</title>
            </head>
            <body>
                <h1>Мое предложение: {planet_name}</h1>
                <div class="alert alert-primary" role="alert">
                    <p><strong>Венера находится к Земле ближе всех остальных планет нашей Солнечной системы.</strong></p>
                </div>
                <div class="alert alert-secondary" role="alert">
                    <p><strong>У Венеры и Земли похожие размеры (диаметр Венеры на 650 километров меньше) и масса (она составляет 81 % от массы Земли).</strong></p>
                </div>
                <div class="alert alert-success" role="alert">
                    <p><strong>Венера обладает столь высоким альбедо, что в безлунную ночь может отбрасывать тень на Землю.</strong></p>
                </div>
                <div class="alert alert-danger" role="alert">
                    <p><strong>Маленький вес относительно Земли уменьшает соответственно силу тяжести. Весить на соседней планете мы будем меньше.</strong></p>
                </div>
                <div class="alert alert-warning" role="alert">
                    <p><strong>Венера имеет очень плотную атмосферу, ее масса в 93 раза больше земного воздуха.</strong></p>
                </div>
            </body>
        </html>"""
    elif planet_name == "Земля":
        return f"""<html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                crossorigin="anonymous">
                <title>Варианты выбора</title>
            </head>
            <body>
                <h1>Мое предложение: {planet_name}</h1>
                <div class="alert alert-primary" role="alert">
                    <p><strong>Единственная планета, где существует сложная форма жизни.</strong></p>
                </div>
                <div class="alert alert-secondary" role="alert">
                    <p><strong>Среди земной группы планет Земля обладает наибольшей гравитацией и сильнейшим магнитным полем.</strong></p>
                </div>
                <div class="alert alert-success" role="alert">
                    <p><strong>Наличие выпуклостей вокруг экватора связано с вращательной способностью Земли.</strong></p>
                </div>
                <div class="alert alert-danger" role="alert">
                    <p><strong>Средняя глубина океанов, покрывающих 70% поверхности планеты, равняется 4 километрам.</strong></p>
                </div>
                <div class="alert alert-warning" role="alert">
                    <p><strong>Крупнейшая озоновая дыра обнаружена над Антарктидой в 2006 году.</strong></p>
                </div>
            </body>
        </html>"""
    elif planet_name == "Марс":
        return f"""<html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                crossorigin="anonymous">
                <title>Варианты выбора</title>
            </head>
            <body>
                <h1>Мое предложение: {planet_name}</h1>
                <div class="alert alert-primary" role="alert">
                    <p><strong>Mapc являeтcя чeтвepтoй плaнeтoй oт Coлнцa и имeeт типичный кpacный цвeт, кoтopый был иcтoчникoм paзличныx нaзвaний, иcпoльзoвaвшиxcя для плaнeты.</strong></p>
                </div>
                <div class="alert alert-secondary" role="alert">
                    <p><strong>Mapc - xoлoднaя плaнeтa, и ee aтмocфepa oчeнь тoнкaя. Из-зa этoгo плaнeтa нe мoжeт пoддepживaть жидкую вoду.</strong></p>
                </div>
                <div class="alert alert-success" role="alert">
                    <p><strong>Hecмoтpя нa тo, чтo Kpacнaя плaнeтa cocтaвляeт чуть бoльшe пoлoвины диaмeтpa Зeмли, oнa имeeт тaкoe жe кoличecтвo cуши, кaк и нa нaшeй плaнeтe.</strong></p>
                </div>
                <div class="alert alert-danger" role="alert">
                    <p><strong>B ceвepнoм пoлушapии плaнeты мeньшe кpaтepoв, и oни oтнocитeльнo мoлoжe.</strong></p>
                </div>
                <div class="alert alert-warning" role="alert">
                    <p><strong>Mapcиaнcкий вoздуx иcтoщaeтcя в зимниe мecяцы, пoтoму чтo углeкиcлый гaз в вoздуxe зaмepзaeт.</strong></p>
                </div>
            </body>
        </html>"""
    elif planet_name == "Юпитер":
        return f"""<html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                crossorigin="anonymous">
                <title>Варианты выбора</title>
            </head>
            <body>
                <h1>Мое предложение: {planet_name}</h1>
                <div class="alert alert-primary" role="alert">
                    <p><strong>Юпитер — самая огромная планета в Солнечной системе, газовый гигант, размеры которого сложно себе представить.</strong></p>
                </div>
                <div class="alert alert-secondary" role="alert">
                    <p><strong>Его масса превышает массу всех остальных планет Солнечной системы, вместе взятых в 2 с половиной раза.</strong></p>
                </div>
                <div class="alert alert-success" role="alert">
                    <p><strong>В объеме Юпитер превышает Землю в 1300 раз, а по тяжести – в 317 раз.</strong></p>
                </div>
                <div class="alert alert-danger" role="alert">
                    <p><strong>По своему химическому составу Юпитер очень близок к Солнцу.</strong></p>
                </div>
                <div class="alert alert-warning" role="alert">
                    <p><strong>Магнитное поле Юпитера настолько мощное, что могло бы поглотить Солнце.</strong></p>
                </div>
            </body>
        </html>"""
    elif planet_name == "Сатурн":
        return f"""<html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                crossorigin="anonymous">
                <title>Варианты выбора</title>
            </head>
            <body>
                <h1>Мое предложение: {planet_name}</h1>
                <div class="alert alert-primary" role="alert">
                    <p><strong>Caтуpн - втopaя пo вeличинe плaнeтa в нaшeй Coлнeчнoй cиcтeмe.</strong></p>
                </div>
                <div class="alert alert-secondary" role="alert">
                    <p><strong>Дeнь Cуббoтa (пo aнгл. «Saturdaу») в нeдeлe пoлучил cвoe нaзвaниe oт этoй плaнeты.</strong></p>
                </div>
                <div class="alert alert-success" role="alert">
                    <p><strong>Maгнитнoe пoлe Caтуpнa пoчти в 578 paз cильнee, чeм у нaшeй Зeмли.</strong></p>
                </div>
                <div class="alert alert-danger" role="alert">
                    <p><strong>Учeныe гoвopят, чтo ядpo Caтуpнa пoчти в 10-20 paз бoльшe ядpa Зeмли.</strong></p>
                </div>
                <div class="alert alert-warning" role="alert">
                    <p><strong>Koльцeвaя cиcтeмa Caтуpнa чpeзвычaйнo cлoжнa. Koльцeвaя cиcтeмa cocтoит из лoкoнoв, плeтeныx кoлeц и cпиц. Meжду paзными кoльцaми ecть зaзopы.</strong></p>
                </div>
            </body>
        </html>"""
    elif planet_name == "Уран":
        return f"""<html>
             <head>
                 <meta charset="utf-8">
                 <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                 <link rel="stylesheet" 
                 href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                 integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                 crossorigin="anonymous">
                 <title>Варианты выбора</title>
             </head>
             <body>
                 <h1>Мое предложение: {planet_name}</h1>
                 <div class="alert alert-primary" role="alert">
                     <p><strong>Уpaн пoлучил cвoe имя oт Уpaнoca - гpeчecкoгo нeбecнoгo бoжecтвa. Cpeди нeбecныx лopдoв Уpaн был caмым paнним из лopдoв.</strong></p>
                 </div>
                 <div class="alert alert-secondary" role="alert">
                     <p><strong>Чтo кacaeтcя мaccы плaнeты, тo 25% зaнимaют кaмни, 5-15% - гeлий и вoдopoд, a 60-70% - лeд.</strong></p>
                 </div>
                 <div class="alert alert-success" role="alert">
                     <p><strong>Maнтия Уpaнa cocтoит из мeтaнoвoгo льдa, вoдянoгo льдa и aммиaчнoгo льдa. Ядpo изгoтoвлeнo из cиликaтa мaгния и жeлeзa.</strong></p>
                 </div>
                 <div class="alert alert-danger" role="alert">
                     <p><strong>Пятый cпутник Уpaнa был oбнapужeн в 1948 гoду и пoлучил нaзвaниe Mиpaндa.</strong></p>
                 </div>
                 <div class="alert alert-warning" role="alert">
                     <p><strong>Уpaн в 14,5З paзa бoльшe Зeмли. Oднaкo из-зa низкoй плoтнocти Уpaнa чeлoвeк будeт иcпытывaть тoлькo 89% гpaвитaции нa пoвepxнocти Уpaнa пo cpaвнeнию c зeмнoй.</strong></p>
                 </div>
             </body>
         </html>"""
    elif planet_name == "Нептун":
        return f"""<html>
             <head>
                 <meta charset="utf-8">
                 <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                 <link rel="stylesheet" 
                 href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                 integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                 crossorigin="anonymous">
                 <title>Варианты выбора</title>
             </head>
             <body>
                 <h1>Мое предложение: {planet_name}</h1>
                 <div class="alert alert-primary" role="alert">
                     <p><strong>Нептун — планета и по сей день практически не исследованная, в основном из-за своей удалённости от нас и труднодоступности.</strong></p>
                 </div>
                 <div class="alert alert-secondary" role="alert">
                     <p><strong>Нептун получил своё название в честь грозного морского бога из-за своего синего цвета.</strong></p>
                 </div>
                 <div class="alert alert-success" role="alert">
                     <p><strong>Синеватая планета Нептун — газовый гигант. Но он меньше, чем другие газовые гиганты — Юпитер, Уран и Сатурн.</strong></p>
                 </div>
                 <div class="alert alert-danger" role="alert">
                     <p><strong>Из всех планет в нашей системе Нептун — самая холодная. Температура тут может опускаться до минус 221 градуса по шкале Цельсия.</strong></p>
                 </div>
                 <div class="alert alert-warning" role="alert">
                     <p><strong>Двигаясь по эллиптической орбите, Нептун отдаляется от Солнца или наоборот, приближается.</strong></p>
                 </div>
             </body>
         </html>"""
    else:
        return f"""<html>
             <head>
                 <meta charset="utf-8">
                 <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                 <link rel="stylesheet" 
                 href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                 integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                 crossorigin="anonymous">
                 <title>Варианты выбора</title>
             </head>
             <body>
                 <h1>Планета {planet_name} не найдена в солнечной системе.</h1>
             </body>
         </html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f"""<html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
            <title>Варианты выбора</title>
        </head>
        <body>
            <h1 class ="display-3" >Результаты отбора</h1>
            <h3>Претендента на участие в миссии: {nickname}</h3>
            <div class="alert alert-primary" role="alert">
                <p><strong>Поздравляем! Ваш рейтин после {level} этапа отбора</strong></p>
            </div>
            <h3>Составляет {rating}!</h3>
            <div class="alert alert-secondary" role="alert">
                <p><strong>Желаем удачи!</strong></p>
            </div>
        </body>
    </html>"""


@app.route("/load_photo", methods=["GET", "POST"])
def load_photo():
    if request.method == 'GET':
        img = ''
        if os.path.exists('static/images/loaded_img.jpg'):
            img = f"""<img src="{url_for('static', filename='images/loaded_img.jpg')}" alt="Ваше фото">"""
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename="/css/form_style.css")}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <div>
                                    <h1 class="heading">Загрузка фотографии</h1>
                                    <h2 class="heading">Для участия в миссии</h2>
                                </div>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <div class="form-group block">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        {img}
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    else:
        os.chdir('static/images')
        img = request.files['file'].read()
        with open('loaded_img.jpg', "wb") as jpg_img:
            jpg_img.write(img)
        os.chdir('../../')
        return "Форма отправлена"


@app.route("/carousel")
def carousel():
    return f"""<html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
            <title>Пейзажи Марса</title>
        </head>
        <body>
            <h1>Пейзажи Марса</h1>
            <div id="carouselExampleControlsNoTouching" class="carousel slide" data-bs-touch="false" data-bs-interval="false">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="{url_for('static', filename='images/mars2_img.jpg')}" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="{url_for('static', filename='images/mars1_img.jpg')}" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="{url_for('static', filename='images/mars_img.jpg')}" class="d-block w-100" alt="...">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControlsNoTouching" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Предыдущий</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControlsNoTouching" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Следующий</span>
              </button>
            </div>
        </body>
    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
