def get_summ(one, two, delimiter = '&'):
    one = str(one).upper()
    two = str(two).upper()

    result = one + delimiter + two
    print(result)

get_summ('Lern', 'Python')