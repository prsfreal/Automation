from decouple import config


class TestData:
    email = config('twitteremail')
    password = config('twitterpassword')

    #Data
    para_01_twitter_login = [
        (email, password)
    ]

    #Data 2
    para_02_discount = [
        (email, password),
        ('string', 'string')
    ]