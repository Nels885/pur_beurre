"""
API OpenfoodFacts management module
"""

import requests

from package.glob import Glob


class ApiRest:

    def __init__(self, log):
        """
        ## Initialize Class Apirest ##
            :param log: logging module
        """
        self.log = log
        self.tag_0 = "&tagtype_0={}&tag_contains_0={}&tag_0={}".format(
            Glob.infoApi['tagtype_0'],
            Glob.infoApi['tag_contains_0'],
            Glob.infoApi['tag_0'])
        self.tag_1 = "&tagtype_1={}&tag_contains_1={}&tag_1=".format(
            Glob.infoApi['tagtype_1'],
            Glob.infoApi['tag_contains_1'])
        self.cmdRequest = "{}&action={}&sort_by={}&page_size={}&json={}".format(
            Glob.infoApi['https'],
            Glob.infoApi['action'],
            Glob.infoApi['sort_by'],
            Glob.infoApi['page_size'],
            Glob.infoApi['json'])
        self.data = 'products'

    def get_request(self, tag):
        """
        ## Execute API request ##
            :param tag: value of the reseach
            :return: data in json format
        """
        r = requests.get("{}{}{}{}".format(self.cmdRequest, self.tag_0, self.tag_1, tag))
        self.log.info("=============================================================\n"
                      "# Status Code: %s #\n"
                      "# Headers: %s #\n" % (r.status_code, r.headers['content-type']))
        return r.json()[self.data]

    def convert_data(self, result, data_name):
        """
        ## Conversion of values ##
            :param result: List of the different values
            :param data_name: Name of the values
            :return: List of values to be included in the table
        """
        val_product = []
        for nb in range(len(data_name)):
            try:
                case = result[data_name[nb]]
                if type(case) is not list:
                    rep_val = {"'": " ", '<span class="allergen">': '', '</span>': '', '\r': ' '}
                    if case != "" and case is not None:
                        for key, value in rep_val.items():
                            case = case.strip().replace(key, value)
                    else:
                        case = "NULL"
                else:
                    case = ", ".join(case)
            except KeyError as err:
                case = "NULL"
                self.log.info("*** Valeur absente dans OFF: %s", err)
            val_product.append(case)
        return val_product


