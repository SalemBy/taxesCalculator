
def transformN(real):
    return float(real.replace(',', '.'))

n1 = str(input("Type here your name: "))

def checkIfValueIsNumber():
    while True:
        try:

            g1 = transformN(str(input("Type here you gains per month: ")))
            t1 = transformN(str(input("Type here how many months did you worked: ")))
            b1 = (g1*t1)

            if g1 <= 1903.98:
                imp = 0
            if g1 >= 1903.99 < 2826.65:
                imp = 7.5
            if g1 >= 2826.66 <  3751.05:
                imp = 15
            if g1 >= 3751.06 < 4664.68:
                imp = 22.50
            if g1 >= 4664.69:
                imp = 27.50

            inss = (b1*imp)/100

            liq1 = b1 - inss
            
            line_1 = f'User: {n1}'
            line_2 = f'Total of salary in this cycle was {b1:,.2f}'
            line_3 = f'The salary with the INSS taxes this cycle was: {liq1:,.2f}'
            line_4 = f'Your taxes correspond to {imp:.2f}% of your salary'
            line_5 = f'The total payed in taxes this cycle was: {inss:,.2f} '
            
            print(line_1)
            print(line_2)
            print(line_3)
            print(line_4)
            print(line_5)

        except ValueError:
            print('Only type numbers')
            continue
        break

checkIfValueIsNumber()