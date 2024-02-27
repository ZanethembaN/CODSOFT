import random
import string

def get_password_length():
    while True:
        password_len = input("Please specify the password length: ")
        if int(password_len) >= 8:
            return password_len
        else:
            print("Password must atleast be 8+ characters long")


def generate_password(password_len):

    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    numbers = string.digits
    punctuation = string.punctuation


    if password_len % 4 > 0:
        lower_len = password_len // 4
        upper_len = password_len // 4
        digit_len = password_len // 4
        punct_len = password_len // 4 + (password_len % 4)

        lower_chars = ''.join(random.choice(lower_case) for _ in range(lower_len))
        upper_chars = ''.join(random.choice(upper_case) for _ in range(upper_len))
        digit_chars = ''.join(random.choice(numbers) for _ in range(digit_len))
        punct_chars = ''.join(random.choice(punctuation) for _ in range(punct_len))

        all_chars = lower_chars + upper_chars + digit_chars + punct_chars

        password = ''.join(random.sample(all_chars, password_len))
    else:
        lower_chars = ''.join(random.choice(lower_case) for _ in range(password_len // 4))
        upper_chars = ''.join(random.choice(upper_case) for _ in range(password_len // 4))
        digit_chars = ''.join(random.choice(numbers) for _ in range(password_len // 4))
        punct_chars = ''.join(random.choice(punctuation) for _ in range(password_len // 4))

        all_chars = lower_chars + upper_chars + digit_chars + punct_chars

        password = ''.join(random.sample(all_chars, password_len))

    return password


def main():
    password_len = int(get_password_length())
    generated_password = generate_password(password_len)
    print("Generated Password:", generated_password)


if __name__ == "__main__":
    main()
