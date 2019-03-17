# -*- coding:utf-8 -*-
import requests
import Auth

base_url = 'http://127.0.0.1:8090/TotalControl/v1/'
user_passwd = 'sigma:F22DF82D'


class App:
    def __init__(self, url, token, devices):
        self.url = url
        self.token = token
        self.devices = devices

    # Support multi_devices
    def close_app(self, packagename):
        resp = ''
        if len(self.devices) == 1:
            url1 = self.url + 'devices/' + self.devices[0] + '/apps/' + packagename
            payload = {'state': 'inactive', **self.token}
            resp = requests.post(url1, data=payload)
        if len(self.devices) > 1:
            url1 = self.url + 'devices/' + self.devices[0] + '/apps/' + packagename
            payload = {'state': 'inactive', **self.token}
            resp = requests.post(url1, data=payload)
        return resp

    def get_foreground_app(self):
        payload = {'q': 'foreground_app', **self.token}
        url1 = self.url + 'devices/' + self.devices[0] + '/apps'
        resp = requests.get(url1, params=payload)
        return resp

    def get_install_apklist(self):
        payload = {'q': 'installed_apk_list', **self.token}
        url1 = self.url + 'devices/' + self.devices[0] + '/apps'
        resp = requests.get(url1, params=payload)
        return resp

    def get_activity(self):
        payload = {'q': 'activity', **self.token}
        url1 = self.url + 'devices/' + self.devices[0] + '/apps'
        resp = requests.get(url1, params=payload)
        return resp

    def restart_app(self, packagename):
        url1 = self.url + 'devices/' + self.devices[0] + '/apps/' + packagename
        payload = {'state': 'restart', **self.token}
        resp = requests.post(url1, data=payload)
        return resp

    # Support multi_devices
    def run_app(self, packagename):
        url1 = self.url + 'devices/' + self.devices[0] + '/apps/' + packagename
        payload = {'state': 'active', **self.token}
        resp = requests.post(url1, data=payload)
        return resp


if __name__ == '__main__':
    my_token = Auth.get_token(base_url, user_passwd)
    print(my_token)
    my_devices = Auth.get_devices(base_url, my_token)
    print(my_devices)
    cellphone = App(base_url, my_token, my_devices)
    a = cellphone.get_foreground_app()
    b = cellphone.run_app('com.oneplus.calculator')
    c = cellphone.get_activity()
    print(a.json())
    print(b.json())
    print(c.json())
