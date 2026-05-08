import csv
import json
import calendar
from datetime import datetime

# 1. Obtener el mes actual
hoy = datetime.now()
mes_actual = hoy.strftime('%Y-%m') # Formato: "2026-05"
dias_del_mes = calendar.monthrange(hoy.year, hoy.month)[1]

datos_mes = []
presupuesto_actual = 0

# 2. Leer el CSV
with open('gastos.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Filtrar solo los del mes actual
        if row['Fecha'].startswith(mes_actual):
            dia = int(row['Fecha'].split('-')[2])
            total_gasto = float(row['Gasto_A']) + float(row['Gasto_B'])
            presupuesto_actual = float(row['Presupuesto'])
            
            datos_mes.append({
                "dia": dia,
                "total": total_gasto
            })

# 3. Preparar el JSON final
output = {
    "mes": mes_actual,
    "dias_del_mes": dias_del_mes,
    "presupuesto": presupuesto_actual,
    "gastos": datos_mes
}

# 4. Guardar el JSON
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=4)

print(f"JSON generado para {mes_actual} con éxito.")
