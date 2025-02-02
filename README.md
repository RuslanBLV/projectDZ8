# Название проекта

Проект получает номер карт и счетов, маскрирует, сортирует по дате

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/RuslanBLV/projectDZ6.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd Git_DZ
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```
   
## Тесты

Так же в репозитории "tests" есть функции для проверки каждого модуля на возможные ошибки

1. Чтобы протестировать все модули, нужно добавить в poetry pytests:
   ```bash
   poetry add --group dev pytest pytest-cov
   ```
2. В консоли наберите:
   ```bash
   pytest
   ```
   
## Использование

Примеры использования функций:

```python
from src.processing import filter_by_state, sort_by_date

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)
```

## Тесты

Так же в репозитории "tests" есть функции для проверки каждого модуля на возможные ошибки