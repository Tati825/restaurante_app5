from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

def solicitar_precio() -> float:
    while True:

        try:
            precio = float(
                input("Precio: ").strip()
            )

            if precio <= 0:
                print(
                    "El precio debe ser mayor que cero."
                )
                continue

            return precio

        except ValueError:
            print(
                "Ingrese un valor numérico válido."
            )


def registrar_producto(
    restaurante: Restaurante
) -> None:

    print("\n--- REGISTRAR PRODUCTO ---")

    try:
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()

        precio = solicitar_precio()

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        if restaurante.registrar_producto(producto):
            print(
                "Producto registrado correctamente."
            )
        else:
            print(
                "No se pudo registrar: "
                "el código ya existe."
            )

    except ValueError as error:
        print(f"Error: {error}")


def buscar_producto(
    restaurante: Restaurante
) -> None:

    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input(
        "Código del producto: "
    ).strip()

    producto = restaurante.buscar_producto(codigo)

    if producto:
        print("\nProducto encontrado:")
        print(producto)
    else:
        print("Producto no encontrado.")


def actualizar_producto(
    restaurante: Restaurante
) -> None:

    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = input(
        "Código del producto: "
    ).strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print("\nDatos actuales:")
    print(producto)

    try:
        nombre = input(
            "Nuevo nombre: "
        ).strip()

        categoria = input(
            "Nueva categoría: "
        ).strip()

        precio = solicitar_precio()

        if restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio
        ):
            print(
                "Producto actualizado correctamente."
            )

    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto(
    restaurante: Restaurante
) -> None:

    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input(
        "Código del producto: "
    ).strip()

    if restaurante.eliminar_producto(codigo):
        print(
            "Producto eliminado correctamente."
        )
    else:
        print("Producto no encontrado.")


def listar_productos(
    restaurante: Restaurante
) -> None:
  
    print("\n--- LISTA DE PRODUCTOS ---")
    productos = restaurante.listar_productos()

    if not productos:
        print(
            "No existen productos registrados."
        )
        return

    for producto in productos:
        print(producto)

    categorias = (
        restaurante.obtener_categorias_unicas()
    )

    print(
        "\nCategorías únicas:"
    )

    for categoria in sorted(categorias):
        print(f"- {categoria}")

def registrar_usuario(
    restaurante: Restaurante
) -> None:

    print("\n--- REGISTRAR USUARIO ---")

    try:
        identificacion = input(
            "Identificación: "
        ).strip()

        nombre = input(
            "Nombre: "
        ).strip()

        correo = input(
            "Correo: "
        ).strip()

        usuario = Usuario(
            identificacion,
            nombre,
            correo
        )

        if restaurante.registrar_usuario(usuario):
            print(
                "Usuario registrado correctamente"
            )
        else:
            print(
                "No se pudo registrar: "
                "la identificación ya existe"
            )

    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios(
    restaurante: Restaurante
) -> None:

    print("\n--- LISTA DE USUARIOS ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print(
            "No existen usuarios registrados"
        )
        return

    for usuario in usuarios:
        print(usuario)


def mostrar_informacion_sistema(
    restaurante: Restaurante
) -> None:

    nombre_sistema, descripcion = (
        restaurante.informacion_sistema
    )

    print("\n--- INFORMACIÓN DEL SISTEMA ---")

    print(
        f"Sistema: {nombre_sistema}"
    )

    print(
        f"Descripción: {descripcion}"
    )

    print("\nCategorías disponibles:")

    for codigo, nombre in (
        restaurante.categorias.items()
    ):
        print(
            f"{codigo} -> {nombre}"
        )

def mostrar_menu() -> None:

    print("\n" + "=" * 50)
    print("              RESTAURANTE APP")
    print("=" * 50)

    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("8. Información del sistema")
    print("0. Salir")

    print("=" * 50)

def ejecutar() -> None:
    restaurante = Restaurante()

    while True:
        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        try:

            if opcion == "1":
                registrar_producto(restaurante)

            elif opcion == "2":
                buscar_producto(restaurante)

            elif opcion == "3":
                actualizar_producto(restaurante)

            elif opcion == "4":
                eliminar_producto(restaurante)

            elif opcion == "5":
                listar_productos(restaurante)

            elif opcion == "6":
                registrar_usuario(restaurante)

            elif opcion == "7":
                listar_usuarios(restaurante)

            elif opcion == "8":
                mostrar_informacion_sistema(
                    restaurante
                )

            elif opcion == "0":
                print(
                    "Programa finalizado"
                )
                break

            else:
                print(
                    "Opción inválida"
                    "Seleccione una opción del menú"
                )

        except Exception as error:
            print(
                f"Ocurrió un error inesperado: {error}"
            )

if __name__ == "__main__":
    ejecutar()
