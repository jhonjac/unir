# Análisis de Visualizaciones - Dataset Superstore 2012

## 📊 Descripción del Proyecto

Este proyecto implementa un análisis completo de visualizaciones utilizando **Matplotlib** y **Seaborn** para analizar el dataset de ventas minoristas Superstore 2012. El proyecto cumple con todos los criterios de evaluación establecidos, incluyendo visualizaciones univariantes, bivariantes y multivariantes.

## 🎯 Objetivos Cumplidos

### ✅ Criterios de Evaluación Implementados:

1. **Implementación de visualizaciones con Matplotlib**
   - ✓ Gráficos univariantes (histogramas, diagramas de barras)
   - ✓ Gráficos bivariantes (dispersión, líneas, barras agrupadas)
   - ✓ Personalización completa (títulos, etiquetas, colores)

2. **Implementación de visualizaciones con Seaborn**
   - ✓ Visualizaciones univariantes (boxplots, violinplots)
   - ✓ Visualizaciones bivariantes (regplot, heatmaps, barplots)
   - ✓ Visualizaciones multivariantes (matriz de correlación, pairplot)

3. **Preparación y manejo de datos con Pandas**
   - ✓ Carga correcta del dataset
   - ✓ Conversión de fechas con manejo de errores
   - ✓ Creación de variables derivadas
   - ✓ Limpieza y preparación de datos

## 📁 Estructura del Proyecto

```
w04/
├── analisis_visualizaciones_superstore.py  # Script principal de análisis
├── dashboard_superstore_2012.png           # Dashboard guardado como imagen
├── superstore_dataset2012.csv              # Dataset original
├── requerimiento.txt                       # Especificaciones del proyecto
└── README.md                               # Documentación del proyecto
```

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Python 3.12
- Entorno virtual activado

### Instalación de Dependencias
```bash
pip install pandas matplotlib seaborn numpy
```

### Ejecución del Análisis
```bash
python analisis_visualizaciones_superstore.py
```

## 📈 Visualizaciones Implementadas

### 1. Visualizaciones Univariantes con Matplotlib
- **Histograma de Ventas**: Distribución de valores de ventas
- **Diagrama de Barras por Categoría**: Frecuencia de productos por categoría
- **Histograma de Beneficios**: Distribución de beneficios con línea de equilibrio
- **Diagrama de Barras por Segmento**: Distribución de clientes por segmento

### 2. Visualizaciones Univariantes con Seaborn
- **Boxplot de Ventas por Categoría**: Distribución y outliers por categoría
- **Violinplot de Beneficios por Segmento**: Densidad de distribución de beneficios
- **Histograma de Descuentos**: Distribución de descuentos con KDE
- **Boxplot de Margen de Beneficio por Región**: Comparación regional de rentabilidad

### 3. Visualizaciones Bivariantes con Matplotlib
- **Scatter Plot Ventas vs Beneficios**: Relación con codificación por descuento
- **Evolución Temporal**: Tendencias mensuales de ventas en 2012
- **Barras Agrupadas**: Ventas promedio por categoría y segmento
- **Scatter Plot Cantidad vs Descuento**: Análisis de patrones de descuento

### 4. Visualizaciones Bivariantes con Seaborn
- **Regplot Ventas vs Beneficios**: Análisis de regresión con intervalos de confianza
- **Heatmap Categoría vs Segmento**: Matriz de ventas promedio
- **Boxplot por Prioridad de Orden**: Distribución de ventas por prioridad
- **Barplot por Modo de Envío**: Beneficio promedio por tipo de envío

### 5. Visualizaciones Multivariantes con Seaborn
- **Matriz de Correlación**: Heatmap de correlaciones entre variables numéricas
- **Pairplot**: Análisis de pares de variables clave por categoría
- **FacetGrid**: Análisis multidimensional por categoría y segmento

### 6. Dashboard Completo
- **Subplots Organizados**: 8 visualizaciones en una figura coherente
- **Análisis Integral**: Combinación de todas las técnicas de visualización
- **Guardado como Imagen**: Dashboard exportado en alta resolución

## 🔍 Insights Principales

### 📊 Hallazgos Clave:
- Las ventas siguen una distribución log-normal con cola larga
- **Technology** genera las ventas más altas pero con mayor variabilidad
- Correlación positiva fuerte entre ventas y beneficios (r≈0.48)
- Los descuentos altos impactan negativamente en los beneficios
- Estacionalidad marcada con picos en Q4 (noviembre-diciembre)
- **Consumer** domina en volumen, **Corporate** tiene mejor rentabilidad
- **Phones** y **Chairs** son las subcategorías más rentables
- **APAC** y **EU** lideran en ventas totales

### 🚀 Recomendaciones Estratégicas:
1. Enfocar marketing en productos Technology para segmento Corporate
2. Optimizar estrategia de descuentos para mantener rentabilidad
3. Aprovechar estacionalidad de Q4 para maximizar ventas
4. Expandir presencia en regiones de alto rendimiento (APAC, EU)
5. Desarrollar programas específicos para segmento Consumer

## 🛠️ Características Técnicas

### Personalización de Gráficos:
- ✅ Títulos descriptivos y profesionales
- ✅ Etiquetas de ejes claras y específicas
- ✅ Paletas de colores apropiadas y consistentes
- ✅ Leyendas informativas cuando es necesario
- ✅ Grids y transparencias para mejor legibilidad

### Organización con Subplots:
- ✅ Múltiples visualizaciones en figuras organizadas
- ✅ Títulos generales para cada conjunto de gráficos
- ✅ Espaciado apropiado entre subplots
- ✅ Tamaños de figura optimizados para visualización

### Manejo de Datos:
- ✅ Carga robusta con manejo de errores
- ✅ Conversión de fechas con `dayfirst=True`
- ✅ Creación de variables derivadas (Year, Month, Quarter, Profit_Margin)
- ✅ Limpieza de valores infinitos y NaN
- ✅ Filtrado de outliers para mejor visualización

## 📝 Comentarios y Documentación

Cada visualización incluye:
- **Comentarios explicativos** sobre las conclusiones obtenidas
- **Análisis de patrones** identificados en los datos
- **Interpretación de resultados** en contexto de negocio
- **Recomendaciones estratégicas** basadas en los hallazgos

## 🎯 Cumplimiento de Requisitos

| Requisito | Estado | Implementación |
|-----------|--------|----------------|
| Gráfico univariante Matplotlib | ✅ | Histogramas y diagramas de barras |
| Gráfico univariante Seaborn | ✅ | Boxplots y violinplots |
| Gráfico bivariante Matplotlib | ✅ | Scatter plots y evolución temporal |
| Gráfico bivariante Seaborn | ✅ | Regplots y heatmaps |
| Visualización multivariante Seaborn | ✅ | Matriz correlación y pairplot |
| Personalización de gráficos | ✅ | Títulos, etiquetas, paletas |
| Organización en subplots | ✅ | Dashboard con 8 visualizaciones |
| Guardar figura como imagen | ✅ | dashboard_superstore_2012.png |
| Comentarios explicativos | ✅ | Conclusiones detalladas |
| Uso del dataset proporcionado | ✅ | superstore_dataset2012.csv |

## 📊 Tecnologías Utilizadas

- **Python 3.12**: Lenguaje de programación principal
- **Pandas 2.3.1**: Manipulación y análisis de datos
- **Matplotlib 3.10.5**: Visualizaciones básicas y personalizadas
- **Seaborn 0.13.2**: Visualizaciones estadísticas avanzadas
- **NumPy 2.3.2**: Operaciones numéricas y estadísticas

## 🏆 Resultados

El proyecto ha generado exitosamente:
- **20+ visualizaciones** diferentes utilizando ambas librerías
- **Dashboard completo** con análisis integral
- **Insights accionables** para la toma de decisiones
- **Documentación completa** con conclusiones detalladas
- **Código limpio y bien estructurado** siguiendo mejores prácticas

---

**Autor**: Jhon Jaime Amaya Correa  
**Fecha**: Agosto-2025  
**Python**: 3.12  
**Dataset**: Superstore 2012 (4,247 registros)