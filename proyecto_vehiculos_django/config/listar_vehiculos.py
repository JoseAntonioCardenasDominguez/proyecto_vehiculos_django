<!-- vehiculo/templates/vehiculo/listar_vehiculos.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Listar Vehículos</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.3.1/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Vehículos</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'index' %}">Inicio</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'agregar_vehiculo' %}">Agregar</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'listar_vehiculos' %}">Listar</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        <h1>Listado de Vehículos</h1>
        <table class="table">
            <thead>
                <tr>
                    <th>Marca</th>
                    <th>Modelo</th>
                    <th>Serial Carrocería</th>
                    <th>Serial Motor</th>
                    <th>Categoría</th>
                    <th>Precio</th>
                </tr>
            </thead>
            <tbody>
                {% for vehiculo in vehiculos %}
                <tr>
                    <td>{{ vehiculo.marca }}</td>
                    <td>{{ vehiculo.modelo }}</td>
                    <td>{{ vehiculo.serial_carroceria }}</td>
                    <td>{{ vehiculo.serial_motor }}</td>
                    <td>{{ vehiculo.categoria }}</td>
                    <td>{{ vehiculo.precio }}</td>
                </tr>
                {% empty %}
                <tr>
                    <td colspan="6">No hay vehículos registrados.</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        <a href="{% url 'index' %}" class="btn btn-secondary">Volver</a>
    </div>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.1/js/bootstrap.min.js"></script>
</body>
</html>
