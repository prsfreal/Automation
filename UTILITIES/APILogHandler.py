import logging

class LogGen:

    @staticmethod
    def loggen():
        #Delete default handlers
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename="/API/LOGS/automation.log",
                            filemode='a',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


    def headerLog(self, fileName, className, function_name, requestParams, jsonbody= None):
        headerLogger = LogGen.loggen()
        headerLogger.info(f'TEST: {fileName}/{className}/{function_name}')
        headerLogger.info(f'PARAMETERS: {requestParams}')
        if jsonbody:
            headerLogger.info(f'JSON: {jsonbody}')





