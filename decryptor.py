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