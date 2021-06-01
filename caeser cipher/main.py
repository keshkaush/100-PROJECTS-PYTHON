from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
def ceaser(go_direction, ciphered_text,shifting):
    plain_text = ""
    if go_direction == "decode":
        shifting *= -1
    for letter in ciphered_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shifting
            if new_position > 25:
                new_position = new_position % 26
            elif new_position < 0:
                new_position = abs(new_position) % 26      
            new_letter = alphabet[new_position]
            plain_text += new_letter
        else:
            plain_text += letter    
    print(f"The {go_direction}d text is {plain_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
            
    ceaser(direction, text, shift)
    result = input("type 'yes' to continue and 'no' to exit .!!\n")
    if result == "no":
        should_continue = False
        print("Goodbye")

