def binario_int(n):
    if n == 0:
        return '0'
    else:
        binario = ''
        while n > 1:
            resto = n % 2
            n = int(n / 2)
            binario += str(resto)
        binario += '1'
    return binario[-1::1]
