# End_to_End_encryption

End-to-end encryption (E2EE) is a system of communication where only the communicating users can read the messages. In principle, it prevents potential eavesdroppers – including telecom providers, Internet providers, and even the provider of the communication service – from being able to access the cryptographic keys needed to decrypt the conversation.

# How does end to end encryption works 

To understand how E2EE works, it helps to look at a diagram. In the example below, Bob wants to say hello to Alice in private. Alice has a public key and a private key, which are two mathematically related encryption keys. The public key can be shared with anyone, but only Alice has the private key.

First, Bob uses Alice’s public key to encrypt the message, turning “Hello Alice” into something called ciphertext — scrambled, seemingly random characters.



![alt text](https://protonmail.com/blog/wp-content/uploads/2015/05/bob-alice.jpg)

Bob sends this encrypted message over the public internet. Along the way, it may pass through multiple servers, including those belonging to the email service they’re using and to their internet service providers. Although those companies may try to read the message (or even share them with third parties), it is impossible for them to convert the ciphertext back into readable plaintext. Only Alice can do that with her private key when it lands in her inbox, as Alice is the only person that has access to her private key. When Alice wants to reply, she simply repeats the process, encrypting her message to Bob using Bob’s public key.

# cipher in encryption

A cipher (or cypher) is an algorithm for performing encryption or decryption—a series of well-defined steps that can be followed as a procedure. An alternative, less common term is encipherment. To encipher or encode is to convert information into cipher or code. In common parlance, "cipher" is synonymous with "code", as they are both a set of steps that encrypt a message; however, the concepts are distinct in cryptography, especially classical cryptography.(source wikipedia)

# some of the ciphers techniques are :

1. atbash cipher
2. Caesar cipher
3. Affine cipher
4. Simple sunstitution cipher
5. Baconian cipher
6. Vigenere cipher
7. Rail-fence cipher and many more ...

# how to run any code 

>> Just type in command shell :
```
      foo@bar: python filename.py
```
>> for example :
```
      foo@bar : python vigenere.py
```
