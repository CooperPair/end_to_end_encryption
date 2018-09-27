# Transposition Cipher hacker
import pyperclip, detectEnglish, decrypt

def main():
    myMsessage = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""
    hackedMessage = hackTransposition(myMsessage)

    if hackedMessage == None:
        print("Fail to hack encryption.")
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        # pyperclip.copy(hackedMessage)

def hackTransposition(message):
    print('Hacking...')
    print('(Press Ctrl-C and Ctrl-D to quit at any time.)')

    #brute force by looping through every possible key
    for key in range(1, len(message)):
        print("Trying key #%s..."%(key))
        decryptedText = decrypt.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
            # check with the user if the decrypted key has been found.
            print()
            print("Possible encryption hack:")
            print('Key %s: %s' % (key, decryptedText[:200]))
            print()
            print("Enter D for done or just press Enter for continue hacking:")
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

if __name__ == '__main__':
    main()
