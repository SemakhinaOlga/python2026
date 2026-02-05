def is_balanced(string):
    if string == "":
        return True

    pairs = ["()", "{}", "[]"]
    find_para = False

    for para in pairs:
        if para in string:
            find_para = True

    if find_para is True:
        for para in pairs:
            while para in string:
                string = string.replace(para, '', 1)

        return is_balanced(string)
    else:
        return False







