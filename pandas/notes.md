# PANDAS

## 🧭 Compendio de Funciones de Pandas para EDA

---

### 📌 1. **Carga y vista inicial del dataset**

```python
pd.read_csv(filepath_or_buffer)            # Leer CSV
pd.read_excel(filepath_or_buffer)          # Leer Excel
pd.read_json(filepath_or_buffer)           # Leer JSON
df.head(n=5)                                # Primeras n filas
df.tail(n=5)                                # Últimas n filas
df.sample(n=5)                              # Muestra aleatoria de n filas
df.shape                                   # Dimensiones (filas, columnas)
df.columns                                 # Nombres de columnas
df.index                                   # Índice del DataFrame
df.dtypes                                  # Tipos de datos por columna
df.info()                                  # Información general del DataFrame
```

---

### 🧹 2. **Datos faltantes y duplicados**

```python
df.isnull().sum()                          # Conteo de valores nulos por columna
df.isna().mean()                           # Porcentaje de valores nulos por columna
df.notnull().sum()                         # Conteo de valores no nulos
df.duplicated().sum()                      # Número de filas duplicadas
df.dropna()                                # Eliminar filas con valores nulos
df.fillna(value)                           # Rellenar valores nulos
df.drop_duplicates()                       # Eliminar filas duplicadas
```

---

### 📊 3. **Estadísticas descriptivas**

```python
df.describe(include='all')                 # Estadísticas generales (numéricas y no numéricas)
df['col'].value_counts()                   # Conteo de frecuencia de valores únicos
df['col'].unique()                         # Valores únicos de una columna
df['col'].nunique()                        # Número de valores únicos
df.corr(numeric_only=True)                # Correlación entre columnas numéricas
df.cov(numeric_only=True)                 # Matriz de covarianza
```

---

### 📈 4. **Agrupamiento y resumen**

```python
df.groupby('col').mean()                   # Media por grupo
df.groupby('col')['otra_col'].agg(['mean', 'median', 'std'])  # Agregaciones múltiples
df.pivot_table(index='col1', columns='col2', values='col3', aggfunc='mean')  # Tabla dinámica
```

---

### 🔍 5. **Filtrado y selección**

```python
df['col']                                  # Selección de columna
df[['col1', 'col2']]                        # Varias columnas
df.loc[filas, columnas]                     # Selección por etiquetas
df.iloc[filas, columnas]                    # Selección por posición
df.query('col > 100 & otra_col == "X"')    # Filtro con expresiones
```

---

### 🧾 6. **Transformaciones y limpieza**

```python
df.rename(columns={'viejo': 'nuevo'})      # Renombrar columnas
df['col'].astype(tipo)                     # Cambiar tipo de dato
df['col'].str.strip()                      # Limpiar espacios en strings
df['col'].str.lower()                      # Convertir a minúsculas
df.sort_values(by='col', ascending=False)  # Ordenar por columna
df.reset_index(drop=True)                  # Resetear el índice
```

---

### 🧮 7. **Creación y modificación de columnas**

```python
df['nueva'] = df['col1'] + df['col2']      # Nueva columna
df['bin'] = df['col'].apply(lambda x: ...) # Aplicar función a columna
pd.cut(df['col'], bins=3)                  # Discretización
pd.qcut(df['col'], q=4)                    # Discretización por cuartiles
```

---

### 🪄 8. **Exploración categórica**

```python
pd.crosstab(df['cat1'], df['cat2'])        # Tablas de contingencia
df.groupby('categoria').size()             # Conteo por categoría
df['cat'].value_counts(normalize=True)     # Distribución porcentual
```

---

### 🔄 9. **Resumen general rápido (opcional, con librerías externas)**

```python
# Requiere instalación: pip install pandas-profiling
from pandas_profiling import ProfileReport
ProfileReport(df)                          # Reporte EDA automático
```