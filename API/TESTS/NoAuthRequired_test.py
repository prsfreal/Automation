import pytest
import inspect

from UTILITIES.PassParameters import PassParameters
from UTILITIES.APIRequests import Reqeusts
from UTILITIES.APILogHandler import *
from API.DATA.NoAuthRequired_Data import *


class Test_ChuckNorris:
    classname = inspect.stack()[0][3]
    logger = LogGen.loggen()
    req = Reqeusts()

    @pytest.mark.parametrize("requestparams", PassParameters.parseParamaters(TestData.para_NameParam))
    def test_NameParam(self, requestparams):
        LogGen.headerLog(self.logger, __name__, self.classname,
                         inspect.currentframe().f_code.co_name, requestparams)
        response = self.req.getRequest(TestData.getRandomJokeURI, params=requestparams)

        # Data Extraction / Test Logic
        joke = response['value']['joke']
        fname = requestparams['firstName']
        lname = requestparams['lastName']

        # Assertion
        assert fname in joke and lname in joke, self.logger.info(f'FAILED:Did not find {fname} and {lname}in response\n')
        self.logger.info(f'JOKE: {joke}')
        self.logger.info(f'PASSED\n')

    @pytest.mark.parametrize("requestparams", PassParameters.parseParamaters(TestData.para_ByID))
    def test_ByID(self, requestparams):
        LogGen.headerLog(self.logger, __name__, self.classname,
                         inspect.currentframe().f_code.co_name, requestparams)
        response = self.req.getRequest(TestData.baseURL + requestparams)

        # Data Extraction / Test Logic
        joke = response['value']['joke']

        # Assertion
        assert "Chuck Norris" in joke, self.logger.info(f'FAILED:Did not find Chuck Norris in Joke\n')
        self.logger.info(f'{joke}')
        self.logger.info(f'PASSED\n')
