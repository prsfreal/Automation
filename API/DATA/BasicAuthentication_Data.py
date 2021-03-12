from decouple import config
from API.HELPERS.BasicAuthentication_JSONFormatter import *


class TestData:
    jform = JSONFormatter()
    appID = config('foodapiid')
    appkey = config('foodapikey')
    authenticationDict = {"app_id": appID, "app_key": appkey}
    GETFoodInfo = "https://api.edamam.com/api/food-database/v2/parser"
    POSTNutrient = "https://api.edamam.com/api/food-database/v2/nutrients"

    # DATA test_NameParam
    para_NameParam = [
        {"ingr": "orange", "app_id": appID, "app_key": appkey},
        {"ingr": "french%20fries", "app_id": appID, "app_key": appkey},
        {"ingr": "lettuce", "app_id": appID, "app_key": appkey}
    ]

    # DATA test_JSONBody
    para_JSONBody = [
        (authenticationDict, jform.nutrientJSON(["food_bnbh4ycaqj9as0a9z7h9xb2wmgat",
                                                 "http://www.edamam.com/ontologies/edamam.owl#Measure_unit",
                                                 1])),
        (authenticationDict, jform.nutrientJSON(["food_bz6b8fsbccyn3zaij72f7av8dl9m",
                                                 "http://www.edamam.com/ontologies/edamam.owl#Measure_serving",
                                                 2])),
        (authenticationDict, jform.nutrientJSON(["food_aregbrwb5q7z2db1h14uxaizfd9f",
                                                 "http://www.edamam.com/ontologies/edamam.owl#Measure_unit",
                                                 3]))
    ]

    # DATA test_JSONBody
    para_ChainAPIs = [
        {"ingr": "lemon", "app_id": appID, "app_key": appkey},
        {"ingr": "pork%20belly", "app_id": appID, "app_key": appkey},
        {"ingr": "spinach", "app_id": appID, "app_key": appkey}
    ]
