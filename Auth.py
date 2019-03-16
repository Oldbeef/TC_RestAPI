# -*- coding:utf-8 -*-
# Author:wyj

import base64
import requests

base_url = 'http://127.0.0.1:8090/TotalControl/v1/'
user_passwd = 'sigma:F22DF82D'


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


if __name__ == '__main__':
    a = get_token(base_url, user_passwd)
    print(a)
    b = get_devices(base_url, a)
    print(b)
