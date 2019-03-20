# -*- coding:utf-8 -*-
# Author:wyj

import base64
import requests


def get_token(url, user_password):
    byte1 = user_password.encode('utf-8')
    str2 = base64.b64encode(byte1).decode('utf-8')
    header = {'Authorization': str2}
    url1 = url + 'login'
    resp = requests.get(url1, headers=header)
    return resp.json()['value']


def get_devices(url, token):
    url1 = url + 'devices'
    payload = {'q': 'all', **token}
    resp = requests.get(url1, params=payload)
    return resp.json()['ids']
