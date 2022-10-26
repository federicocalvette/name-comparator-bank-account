from difflib import SequenceMatcher as SM


def name_comparator(name_form, name_response):
    s1 = name_form.lower()
    s2 = name_response.lower()

    match_decimal = SM(None, s1, s2).ratio()

    match_percentage = (match_decimal * 100)

    porcentage = f'{match_percentage:.2f}'

    return porcentage


def name_comparator_mask(name_form, name_response):
    s1 = name_form.lower()
    s2 = name_response.lower()

    s1_list_splited = s1.split(' ')

    s2_list = s2.split(' ')
    s2_list_splited = []

    for item in s2_list:
        s2_list_splited.append(item.strip("*"))

    s2_str = " ".join(s2_list_splited)

    s1_list_equal_len = []

    for valor_1, valor_2 in zip(s1_list_splited, s2_list_splited):
        s2_len = len(valor_2)
        s1_equal_len = valor_1[:s2_len]
        s1_list_equal_len.append(s1_equal_len)

    s1_str_equal_len = " ".join(s1_list_equal_len)
    print(s1_str_equal_len + " " + s2_str)

    match_decimal = SM(None, s1_str_equal_len, s2_str).ratio()
    match_percentage = (match_decimal * 100)
    porcentage = f'{match_percentage:.2f}'

    return porcentage
