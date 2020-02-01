import random

def zundoko():
    """ Doc: description

    Function:
        Random printing the word "ズン" or "ドコ".
        If "ズン", "ズン", "ズン", "ズン", "ドコ" appear in order,
        it would return "キ・ヨ・シ！" and program finish.

    Parameter:
        array_zundoko (list):
            main list to be appended "ズン" or "ドコ" randomly.
        array_zundoko_finish (list):
            judgement key about array_zundoko has "ズン", "ズン", "ズン", "ズン", "ドコ" or not.
    """
    array_zundoko = []
    array_zundoko_finish = ["ズン", "ズン", "ズン", "ズン", "ドコ"]

    for _ in range(100):
        zun_or_doko = random.choice(["ズン", "ドコ"])
        array_zundoko.append(zun_or_doko)
        print(array_zundoko[-1])

        if array_zundoko[-5:] == array_zundoko_finish:
            print("キ・ヨ・シ！")
            return
        else:
            pass

if __name__ == '__main__':
    print(zundoko.__doc__)
    zundoko()
