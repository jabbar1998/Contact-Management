import re


def is_valid_email(email):
    email_regex = r"^[^@]+@[a-zA-Z-]+(?:\.[a-zA-Z-]{2,4})*$"
    return re.match(email_regex, email)


def is_valid_phone(phone):
    phone_regex = r'0\d{10}'
    return re.match(phone_regex, phone)
def is_valid_Password(phone):
    phone_regex = r'^[\w\.]'
    return re.match(phone_regex, phone)