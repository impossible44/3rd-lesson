import requests
name="Oleg"

age_url=f"https://api.agify.io?name={name}"
age_response=requests.get(age_url)
age_data=age_response.json()

gender_url=f"https://api.genderize.io?name={name}"
gender_response=requests.get(gender_url)
gender_data= gender_response.json()

age= age_data["age"]
gender=gender_data["gender"]
probability=gender_data["probability"]

if gender == "female":
    female_probability = probability * 100
elif gender == "male":
    female_probability=(1-probability)*100
else:
    female_probability = 0
print(f"Цель: {name}")
print(f"Вероятный возраси: {age}")
print(f"Вероятность женск пола: {female_probability:.0f}%")