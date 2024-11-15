def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    
    alphabet_len = 26
    for letter in plaintext:
        if letter.isupper():
            ciphertext_letter = chr(ord("A") + (ord(letter) - ord("A") + shift) % alphabet_len)

        elif letter.islower():
            ciphertext_letter = chr(ord("a") + (ord(letter) - ord("a") + shift) % alphabet_len)

        else:
            ciphertext_letter = letter

        ciphertext += ciphertext_letter
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    
    alphabet_len = 26
    for letter in ciphertext:
        if letter.isupper():
            plaintext_letter = chr(ord("A") + (ord(letter) - ord("A") - shift) % alphabet_len)

        elif letter.islower():
            plaintext_letter = chr(ord("a") + (ord(letter) - ord("a") - shift) % alphabet_len)

        else:
            plaintext_letter = letter

        plaintext += plaintext_letter
    return plaintext
