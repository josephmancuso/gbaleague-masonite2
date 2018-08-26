import requests
import os


class NexmoComponent:

    _text = ''

    def message(self, message):
        if not self._text:
            self._text += message
        else:
            self._text += ' ' + message
        return self

    def from_number(self, number):
        self._number = number
        return self

    def text(self):
        raise Exception('Method not implementwd')

    def fire_text(self):
        print(requests.post('https://rest.nexmo.com/sms/json', {
            'api_key': os.getenv('NEXMO_CLIENT'),
            'api_secret': os.getenv('NEXMO_SECRET'),
            'to': self._to,
            'from': '12013800445',
            'text': self._text
        }).text)
