import random

def generate_credit_card():
    # Generar los primeros 15 dígitos del número de tarjeta de crédito
    card_number = "483316016989" + str(random.randint(100, 999))

    # Calcular el dígito de verificación utilizando el algoritmo de Luhn
    digits = [int(x) for x in card_number]
    for i in range(len(digits)):
        if i % 2 == 0:
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

    checksum = sum(digits) % 10
    if checksum != 0:
        checksum = 10 - checksum

    # Generar el número de tarjeta de crédito completo
    card_number += str(checksum)

    # Generar el mes de vencimiento
    expiration_month = random.randint(1, 12)

    # Generar el año de vencimiento
    expiration_year = random.randint(2023, 2033)

    # Generar el código de seguridad (CVV)
    cvv = random.randint(100, 999)

    return card_number, expiration_month, expiration_year, cvv

# Generar 10 tarjetas de crédito
for _ in range(10):
    card_number, expiration_month, expiration_year, cvv = generate_credit_card()
    print(card_number,"|",expiration_month,"|",expiration_year,"|",cvv)
    print("---")
