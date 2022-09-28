import requests


class ApiFetcher:
    def __init__(self):
        self.api = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

    def get_word_data(self, word:str) -> list:
        try:
            return requests.get(f'{self.api}{word}').json()[0]
        except Exception:
            return {
                'error': 'No such word found'
            }
