import time
import string

def get_value(msg: str, key = None, error_msg = None | str) -> int:
    while True:
        try:
            value = int(input(msg))
        except ValueError:
            print("Please enter a parsable integer.")
            continue
        if key:
            if key(value):
                break
            else:
                print(error_msg)
        break
    return value

b_10 = get_value("Enter the number you would like to change the base of(in base 10): ")
target_base = get_value("Enter the base you would like to change to(2 <= base <= 36): ",
                        key = lambda x: 2 <= x <= 36, 
                        error_msg = "Ensure that the base is in the provided range")

encoding_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}
def change_base(b_10: int, target_base: int) -> str:
    if b_10 == 0: return "0"
    sign = -1 if b_10 < 0 else 1
    number *= sign
    div, mod = divmod(b_10, target_base)
    num = [mod]
    while div != 0:
        div, mod = divmod(div, target_base)
        num.append(mod)
    encoding = "".join(f"({encoding_map[num]})" for num in num[::-1])
    if sign == -1:
        encoding = "-" + encoding
    return(encoding)


print(change_base(b_10=b_10, target_base=target_base))

