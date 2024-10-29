# Маємо набір монет
coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    """
    Функція знаходить мінімальну кількість монет для заданої суми, використовуючи жадібний алгоритм.
    :param amount: сума, яку потрібно видати
    :return: словник з номіналами монет та їх кількістю
    """
    # Сортуємо монети в порядку спадання
    sorted_coins = sorted(coins, reverse=True)
    # Ініціалізуємо словник для збереження результату
    result = {}
    # Проходимося по кожній монеті
    for coin in sorted_coins:
        # Рахуємо кількість монет даного номіналу
        count = amount // coin
        if count > 0:
            result[coin] = count
            # Зменшуємо суму на номінал монет
            amount -= coin * count
    return result

def find_min_coins(amount):
    """
    Функція знаходить мінімальну кількість монет для заданої суми, використовуючи динамічне програмування.
    :param amount: сума, яку потрібно видати
    :return: словник з номіналами монет та їх кількістю
    """
    # Ініціалізуємо масив для збереження мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    # Базовий випадок: для суми 0 потрібно 0 монет
    dp[0] = 0
    # Масив для відстеження монет, які використовуються
    coin_used = [0] * (amount + 1)
    # Проходимося по всіх сумах від 1 до amount
    for i in range(1, amount + 1):
        # Проходимося по кожній монеті
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    # Якщо неможливо скласти суму з даних монет
    if dp[amount] == float('inf'):
        return {}
    # Відновлюємо використані монети
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    return result

# Приклад використання функцій
print("Жадібний алгоритм:", find_coins_greedy(113))
print("Динамічне програмування:", find_min_coins(113))
