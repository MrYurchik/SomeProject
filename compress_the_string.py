def compress_the_string(number: int):
    if not str(number).isdigit():
        raise ValueError('Number must be integer')
    count = 0
    number = list(map(int, str(number)))
    past = number[0]
    result = []
    for num in number:
        if num != past:
            result.append([count, past])
            count = 1
        else:
            count += 1
        past = num
    result.append([count, past])
    return result

# if __name__ == '__main__':
#     compress_the_string(a)
#     compress_the_string('asd')
