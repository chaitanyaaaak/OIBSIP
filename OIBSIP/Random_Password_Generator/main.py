import random
import string

def user_preferences():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    print("Select character types to include in your password:")
    include_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
    
    if not (include_letters or include_numbers or include_symbols):
        print("You must select at least one character type. Please start again.")
        return user_preferences()
    
    return length, include_letters, include_numbers, include_symbols

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters  # a-zA-Z
    if use_numbers:
        character_pool += string.digits         # 0-9
    if use_symbols:
        character_pool += string.punctuation    # special symbols
    
    # Ensure password contains at least one character from each selected type
    password_chars = []
    if use_letters:
        password_chars.append(random.choice(string.ascii_letters))
    if use_numbers:
        password_chars.append(random.choice(string.digits))
    if use_symbols:
        password_chars.append(random.choice(string.punctuation))
    
    # Fill the remaining length with random choices
    remaining_length = length - len(password_chars)
    password_chars.extend(random.choice(character_pool) for _ in range(remaining_length))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password_chars)
    
    return ''.join(password_chars)

def main():
    while True:
     length, use_letters, use_numbers, use_symbols = user_preferences()
     password = generate_password(length, use_letters, use_numbers, use_symbols)
     print("\nGenerated Password:")
     print(password)

     again = input("\nWould you like to generate another password? (y/n): ").strip().lower()
     if again != 'y':
        print("Thanks for using the Password Generator! Stay safe.")
        break
         

if __name__ == "__main__":
    main()
