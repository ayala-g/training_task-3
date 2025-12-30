"""
    פונקציה שבודקת שיש:
    - לפחות אות קטנה אחת
    - לפחות אות גדולה אחת
    - לפחות ספרה אחת
    - לפחות תו מיוחד אחד
"""
def has_required_types(password: str):

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    return has_lower and has_upper and has_digit and has_special


# פונקציה שבודקת שאין תו שמופיע 3 פעמים ברצף.
def no_triple_repetition(password: str) :
    for i in range(2, len(password)):
        if password[i] == password[i - 1] == password[i - 2]:
            return False
    return True

#פונקציה שבודקת שאין רצפים של 3 תווים עוקבים (לכיוון עולה בעוקבים) 
def no_consecutive_sequences(password: str) :

    for i in range(len(password) - 2):
        a, b, c = password[i], password[i + 1], password[i + 2]

        # רצף אותיות
        if a.isalpha() and b.isalpha() and c.isalpha():
            a_l = a.lower()
            b_l = b.lower()
            c_l = c.lower()
            if ord(b_l) == ord(a_l) + 1 and ord(c_l) == ord(b_l) + 1:
                return False

        # רצף ספרות
        if a.isdigit() and b.isdigit() and c.isdigit():
            if int(b) == int(a) + 1 and int(c) == int(b) + 1:
                return False

    return True

    """
    פונקציה שבודקת את כל הקריטריונים יחד:
    - אורך מינימלי 8
    - סוגי תווים (קטנה, גדולה, ספרה, מיוחד)
    - אין תו שחוזר יותר מ-2 פעמים ברצף
    - אין רצפים עוקבים של 3 תווים
    """
def is_strong_password(password: str) -> bool:
    # אורך
    if len(password) < 8:
        return False

    # סוגי תווים
    if not has_required_types(password):
        return False

    # חזרות רצופות
    if not no_triple_repetition(password):
        return False

    # רצפים עוקבים
    if not no_consecutive_sequences(password):
        return False

    return True


if __name__ == "__main__":
    pwd = input("הכניסי סיסמה לבדיקה: ")
    if is_strong_password(pwd):
        print("strong password")
    else:
        print("weak password")
