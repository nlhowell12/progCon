def find_intersection(str1, str2):
    return ''.join(set(str1[1:-1]).intersection(str2[1:-1]))


def find_first_matching_index(str1, str2):
    ind_dict = {}
    for let in find_intersection(str1, str2):
        ind_dict[let] = [str1[1:-1].find(let)+1, str2[1:-1].find(let)+1]
    return ind_dict

str 1 - str2, str3, str4
str2 - str3, str4
str3 - str4

print find_first_matching_index('OIMDIHEIAFNL', 'CHJDBJMHPJKD')
