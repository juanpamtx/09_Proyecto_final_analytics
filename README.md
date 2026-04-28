# Proyecto Final – Enterprise E‑Commerce Analytics

## Descripción general
Este proyecto corresponde al **proyecto final del Máster en Data Analytics**, centrado en el análisis integral de un e‑commerce desde una perspectiva **técnica y de negocio**.

El objetivo principal es transformar diferentes fuentes de datos en conocimiento accionable mediante:
- Procesos de limpieza y análisis exploratorio en **Python**
- Integración de datos en un dataset final consolidado
- Visualización y síntesis de resultados en **Power BI**

El resultado final es un **dashboard interactivo** que permite analizar ventas, comportamiento del cliente, fraude, productos y churn.

---

## Objetivos del proyecto
- Analizar el comportamiento del cliente y su relación con el abandono y el churn
- Identificar patrones de fraude según método de pago y dispositivo
- Evaluar la rentabilidad de los productos por categoría
- Detectar posibles estacionalidades en las transacciones
- Sintetizar los resultados en un dashboard claro y orientado a negocio

---

## Estructura del proyecto

Proyecto_09_Enterprise_E_commerce/
│
├── dashboard/
│   └── ecommerce_dashboard.pbix
│
├── data/
│   ├── 01_raw/
        └── behavior.csv
        └── customers.csv
        └── products.csv
        └── transaction.csv
│   ├── 02_processed/
        └── behavior_clean.csv
        └── customers_clean.csv
        └── products_clean.csv
        └── transaction_clean.csv
│   └── 03_final/
│       └── ecommerce_master_dataset.csv
│
├── notebooks/
│   ├── 00_pre_eda.ipynb
│   ├── 01_eda_quality.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_export_final.ipynb
│   └── 04_eda_final.ipynb
│
├── docs/
│   ├── informe_final_ecommerce.docx
│   └── informe_final_ecommerce.pdf
│
├── images/
│   ├── dashboard_comportamiento.png
│   ├── dashboard_fraude.png
│   ├── dashboard_productos.png
│   ├── dashboard_resumen.png
│   └── dashboard_temporal.png 
│
├── src_utils/
│   ├── cleaning_utils.py
│   └── eda_utils.py
│
└── README.md

---

## Datos utilizados
El análisis se basa en cuatro fuentes principales:
- **Clientes**: información demográfica y de país
- **Productos**: categoría, precio y margen
- **Transacciones**: pedidos, pagos y fraude
- **Comportamiento**: interacción digital, abandono y churn

Estas fuentes se limpiaron, normalizaron y unificaron en un único dataset final para facilitar el análisis.

---

## Metodología

### 1. Análisis Exploratorio (EDA)
Se realizó un EDA inicial para:
- Detectar valores nulos y atípicos
- Analizar la distribución de variables clave
- Evaluar la calidad de los datos

### 2. Limpieza y transformación
Durante esta fase:
- Se normalizaron variables porcentuales
- Se corrigieron inconsistencias de escala
- Se generaron variables finales aptas para visualización

### 3. Dataset final
El dataset `ecommerce_master_dataset.csv` integra toda la información necesaria para el análisis y es la fuente de datos utilizada en Power BI.

### 4. Dashboard en Power BI
El dashboard sintetiza los principales insights a través de visualizaciones interactivas, organizadas en diferentes páginas temáticas.

---

## Dashboard – Descripción de páginas

### Resumen general
Visión ejecutiva del estado del e‑commerce, incluyendo KPIs clave como ingresos, transacciones y tasa de churn de comportamiento.

images/dashboard_resumen.png

---

### Análisis temporal
Análisis de la evolución de las transacciones a lo largo del tiempo para detectar tendencias o estacionalidades.

images/dashboard_temporal.png

---

### Análisis de fraude
Identificación de patrones de fraude según métodos de pago y dispositivos, útil para priorizar medidas de control.

images/dashboard_fraude.png

---

### Análisis de productos
Evaluación del precio medio y margen por categoría, poniendo de manifiesto que precio elevado no implica necesariamente mayor rentabilidad.

images/dashboard_productos.png

---

### Análisis del comportamiento del cliente
Estudio del churn de comportamiento, abandono del carrito, interacción del cliente y puntuaciones de reviews.

images/dashboard_comportamiento.png


*Principales hallazgos*:
- Tasa de churn de comportamiento ≈ **34,44 %**
- Abandono del carrito estable por categoría (~35 %)
- Alta concentración de interacción en determinados rangos
- Satisfacción del cliente moderada (reviews ≈ 2,3–2,7)

---

## Principales conclusiones
- El principal reto del e‑commerce no es el catálogo, sino el **comportamiento del usuario**
- La tasa de abandono del carrito representa una oportunidad clara de mejora
- No existe una relación directa entre precio y margen
- El fraude se concentra en combinaciones específicas de pago y dispositivo
- Pequeñas mejoras en experiencia pueden tener un impacto significativo en la retención

---

## Tecnologías utilizadas
- **Python** (pandas, numpy, matplotlib, seaborn)
- **Power BI**
- **Visual Studio Code**

---

## Autor
Juan Pablo Planelles  
Proyecto final – Máster en Data Analytics