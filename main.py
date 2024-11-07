from .src.masks import get_mask_account
from .src.masks import get_mask_card_number

card_number = str(input("Введите номер карты: "))
account_number = str(input("Введите номер счёта: "))
STANDART_LENGTH_CARD_NUMBER = 16
STANDART_ACCOUNT_NUMBER = 20
long_card_number = len(card_number)
long_account_number = len(account_number)

print(get_mask_card_number(card_number))
print(get_mask_account(account_number))