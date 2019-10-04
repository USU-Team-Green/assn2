import math, random
from pip._vendor.distlib.compat import raw_input

#Aaron Adams

def columnar_transpose(key,msg):

    cipher_text = ""

    key_index = 0

    message_length = float(len(msg))

    message_list = list(msg)

    key_list = sorted(list(key))

    column = len(key)

    row = int(math.ceil(message_length / column))

    fill_null = int((row * column) - message_length)

    message_list.extend('_' * fill_null)

    matrix = [message_list[i: i + column]
              for i in range(0, len(message_list), column)]

    for _ in range(column):

        curr_idx = key.index(key_list[key_index])

        cipher_text += ''.join([row[curr_idx]
                           for row in matrix])

        key_index += 1

    return cipher_text
 


def contains_zero(number):

    for c in map(int, str(number)):

        if(c == 0):
            return True

    return False



def brute_force(plain_text, cipher_text):


    #need to exclude numbers containing 0
    for i in range(1, 7654321):

        contains_a_zero = contains_zero(i)

        if contains_a_zero == False:
            #print('testing ',i )

            test_key_string = str(i)

            test_cipher = columnar_transpose(test_key_string, plain_text)
            test_cipher_final = remove_underscores(test_cipher)

            if test_cipher_final == cipher_text:
                return i

    return 0



def condense_message(plain_text):
    message_nostrings = plain_text.replace(' ', '')
    message = message_nostrings.lower()
    return message

def remove_underscores(plain_text):
    message_nostrings = plain_text.replace('_', '')
    message = message_nostrings.lower()
    return message




#test case
#you need to find the key
#ntneudihyyeodkoefte
#output 3421

if __name__ == '__main__':

    plain_text_original = raw_input('Plain Text: ')
    cipher_text = raw_input('Cipher Text: ')

    plain_text = condense_message(plain_text_original)

    key  = brute_force(plain_text, cipher_text)
    print('key: ', key)


