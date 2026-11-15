import requests
import os

#ЭТАП 1. РАЗВЕДКА

print("\nЭТАП 1. РАЗВЕДКА")

name = input("Введите имя цели: ").strip()
journal_number = input("Введите ваш номер по журналу: ").strip()

age = None
gender =None
gender_probability = None

#Получение возраста
try:
    response = requests.get(
        "https://api.agify.io",
        params={"name": name},
        timeout=5
    )

    response.raise_for_status()
    age_data= response.json()
    age = age_data.get("age")

    print(f"Получен предполагаемый возраст: {age}")

except requests.exceptions.Timeout:
    print("Превышено время ожидания при получении возраста.")

except requests.exceptions.HTTPError as e:
    print(f"Ошибка HTTP при получении возраста: {e}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка соединения при получении возраста: {e}")


#Получение пола
try:
    response= requests.get(
        "https://api.genderize.io",
        params={"name": name},
        timeout=5
    )

    response.raise_for_status()
    gender_data = response.json()

    gender = gender_data.get("gender")
    probability = gender_data.get("probability")

    if probability is not None:
        if gender == "female":
            gender_probability = probability * 100
        elif gender == "male":
            gender_probability = (1 - probability) * 100

    print(f"Предполагаемый пол: {gender}")

except requests.exceptions.Timeout:
    print("Превышено время ожидания при получении пола.")

except requests.exceptions.HTTPError as e:
    print(f"Ошибка HTTP при получении пола: {e}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка соединения при получении пола: {e}")


print("\n========== ДОСЬЕ ==========")
print(f"Цель: {name}")
print(f"Вероятный возраст: {age}")

if gender_probability is not None:
    print(f"Вероятность женского пола: {gender_probability:.2f}%")
else:
    print("Вероятность женского пола: неизвестна")


# ЭТАП 2. МАСКИРОВКА

print("\nЭТАП 2. МАСКИРОВКА")

posts = []

try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "ru-RU,ru;q=0.9"
    }

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": journal_number},
        headers=headers,
        timeout=5
    )

    response.raise_for_status()

    posts = response.json()

    print(f"Количество полученных постов: {len(posts)}")

    if posts:
        print("Заголовок первого поста:")
        print(posts[0]["title"])

        print("\nСодержание первого поста:")
        print(posts[0]["body"])
    else:
        print("Посты не найдены.")

except requests.exceptions.Timeout:
    print("Превышено время ожидания при получении постов.")

except requests.exceptions.HTTPError as e:
    print(f"Ошибка HTTP при получении постов: {e}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка соединения при получении постов: {e}")

except ValueError:
    print("Ошибка обработки JSON с постами.")


#ЭТАП 3. ПЕРЕДАЧА ДАННЫХ

print("\nЭТАП 3. ПЕРЕДАЧА ДАННЫХ")

report = {
    "name": name,
    "age": age,
    "gender": gender,
    "posts_count": len(posts)
}

try:
    response = requests.post(
        "https://httpbin.org/post",
        json=report,
        timeout=5
    )

    response.raise_for_status()

    result = response.json()

    print("Отчет успешно отправлен!")
    print("Данные, принятые сервером:")
    print(result.get("json"))

except requests.exceptions.Timeout:
    print("Превышено время ожидания при отправке отчета.")

except requests.exceptions.HTTPError as e:
    print(f"Ошибка HTTP при отправке отчета: {e}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка соединения при отправке отчета: {e}")

except ValueError:
    print("Сервер вернул некорректный JSON.")


# ЭТАП 4. ЗАГРУЗКА УЛИК

print("\nЭТАП 4. ЗАГРУЗКА УЛИК")

try:
    response = requests.get(
        "https://picsum.photos/400/300",
        stream=True,
        timeout=10
    )

    response.raise_for_status()

    with open("evidence.jpg", "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

    file_size = os.path.getsize("evidence.jpg")

    print("Изображение успешно скачано!")
    print("Имя файла: evidence.jpg")
    print(f"Размер файла: {file_size} байт")

except requests.exceptions.Timeout:
    print("Превышено время ожидания при скачивании изображения.")

except requests.exceptions.HTTPError as e:
    print(f"Ошибка HTTP при скачивании изображения: {e}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка соединения при скачивании изображения: {e}")

except OSError as e:
    print(f"Ошибка сохранения файла: {e}")


#ЭТАП 5. ОБРАБОТКА СБОЕВ

print("\nЭТАП 5. ОБРАБОТКА СБОЕВ")

#Проверка ошибки HTTP 404
try:
    response = requests.get(
        "https://httpbin.org/status/404",
        timeout=5
    )

    response.raise_for_status()

except requests.exceptions.Timeout:
    print("Превышено время ожидания сервера.")

except requests.exceptions.HTTPError:
    print("Перехвачена ошибка HTTP 404: страница не найдена.")

except requests.exceptions.RequestException as e:
    print(f"Ошибка соединения: {e}")


#Проверка тайм-аута
try:
    response = requests.get(
        "https://httpbin.org/delay/6",
        timeout=3
    )

    response.raise_for_status()

except requests.exceptions.Timeout:
    print("Перехвачена ошибка Timeout: сервер не ответил за 3 секунды.")

except requests.exceptions.HTTPError as e:
    print(f"Ошибка HTTP: {e}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка соединения: {e}")



print("РАБОТА ЗАВЕРШЕНА")
