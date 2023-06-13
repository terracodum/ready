# import subprocess
#
# x = input('Введите q чтобы начать: ')
#
# try:
#     data = subprocess.check_output("netsh wlan show profiles").decode('cp866').split('\n')
#     profiles = [i.split(":")[1][1:-1] for i in data if "Все профили пользователей" in i]
#     pass_wifi = ''
#     for i in profiles:
#         results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp866').split('\n')
#         for j in results:
#             if "Содержимое ключа" in j:
#                 pass_wifi += f"{i} -- {j.split(':')[1][1:-1]}\n"
#                 print(pass_wifi)
# except Exception as ex:
#     print(f'Ошибка: {ex}')
47458321
def dels(n):
    res = []
    for i in range(1, 1 + int(n ** 0.5)):
        if n % i == 0:
            res.append(i)
            res.append(n // i)
    return sorted(res)

print(dels(47458321))