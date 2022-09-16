alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','q','r','s','t','u','v','w','x','y','z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','q','r','s','t','u','v','w','x','y','z']

alpha_len = len(alphabet)
direction = input("Type 'encode' to encrypt, type 'decode to decrypt: \n")

text = input("Type your message: \n")
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_number):
  encryption =''
  for letter in plain_text:
    get_index = alphabet.index(letter)
    result = get_index + shift_number
    new_letter = alphabet[result] 
    encryption += new_letter 
  print(encryption)

def decrypt(de_text, de_num):
 
        get_mess = ''
        for letter in de_text:
            old_letter = alphabet.index(letter)
            prev_index = old_letter - de_num
            result = alphabet[prev_index] 
            get_mess += result
        print(get_mess)


if direction == 'encode':
    encrypt(plain_text= text, shift_number= shift)
elif direction == 'decode':
    decrypt(de_text= text, de_num= shift)