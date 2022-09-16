from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','q','r','s','t','u','v','w','x','y','z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','q','r','s','t','u','v','w','x','y','z']

print(logo)
alpha_len = len(alphabet)
direction = input("Type 'encode' to encrypt, type 'decode to decrypt: \n")

text = input("Type your message: \n")
shift = int(input("Type the shift number:\n"))

def ceaser(plain_text, shift_num, project):
    crypt = ""
    for letter in text:
        if direction == 'encode':
            num = alphabet.index(letter)
            shift_path = num + shift_num
            ret = alphabet[shift_path]
            crypt += ret
    
        elif direction == 'decode':
            num = alphabet.index(letter)
            shift_path = num - shift_num
            ret = alphabet[shift_path]
            crypt += ret
    print(crypt)

ceaser(plain_text= text, shift_num= shift, project= direction)