def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword_len = len(keyword)
    keyword = keyword.lower()
    alpha_len = 26
    i = 0
    for letter in plaintext:

        if letter.isalpha():

            if letter.isupper():
                ciphertext += chr(ord("A") + ((ord(letter) - ord("A")) + (ord(keyword[i]) - ord("a"))) % alpha_len)
            else:
                ciphertext += chr(ord("a") + ((ord(letter) - ord("a")) + (ord(keyword[i]) - ord("a"))) % alpha_len)

            i += 1
            if i == keyword_len:
                i = 0

        else:
            ciphertext += letter

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword_len = len(keyword)
    keyword = keyword.lower()
    alpha_len = 26
    i = 0
    for letter in ciphertext:

        if letter.isalpha():

            if letter.isupper():
                plaintext += chr(ord("A") + ((ord(letter) - ord("A")) - (ord(keyword[i]) - ord("a"))) % alpha_len)
            else:
                plaintext += chr(ord("a") + ((ord(letter) - ord("a")) - (ord(keyword[i]) - ord("a"))) % alpha_len)

            i += 1
            if i == keyword_len:
                i = 0

        else:
            plaintext += letter

    return plaintext
