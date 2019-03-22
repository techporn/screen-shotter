import requests


def test():
    url = "http://127.0.0.1:5042/capture"
    data = {
        "browser": "chrome",
        "width": 1200,
        "height": 500,
        "url": "https://qiita.com/Gen6/items/f1636be0fe479f42b3ee",
    }
    requests.post(url, data=data)


def get(id):
    url = "http://127.0.0.1:5042/img/{}".format(id)
    return requests.get(url)


test()