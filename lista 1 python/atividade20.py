blusa = float(input("Insira a quantidade de blusas: "))
fio_por_blusa = 120
fio_por_novelo = 12
novelos_blusa = (fio_por_blusa // fio_por_novelo)
print(f"Quantidade de novelos necessários para cada blusa: {novelos_blusa}")
total_novelos = novelos_blusa * blusa
print(f"Quantidade total de novelos para {blusa} blusas: {total_novelos}")