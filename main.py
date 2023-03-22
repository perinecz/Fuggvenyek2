# functions
def fuggveny(xx):
    return 3*xx**2 - 7*xx + 5

#0
print("Függvényértékek meghatározása.")

#1
a = float(input("a = ").replace(',' , '.'))
b = float(input("b = ").replace(',' , '.'))
d = float(input("d = ").replace(',' , '.'))

#2
if a>b:
    a, b = b, a

x = []
y = []
while a<=b:
    x.append(a)
    y.append(fuggveny(a))
    a += d


#3
print(f"{'x':^10} | {'y':^10}")
print('_'*23)
for i in range(len(x)):
    print(f"{x[i]:10.2f} | {y[i]:10.2f}")
