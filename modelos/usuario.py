#Creación de la clase Usuario
class Usuario:
    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ) -> None:

        self.identificacion = self._validar_texto(
            identificacion,
            "La identificación no puede estar vacía"
        )

        self.nombre = self._validar_texto(
            nombre,
            "El nombre no puede estar vacío"
        )

        self.correo = self._validar_correo(correo)

    @staticmethod
    def _validar_texto(valor: str, mensaje: str) -> str:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(mensaje)
        return valor.strip()

    @staticmethod
    def _validar_correo(correo: str) -> str:
        if (
            not isinstance(correo, str)
            or "@" not in correo
            or "." not in correo
        ):
            raise ValueError(
                "El correo electrónico no tiene un formato válido."
            )

        return correo.strip()

    def __str__(self) -> str:
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )
