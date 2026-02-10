# 🧪 Python Data Analysis - Guía Práctica

Una colección estructurada de notebooks con ejemplos propios y patrones prácticos para análisis de datos.

> *Progresión lógica: desde fundamentos de Python hasta técnicas avanzadas de análisis.*

---

## 🐍 Contenido

### 01 - Python Fundamentals
| Notebook | Descripción |
|----------|-------------|
| [01_01_variables_and_types](python/01_python_fundamentals/01_01_variables_and_types.ipynb) | Variables, tipos básicos, casting |
| [01_02_data_structures](python/01_python_fundamentals/01_02_data_structures.ipynb) | Listas, tuplas, diccionarios, sets |

### 02 - Functions & Modules
| Notebook | Descripción |
|----------|-------------|
| [02_01_functions_basics](python/02_functions_and_modules/02_01_functions_basics.ipynb) | Funciones, parámetros, docstrings, lambdas |

### 03 - NumPy Essentials
| Notebook | Descripción |
|----------|-------------|
| [03_01_arrays_basics](python/03_numpy_essentials/03_01_arrays_basics.ipynb) | Crear arrays, shapes, dtypes |
| [03_02_indexing_slicing](python/03_numpy_essentials/03_02_indexing_slicing.ipynb) | Acceder elementos, máscaras booleanas |
| [03_03_operations](python/03_numpy_essentials/03_03_operations.ipynb) | Operaciones vectorizadas, agregaciones |

### 04 - Pandas Basics
| Notebook | Descripción |
|----------|-------------|
| [04_01_series_dataframe](python/04_pandas_basics/04_01_series_dataframe.ipynb) | Series, DataFrames, estructura básica |
| [04_02_reading_data](python/04_pandas_basics/04_02_reading_data.ipynb) | Leer CSV, JSON, Excel, parámetros útiles |
| [04_03_selection_filtering](python/04_pandas_basics/04_03_selection_filtering.ipynb) | loc, iloc, filtrado booleano, query() |

### 05 - Pandas Intermediate
| Notebook | Descripción |
|----------|-------------|
| [05_01_groupby](python/05_pandas_intermediate/05_01_groupby.ipynb) | GroupBy, agregaciones, transform, filter |
| [05_02_merge_join](python/05_pandas_intermediate/05_02_merge_join.ipynb) | Merge, tipos de join, concat |
| [05_03_pivot_reshape](python/05_pandas_intermediate/05_03_pivot_reshape.ipynb) | Pivot tables, melt, wide/long |

### 06 - Data Cleaning
| Notebook | Descripción |
|----------|-------------|
| [06_01_missing_values](python/06_data_cleaning/06_01_missing_values.ipynb) | Detectar, eliminar y rellenar NaN |
| [06_02_duplicates_outliers](python/06_data_cleaning/06_02_duplicates_outliers.ipynb) | Duplicados, IQR, Z-score |
| [06_03_data_types](python/06_data_cleaning/06_03_data_types.ipynb) | Conversión tipos, limpieza texto, fechas |

### 07 - Visualization
| Notebook | Descripción |
|----------|-------------|
| [07_01_matplotlib_basics](python/07_visualization/07_01_matplotlib_basics.ipynb) | Figure, axes, líneas, barras, histogramas |
| [07_02_pandas_plotting](python/07_visualization/07_02_pandas_plotting.ipynb) | Gráficos directos desde DataFrames |
| [07_03_seaborn](python/07_visualization/07_03_seaborn.ipynb) | Gráficos estadísticos, hue, facetas |
| [07_04_matplotlib_dashboard](python/07_visualization/07_04_matplotlib_dashboard.ipynb) | Dashboard completo, GridSpec, estilos profesionales |

### 08 - Geospatial
| Notebook | Descripción |
|----------|-------------|
| [08_01_geopandas_intro](python/08_geospatial/08_01_geopandas_intro.ipynb) | GeoDataFrame, geometrías, CRS |
| [08_02_spatial_operations](python/08_geospatial/08_02_spatial_operations.ipynb) | Distancias, buffers, spatial join |
| [08_03_folium_maps](python/08_geospatial/08_03_folium_maps.ipynb) | Mapas interactivos, marcadores, heatmaps |

### 09 - Temporal Analytics 🔜
### 10 - Advanced Patterns 🔜

---

## 📖 Cómo usar

Cada notebook es **autocontenido** con:
- Explicación del concepto
- Código comentado con ejemplos
- Ejercicios prácticos
- Enlaces al anterior y siguiente

**Recomendación:** Sigue el orden numérico (01_01 → 01_02 → 02_01 → ...).

---

## 🚀 Requisitos

```bash
# Core
pip install numpy pandas matplotlib seaborn jupyter

# Geospatial (opcional)
pip install geopandas folium
```
