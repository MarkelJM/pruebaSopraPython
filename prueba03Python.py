horas_trabajadas = float(input("¿Cuántas horas has trabajado?: "))
tarifa_hora = float(input("¿Cuál es tu 'tarifa' sueldo/hora?: "))

horas_minimas = 40
multiplicador_horas_extra = 1.5

#si trabaja  horas extra habrá que calcular el importe de ésta
if horas_trabajadas > horas_minimas:
    sueldo = ( horas_minimas * tarifa_hora) +  ((horas_trabajadas - horas_minimas) *     tarifa_hora * multiplicador_horas_extra)    
else:
    sueldo = horas_trabajadas * tarifa_hora

print(f"El sueldo del trabajador es: {sueldo} €")


