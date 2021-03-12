import random


class TestData:
    baseURL = "http://api.icndb.com/jokes/"
    getRandomJokeURI = "http://api.icndb.com/jokes/random/"


    para_NameParam =[
        {"firstName": "Philip", "lastName": "Realini"},
        {"firstName": "Yuko", "lastName": "Takagi"},
        {"firstName": "Leo", "lastName": "Takalini"}
    ]

    para_ByID = [
        str(random.randint(1, 500)),
        str(random.randint(1, 500)),
        str(random.randint(1, 500))
    ]