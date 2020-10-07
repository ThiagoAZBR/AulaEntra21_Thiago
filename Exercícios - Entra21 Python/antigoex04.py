preço = 24.95
regrade3 = preço / (40.0*100.0)
logistica = (60.0 * 0.75) + 3.0
total = (preço - regrade3) + logistica
print(f'O Total é R$: {total:.2f}')