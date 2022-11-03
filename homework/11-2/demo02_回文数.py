def is_palin(n):
    original = str(n)
    reverse = ''
    for i in original:
        reverse = i + reverse
    return original == reverse


print(is_palin("上海自来水来自海上"))

    