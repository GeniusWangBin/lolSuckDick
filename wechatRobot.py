import itchat
import requests
import re

#获取消息
def getHtmlText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

@itchat.msg_register(['Text','Map','Card','Note','Sharing','Picture'])

def text_reply(msg):
    if not msg['FromUserName'] == Name["天才Tuang"]:
        url = "http://www.tuling123.com/openapi/api?key=87f4c0f17b2345febf740b9048c14b34&info="
        url = url + msg['Text']
        html = getHtmlText(utl)
        message = re.findall(r'\"text\"\:\".*?\"',html)
        reply = eval(message[0].split(':')[1])
        return reply
    
if __name__=='__main__':
    itchat.auto_login()
    friends = itchat.get_friends(update=True)[0:]
    #名称
    Name  = {}
    #用户名
    Nic = []
    #好友用户名
    Uesr = []
    for i in range(len(friends)):
        Nic.append(friends[i]["NickName"])
        User.append(friends[i]["UserName"])
    for i in range(len(friends)):
        Name[Nic[i]] = User[i]
        itchat.run()
