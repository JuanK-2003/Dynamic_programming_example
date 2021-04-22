import sys

def factorial_Dinamico( n , memo = {} ) :
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado = n*factorial_Dinamico(n-1, memo)
        memo[n] = resultado
        return resultado
    

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    while True:
        n = int(input('Elige un numero: '))
        resultado = factorial_Dinamico(n)
        print(resultado) 
        if n == 0:
            break
    