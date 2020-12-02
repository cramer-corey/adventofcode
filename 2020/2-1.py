from util import file_to_list

passwords = file_to_list("day_2.txt")


def password_validator(input):
    policy, password = input.split(':')
    count, required_letter = policy.split(" ")
    min, max = count.split("-")
    occurrences = password.count(required_letter)
    return (occurrences >= int(min) and occurrences <= int(max))


valid_passwords = 0

for password in passwords:
    if password_validator(password):
        valid_passwords += 1

print(valid_passwords)
