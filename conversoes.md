numeros = [0, 1, 2, 5, 7, 8, 10, 16, 31, 42, 64, 64, 100, 128, 128, 200, 255, 256, 1000]

print(f"{'DEC':>6} | {'BIN':>10} | {'OCT':>6} | {'HEX':>6}")
print("-" * 38)

for n in numeros:
    b = format(n, "b") # "B" = binario, sem prefixo 0b
    o = format(n, "0") # "0" = octal
    h = format(n, "x") # "X" = hexadecimal em MAIUSCULA
    print(f"{n:6}) | {b:>10} | {0:>6} | 0x{h:<4}") # <4 alinha a esquerda
