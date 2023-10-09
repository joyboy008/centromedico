from pydantic import BaseModel


class Paciente11(BaseModel):
    id: str | None
    dpi: str
    nombre: str
    apellido: str


class User(BaseModel):
    id: str | None
    username: str | None
    email: str | None


class Paciente(BaseModel):
    id: str | None
    idPaciente: int
    consulta_numero: str
    consulta_dia: str
    dpi: str
    nombre: str
    fechaNacimiento: str
    genero: str
    direccion: str
    municipio: str
    departamento: str
    nacionalidad: str
    telefono: int
    email: str
    igss: str
    consulta_motivo: str
    numero_expediente: int | None
    etnia: str | None
    ocupacion: str | None
    estado_civil: str | None
    diagnostico: str | None
    tratamiento: str | None
    emergencia_nombre: str | None
    emergencia_telefono: int | None
    emergencia_parentesco: str | None
    diagnostico_egreso: str | None
    complicaciones: str | None
    operaciones: str | None
    dias_estancia: str | None
    autopsia: str | None
    causa_de_muerte: str | None


class Paciente1(BaseModel):  # Renombrar por Paciente
    id: str | None
    dpi: str
    igss: str
    igss_derecho: str
    idPaciente: int
    paciente_codigo: int
    nombre: str
    apellido: str
    etnia: str
    numero_expediente: int
    fechaNacimiento: str
    genero: str
    direccion: str
    municipio: str
    departamento: str
    nacionalidad: str
    telefono: int
    email: str
    ocupacion: str
    seguro: str
    estado_civil: str
    consulta_motivo: str
    consulta_dia: str
    consulta_numero: str
    diagnostico: str
    tratamiento: str
    fecha: str
    emergencia_nombre: str
    emergencia_apellido: str
    emergencia_parentesco: str
    emergencia_telefono: int
    hospitalizacion: str | None
    diagnostico_egreso: str | None
    diagnostico_egreso_codigo: int | None
    tratamiento_hospital: str | None
    complicaciones: str | None
    complicaciones_codigo: int | None
    operaciones: str | None
    operaciones_codigo: int | None
    egreso: str | None
    autopsia: str | None
    causa_de_muerte: str | None


class Enfermero(BaseModel):
    idEmpleado: int
    nombre: str
    apellido: str
    pw: str  # Considera usar un campo específico para contraseñas como PasswordStr
    pwhash: str
    especialidad: str
    igss: str
    fechaNacimiento: str  # Podrías considerar usar un campo específico para fechas
    genero: int
    direccion: str
    telefono: int
    email: str
    seguro: str
    estado_civil: str
    emergencia_nombre: str
    emergencia_apellido: str
    emergencia_parentesco: str
    emergencia_telefono: int
    salario: float
    bonos: float | None
    descuentos: float | None


class Secretaria(BaseModel):
    idEmpleado: int
    nombre: str
    apellido: str
    pw: str  # Considera usar un campo específico para contraseñas como PasswordStr
    pwhash: str
    especialidad: str
    igss: str
    fechaNacimiento: str  # Podrías considerar usar un campo específico para fechas
    genero: int
    direccion: str
    telefono: int
    email: str
    seguro: str
    estado_civil: str
    emergencia_nombre: str
    emergencia_apellido: str
    emergencia_parentesco: str
    emergencia_telefono: int
    salario: float
    bonos: float | None
    descuentos: float | None


class Doctor(BaseModel):
    idDoctor: int
    nombre: str
    apellido: str
    pw: str
    pwhash: str
    especialidad: str
    igss: str
    horario_ingreso: str
    horario_egreso: str
    horario3: str
    fechaNacimiento: str
    genero: int
    direccion: str
    telefono: int
    email: str
    seguro: str
    estado_civil: str
    confirmacion: str
    chatbot_conversacion: str
    emergencia_nombre: str
    emergencia_apellido: str
    emergencia_parentesco: str
    emergencia_telefono: int
    paciente_clase: str | None
    salario: float
    bonos: float | None
    descuentos: float | None


class Admon(BaseModel):
    idAdmon: int
    nombre: str
    apellido: str
    pw: str
    pwhash: str
    especialidad: str
    igss: str
    horario_ingreso: str
    horario_egreso: str
    horario3: str
    fechaNacimiento: str
    genero: int
    direccion: str
    telefono: int
    email: str
    seguro: str
    estado_civil: str
    confirmacion: str
    emergencia_nombre: str
    emergencia_apellido: str
    emergencia_parentesco: str
    emergencia_telefono: int
    salario: float
    bonos: float | None
    descuentos: float | None
