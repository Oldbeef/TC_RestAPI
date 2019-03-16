# -*- coding:utf-8 -*-
import requests
import Auth

base_url = 'http://127.0.0.1:8090/TotalControl/v1/'
user_passwd = 'sigma:F22DF82D'
package_name = 'com.tencent.tmgp.pubgmhd'


class App:
    def __init__(self, url, token, devices):
        self.url = url
        self.token = token
        self.devices = devices

    def close_app(self, packagename):
        url1 = self.url + 'devices/' + self.devices[0] + '/apps/' + packagename
        payload = {'state': 'inactive', **self.token}
        resp = requests.post(url1, data=payload)
        return resp


if __name__ == '__main__':
    my_token = Auth.get_token(base_url, user_passwd)
    print(my_token)
    my_devices = Auth.get_devices(base_url, my_token)
    print(my_devices)
    cellphone = App(base_url, my_token, my_devices)
    cellphone.close_app(package_name)
