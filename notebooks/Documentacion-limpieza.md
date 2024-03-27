**CAMBIOS REALIZADOS**

COLUMNAS ELIMINADAS:

- 'employeecount': todos tenían el mismo valor (1)
- 'NUMBERCHILDREN': la columna no tenía ningún dato
- 'SameAsMonthlyIncome': era la copia exacta de monthly_income
- 'Salary': todos tenían el mismo valor y además era un valor claramente erróneo (1000000000$)
- 'Over18': No aporta ningún dato extra que no aporte el año de nacimiento y es un valor que podría variar de un año a otro por lo que requiere mantenimiento
- 'Age': No aporta ningún dato extra que no aporte el año de nacimiento, es un valor que podría variar de un año a otro por lo que requiere mantenimiento lo que puede llevar a errores. De hecho, muchos casos tenía nulos y valores que no concuerdan con el año de nacimiento por lo que hemos decidido quedarnos con date_birth que es más fiable y seguro
- 'StandardHours': tenía un 74% de nulos y además, los datos que tenía eran todos el mismo: 80h
- 'RoleDepartment': los datos de esta columna ya los tenemos por separado en otras dos columnas: JobRole y Departament
- 'standard_hours' : tiene muchos nulos  y el resto tienen todos el mismo dato : 80.0
- 'years_in_current_role' : tiene muchos nulos (97.9%) 
DUPLICADOS:

- Hemos eliminado los duplicados exactos (registros totalmente iguales)
- Hemos revisado el resto de duplicados y decidido dejarlos como están

CAMBIOS DE TIPOS DE DATO:

- Hemos convertido en booleanos y cambiado los valores por True y False (para homogenizarlos) en las columnas:
    - 'Attrition', 'RemoteWork', 'OverTime'
- Hemos convertido en float los valores numéricos en las columnas: 
    - 'employeenumber', 'PerformanceRating', 'TOTALWORKINGYEARS', 'YearsInCurrentRole', 'DailyRate', 'WORKLIFEBALANCE', 'MonthlyIncome'
- Hemos homogenizado los valores tipo object poniéndolos en minúscula y quitande espacios antes y después del valor en las columnas:
    - columnas obj
COLUMNAS:

- Hemos renombrado las columnas poniendo _ donde debería haber espacios y quitando mayúsculas

VALORES:

- Hemos cambiado los valores de  'BusinessTravel' para hacerlos más amigables:
    - {"non-travel":"no", "travel_rarely":"rarely", "travel_frequently":"frequently"}
- Hemos visto que hay valores negativos en "DistanceFromHome" y al analizarlo hemos visto que parecía que el único error era el símbolo ya que eran distancias realistas, por lo que hemos convertido todos los valores en positivo.
- Hemos cambiado los valores de Gender para hacerlos más amigables:
    - ({1: "F", 0: 'M'})
- Hemos corregido errores en la escritura de la columna 'MaritalStatus' (en algunos casos estaba escrito 'marreid' en lugar de 'married')
- Hemos cambiado los datos tipo 'Not Available' por nulos
- Hemos pasado los datos de "PercentSalaryHike" a porcentajes como indica su nombre