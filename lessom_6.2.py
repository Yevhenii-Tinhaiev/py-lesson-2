sec_input = int(input("Введіть кількість секунд: "))
days, sec_input = divmod(sec_input, 86400)
hours, sec_input = divmod(sec_input, 3600)
minutes, seconds = divmod(sec_input, 60)
if days == 1:
    day_str = "день"
elif 2 <= days <= 4:
    day_str = "дні"
else:
    day_str = "днів"
time = f"{days} {day_str}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(time)