import time
from machine import Pin

segmento = [
    Pin(2, Pin.OUT),  # A
    Pin(4, Pin.OUT),  # B
    Pin(5, Pin.OUT),  # C
    Pin(12, Pin.OUT), # D
    Pin(13, Pin.OUT),  # E
    Pin(14, Pin.OUT),  # F
    Pin(18, Pin.OUT),  # G
]

chaves = [
    Pin(33, Pin.IN), # Chave 1
    Pin(19, Pin.IN), # Chave 2
    Pin(21, Pin.IN), # Chave 3
    Pin(22, Pin.IN), # Chave 4
    Pin(15, Pin.IN) # Chave Mestra
]

valor = [
    0b11000000, # 0
    0b11111001, # 1
    0b10100100, # 2 
    0b10110000, # 3
    0b10011001, # 4
    0b10010010, # 5
    0b10000010, # 6
    0b11111000, # 7
    0b10000000, # 8
    0b10011000, # 9
    0b10001000, # A
    0b10000011, # B
    0b11000110, # C
    0b10100001, # D
    0b10000110, # E
    0b10001110,  # F
]


def mostrar_valor(valor):
    for i in range(7):
        segmento[i].value((valor & (1 << i)) != 0)

def sequencia():
    for num_binario in valor:
        mostrar_valor(num_binario)
        time.sleep(0.5)

    for num_binario in reversed(valor):
        mostrar_valor(num_binario)
        time.sleep(0.5)

def main():
    while True:
        if chaves[-1].value():
            indice = sum(chave.value() << i for i, chave in enumerate(chaves[:-1]))
            mostrar_valor(valor[indice])
        else:
            sequencia()

main()