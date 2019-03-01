def get_summ(one, two, delimiter = '&'):
    one = str(one)
    two = str(two)

    result = one + delimiter + two
    print(result)

get_summ('Lern', 'Python')