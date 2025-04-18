# email_validator.py
import re

def is_valid_email(email):
    # Регулярное выражение для проверки корректности email-адреса
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Дополнительная проверка на наличие двух точек подряд
    if re.match(pattern, email) and '..' not in email.split('@')[1]:
        return True
    return False