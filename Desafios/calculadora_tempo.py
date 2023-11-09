total = 2000000
sobra = total

# total semanas
semana = int(sobra / 604800)
sobra = sobra % 604800

# total dias
dia = int(sobra / 86400)
sobra = sobra % 86400

# total de horas
horas = int(sobra / 3600)
sobra = sobra % 3600

# minutos/segundos
minutos = int(sobra / 60)
sobra = sobra % 60

#segundos
segundos = sobra

print(f'{total} segundos equivalem a {semana}, {dia} dia, {horas} horas e {minutos} minutos {segundos} segundos.')