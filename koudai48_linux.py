import json
import configparser
import os
import time
import setting
import color_linux
import requests
import urllib3
import time, datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
localtime = time.localtime(time.time())
img_start="https://source.48.cn"
live_start = "https://h5.48.cn/"+str(localtime.tm_year)+"appshare/memberLiveShare/index.html?id="
mention= r"""
执行成功已返回上一级,请重新选择功能或者输入exit退出.功能提示:
                    #口袋48
        1.查看成员ID                    7.根据ID查询用户信息
        2.查看首推成员发言      8.登陆
        3.查看首推留言版信息    9.获取直播列表
        4.查看首推房间信息      10.每日签到
        5.查看个人房间列表   11.关注/取关小偶像
        6.获取好友ID        12.关注/取关聚聚
    """

banner = r"""
super
      ___         ___   __             ___         ___   __           _______        ___        ___        ___
     / _ \       / //  /  \           / _ \       / //  /  \         //-----//      / //       / //       / //
    / //\ \     / //  / /\ \         / //\ \     / //  / /\ \       ///            / //_______/ //       / //
   / //  \ \   / //  / //_\ \       / //  \ \   / //  / //_\ \      \\\____       / //_______/ //       / //
  / //    \ \ / //  / /____\ \     / //    \ \ / //  / /____\ \      \-----/|    / //-------/ //       / //
 / //      \ / //  / /------\_\   / //      \ / //  / /------\_\     _____/ /   /_//       /_//       /_//
|_|/        \_//  |_|/       |_| |_|/        \_//  |_|/       |_|   |_____|/   |_|/       |_|/       |_|/
                                                                                                            by:Zhu013
                                                                                                            

    #口袋功能列表
    # 一.搜索成员ID信息(无需登陆,可进一步关注)
    # 二.查看首推成员发言(25条)
    # 三.查看首推留言版信息（25条）
    # 四.查看首推房间信息
    # 五.查看个人房间列表(可进一步查看主人发言)
    # 六.获取好友ID(包括成员)
    # 七.根据ID查询用户信息
    # 八.登陆
    # 九.获取直播列表
    # 十.每日签到
    # 十一.关注/取关小偶像
    #十二.关注/取关聚聚

    #48商城功能列表
    # 十一.切票(画饼未开放)

    #使用方法
    #口袋:
    # 一.使用1查询成员id和房间号
    # 一.设置setting.conf文件内的user和password以及首推偶像的name,group,id和房间号
    # 二.第一次使用请选择8登陆,token未过期可不用反复登陆。
    # 
    

    #温馨提示
    #每一次查询请间隔5s,否则可能会封。
"""

box = r"""||||||||||||||||||||||||||SuperNanashi*冯薪朵0124生日快乐||||||||||||||||||||||||||||
"""

#搜索成员ID号
def searchmember(membername):
    url = "https://pocketapi.48.cn/im/api/v1/im/search"
    form = {
        'name': membername
    }
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
    try:
        response = requests.post(
            url,
            data=json.dumps(form),
            headers=header,
            verify=False,
            timeout=15).json()
        return response
    except Exception as e:
        raise e


#快捷查看首推发言
def getMainpage():
        roomId, ownerId = setting.roomId()
        url = "https://pocketapi.48.cn/im/api/v1/chatroom/msg/list/homeowner"
        form = {
            'ownerId': int(ownerId),
            'roomId': int(roomId)
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
            'token': setting.token()
        }
        try:
            response = requests.post(
                url,
                data=json.dumps(form),
                headers=header,
                verify=False,
                timeout=15).json()
            return response
        except Exception as e:
            raise e

#查询房间发言
def getownermsg(ownerid,roomid):
        
        url = "https://pocketapi.48.cn/im/api/v1/chatroom/msg/list/homeowner"
        form = {
            'ownerId': int(ownerid),
            'roomId': int(roomid)
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
            'token': setting.token()
        }
        try:
            response = requests.post(
                url,
                data=json.dumps(form),
                headers=header,
                verify=False,
                timeout=15).json()
            return response
        except Exception as e:
            raise e
 #查看留言版信息
def getVisitpage():
        roomId, ownerId = setting.roomId()
        url = "https://pocketapi.48.cn/im/api/v1/chatroom/msg/list/all"
        form = {
            'ownerId': int(ownerId),
            'roomId': int(roomId)
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
            'token': setting.token()
        }
        try:
            response = requests.post(
                url,
                data=json.dumps(form),
                headers=header,
                verify=False,
                timeout=15).json()
            return response
        except Exception as e:
            raise e


#查看房间信息
def getroomlist():
        roomId, ownerId = setting.roomId()
        url = "https://pocketapi.48.cn/im/api/v1/conversation/page"
        form = {
            'ownerId': int(ownerId),
            'roomId': int(roomId)
            #'targetType':0
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
            'token': setting.token()
        }
        try:
            response = requests.post(
                url,
                data=json.dumps(form),
                headers=header,
                verify=False,
                timeout=15).json()
            return response
        except Exception as e:
            raise e


#查看个人房间列表
def getroominfo():
        roomId, ownerId = setting.roomId()
        url = "https://pocketapi.48.cn/im/api/v1/im/room/info"
        form = {
            'ownerId': int(ownerId),
            'roomId': int(roomId),
            'targetType':0
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
            'token': setting.token()
        }
        try:
            response = requests.post(
                url,
                data=json.dumps(form),
                headers=header,
                verify=False,
                timeout=15).json()
            return response
        except Exception as e:
            raise e           


#获取好友ID
def getfriendsid():
        #roomId, ownerId = setting.roomId()
        url = "https://pocketapi.48.cn/user/api/v1/friendships/friends/id"
        form = {
            #'needMuteInfo': 0,
            #'userid':'627751'
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
            'token': setting.token()
        }
        try:
            response = requests.post(
                url,
                data=json.dumps(form),
                headers=header,
                verify=False,
                timeout=15).json()
            return response
        except Exception as e:
            raise e          


#根据ID获取用户信息
def getuserinfo(id):
        #roomId, ownerId = setting.roomId()
        url = "https://pocketapi.48.cn/user/api/v1/user/info/home/small"
        form = {
            'needMuteInfo': 0,
            'userId':id
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
            'token': setting.token()
        }
        try:
            response = requests.post(
                url,
                data=json.dumps(form),
                headers=header,
                verify=False,
                timeout=15).json()
            return response
        except Exception as e:
            raise e   
#获取直播详情
def livedetail(liveId):
        '''
        获取直播详情
        :param liveId: 直播编号 int
        :return: playStreamPath string, response
        '''
        url = "https://pocketapi.48.cn/live/api/v1/live/getLiveOne"
        form = {
            "liveId": str(liveId)
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
            'token': setting.token()
        }
        try:
            response = requests.post(
                url,
                json=form,
                headers=header,
                timeout=15).json()
            if response['status'] == 200:
                playStreamPath = response['content']['playStreamPath']
                return playStreamPath
        except Exception as e:
            raise e     

#获取直播列表
def getlivelist():
        #roomId, ownerId = setting.roomId()
        url = "https://pocketapi.48.cn/live/api/v1/live/getLiveList"
        form = {
            'groupId':0,
            'debug': 'true',
            'next': 0,
            'record': 'false'
            #'needMuteInfo': 0,
            #'userid':'627751'
        }
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
        try:
            response = requests.post(
                url,
                data=json.dumps(form),
                headers=header,
                verify=False,
                timeout=15).json()
            return response
        except Exception as e:
            raise e  
#每日签到
def checkin():
        #roomId, ownerId = setting.roomId()
        url = "https://pocketapi.48.cn/user/api/v1/checkin"
        form={

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
            'token':setting.token()
        }
        try:
            response = requests.post(
                url,
                data=json.dumps(form),
                headers=header,
                verify=False,
                timeout=15).json()
            return response
        except Exception as e:
            raise e          



#登陆获取cookie       
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
#时间戳转化为日期
def timeStamp(timeNum):
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)

#鸡腿翻牌详情处理
def answerdetails(questionId,answerId):
        #roomId, ownerId = setting.roomId()
        url = "https://pocketapi.48.cn/idolanswer/api/idolanswer/v1/question_answer/detail"
        form={
            'questionId':questionId,
            'answerId':answerId#,
            #'roomId':'67370575'
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
            'token':setting.token()
        }
        try:
            response = requests.post(
                url,
                data=json.dumps(form),
                headers=header,
                verify=False,
                timeout=30).json()
            return response
        except Exception as e:
            raise e          
#idol房间信息处理
def printAllidol(reAll):
    length = len((reAll['content']['message']))
    if(length<26):
        num = length
    else:
        num = 26
    for i in range(0,num):
        re1=reAll['content']['message'][num-1-i]
        #re1 = re1.sort(key = lambda x:x["msgTime"])
        #print(re1['bodys'])
        if(re1['msgType']=='TEXT'):
            re2 = json.loads(re1['extInfo'])
            if(re2['messageType'] == 'LIVEPUSH'):
                color_linux.printBlue(box)
                print("-----------------直播---------------")
                timeStamp((re1['msgTime']))
                print("小偶像直播啦！")
                print("直播标题:"+re2['liveTitle'])
                print("直播封面:"+img_start+re2['liveCover'])
                print("直播地址:"+live_start+re2['liveId'])
                try:
                    print("推流地址:"+livedetail(re2['liveId']))
                except:
                    print("获取推流地址失败，直播可能已被删除。请使用浪客查找。")
                print("----------------—END——--------------")
            elif(re2['messageType'] == 'REPLY'):
                color_linux.printGreen(box)
                print("--------------普通翻牌---------------")
                timeStamp((re1['msgTime']))
                print("小偶像普通翻牌啦！")
                print("粉丝："+re2['replyName'])
                print("提问:"+(re2['replyText']))
                print(re2['user']['nickName']+"回答:"+re2['text'])
                print("----------------—END——--------------")

            elif(re2['messageType'] == 'FLIPCARD'):
                color_linux.printYellow(box)
                print("--------------鸡腿翻牌---------------")
                timeStamp((re1['msgTime']))
                print("小偶像鸡腿翻牌啦！")
                #print(re2['questionId'])
                re3 = answerdetails(re2['questionId'],re2['answerId'])['content']
                print("粉丝："+re3['userName'])
                print("提问:"+re3['question'])
                print("偶像回答:"+re2['answer'])
                #time.sleep(2)
                print("----------------—END——--------------")

            elif(re2['messageType'] == 'SHARE_POSTS'):
                color_linux.printPurple(box)
                print("----------------—帖子——--------------")
                timeStamp((re1['msgTime']))
                print(re2['user']['nickName']+"分享帖子！")
                print("分享标题:"+re2['shareDesc'])
                print("预览图片:"+img_start+re2['sharePic'])
                print("----------------—END——--------------")
            else:
                color_linux.printSkyBlue(box)
                print("----------------—信息——--------------")
                timeStamp((re1['msgTime']))
                print("用户名:"+re2['user']['nickName'])
                print("用户ID号:")
                print(re2['user']['userId'])
                print("用户发送内容:")
                print(re1['bodys'])
                #print("用户使用型号")
                #print(re2['config']['phoneName'])
                print("----------------—END——--------------")

        elif(re1['msgType']=='VIDEO'):
            re2 = json.loads(re1['bodys'])
            timeStamp((re1['msgTime']))
            color_linux.printRed(box)
            print("----------------—视频——--------------")
            print("小偶像分享视频啦！")
            print("视频链接:")
            print(re2['url'])
            print("----------------—END——--------------")

        elif(re1['msgType']=='IMAGE'):
            re2 = json.loads(re1['bodys'])
            color_linux.printPurple(box)
            print("----------------—图片——--------------")
            timeStamp((re1['msgTime']))
            print("小偶像分享图片啦！")
            print("图片链接:")
            print(re2['url'])
            print("----------------—END——--------------")

#留言板粉丝信息(包括手机型号)
def printAllifans(reAll):
    for i in range(0,26):
        re1=reAll['content']['message'][25-i]
        #print(re1['bodys'])
        if(re1['msgType']=='TEXT'):
            re2 = json.loads(re1['extInfo'])
            if(re2['messageType'] == 'LIVEPUSH'):
                color_linux.printRed(box)
                timeStamp((re1['msgTime']))
                print("小偶像直播啦！")
                print("直播标题:"+re2['liveTitle'])
                print("直播封面:"+img_start+re2['liveCover'])
                print("直播地址:"+live_start+re2['liveId'])
                
            elif(re2['messageType'] == 'SHARE_POSTS'):
                print("----------------—帖子——--------------")
                color_linux.printPurple(box)
                timeStamp((re1['msgTime']))
                print(re2['user']['nickName']+"分享帖子！")
                print("分享标题:"+re2['shareDesc'])
                print("预览图片:"+img_start+re2['sharePic'])
                print("----------------—END——--------------")
            else:
                print("----------------—信息——--------------")
                color_linux.printYellow(box)
                timeStamp((re1['msgTime']))
                print("用户名:"+re2['user']['nickName'])
                print("用户ID号:")
                print(re2['user']['userId'])
                print("用户发送内容:")
                print(re1['bodys'])
                print("用户使用型号")
                print(re2['config']['phoneName'])
                print("----------------—END——--------------")

        elif(re1['msgType']=='VIDEO'):
            color_linux.printGreen(box)
            print("----------------—视频——--------------")
            re2 = json.loads(re1['bodys'])
            timeStamp((re1['msgTime']))
            print("------------视频------------")
            print("小偶像分享视频啦！")
            print("视频链接:")
            print(re2['url'])
            print("----------------—END——--------------")

        elif(re1['msgType']=='IMAGE'):
            color_linux.printBlue(box)
            re2 = json.loads(re1['bodys'])
            print("----------------—图片——--------------")
            timeStamp((re1['msgTime']))
            print("小偶像分享图片啦！")
            print("图片链接:")
            print(re2['url'])
            print("----------------—END——--------------")


#获取关注好友ID(包括粉丝,偶像)
def printfriendsID(refriendsid):
    re = refriendsid['content']['data']
    print(re)

#ID查询处理
def printidinfo(reuserinfo):
    re = reuserinfo['content']['userInfo']
    if(re['userRole'] == 1):
        print("粉丝用户")
    elif(re['userRole'] == 3):
        print("小偶像")
    elif(re['userRole'] == 999):
        print("袋王")
    print("用户名:"+re['nickname'])
    print("用户头像:"+img_start+re['avatar'])
    print("用户等级:"+str(re['level']))
    print("偶像身份:"+str((re['isStar'])))
    print("VIP:"+str(re['vip']))

def fdremove(id):
        url = "https://pocketapi.48.cn/user/api/v1/friendships/friends/remove"
        form={
            'toUserId':id
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
            'token':setting.token()
        }
        try:
            response = requests.post(
                url,
                data=json.dumps(form),
                headers=header,
                verify=False,
                timeout=30).json()
            return response
        except Exception as e:
            raise e       

def fdadd(id):
        url = "https://pocketapi.48.cn/user/api/v1/friendships/friends/add"
        form={
            'toUserId':id
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
            'token':setting.token()
        }
        try:
            response = requests.post(
                url,
                data=json.dumps(form),
                headers=header,
                verify=False,
                timeout=30).json()
            return response
        except Exception as e:
            raise e       

def main(option):

    if(option == 1):
        #搜索成员ID号
        while(1):
            try:
                name = input('请输入成员姓名:')
                if(name == 'back'):
                    break
                mes = searchmember(name)
                print("房间号:"+mes['content']['data'][0]['targetId'])
                print("ID:"+mes['content']['data'][0]['ownerId'])
                print("查询成功,输入姓名继续查询或者输入back返回上一级")
            except:
                print("输入错误!请重新输入！或者输入back返回上一级")

        print(mention)
    elif(option == 2):
        #查看房间主人发言
        print("choose 2")
        reOwner=getMainpage()
        printAllidol(reOwner)
        print(mention)
    elif(option == 3):
        #查看留言版信息
        print("choose 3 ")
        reAll = getVisitpage()
        printAllifans(reAll)
        print(mention)
    elif(option == 4):
        #查看首推房间信息
        print("查看首推房间信息 ")
        re1 = getroominfo()['content']['roomInfo']
        print("房间创建时间:")
        #print(re1['ctime'])
        timeStamp(int(re1['ctime']))
        print("房间标题:"+re1['roomTopic'])
        print("房间主人:"+re1['ownerName'])
        print("房间背景图:"+img_start+re1['bgImg'])
        #print("信息还未处理,测试中")
        print(mention)
    elif(option == 5):
        #查看个人关注的房间列表
        ownerid = ''
        roomid = ''
        print("choose 5 查看个人关注的房间列表")
        #print(getroomlist()['content']['conversations'])
        num = len(getroomlist()['content']['conversations'])
        print(num)
        while(1):
            try:
                for i in range(0,num):
                    re1 = getroomlist()['content']['conversations'][i]
                    color_linux.printGreen(box)
                    print("------------------房间-----------------")
                    print("房间"+str(i)+"号")
                    print("创建时间:")
                    timeStamp(int(re1['msgTime']))
                    print("房间主人:"+re1['ownerName'])
                    print("主人ID:"+str(re1['ownerId']))
                    print("房间ID:"+str(re1['targetId']))
                    print("------------------End-----------------")
                choose = input("输入房间号获取房间主人发送的信息，或者back返回")
                if(choose == 'back'):
                    break
                print(getroomlist()['content']['conversations'][int(choose)]['ownerId'])
                ownerid = getroomlist()['content']['conversations'][int(choose)]['ownerId']
                roomid = getroomlist()['content']['conversations'][int(choose)]['targetId']
                reOwner=getownermsg(ownerid,roomid)
                #print(reOwner)
                printAllidol(reOwner)
            except:
                print("获取主人房间信息出现错误,请反馈")
                break
        #print("信息还未处理,测试中")
        print(mention)

    elif(option == 6):
        #获取好友ID
        print("choose 6")
        refriendsid = getfriendsid() 
        printfriendsID(refriendsid)
        print(mention)
    elif(option == 7):
        #根据ID获取用户信息
        print("请输入要查询的ID,或者back返回上一级")
        id = ''
        while(1):
            try:
                id = input()
                if(id == 'back'):
                    break
                reuserinfo = getuserinfo(int(id))
                printidinfo(reuserinfo)
                print("查询成功,继续输入ID查询或者输入back返回上一级")
            except:
                print("ID错误!请重新输入!")
        print(mention)
    elif(option == 8):
        #登陆
        print(getNewToken())
        print(mention)
    elif(option == 9):
        #获取直播列表
        print("获取正在直播列表")
        num = len(getlivelist()['content']['liveList'])
        #print(num)
        for i in range(0,num):
            re1 = getlivelist()['content']['liveList'][i]
            color_linux.printPurple(box)
            print("_____________直播"+str(i)+"号___________")
            print("开始直播时间:")
            timeStamp(int(re1['ctime']))
            print("直播标题:"+re1['title'])
            print("小偶像:"+re1['userInfo']['nickname'])
            print("直播链接:"+live_start+str(re1['liveId']))
            print("直播流:"+livedetail(re1['liveId']))
            print("_____________END"+str(i)+"号___________")
        #re = getlivelist()
        #print(re)
        print(mention)
    elif(option == 10):
        #每日签到
        print("每日签到")
        re = checkin()
        print(re['message'])
        print(mention)
        #{'status': 200, 'success': True, 'message': 'OK', 'content': {'addExp': 1, 'addSupport': 1, 'addMoney': 0, 'days': 1}}
    elif(option == 11):
         #关注小偶像
        while(1):
            try:
                name = input('请输入要关注/取关的小偶像名字，或者back返回上一级:')
                if(name == 'back'):
                    break
                mes = searchmember(name)
                ID = mes['content']['data'][0]['ownerId']
                while(1):
                    choose = input('关注输入1，取关输入0:')
                    num = int(choose)
                    if(num==1):
                        print("关注:")
                        print(fdadd(int(ID))['success'])
                        break
                    if(num==0):
                        print("取关:")
                        print(fdremove(int(ID))['success'])
                        break
                    else:
                        print("输入错误，请重新输入")

            except:
                print("输入错误!请重新输入！或者输入back返回上一级")
        print(mention)
    elif(option == 12):
         #关注小偶像
        while(1):
            try:
                name = input('请输入要关注/取关的粉丝ID，或者back返回上一级:')
                if(name == 'back'):
                    break
                ID = int(name)
                while(1):
                    choose = int(input('关注输入1，取关输入0:'))
                    num = ID
                    if(choose==1):
                        print("关注:")
                        print(fdadd(int(ID))['success'])
                        break
                    if(choose==0):
                        print("取关:")
                        print(fdremove(int(ID))['success'])
                        break
                    else:
                        print("输入错误，请重新输入")

            except:
                print("输入错误!请重新输入！或者输入back返回上一级")
        print(mention)
    else:
        print("您输入的数字已经不范围内")
        pass

if __name__ == '__main__':
    color_linux.printGreen(banner)
    option = ''
    print("请输入相应功能对应的阿拉伯数字或者exit退出")
    while(1):
        try:
            option = input()
            if(option == 'exit'):
                break

            main(int(option))
        except:
            print("输入错误！自动退出！")
            break
    print("退出成功")