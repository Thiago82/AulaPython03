# MODULES1

from Modules2 import validate_and_execute, user_input_message
# from Modules2 import * ### Importa a porra toda
#import Modules2 as nome_temporario ### Importa batizando com outro nome

#built in Modules
# import os
# print(os.name)

import logging
logger = logging.getLogger("MAIN")
logger.error("Error happened")

# user_input = ""
# while user_input != "exit":
#     user_input = input(user_input_message)
#     days_and_unit = user_input.split(":")
#     days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
#     validate_and_execute(days_and_unit_dictionary)
    #nome_temporario.validate_and_execute(days_and_unit_dictionary)