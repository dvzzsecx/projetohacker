# declarando as portas lógicas (vimos na aula anterior)
def AND(a, b): return a & b
def OR(a, b): return a | b
def NOT(a): return 1 - a
def XOR(a, b): return a ^ b

def half_adder(a, b):
    soma = XOR(a, b)  # a lampada "escreve": 1 só se forem diferentes
    vai_um = AND(a, b)  # a lampada "vai-um": só 1 + 1 acende ela
    return soma, vai_um

def full_adder(a, b, vem_um):
    s1, v1 = half_adder(a, b)  # caixa 1: soma só a e b
    soma, v2 = half_adder(s1, vem_um)  # caixa 2: soma o parcial com o troco que veio de antes
    vai_um = OR(v1, v2)  # os dois nunca acendem juntos, então um OR basta
    return soma, vai_um

def int_para_bits(n, largura=4):
    # quebra o número em bits, do mais à esquerda para o mais à direita
    # (n >> i) & 1 = "me dá só o bit da posição i"
    return [(n >> i) & 1 for i in range(largura - 1, -1, -1)]

def bits_para_int(bits):
    # caminho inverso: a cada bit, empurra o valor uma casa pra esquerda (x2) e soma o bit
    valor = 0
    for bit in bits:
        valor = valor * 2 + bit
    return valor

def somador_4bits(a_bits, b_bits, vem_um=0):
    # quatro full-adders em fila: o vai-um de um alimenta o próximo (ripple-carry)
    resultado = [0, 0, 0, 0]
    vai_um = vem_um
    for i in range(3, -1, -1):  # da coluna da direita (bit 0) para a da esquerda
        resultado[i], vai_um = full_adder(a_bits[i], b_bits[i], vai_um)
    return resultado, vai_um  # o vai-um que sobra no fim é o "estouro" (overflow)

def ula_4bits(a, b, opcode):
    ab, bb = int_para_bits(a), int_para_bits(b)
    vai_um = 0
    if opcode == 0b000:
        r, vai_um = somador_4bits(ab, bb)
    elif opcode == 0b001:
        b_inv = [NOT(x) for x in bb]
        r, vai_um = somador_4bits(ab, b_inv, 1)
    elif opcode == 0b010:
        r = [AND(x, y) for x, y in zip(ab, bb)]
    elif opcode == 0b011:
        r = [OR(x, y) for x, y in zip(ab, bb)]
    elif opcode == 0b100:
        r = [XOR(x, y) for x, y in zip(ab, bb)]
    elif opcode == 0b101:
        r = [NOT(x) for x in ab]
    else:
        raise ValueError(f"opcode desconhecido: {opcode:03b}")
    valor = bits_para_int(r)
    zero = 1 if valor == 0 else 0
    return valor, vai_um, zero  # mesma ordem que o print lá embaixo espera

print("\n=== FULL-ADDER ===")
print("a b vem-um | soma vai-um")
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            s, v = full_adder(a, b, c)
            print(f"{a} {b}    {c}     |  {s}      {v}")

a, b = 11, 6
print(f"\na = {a} ({a:04b})   b = {b} ({b:04b})")  # :04b = binário com 4 dígitos
print("opcode  op      resultado  bin   vai-um  zero")
for op, nome in [(0b000, "ADD"), (0b001, "SUB"), (0b010, "AND"),
                 (0b011, "OR"), (0b100, "XOR"), (0b101, "NOT_A")]:
    v, c, z = ula_4bits(a, b, op)  # é o mesmo circuito, seis operações
    print(f"{op:03b}     {nome:<6} {v:<10} {v:04b}  {c}      {z}")
