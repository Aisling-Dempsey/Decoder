# function that takes an encoded string and returns a decoded string
def decode(encoded_str):
    decoded_str = ""
    # number we're on
    cur_index = 0
    # slice of string
    string_char = encoded_str[cur_index]
    if string_char.isdigit():
        string_char = int(string_char)

        decoded_str += encoded_str[string_char + 1]
        # cur_index = encoded_str[string_char + 2]
        encoded_str = encoded_str[(string_char + 2):]

    decode(encoded_str)

    print decoded_str

decode('0h1ae2bcy')