BASE_HOURS = 40  # Базовые часы в неделю.
ON_MULTIPLAYER = 1.5  # Мультипликатор сверхурочного времени.

# Получить отработанные часы и почасовую ставку оплаты труда.

hours_worked = float(input("Введите количество отработанных часов"))
hourly_rate = float(input("Введите почасовую ставку"))

if hours_worked > BASE_HOURS:

    # Сначала получить количество отработанных сверхурочных часов.
    overtime_hours = hours_worked - BASE_HOURS

    # Рассчитать оплату за работу в сверхурочное время.
    overtime_pay = overtime_hours * hourly_rate * ON_MULTIPLAYER

    # Рассчитать заработную плату до удержаний.
    gross_pay = BASE_HOURS * hourly_rate + overtime_pay

else:

    # Рассчитать заработную плату до удержаний без сверхурочных.
    gross_pay = hourly_rate * hours_worked

print("Заработная плата до удержаний составляет: $", format(gross_pay, ',.2f'), sep='')
