boolean_value=False

while not boolean_value:

    def encrypt(original_text,shift_number):
        cipher_text=''
        
        for letter in original_text:
            if letter not in alphabet:
                cipher_text+=letter
            else:
                index_of_alphabet=alphabet.index(letter)+shift_number    
                cipher_text+=alphabet[index_of_alphabet]
        print(f"Encrypted Text:{cipher_text}" )
    def decrypt(shift_number,original_text):
        decrypted_text=''
        for letter in original_text:
            if letter not in alphabet:
                decrypted_text+=letter
            else:
                index_of_alphabet=alphabet.index(letter)-shift_number
                decrypted_text+=alphabet[index_of_alphabet]
        print(f"Decrypted text is:{decrypted_text}")


    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    input_of_user=input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()

    message=input('Type your message: ')

    shift_number=int(input('Type the shift number: '))
    try_again=True
    while try_again:
        if input_of_user=='encode':
            encrypt(message,shift_number)
            try_again=False
        elif input_of_user=='decode':
            decrypt(shift_number,message)
            try_again=False
        else:
            print('Invalid input.Try Again!')
            try_again=True

    boolean=True
    while boolean:

        choice=input('Want to Continue? (Yes or No): ').lower()

        if choice=='yes':
            boolean_value=False
            boolean=False
        elif choice=='no':
            boolean_value=True
            boolean=False
        else:
            print('Invalid input, Try Again!')
            boolean=True
    


