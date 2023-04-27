# merge dict


def merge_dict(dict_1: dict, dict_2: dict):
    result = {}
    for key, val in dict_1.items():
        if key not in dict_2.keys():
            result[key] = val
        else:
            result[key] = dict_1[key] + dict_2[key]

    for key, val in dict_2.items():
        if key not in result.keys():
            result[key] = val

    print(result)


marks_1 = {"maths": 20, "science": 15, "english": 17}

marks_2 = {"computer": 20, "maths": 18, "hindi": 18}

merge_dict(marks_1, marks_2)
