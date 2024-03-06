import SparkApi

# 以下密钥信息从控制台获取
appid = "ee171657"  # 填写控制台中获取的 APPID 信息
api_secret = "YzIyYmIxY2M1N2FlMWI0YTM4NDc2NDhi"  # 填写控制台中获取的 APISecret 信息
api_key = "d3ca7820e887bdf50c2682fb86ec8874"  # 填写控制台中获取的 APIKey 信息

domain = "generalv3"  # v3版本
# 云端环境的服务地址
Spark_url = "ws://spark-api.xf-yun.com/v3.5/chat"  # v3环境的地址（"wss://spark-api.xf-yun.com/v3.1/chat）

text = []


# length = 0

def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text


def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length


def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text


def running(inputs):
    question = checklen(getText("user", inputs))
    # SparkApi.answer = ""
    # print("星火:", end="")
    SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
    res = SparkApi.answer
    return res


if __name__ == '__main__':
    answer = ""
    res = ""
    while True:
        inputs = input("\n" + "我：")
        tempt = answer
        answer = running(inputs)
        res = answer[len(tempt):]
        print("回答：", res)