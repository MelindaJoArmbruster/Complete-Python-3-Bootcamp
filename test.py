def up_low(s):
    d = {'upper': 0, 'lower': 0}

    for char in s:
        if char.isupper():
            d['upper'] += 1
        elif char.islower():
            d['lower'] += 1
        else:
            pass
    print(
        f'No. of Upper case characters : {d["upper"]}\nNo. of Lower case characters : {d["lower"]}')


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
