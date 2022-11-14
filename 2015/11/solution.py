def is_valid_pwd(pwd_chars):
    consecutive_increasing = False
    consecutive_repeating = set()

    if any(char in pwd_chars for char in ['i', 'o', 'l']):
        return False

    for i in range(2, len(pwd_chars)):
        code1 = ord(pwd_chars[i-2])
        code2 = ord(pwd_chars[i-1])
        code3 = ord(pwd_chars[i])

        if code1 + 1 == code2 and code2 + 1 == code3:
            consecutive_increasing = True
            break

    if not consecutive_increasing:
        return False

    i = 1
    while i < len(pwd_chars):
        if (pwd_chars[i] == pwd_chars[i-1]):
            consecutive_repeating.add(pwd_chars[i])
            i += 2
        else:
            i += 1

    return len(consecutive_repeating) >= 2

def increment_pwd(pwd_chars):
    i = len(pwd_chars) - 1
    while i > 0:
        code = ord(pwd_chars[i])
        code += 1
        code = code if code < 123 else (code % 122) + 96
        pwd_chars[i] = chr(code)

        if (code == 97):
            i -= 1
        else:
            break

    return pwd_chars

def get_new_valid_pwd(pwd):
    pwd_chars = list(pwd)
    while True:
        pwd_chars = increment_pwd(pwd_chars)
        if is_valid_pwd(pwd_chars):
            return ''.join(pwd_chars)
            
# input
pwd = 'cqjxjnds'

# part 1
new_pwd = get_new_valid_pwd(pwd)
print(new_pwd)

# part 2 uses the same code
print(get_new_valid_pwd(new_pwd))