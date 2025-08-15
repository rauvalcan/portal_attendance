# -*- coding: utf-8 -*-
{
    'name': "Portal de Asistencias de Empleados",
    'summary': """
        Permite a los usuarios del portal ver su propio registro de asistencias
        desde su cuenta personal.""",
    'description': """
        Este módulo añade una nueva sección en el portal de cliente/empleado 
        para que puedan consultar sus horas de entrada y salida (asistencias).
        - Añade un menú "Mis Asistencias" en el portal.
        - Muestra una vista de lista con las asistencias del usuario conectado.
        - Asegura que cada usuario solo pueda ver sus propios registros.
    """,
    'author': "Tu Nombre Aquí",
    'website': "https://www.tuweb.com",
    'category': 'Human Resources/Attendances',
    'version': '1.0',
    # Dependencias necesarias para que funcione
    'depends': ['portal', 'hr_attendance'],
    # Archivos que se cargarán (en orden)
    'data': [
        'security/ir.model.access.csv',
        'views/portal_attendance_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
