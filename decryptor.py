'''
Filename: decrypt.py
This program decrypts a message so that it is human-readable
'''
# Create dictionary (hashmap) to look up from for better performance
decrypt_keys = {
    "*": "a",
    "&": "e",
    "#": "i",
    "+": "o",
    "!": "u"
}

def decrypt(text):
    completed_word = ''
    for letter in text:

        # Iterate through every character from the phrase that user entered, and then manipulate with respect to the set of decryption keys
        if letter in decrypt_keys:
            completed_word += decrypt_keys[letter]

        else:
            completed_word += letter

    return completed_word