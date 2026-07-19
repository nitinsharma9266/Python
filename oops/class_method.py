class employee:
    a=1
    @classmethod  
    
    #cls means class ,class method ka kaam hota hai ki jo value class me de rakhi hai vahi show karega aur jo aapne 45 di hai vo nhi show karega.

    def show(cls):
        print(f"the value of class attribute is a {cls.a}")

e=employee()
e.a=45
e.show()