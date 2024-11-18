from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    context: dict[str, str] = {'home_active': 'active',
                               'home_link': '/',
                               'about_link': '/about/'}
    return render_template('home.html', **context)


@app.route('/about/')
def about() -> str:
    context: dict[str, str] = {'about_active': 'active',
                               'home_link': '/',
                               'about_link': '/about/'}
    return render_template('about.html', **context)


if __name__ == '__main__':
    app.run()