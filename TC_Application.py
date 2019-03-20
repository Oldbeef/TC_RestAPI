# -*- coding:utf-8 -*-
import requests


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
            resp = requests.post(url1, json=payload)
        if len(self.devices) > 1:
            url1 = self.url + 'devices/ids/apps/' + packagename
            payload = {'state': 'inactive', **self.token, 'ids': self.devices}
            resp = requests.post(url1, json=payload)
        return resp

    def get_foreground_app(self):
        url1 = self.url + 'devices/' + self.devices[0] + '/apps'
        payload = {'q': 'foreground_app', **self.token}
        resp = requests.get(url1, params=payload)
        return resp

    def get_install_apklist(self):
        url1 = self.url + 'devices/' + self.devices[0] + '/apps'
        payload = {'q': 'installed_apk_list', **self.token}
        resp = requests.get(url1, params=payload)
        return resp

    def get_activity(self):
        url1 = self.url + 'devices/' + self.devices[0] + '/apps'
        payload = {'q': 'activity', **self.token}
        resp = requests.get(url1, params=payload)
        return resp

    def restart_app(self, packagename):
        url1 = self.url + 'devices/' + self.devices[0] + '/apps/' + packagename
        payload = {'state': 'restart', **self.token}
        resp = requests.post(url1, json=payload)
        return resp

    # Support multi_devices
    def run_app(self, packagename):
        resp = ''
        if len(self.devices) == 1:
            url1 = self.url + 'devices/' + self.devices[0] + '/apps'
            payload = {'state': 'active', **self.token}
            resp = requests.post(url1, json=payload)
        if len(self.devices) > 1:
            url1 = self.url + 'devices/ids/apps/' + packagename
            payload = {'state': 'active', **self.token, 'ids': self.devices}
            resp = requests.post(url1, json=payload)
        return resp

    # Support multi_devices
    def install_app(self, file_path):
        resp = ''
        if len(self.devices) == 1:
            url1 = self.url + 'devices/' + self.devices[0] + '/apps'
            payload = {**self.token, 'file_name': file_path}
            resp = requests.post(url1, json=payload)
        if len(self.devices) > 1:
            url1 = self.url + 'devices/ids/apps'
            payload = {**self.token, 'ids': self.devices, 'file_name': file_path}
            resp = requests.post(url1, json=payload)
        return resp

    def uninstall_app(self, packagename):
        url1 = self.url + 'devices/' + self.devices[0] + '/apps/' + packagename
        payload = {**self.token}
        resp = requests.delete(url1, json=payload)
        return resp


class Color:
    def __init__(self, url, token, devices):
        self.url = url
        self.token = token
        self.devices = devices

    def get_pixel_color(self, x, y):
        url1 = self.url + 'devices/' + self.devices[0] + '/screen/colors'
        payload = {'q': 'color', **self.token, 'x': x, 'y': y}
        resp = requests.get(url1, params=payload)
        return resp

    def get_color_count(self, rect):
        url1 = self.url + 'devices/' + self.devices[0] + '/screen/colors'
        payload = {'q': 'count', **self.token, 'rect': rect}
        resp = requests.get(url1, params=payload)
        return resp

    def get_color_bits(self):
        url1 = self.url + 'devices/' + self.devices[0] + '/screen/colors'
        payload = {'q': 'bits', **self.token}
        resp = requests.get(url1, params=payload)
        return resp


class Image:
    def __init__(self, url, token, devices):
        self.url = url
        self.token = token
        self.devices = devices

    def screen_shot(self, imagetype, **kw):
        url1 = self.url + 'devices/' + self.devices[0] + '/screen/images'
        payload = {**self.token, 'type': imagetype, **kw}
        resp = requests.get(url1, params=payload)
        return resp
