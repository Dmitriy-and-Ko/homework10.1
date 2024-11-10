from operator import index

from src import masks
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data_bank: str) -> str:
    """Фцнкция принимает и маскирует полностью как карту банка, так и номер счёта"""
    alpha_part_data_bank = ""
    digit_part_data_bank = ""
    for element in data_bank:
        if element.isalpha() == True:
            alpha_part_data_bank += element
        elif element.isdigit() == True:
            digit_part_data_bank += element
    if len(digit_part_data_bank) == 16:
        return f"{alpha_part_data_bank} {get_mask_card_number(digit_part_data_bank)}"
    elif len(digit_part_data_bank) == 20:
        return f"{alpha_part_data_bank} {get_mask_account(digit_part_data_bank)}"
    else:
        return "Вы ввели неверное колличество цифр"


def get_date(real_time: str) -> str:
    only_date = real_time[:10]
    list_only_date = only_date.split("-")
    sorted_list_only_date = list()
    sorted_list_only_date.insert(0, list_only_date[2])
    sorted_list_only_date.insert(1, list_only_date[1])
    sorted_list_only_date.insert(2, list_only_date[0])
    sorted_string_only_date = ".".join(sorted_list_only_date)
    return sorted_string_only_date

print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_card("visa 1234567890123456"))
print(mask_account_card("bild 12345678901234567890"))
print(mask_account_card("Maestro 12345678"))