import pytest
import requests
import inspect
from bs4 import BeautifulSoup as BS

from API.DATA.CSRFTokenAuthentication_Data import *
from UTILITIES.PassParameters import PassParameters
from UTILITIES.APILogHandler import *


#CSRF Token Authentication using bs4
class Test_CSRFToken():
    classname = inspect.stack()[0][3]
    logger = LogGen.loggen()

    @pytest.mark.parametrize("requestparams",
                             PassParameters.parseParamaters(testdata.para_login))
    def test_CSRFTOKEN(self, requestparams):
        LogGen.headerLog(self.logger, __name__, self.classname,
                         inspect.currentframe().f_code.co_name, requestparams)

        #TODO HELPERS Login function
        # Open a session, get the URL html
        with requests.session() as session:
            htmlresponse = session.get(testdata.testURL)

        # Initiate bs4 with html parser
        loginpagehtml = BS(htmlresponse.text, 'html.parser')

        # capture the csrf token on the webpage
        csrf = loginpagehtml.select("#csrf_token")[0].get("value")
        self.logger.info(f'CRSF: {csrf}')

        #Update Parameters
        requestparams["_csrf_token"] = csrf

        #Make a POST request and try to login
        resp2 = session.post(testdata.testURL2, data=requestparams)

        #TODO good canidate for selenium integration
        #Test to see if login worked by looking for logout in the html of the account page
        #This is bad code but will leave now as a verification placeholder
        import re
        assert re.search("logout", resp2.text), (self.logger.info(f'FAILED: Did not login\n'))
        self.logger.info(f'PASSED: Successfully logged in\n')