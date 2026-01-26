
alph=' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(text: str, shift: int):
    shifr = ''
    for bukva in text:
        if bukva == ' ':
            shifr+=' '
            continue
        index = alph.find(bukva)
        if index == -1:
            shifr+=bukva
        else:
            new_index=index+shift
            new_bukva=alph[new_index]
            shifr+=new_bukva

    print(shifr)



def decrypt(text: str, shift: int):
    shifr = ''
    for bukva in text:
        if bukva == ' ':
            shifr+=' '
            continue
        index = alph.find(bukva)
        if index == -1:
            shifr += bukva
        else:

            new_index = index - shift
            new_bukva = alph[new_index]
            shifr += new_bukva

    print(shifr)

