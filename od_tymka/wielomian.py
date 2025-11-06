n=(int(input("Prosze podac stopien wielomianu")))
X=(int(input("Prosze podac wart. X")))
an=int(input("prosze podaj 0 ty wspolczynnik"))
wx=an*X
i=n-1
while i>0:      
    an=int(input(f"prosze podaj {n-i} ty wspolczynnik"))
    wx=n+an*X**(n-i)
    i=i-1
print("wartosc wielomianu wynosi {wx}".format(wx=wx))
