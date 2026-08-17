# Cración de la clase Producto
class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> None:
        self.codigo = self._validar_texto(
            codigo,
            "El código no puede estar vacío"
        )

        self.nombre = self._validar_texto(
            nombre,
            "El nombre no puede estar vacío"
        )

        self.categoria = self._validar_texto(
            categoria,
            "La categoría no puede estar vacía"
        )

        try:
            precio_numerico = float(precio)
        except (TypeError, ValueError) as exc:
            raise ValueError(
                "El precio debe ser un número válido"
            ) from exc

        if precio_numerico <= 0:
            raise ValueError(
                "El precio debe ser mayor que cero"
            )

        self.precio = precio_numerico

    @staticmethod
    def _validar_texto(valor: str, mensaje: str) -> str:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(mensaje)
        return valor.strip()

    def actualizar(
        self,
        nombre: str,
        categoria: str,
        precio: float
    ) -> None:

        self.nombre = self._validar_texto(
            nombre,
            "El nombre no puede estar vacío."
        )

        self.categoria = self._validar_texto(
            categoria,
            "La categoría no puede estar vacía."
        )

        try:
            precio_numerico = float(precio)
        except (TypeError, ValueError) as exc:
            raise ValueError(
                "El precio debe ser un número válido."
            ) from exc

        if precio_numerico <= 0:
            raise ValueError(
                "El precio debe ser mayor que cero."
            )

        self.precio = precio_numerico

    def __str__(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f}"
        )
