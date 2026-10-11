import json

with open('conf.json', 'r', encoding='utf-8') as file:
    users = json.load(file)

cities = {} #Пустой словарь для складывания результиата

for user in users:
    name = user["name"]
    city = user["address"]["city"]

    if city not in cities: #если города нет в словаре, созд лдля него пустой список
        cities[city] = []
        
    cities[city].append(name)#добавляем имя пользователя в список нужного города

with open('cities.json', 'w', encoding='utf-8') as file:
    json.dump(cities, file, ensure_ascii=False, indent=4)

print("Файл cities.json успешно создан")