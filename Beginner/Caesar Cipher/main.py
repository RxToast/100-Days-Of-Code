from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

program_on = True


def caesar(original_text, shift_amount, encode_or_decode):
    global program_on
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}\n")


while program_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    use_again = input("Would you like to use it again? Type yes or no\n").lower()
    if use_again == "yes":
        program_on = True
    elif use_again == "no":
        print("\nByeBye")
        program_on = False
    else:
        print("Invalid entry. Shutting down.\n")
        program_on = False
