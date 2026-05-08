import csv
import json
import calendar
from collections import defaultdict

# Usamos un diccionario para agrupar los datos por mes
datos_por_mes = defaultdict(lambda: {"presupuesto": 0, "gastos": []})

with open('gastos.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        fecha = row['Fecha']
        mes_anio = fecha[:7]  # Extrae "YYYY-MM" (ej: "2026-05")
        dia = int(fecha.split('-')[2])
        
        total_gasto = float(row['Gasto_A']) + float(row['Gasto_B'])
        presupuesto = float(row['Presupuesto'])
        
        datos_por_mes[mes_anio]["presupuesto"] = presupuesto
        datos_por_mes[mes_anio]["gastos"].append({
            "dia": dia,
            "total": total_gasto
        })

# Preparamos el formato final añadiendo los días que tiene cada mes
output = {}
for mes, datos in datos_por_mes.items():
    year, month = map(int, mes.split('-'))
    dias_del_mes = calendar.monthrange(year, month)[1]
    
    output[mes] = {
        "dias_del_mes": dias_del_mes,
        "presupuesto": datos["presupuesto"],
        "gastos": datos["gastos"]
    }

# Guardamos el JSON con todo el histórico
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=4)

print("JSON histórico generado con éxito.")
