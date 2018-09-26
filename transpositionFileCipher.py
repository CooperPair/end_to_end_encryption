import time, os, sys, encrypt, decrypt

def main():
    file = "frankstein.txt"# name of file to be encrypted
    op_file = "frankstein_encrypted.txt"# the encrypteed file to be saved into this file
    my_key = 10
    my_mode = 'encrypt'# can be encrypt or decrypt

    #if input file does not exhist then program will terminates easily
    if not os.path.exists(file):
        print('The file %s does not exist. Quitting ...'%(file))
        sys.exit()

    # if the output file already exists, give the user the chance to exit
    if os.path.exists(op_file):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?')%(op_file)
        response = input("> ")
        if not response.lower().startswith('c'):
            sys.exit()

    #Read in the message from the input file 
    fileObj = open(file)
    content = fileObj.read()
    fileObj.close()

    print('%sing...'%(my_mode.title()))

    #measuring how long the encrption will take
    start_time = time.time()

    if my_mode == 'encrypt':
        translated = encrypt.encryptMessage(my_key, content)
    elif my_mode == 'decrypt':
        translated = decrypt.encryptMessage(my_key, content)

    totalTime = round(time.time()-start_time, 2)
    print('%sion time: %s seconds'%(my_mode.title(), totalTime))

    #writing out the translated file to the output file.
    outFileObj = open(op_file,'w')
    outFileObj.write(translated)
    outFileObj.close()

    print('Done %sing %s (%s characers).'%(my_mode, file, len(content)))
    print('%sed file is %s.'%(my_mode.title(), op_file))

if __name__ == '__main__':
    main()