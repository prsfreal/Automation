import requests
import json as JS
from UTILITIES.APILogHandler import *



class Reqeusts():
    logger = LogGen.loggen()

    def getRequest(self, uri, params=None, **kwargs):
        request = requests.get(uri, params, **kwargs).json()
        response = JS.loads(JS.dumps(request))
        self.logger.info(f'REQUEST: {JS.dumps(request)}')
        self.logger.info(f'RESPONSE: {JS.dumps(response)}')
        return response

    def postRequest(self, uri, data=None, json=None, **kwargs):
        request = requests.post(uri, data, json, **kwargs).json()
        response = JS.loads(JS.dumps(request))
        self.logger.info(f'REQUEST: {JS.dumps(request)}')
        self.logger.info(f'RESPONSE: {JS.dumps(response)}')
        return response


