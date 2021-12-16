from datetime import datetime

import requests
EXERCISE_END=" https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID="06e65f40"
API_KEY="5b7e376ad4cf16bef9553b2df21426e3"


GENDER = "male"
WEIGHT_KG = "108"
HEIGHT_CM = "179"
AGE = "30"



exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


sheet_ENDPOINT="https://api.sheety.co/0cce96670d5cffacc02900b631d06807/myworkout/workouts"
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_ENDPOINT, json=sheet_inputs)

    print(sheet_response.text)