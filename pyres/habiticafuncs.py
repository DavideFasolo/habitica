from json import loads, dumps
from requests import get, put
from pyres.environment import userdata_url, headers, user_url


def responseok(resp):
    return not(resp-200)


def getuserdata():
    try:
        response = get(userdata_url, headers=headers)
        if responseok(response.status_code):
            return loads(response.text)
        else:
            return loads("{}")
    except:
        return loads("{}")


def setuserdata(data):
    try:
        response = put(user_url, headers=headers, data=dumps(data))
        if responseok(response.status_code):
            return True
        else:
            return False
    except:
        return False


def setmoney(gp):
    data = {"stats.gp": gp}
    setuserdata(data)


def getmoney():
    return getuserdata()["stats"]["gp"]
