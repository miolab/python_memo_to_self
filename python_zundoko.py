import random

def fn_zundoko():
    """ Doc: description

    Function:
        Random printing the word "ズン" or "ドコ".
        If "ズン", "ズン", "ズン", "ズン", "ドコ" appear in order,
        it would return "キ・ヨ・シ！" and finish program.

    Parameter:
        array_zundoko (list):
            main list to be appended "ズン" or "ドコ" randomly.
    """
    array_zundoko = []

    for _ in range(100):
        zun_or_doko = random.choice(["ズン", "ドコ"])
        array_zundoko.append(zun_or_doko)
        print(array_zundoko[-1])

        if array_zundoko[-5:] == ["ズン", "ズン", "ズン", "ズン", "ドコ"]:
            print("キ・ヨ・シ！")
            return
        else:
            pass

if __name__ == '__main__':
    print(fn_zundoko.__doc__)
    fn_zundoko()
