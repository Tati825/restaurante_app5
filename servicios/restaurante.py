from typing import Optional
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    def __init__(self) -> None:

        #Lista de productos
        self._productos: list[Producto] = []

        #Lista de usuarios
        self._usuarios: list[Usuario] = []

        #Tupla de la informacipón del sistema
        self.informacion_sistema: tuple[str, str] = (
            "Restaurante App",
            "Sistema de administración de productos y usuarios",
        )

        #Diccionario relacionando clave->valor
        self.categorias: dict[str, str] = {
            "ENT": "Entrada",
            "PLA": "Plato principal",
            "BEB": "Bebida",
            "POS": "Postre",
        }

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        return True

    def buscar_producto(
        self,
        codigo: str
    ) -> Optional[Producto]:

        codigo = codigo.strip()

        for producto in self._productos:

            if producto.codigo.lower() == codigo.lower():
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.actualizar(
            nombre,
            categoria,
            precio
        )

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False

        self._productos.remove(producto)
        return True

    def listar_productos(self) -> list[Producto]:
        return self._productos.copy()

    def obtener_categorias_unicas(self) -> set[str]:
        return {
            producto.categoria
            for producto in self._productos
        }
      
    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario si su identificación no existe."""

        if self.buscar_usuario(
            usuario.identificacion
        ) is not None:
            return False

        self._usuarios.append(usuario)

        return True

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Optional[Usuario]:

        identificacion = identificacion.strip()

        for usuario in self._usuarios:
            if (
                usuario.identificacion.lower()
                == identificacion.lower()
            ):
                return usuario

        return None

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    def cantidad_productos(self) -> int:
        return len(self._productos)

    def cantidad_usuarios(self) -> int:
        return len(self._usuarios)
