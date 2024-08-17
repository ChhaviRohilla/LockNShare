# LockNShare 
LockNShare is an Asymmetric-Key Encryptor-Decryptor that enables users to securely share passwords, secret codes, or files over public channels. Only the recipient with the correct private key can decrypt the encrypted data.<br><br>
![image](https://github.com/user-attachments/assets/fd2ac936-13ce-4aea-8448-2bcc618cfb98)

The program utilizes a combination of Diffie-Hellman key exchange and XOR cipher for encrypting and decrypting the file content. The Diffie-Hellman algorithm ensures secure key exchange, while the XOR operation provides a method for actual data encryption.

## Key Points:
#### Diffie-Hellman Key Exchange: 
This algorithm is used to securely exchange cryptographic keys over a public channel. In this case, it is used to generate a shared public key between the sender and receiver using the private key which is only known to the one who generates it.

#### XOR Cipher: 
The actual encryption and decryption of file content are done using the XOR operation with the shared secret key derived from the Diffie-Hellman exchange.

## Encryption Process:

Step 1: The user enters two public numbers and a private key(known only to user).<br>
Step 2: The public key will get calculated using the mathematical formula.<br>
Step 3: The public key, along with the two public numbers, is shown to the user, which they can share with the desired recipient freely over any public channel.<br>
Step 4: The user then inputs the exchanged public key received from the recipient and selects a file to be encrypted.<br>
Step 5: The file content is encrypted.<br>
Step 6: The encrypted file is saved as "Encrypt.txt".<br>
Step 7: Sender can share the encrypted file to recipient over any public channel.<br>

## Decryption Process:

Step 1: Similar to encryption, the user enters the two public numbers(received from sender) and a private key(known only to user).<br>
Step 2: The public key is calculated and shown to the user.<br>
Step 3: The user then inputs the exchanged public key received from the sender and selects the encrypted file to be decrypted.<br>
Step 4: The file content is decrypted.<br>
Step 5: The decrypted file is saved as "Decrypt.txt".<br>
