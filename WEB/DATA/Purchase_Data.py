from collections import namedtuple


class TestData:

    User = namedtuple('User', 'firstname lastname address city state zip phone email contractorname '
                              'contractoremail coupon ccnumber, ccdate, cccode')

    user1 = User('John', 'Tester', '123 Fake ST', 'Detroit', 'WI', '23145',
                 '098-08-1234', 'yojohn@john.com', 'Herbert', 'herbert@herbert.com', '123bc',
                 '4242424242424242', '1225', '000')

    user2 = User('Thomas', 'Testing', '453 Fake ST', 'Green Bay', 'MI', '35466',
                 '234-456-2345', 'yoyo@thomas.com', 'Sherbert', 'sherbert@sherbert.com', '123bc',
                 '4242424242424242', '1225', '000')

    para_make_a_purchase = [
        (user1),
        (user2)
    ]