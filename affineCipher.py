import sys, cryptomath, random

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]
^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front

def main():
    myMessage = """A computer would deserve to be called intelligent if it could deceive a human into believing that it was human," -Alan Turing"""
    myKEY = 2023
    mode = 'encrypt'

    if mode == 'encrypt':
        translated = encryptMessage(myKEY, myMessage)

    elif mode == 'decrypt':
        translated = decryptMessage(myKEY, myMessage)

    print('Key : %s' %(myKEY))
    print('%sed text:'%(mode.title()))
    print(translated)

def getKeyParts(key):
    keyA = key//len(SYMBOLS)
    keyB key%len(SYMBOLS)

    return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('The affine cipher becomes inredibely weak when key A is set to 1. Choose a different Key.')

    if keyB == 0 and mode == 'encrypt':
        sys.exit('The affine cipher becomes inredibely weak when key B is set to 0. Choose a different Key.')
    
    if keyA < 0 and keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('key A must be greater than 0 and key B must be between 0 and %s.'%(len(SYMBOLS)-1))

    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are notrelatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))


def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # encrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * keyA + keyB)%len(SYMBOLS)]
        
        else:
            ciphertext += symbol
    
    return ciphertext

def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            #decrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex-keyB) * modInverseOfKeyA % len(SYMBOLS)]
            
        else:
            plaintext += symbol
        
    return plaintext

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))

        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


if __name__ == "__main__":
    main()