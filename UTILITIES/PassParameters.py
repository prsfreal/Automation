import os


class PassParameters:

    def parseParamaters(parameterlist):
        parameterPosition = os.getenv('ss')
        if parameterPosition is None:
            return parameterlist

        if int(parameterPosition) < len(parameterlist) -1 or int(parameterPosition) > len(parameterlist) -1:
            print(f'{parameterPosition} is out of range')
            return parameterlist

        else:
            newlist = [parameterlist[int(parameterPosition)]]
            return newlist

