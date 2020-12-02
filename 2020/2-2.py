from util import file_to_list

passwords = file_to_list("day_2.txt")


def password_validator(input):
    policy, password = input.split(':')
    positions, required_letter = policy.split(" ")
    position1, position2 = positions.split("-")
    is_position_1 = password[int(position1)] == required_letter
    is_position_2 = password[int(position2)] == required_letter
    if is_position_1 and is_position_2:
        return False
    elif not is_position_1 and not is_position_2:
        return False
    else:
        return True


valid_passwords = 0

for password in passwords:
    if password_validator(password):
        valid_passwords += 1

print(valid_passwords)
