from decouple import config


class TestData:

    userName = config('TESTID')
    password = config('PASSKEY')

    # DATA test_NameParam
    para_01_Successful_Login = [
        (userName, password),
        ('string', 'string')
    ]
