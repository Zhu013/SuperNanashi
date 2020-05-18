import random
import configparser
import os
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def idol_name():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    # with open(file_path, 'r') as cfgfile:
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        # idol name
        idol_name = cf.get('idol', 'name')
    return str(idol_name)

    # 口袋48:roomId
def roomId():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    # with open(file_path, 'r') as cfgfile:
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        roomId = cf.get('koudai48', 'roomId')
        ownerId = cf.get('koudai48', 'ownerId')
    return int(roomId), int(ownerId)


# 获取配置中存储的口袋房间消息时间
def read_kdmsg_time13():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        msgtime = cf.get('koudai48', 'msgTime')
    return int(msgtime)


# 写入配置中存储的口袋房间消息时间
def write_kdmsg_time13(msgtime13):
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        with open(file_path, 'w+', encoding='utf-8') as cfgfile2:
            cf.set('koudai48', 'msgTime', str(msgtime13))
            cf.write(cfgfile2)


# 获取配置中存储的token
def token():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    # with open(file_path, 'r') as cfgfile:
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        # koudai48
        # user = cf.get('koudai48', 'user')
        # password = cf.get('koudai48', 'password')
        token = cf.get('koudai48', 'token')
    return str(token)


# 验证token
def token_verify():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    # with open(file_path, 'r') as cfgfile:
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        # koudai48
        # user = cf.get('koudai48', 'user')
        # password = cf.get('koudai48', 'password')
        token = cf.get('koudai48', 'token')
    url = 'https://pocketapi.48.cn/user/api/v1/user/info/home'
    form = {
        "userId": 1
    }
    header = {
        'Host': 'pocketapi.48.cn',
        'accept': '*/*',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'User-Agent': 'PocketFans201807/6.0.0 (iPhone; iOS 12.2; Scale/2.00)',
        'Accept-Encoding': 'gzip, deflate',
        'appInfo': '{"vendor":"apple","deviceId":"0","appVersion":"6.0.0","appBuild":"190409","osVersion":"12.2.0","osType":"ios","deviceName":"iphone","os":"ios"}',
        'Content-Type': 'application/json;charset=utf-8',
        'Connection': 'keep-alive',
        'token': token
    }
    response = requests.post(
            url,
            data=json.dumps(form),
            headers=header,
            verify=False,
            timeout=15).json()
    if response['status'] == 200:
        return True
    else:
        return False


# 获取新token
def getNewToken():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    # with open(file_path, 'r') as cfgfile:
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        # koudai48
        user = cf.get('koudai48', 'user')
        password = cf.get('koudai48', 'password')
        # token = cf.get('koudai48', 'token')
        # request
        ajax_url = "https://pocketapi.48.cn/user/api/v1/login/app/mobile"
        header = {
            'Host': 'pocketapi.48.cn',
            'accept': '*/*',
            'Accept-Language': 'zh-Hans-CN;q=1',
            'User-Agent': 'PocketFans201807/6.0.0 (iPhone; iOS 12.2; Scale/2.00)',
            'Accept-Encoding': 'gzip, deflate',
            'appInfo': '{"vendor":"apple","deviceId":"0","appVersion":"6.0.0","appBuild":"190409","osVersion":"12.2.0","osType":"ios","deviceName":"iphone","os":"ios"}',
            'Content-Type': 'application/json;charset=utf-8',
            'Connection': 'keep-alive'
        }
        form = {
            "mobile": user,
            "pwd": password
        }
        response = requests.post(
            ajax_url,
            data=json.dumps(form),
            headers=header,
            verify=False
        ).json()
        if response['status'] == 200:
            newToken = response['content']['token']
            cf.set('koudai48', 'token', newToken)
            with open(file_path, 'w+', encoding='utf-8') as cfgfile2:
                cf.write(cfgfile2)
            return 'success'
        else:
            return response['message']
