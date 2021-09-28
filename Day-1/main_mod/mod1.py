def tabel():
    num = int(input("Enter the value:"))
    for i in range(1,11):
        num2 = i * num
        print(f"{num} * {i} = {num2}")
        
def func2(var1,var2):
    var3 = var1 + var2
    print("Sum:",var3)