from src.wedget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions,transactions_clear

#print(mask_account_card("Maestro 7000792289606361"))
#print(mask_account_card("Счет 35383033474447895560"))
#print(get_date("2024-03-11T02:26:18.671407"))
#print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
#print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

#usd_transactions = filter_by_currency(transactions_clear, "USD")
#for i in range(4):
    #print(next(usd_transactions))

#descriptions = transaction_descriptions(transactions_clear)
#for _ in range(8):
    #print(next(descriptions))

#for card_number in card_number_generator(9999999999999900, 10000000000000000):
    #print(card_number)