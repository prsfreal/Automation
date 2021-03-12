import pytest
import inspect
import random

from UTILITIES.APILogHandler import *
from UTILITIES.PassParameters import PassParameters
from UTILITIES.APIRequests import Reqeusts
from API.DATA.BasicAuthentication_Data import *



class Test_FoodIsTooFatty:
    classname = inspect.stack()[0][3]
    logger = LogGen.loggen()
    req = Reqeusts()
    jform = JSONFormatter()

    @pytest.mark.parametrize("requestparams",
                             PassParameters.parseParamaters(TestData.para_NameParam))
    def test_NameParam(self, requestparams):
        LogGen.headerLog(self.logger, __name__, self.classname,
                         inspect.currentframe().f_code.co_name, requestparams)
        response = self.req.getRequest(TestData.GETFoodInfo, requestparams)

        # Data Extraction / Test Logic
        listofdictstorefactory = []
        dictconstructor = {}
        counter = 0


        # Create a working dict from JSON response
        for i in response['hints']:
            # Navigate to the correct level of JSON
            for j, k in i['food'].items():
                # Extract k v of foodId
                if j == 'foodId':
                    dictconstructor[j] = k
                # Multiple Nutrient dicts per foodId extraction, create completed dict,
                # append to listofdictstorefactory, and reset dictconstructor
                if j == 'nutrients':
                    dictconstructor[j] = k
                    listofdictstorefactory.append(dictconstructor)
                    dictconstructor = {}

        # Calculates number of foods with any fat per foodId
        for i in listofdictstorefactory:
            for k, v in i['nutrients'].items():
                if k == 'FAT' and v > 0.0:
                    counter += 1

        # Assertion
        # if less than half of foods per foodId contain fat = pass
        assert counter <= len(listofdictstorefactory) / 2, (self.logger.info(f'FAILED: {counter} greater than len(listofdictstorefactory) / 2\n'))
        self.logger.info('PASSED: This is a good low fat option and passes\n')

    @pytest.mark.parametrize("requestparams, jsonbody",
                             PassParameters.parseParamaters(TestData.para_JSONBody))
    def test_JSONBody(self, requestparams, jsonbody):
        LogGen.headerLog(self.logger, __name__, self.classname,
                         inspect.currentframe().f_code.co_name,
                         requestparams, jsonbody=jsonbody)
        response = self.req.postRequest(TestData.POSTNutrient, requestparams, jsonbody)

        self.logger.info("PASSED: End of test_JSONBody\n")

    @pytest.mark.parametrize("requestparams",
                             PassParameters.parseParamaters(TestData.para_ChainAPIs))
    def test_ChainAPIs(self, requestparams):
        LogGen.headerLog(self.logger, __name__, self.classname,
                         inspect.currentframe().f_code.co_name, requestparams)
        response = self.req.getRequest(TestData.GETFoodInfo, requestparams)

        # Data Extraction / Test Logic
        jsonlistconstructor = []
        listofjson = []

        # Create a working dict from JSON response
        for i in response['hints']:
            # Navigate to the correct level of JSON
            for j, k in i['food'].items():
                # Extract foodId value
                if j == 'foodId':
                    jsonlistconstructor.append(k)

            for m, n in i['measures'][0].items():
                # Extract measure uri
                if m == "uri":
                    jsonlistconstructor.append(n)

            # Extract a random quantity
            jsonlistconstructor.append(random.randint(1, 7))

            #create a list of values needed for next api request(s)
            #newjson = JSONFormatter.nutrientJSON(jsonlistconstructor)
            newjson = self.jform.nutrientJSON(jsonlistconstructor)
            listofjson.append(newjson)
            jsonlistconstructor = []

        #make the next api request and capture to log, limit 2 reqeusts to be polite
        for i in listofjson[0:2]:
            response2 = self.req.postRequest(TestData.POSTNutrient, params=TestData.authenticationDict, json=i)
            self.logger.info(f'2ndAPIResponse: {response2}')

        self.logger.info("PASSES: End of test_ChainAPIs\n")





