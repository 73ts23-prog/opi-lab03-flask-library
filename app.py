from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    # debug=True: автоматичний перезапуск після змін у коді та детальні повідомлення про помилки.
    # Використовується лише під час розробки.
    app.run(debug=True)
