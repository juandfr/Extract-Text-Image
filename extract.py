import easyocr

# Define Português como idioma
reader = easyocr.Reader(['pt'])

# Lê a imagem
resultados = reader.readtext('placadecarro.png', paragraph=False)

# Itera sobre o resultado
for resultado in resultados:
    print(f'Texto da imagem:\n'
          f'\tPosição: {resultado[0]}\n'
          f'\tTexto: {resultado[1]}\n')