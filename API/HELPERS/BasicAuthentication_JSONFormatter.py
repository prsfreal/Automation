
class JSONFormatter:

    #for use with BasicAuthentication test_ChainAPIs

    def nutrientJSON(self ,parameterJSONList):
        newjson = {
            "ingredients": [
                {

                    "foodId": parameterJSONList[0],
                    "measureURI": parameterJSONList[1],
                    "quantity": parameterJSONList[2]

                }
            ]
        }
        return newjson




