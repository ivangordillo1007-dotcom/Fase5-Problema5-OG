# =====================================================================
# Curso: Fundamentos de Programación (213022A_2201)
# Fase 5 - Evaluación Final POA
# Problema 5: Control de Horas Laborales y Sobretiempo 
# Estudiante: Oscar Ivan Gordillo Ramirez
# Código Fuente: autoría propia
# =====================================================================

# --- CONSTANTES ---
UMBRAL_ESTANDAR = 40
LIMITE_RECURSOS = 4

def mostrar_banner():
    """
    MÓDULO: Capa de Presentación (Banner).
    Dibuja el encuadre tipo banner
    """
    print("=" * 70)
    print(" 🏢   SISTEMA AUTOMATIZADO DE CONTROL DE TIEMPO LABORAL v3.0 (HMI)  ")
    print("=" * 70)
    print(f" CONFIGURACIÓN GLOBAL | Recursos máximos: {LIMITE_RECURSOS} | Umbral: {UMBRAL_ESTANDAR} hrs/sem.")
    print("-" * 70)

def capturar_datos_rh():
    """
    MÓDULO: Almacenamiento y Captura Dinámica.
    Permite al Jefe de RH ingresar los 4 recursos y sus horas en una sola línea.
    """
    matriz_personal = []
    print("\n[ FASE DE REGISTRO DE ASISTENCIA POR EL JEFE DE RH ]\n")
    
    for i in range(1, LIMITE_RECURSOS + 1):
        print(f"👤 RECURSO #{i}:")
        nombre = input("   -> Ingrese el Nombre: ").strip().upper()
        
        while True:
            entrada_horas = input("   -> Ingrese las horas de Lunes a Viernes (separadas por espacios): ")
            lista_temporal = entrada_horas.split()
            
            if len(lista_temporal) != 5:
                print("   ❌ Error: Debe ingresar exactamente 5 valores (uno por cada día de Lunes a Viernes).")
                continue
                
            try:
                horas_enteros = [int(hora) for hora in lista_temporal]
                
                if any(h < 0 for h in horas_enteros):
                    print("   ❌ Error: Las horas no pueden ser valores negativos.")
                    continue
                    
                break
            except ValueError:
                print("   ❌ Error: Ingrese únicamente números enteros válidos.")
        
        fila_recurso = [nombre] + horas_enteros
        matriz_personal.append(fila_recurso)
        print("   ✅ Datos registrados correctamente.\n")
        
    return matriz_personal

def calcular_y_clasificar_jornada(recurso):
    """
    MÓDULO: Lógica de Negocio.
    Procesa una fila de la matriz, calcula la sumatoria y define el estado.
    Clasifica en: 'Sobretiempo', 'Horario Estándar' (exactamente 40) o 'Inferior' (menos de 40).
    """
    nombre = recurso[0]
    horas_diarias = recurso[1:] 
    
    total_horas = sum(horas_diarias)
    
    if total_horas > UMBRAL_ESTANDAR:
        clasificacion = "Sobretiempo"
    elif total_horas == UMBRAL_ESTANDAR:
        clasificacion = "Horario Estándar"
    else:
        clasificacion = "Inferior"
        
    return nombre, total_horas, clasificacion

def generar_tabla_reporte(matriz_personal):
    """
    MÓDULO: Capa de Presentación (Tabla).
    """
    print("\n" + "=" * 70)
    print("                     TABLA RESUMEN DE DESEMPEÑO")
    print("=" * 70)
    print(f"{'NOMBRE DEL RECURSO':<25} | {'HORAS SEMANALES':<18} | {'CLASIFICACIÓN JORNADA':<20}")
    print("-" * 70)
    
    for fila in matriz_personal:
        nombre, total, estado = calcular_y_clasificar_jornada(fila)
        print(f"{nombre:<25} | {total:<18} | {estado:<20}")
        
    print("=" * 70)
    print("🏁 Fin del reporte. Datos listos para la toma de decisiones en RH.\n")

def main():
    """
    MÓDULO PRINCIPAL: Orquestador del flujo del programa.
    """
    mostrar_banner()
    
    matriz_sistema = capturar_datos_rh()
    
    generar_tabla_reporte(matriz_sistema)

if __name__ == "__main__":
    main()
    input("Presione Enter para cerrar la aplicación...")
