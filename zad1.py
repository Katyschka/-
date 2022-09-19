x=2
y=5
def Ket(x,y):
    if y==1:
        return x
    if y!=1:
        return x*Ket(x,y-1)

print("Возведение в степень равен:",Ket(x,y))