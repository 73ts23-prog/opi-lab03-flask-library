"""Навчальна бібліотека «Читай»: маршрути та статична добірка книжок."""

from flask import Flask, render_template

app = Flask(__name__)

BOOKS = [
    {'title': 'Кобзар', 'author': 'Тарас Шевченко', 'genre': 'Поезія', 'color': 'clay'},
    {'title': 'Лісова пісня', 'author': 'Леся Українка', 'genre': 'Драма-феєрія', 'color': 'forest'},
    {'title': 'Захар Беркут', 'author': 'Іван Франко', 'genre': 'Історична повість', 'color': 'ochre'},
    {'title': 'Тіні забутих предків', 'author': 'Михайло Коцюбинський', 'genre': 'Повість', 'color': 'forest'},
    {'title': 'Кайдашева сім’я', 'author': 'Іван Нечуй-Левицький', 'genre': 'Повість', 'color': 'ochre'},
    {'title': 'Місто', 'author': 'Валер’ян Підмогильний', 'genre': 'Роман', 'color': 'clay'},
]


@app.route('/')
def home():
    """Показує вступ до бібліотеки та перші три книжки."""
    return render_template('home.html', books=BOOKS[:3])


@app.route('/about')
def about():
    """Пояснює ідею та навчальне призначення проєкту."""
    return render_template('about.html')


@app.route('/catalog')
def catalog():
    """Показує статичну добірку із шести творів."""
    return render_template('catalog.html', books=BOOKS)


@app.route('/contacts')
def contacts():
    """Показує автора та посилання на GitHub."""
    return render_template('contacts.html')


@app.errorhandler(404)
def page_not_found(error):
    """Повертає оформлену сторінку зі статусом 404."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    # Локальний навчальний сервер без увімкненого налагоджувача.
    app.run(host='127.0.0.1', port=5000, debug=False)
