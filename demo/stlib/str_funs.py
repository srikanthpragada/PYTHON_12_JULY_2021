# String functions

def hasdigit(st: str) -> bool:
    """
    Checks whether the given string has any digit
    :param st: string to check
    :return: True if string has digit otherwise false
    """
    for c in st:
        if c.isdigit():
            return True

    return False


def isvalidmobile(st):
    return len(st) == 10 and st.isdigit()
