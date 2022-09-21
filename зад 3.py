#f=добавка к мороженому
class IceCream:
    
    
    def __init__(self,f):
        if isinstance(f,str):
            self.f=f
        else:
            self.f=None


    def info_about_icecream(self):
        if self.f:
            print(f"мороженое и {self.f}")
        else:
            print("обычное мороженое")



a1=IceCream("черника")
a2=IceCream("малина")
a3=IceCream(4)
a1.info_about_icecream()
a2.info_about_icecream()
a3.info_about_icecream()
