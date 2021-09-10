import re


def code_land_user_name_validation(str_param):
    match_obj = re.findall('^\D[a-z0–9A-Z_]{2,25}[^_]$', str_param)
    if match_obj:
        print(True)
    else:
        print(False)
    return str_param


print(code_land_user_name_validation(input()))

# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.
#
# If the username is valid then your program should return the string true, otherwise return the string false.
