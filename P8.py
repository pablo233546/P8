# найважливіше: init(), Fore, Back, Style.
# чому: саме вони дають можливість швидко і просто керувати кольорами та стилями тексту в консолі.
# фішка: параметр autoreset=True у init() — дуже зручний, бо не треба вручну додавати Style.RESET_ALL після кожного рядка.
#приклад використання
from colorama import init, Fore, Back, Style

# ініціатива
init(autoreset=True)

print(Fore.RED + "цей текст червоний")
print(Back.GREEN + " тут зелений фон")
print(Style.BRIGHT + Fore.BLUE + "яскравий синій текст")
print(Style.RESET_ALL + "норм текст")