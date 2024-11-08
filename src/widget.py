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

print(mask_account_card("visa 1234567890123456"))
print(mask_account_card("bild 12345678901234567890"))
print(mask_account_card("Maestro 123456789"))