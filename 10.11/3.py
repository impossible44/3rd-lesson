import requests

try:
    response=requests.get('url', timeout=5)
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("Сервер загружен время вышло")
except requests.exceptions.HTTPError as e:
    print(f"Ошибка http: {e}")
except requests.exceptions.ConnectionError:
    print("Нет связи с сервером")
except requests.exceptions.RequestException as e:
    print(f"Непредвиденная ошибка {e}")
url= 'http:site.com/downloads/large_movie.mp4'
with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open('vidos.mp4', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)