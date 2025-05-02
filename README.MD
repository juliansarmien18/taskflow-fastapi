# 🧠 Proyecto Backend en FastAPI: TaskFlow

Una API para gestionar tareas personales con usuarios, etiquetas, estados y fechas de vencimiento. Implementada con FastAPI, SQLAlchemy, Alembic, Pydantic, Uvicorn y base de datos SQLite.

---

## 📌 Nombre del proyecto: `TaskFlow`

### 🎯 Objetivo
Una API RESTful para que los usuarios creen y gestionen tareas con autenticación, etiquetas y fechas.

---

## 🧠 Historias de Usuario (HU)

### 👤 HU01 - Registro de usuario
> Como usuario quiero registrarme con email y contraseña para gestionar mis propias tareas.
- Endpoint: `POST /user/create-user/`
- Email único
- Contraseña en hash

### 🔐 HU02 - Login y autenticación
> Como usuario quiero iniciar sesión para obtener un token de acceso a mis recursos.
- Endpoint: `POST /auth/token`
- JWT

### 📝 HU03 - Crear tarea
> Como usuario quiero crear una tarea con título, descripción, vencimiento y etiquetas para organizar mi día.
- Endpoint: `POST /taskflow/`
- Relación con el usuario autenticado
- Campo `completada` por defecto en `False`

### 📋 HU04 - Listar tareas
> Como usuario quiero ver una lista de mis tareas para saber qué tengo pendiente.
- Endpoint: `GET /taskflow/list-all` / `/taskflow/id`
- Filtros: completadas, vencidas, por etiqueta

### ✏️ HU05 - Actualizar tarea
> Como usuario quiero poder editar el contenido de una tarea para corregir o cambiar la información.
- Endpoint: `PUT /taskflow/{id}`

### 🗑️ HU06 - Eliminar tarea
> Como usuario quiero eliminar tareas que ya no necesito.
- Endpoint: `DELETE /taskflow/{id}`

---

## 🧱 Stack y arquitectura

| Tecnología        | Uso                          |
|-------------------|-------------------------------|
| FastAPI           | API REST                      |
| SQLAlchemy        | ORM                           |
| Alembic           | Migraciones                   |
| SQLite            | Base de datos                 |
| Pydantic          | Validación de datos           |
| Uvicorn           | Servidor ASGI                 |
| JWT               | Autenticación segura          |

---