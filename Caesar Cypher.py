alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
while True:
    direction = input("Type encode to encrypt,  type decode to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
         print("Invalid input. Please type 'encode' or 'decode'.")
         continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift:\n"))
    import time


    def ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction):
        output_text = ""
        if encode_or_decode == "decode":
            shift_amount *= -1
        for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        for i in range(1, 4):
            print(f"Please wait{'.' * i}")
            time.sleep(1)
        print(f"Here is your {encode_or_decode}d result: {output_text}")
        print("\n\n")
     
    ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    try_again = input("Would you like to try again? Y/N\n").lower()
    if try_again == "y":
        continue
    else:
        break  
    
    

    
        
        
        
        