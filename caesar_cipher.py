alphabets = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

direction = input("type 'encode' to encrypt and 'decode' for decrypt\n").lower()
text = input("type your message : \n").lower()
shift = int(input("Type the shift number : "))
if direction =="encode":
    def encrypt(orignal_text , shifted_text):
        chipher_text = ""

        for letter in orignal_text:
            if letter in alphabets:
                shifted_position = alphabets.index(letter) + shifted_text
                shifted_position %= len(alphabets)
                chipher_text += alphabets[shifted_position]
            else:
                chipher_text += letter
        print(f"here is your encoded result : {chipher_text}")

    encrypt(orignal_text = text, shifted_text = shift)

else:   
    def decrypt(orignal_text , shifted_text):
        chipher_text = ""

        for letter in orignal_text:
            if letter in alphabets:
                shifted_position = alphabets.index(letter) - shifted_text
                shifted_position %= len(alphabets)
                chipher_text += alphabets[shifted_position]
            else:
                chipher_text += letter
        print(f"here is your decoded result : {chipher_text}")
    
    decrypt(orignal_text = text, shifted_text = shift)
