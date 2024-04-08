import numpy as np
import pandas as pd
import re
from scipy.stats import chi2_contingency

# LIMPIEZA
lista_bool = ['Attrition', 'RemoteWork', 'OverTime']
lista_float =  ['employeenumber', 'PerformanceRating', 'TOTALWORKINGYEARS','DailyRate', 'WORKLIFEBALANCE', 'MonthlyIncome']

def true_false(valor):

    if valor in ['Yes', 'yes', '1', 'Y']:
        valor = True
    
    elif valor in ['False', 'No', '0', 'false']:
        valor = False
    

    else:
        valor = np.nan

    return valor

def to_float(valor):
    try:
        if type(valor) != str or np.nan:
            str(valor)
        
            
        if '$' in valor:
            valor = valor.replace('$', '')
        elif '%' in valor:
            valor = valor.replace('%', '')
        return float(valor.replace(",", "."))     
    except:
        
        return np.nan

def new_columns(df):
    nuevas_columnas = []
    for nombre in df.columns:

        patron = re.compile(r'[a-zA-Z][a-z]*[A-Z][a-z][\d]*')

        if re.search(patron, nombre):
            col_sep = re.sub(r'(?<=[a-z])(?=[A-Z])', '_', nombre) #cada vez que encuentro una minúscula seguida de mayúscula lo cambio por _ 
            nuevas_columnas.append(col_sep.lower().strip())
        
        elif nombre == 'employeenumber':
            nuevas_columnas.append('employee_number')
        
        elif nombre == 'NUMCOMPANIESWORKED':
            nuevas_columnas.append('num_companies_worked')
        
        elif nombre == 'TOTALWORKINGYEARS':
            nuevas_columnas.append('total_working_years')

        elif nombre == 'WORKLIFEBALANCE':
                nuevas_columnas.append('work_life_balance')

        elif nombre == 'YEARSWITHCURRMANAGER':
            nuevas_columnas.append('years_with_current_manager')
        
        else:
            nuevas_columnas.append(nombre.lower())

    return df.rename(columns=dict(zip(df.columns, nuevas_columnas)), inplace= True)

def unificacion(valor):
    if type(valor) == str:
        return valor.lower().strip()
    else:
        return valor
    
def homog_df(df):
    new_columns(df)
    
    for columna in df.columns:
        df[columna] = df[columna].apply(unificacion)
   

   
def limpieza(df):
    df.drop(['employeecount', 'NUMBERCHILDREN', 'SameAsMonthlyIncome', 'Salary', 'Age', 'Over18', 'StandardHours', 'RoleDepartament', 'YearsInCurrentRole'], axis=1, inplace=True)
    df['EnvironmentSatisfaction'] = df['EnvironmentSatisfaction'].apply(lambda x: x if x in range(1,5) else np.nan)
    df['BusinessTravel'] = df['BusinessTravel'].map({"non-travel":"no", "travel_rarely":"rarely", "travel_frequently":"frequently"})
    df["DistanceFromHome"] = abs(df["DistanceFromHome"])
    df['Gender'] = df['Gender'].map({1: "F", 0: 'M'})
    df['MaritalStatus'] = df['MaritalStatus'].str.replace('Marreid', 'married')
    df['HourlyRate'] = df['HourlyRate'].replace('Not Available', np.nan)
    df["PercentSalaryHike"] = (df["PercentSalaryHike"]).astype(float) / 100
    for columna in lista_float:
        df[columna] = df[columna].apply(to_float)

    for columna in lista_bool:
        df[columna] = df[columna].apply(true_false)
    
    homog_df(df)



# AB TESTING
def df_testeo(df):
    df2 = df.copy()
    df2['grupo_edad'] = df['date_birth'].apply(lambda x: '+40' if x > 1983 else '-40')
    df2['grupo_working_years'] = df['total_working_years'].apply(lambda x: '+20' if x > 20 else '-20')
    df2['grupo_testeo'] = np.where(
                            (df2['grupo_edad'] == '+40') & (df2['grupo_working_years'] == '-20'), 'A',
                          np.where(
                            (df2['grupo_edad'] == '-40') | (df2['grupo_working_years'] == '+20'), 'B', ''))
    
    return df2

def chi2_contingency_test(contingency_table):

    """
    Realiza un test de chi-cuadrado de independencia en una tabla de contingencia.

    Parámetros:
    contingency_table : array_like
        Una tabla de contingencia en forma de matriz, donde las filas representan las categorías de una variable
        y las columnas representan las categorías de otra variable.

    Devuelve:
    chi2_statistic : float
        Estadística chi-cuadrado del test.
    p_value : float
        Valor p del test.
    degrees_of_freedom : int
        Grados de libertad del test.
    expected : ndarray
        Matriz de valores esperados bajo la hipótesis nula de independencia.
    """
    chi2_stat, p_val, dof, expected = chi2_contingency(contingency_table)
    
    print("Estadística Chi-cuadrado:", chi2_stat)
    print("Valor p:", p_val)
   
    
    