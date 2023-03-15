

def numeros_pares_impares(num):
    if num % 2 == 0:  # El número es par
        for i in range(num, -1, -2): #-2 para que descienda de dos en dos
            print(i)
    else:  # El número es impar
        for i in range(num, 0, -2):
            print(i)


numeros_pares_impares(10)

numeros_pares_impares(7)  

print("TEST:")
def test_numeros_pares_impares():
    assert numeros_pares_impares(10) == [10, 8, 6, 4, 2, 0]
    assert numeros_pares_impares(7) == [7, 5, 3, 1]
    assert numeros_pares_impares(0) == [0]
    assert numeros_pares_impares(1) == [1]
    assert numeros_pares_impares(-5) == [-5, -3, -1]
    

