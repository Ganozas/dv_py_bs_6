
def is_very_long(password):
    return len(password) >=  12
    

def has_digit(password):
    return any(i.isdigit() for i in password)


def has_upper_letters(password):
    return any (i.isupper() for i in password)


def has_lower_letters(password):
    return any (i.islower() for i in password)


 def has_sambols(password):
    return any (not i.isdigit() and not i.isalpha() for i in password)


def has_latters(password):
    return any (i.isalpha() for i in password)


if __name__ == '__main__':
    password = (input("Введите пароль: "))
    score = 0

    function_list = [
        is_very_long,
        has_digit,
        has_lower_letters,
        has_upper_letters,
        has_sambols,
]

    for i in function_list:
        result = i(password)
        if result:
            score += 2
   	
    print("Рейтинг пароля",score)