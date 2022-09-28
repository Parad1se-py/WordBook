from flask import Flask, request

from py_utils import *


app = Flask('WordBook API Helper')
api_fetcher = ApiFetcher()

@app.route('/', methods = ['GET', 'POST'])
def home():
    word = request.args.get('word', default = None, type = str)

    return api_fetcher.get_word_data(word)

if __name__ == '__main__':
    app.run(port=2222)
