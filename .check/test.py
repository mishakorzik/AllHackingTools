from requests import get, post

def generate_proxy():
    proxy = get("https://raw.githubusercontent.com/mishakorzik/mishakorzik.menu.io/master/%D0%A1%D0%B5%D1%80%D0%B2%D0%B5%D1%80/ProxyList.txt").text
    return {"http": proxy, "https": proxy}
