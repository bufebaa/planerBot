from flask import Flask, request, redirect
from urllib.parse import parse_qs, urlparse

app = Flask(__name__)
app.secret_key = b'fk1_s*dfz2^o3p\a*'


@app.route('/')
def home():
    return 'HELLO'


@app.route('/oauth2callback')
def oauth2callback():
    parsed_url = urlparse(request.url)
    code = parse_qs(parsed_url.query)['code'][0]
    return redirect(location=f'https://t.me/superplanerbot?start={code}')


if __name__ == '__main__':
    app.run('localhost', debug=True)
