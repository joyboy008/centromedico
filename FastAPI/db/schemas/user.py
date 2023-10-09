from db.models.basemodel import Paciente


def paciente_schema(paciente: Paciente) -> dict:
    json = {
        "id": str(paciente["_id"]),
        "idPaciente": int(paciente["idPaciente"]),
        "consulta_numero": str(paciente["consulta_numero"]),
        "consulta_dia": str(paciente["consulta_dia"]),
        "dpi": str(paciente["dpi"]),
        "nombre": str(paciente["nombre"]),
        "fechaNacimiento": str(paciente["fechaNacimiento"]),
        "genero": str(paciente["genero"]),
        "direccion": str(paciente["direccion"]),
        "municipio": str(paciente["municipio"]),
        "departamento": str(paciente["departamento"]),
        "nacionalidad": str(paciente["nacionalidad"]),
        "telefono": int(paciente["telefono"]),
        "email": str(paciente["email"]),
        "igss": str(paciente["igss"]),
        "consulta_motivo": str(paciente["consulta_motivo"]),
        "numero_expediente": int(paciente["numero_expediente"])
        if "numero_expediente" in paciente
        else None,
        "etnia": str(paciente["etnia"]) if "etnia" in paciente else None,
        "ocupacion": str(paciente["ocupacion"]) if "ocupacion" in paciente else None,
        "estado_civil": str(paciente["estado_civil"])
        if "estado_civil" in paciente
        else None,
        "diagnostico": str(paciente["diagnostico"])
        if "diagnostico" in paciente
        else None,
        "tratamiento": str(paciente["tratamiento"])
        if "tratamiento" in paciente
        else None,
        "emergencia_nombre": str(paciente["emergencia_nombre"])
        if "emergencia_nombre" in paciente
        else None,
        "emergencia_telefono": int(paciente["emergencia_telefono"])
        if "emergencia_telefono" in paciente
        else None,
        "emergencia_parentesco": str(paciente["emergencia_parentesco"])
        if "emergencia_parentesco" in paciente
        else None,
        "diagnostico_egreso": str(paciente["diagnostico_egreso"])
        if "diagnostico_egreso" in paciente
        else None,
        "complicaciones": str(paciente["complicaciones"])
        if "complicaciones" in paciente
        else None,
        "operaciones": str(paciente["operaciones"])
        if "operaciones" in paciente
        else None,
        "dias_estancia": str(paciente["dias_estancia"])
        if "dias_estancia" in paciente
        else None,
        "autopsia": str(paciente["autopsia"]) if "autopsia" in paciente else None,
        "causa_de_muerte": str(paciente["causa_de_muerte"])
        if "causa_de_muerte" in paciente
        else None,
    }
    return json


def user_schema(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
    }


def users_schema(users) -> dict:
    return [user_schema(user) for user in users]


def pacientes_schema(pacientes) -> dict:
    return [paciente_schema(paciente) for paciente in pacientes]
