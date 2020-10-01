cod1, quant1, unitprice1 = input().split()
cod2, quant2, unitprice2 = input().split()

calculation = int(quant1) * float(unitprice1) + int(quant2) * float(unitprice2)
print(f'VALOR A PAGAR: R$ {calculation:.2f}')