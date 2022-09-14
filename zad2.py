d=float(input("Введите число"))
def nom(d):
    if d%2==0 or (d+1)%2==0:
        return True
    return False
print(nom(d))