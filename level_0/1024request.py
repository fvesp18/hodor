#!/usr/bin/python3
if __name__ == "__main__":
    import requests

    API_EP = "http://158.69.76.135/level0.php"

    data = {"id":"1081",
            "holdthedoor":"Submit"}

    for i in range(0, 1023):
        r = requests.post(url = API_EP, data = data)
