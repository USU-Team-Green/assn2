import math, random
from pip._vendor.distlib.compat import raw_input



def encrypt(key,msg):
    cipher = ""

    k_indx = 0

    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))

    col = len(key)

    row = int(math.ceil(msg_len / col))

    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx]
                           for row in matrix])
        k_indx += 1

    return cipher
 


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
            print('testing ',i )

            test_key_string = str(i)

            test_cipher = encrypt(test_key_string, plain_text)
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

if __name__ == '__main__':

    plain_text_original = raw_input('plain text: ')
    cipher_text = raw_input('cipher text: ')

    plain_text = condense_message(plain_text_original)

    key  = brute_force(plain_text, cipher_text)
    print('key: ', key)


