# Variables
B_ALTA_DIRECTIVO = 0.20
B_MEDIA_DIRECTIVO = 0.10
B_ALTA_OPERATIVO = 0.15
B_MEDIA_OPERATIVO = 0.05

# operaciones
def operaciones(nivel_desempeno, cargo, salario):
    if cargo == "directivo" and nivel_desempeno == "alto":
        bonificacion = salario * B_ALTA_DIRECTIVO
        total_recibir = salario + bonificacion
    elif cargo == "directivo" and nivel_desempeno == "medio":
        bonificacion= salario * B_MEDIA_DIRECTIVO
        total_recibir = salario + bonificacion
    elif cargo == "operativo" and nivel_desempeno == "alto":
        bonificacion = salario * B_ALTA_OPERATIVO
        total_recibir = salario + bonificacion
    elif cargo == "operativo" and nivel_desempeno == "medio":
        bonificacion = salario * B_MEDIA_OPERATIVO
        total_recibir = salario + bonificacion
    else:
        bonificacion=0
        return None
    return nivel_desempeno, cargo, salario, bonificacion, total_recibir

def generar_mensaje(cargo, nivel_desempeno, salario, total_recibir, bonificacion):
    return (f"Cargo: {cargo}\n"
            f"Nivel de desempeno: {nivel_desempeno}\n"
            f"Salario Base: ${salario}\n"
            f"Bonificación: ${bonificacion}\n"
            f"Total a Recibir: ${total_recibir}\n")
#validar mensaje
def validar_datos(nivel_desempeno, cargo, salario):
    resumen="Resumen de Pago"
    if cargo != "operativo" or cargo != "directivo" and nivel_desempeno != "alto" or nivel_desempeno != "medio" or nivel_desempeno != "bajo":
        cargo=cargo.lower()
        nivel_desempeno=nivel_desempeno.lower()
        resultado= operaciones(nivel_desempeno, cargo, salario)
        nivel_desempeno, cargo, salario, bonificacion, total_recibir = resultado
        mensaje= generar_mensaje(cargo, nivel_desempeno, salario, int(total_recibir), int(bonificacion))
        print(resumen.center(45, "-"))
        print(mensaje+" \n-------------------------------------")
    else:
        print("Verifique los datos")
#entradas
salario=int (input("Salario base mensual $: "))
cargo= input("Cargo empleado: ")
nivel_desempeno= input("Nivel de desempeno: ")

#salidas
validar_datos(nivel_desempeno, cargo, salario)