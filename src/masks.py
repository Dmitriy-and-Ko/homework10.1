from typing import Union



card_number = str(input("Введите номер карты: "))
account_number = str(input("Введите номер счёта: "))
STANDART_LENGTH_CARD_NUMBER = 16
STANDART_ACCOUNT_NUMBER = 20
long_card_number = len(card_number)
long_account_number = len(account_number)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер карты в формате XXXX XX** **** XXXX, где X - цифра"""
    if long_card_number == STANDART_LENGTH_CARD_NUMBER:
        mask_card_number = card_number.replace(card_number[6:12], "******")
        list_mask_card_number = []
        for element in range(long_card_number // 4):
            list_mask_card_number.append(f"{mask_card_number[element*4:(element+1)*4]}")
        splited_mask_card_number = " ".join(list_mask_card_number)
        return splited_mask_card_number
    else:
        return "Набранный Вами номер карты не соответствует колличеству в 16 цифр"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер счёта в формате **ХХХХ, где XXXX, последние 4 цифры номера"""
    if long_account_number == STANDART_ACCOUNT_NUMBER:
        mask_account_number = f"**{account_number[-5:-1]}"
        return mask_account_number
    else:
        return "Набранный Вами номер счёта не соответствует колличеству в 16 цифр"


print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
