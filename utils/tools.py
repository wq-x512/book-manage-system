import base64
import hashlib
import uuid
import arrow

def Pic_to_Base64(path):
    try:
        with open(path, 'rb') as f:
            content = f.read()
            img = base64.b64encode(content)
        return bytes(img)
    except:
        return None


def Base64_to_Pic(path, string):
    try:
        with open(path, 'wb') as f:
            f.write(base64.b64decode(string))
    except:
        return None


def generate_u_uid():
    return uuid.uuid4().hex


def encrypted(plain):
    try:
        cipher = hashlib.sha256(plain.encode('utf-8')).hexdigest()
        return cipher
    except:
        return None


def get_time():
    return arrow.now().shift().format("MM-DD HH:mm:ss")


def diff_time():
    # YYYY-MM-DD HH:mm:ssZZ
    # years, months, days, hours, minutes, seconds, microseconds, weeks, quarters, weekday
    return arrow.now().shift(hours=-12).format("MM-DD HH:mm:ss")


def convertBook(respond, additional):
    res = []
    idx = {}
    for i in range(len(list(respond))):
        res.append(list(respond[i]))
        idx[f'{respond[i][1]}'] = i
    for item in additional:
        if item[0] in idx.keys():
            res[idx[item[0]]][6] += int(item[1])
    return res


def convertRecord(respond):
    res = []
    for item in respond:
        a = []
        for i in range(len(item)):
            if i == 3:
                a.append('借书' if int(item[i]) == -1 else '还书')
            elif i == 2 and item[i] == '':
                a.append('已删除')
            else:
                a.append(item[i])
        res.append(a)
    return res


def convertUser(respond):
    res = []
    for item in respond:
        a = []
        for i in range(len(item)):
            if i == 2:
                a.append('管理员' if item[i] == '1' else '用户')
            elif i == 3:
                a.append('在线' if item[i] == 1 else '离线')
            else:
                a.append(item[i])
        res.append(a)
    return sorted(res,reverse=True,key=lambda x: x[2])
