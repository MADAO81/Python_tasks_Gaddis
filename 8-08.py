# sentences corrector

def main():
    # get user's input
    user_string = input('Enter the string value: ')

    # call  capitalize function
    result = capitalize(user_string)

    # show result.
    print(result)

def capitalize(string):
    result = ''
    new_sentence = True
    result_word = ''

    words = string.split()

    for item in words:
        if new_sentence:
            result_word = item[0].upper() + item[1:]
        else:
            result_word = item
        result = result + result_word + ' '

        if item[-1] == '.' or item[-1] == '?' or item[-1] == '!':
            new_sentence = True
        else:
            new_sentence = False
    return result

main()
