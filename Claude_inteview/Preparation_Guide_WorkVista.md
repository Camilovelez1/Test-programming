# Guía de Preparación: Prueba de Código para Data Scientist
## Work Vista - Remote Position

---

## 📊 Análisis de la Posición

**Empresa:** Work Vista  
**Rol:** Data Scientist (AI-focused)  
**Tipo:** Contrato independiente, 20-40 hrs/semana  
**Ubicación:** Remote (Australia)

### Skills Críticos Mencionados:
1. ✅ Python (Jupyter, numpy, pandas, scipy, scikit-learn, torch, tensorflow)
2. ✅ EDA (Exploratory Data Analysis)
3. ✅ Statistical inference
4. ✅ Model evaluation
5. ✅ Feature engineering
6. ✅ Experimentation
7. ✅ **Prompt engineering** (específico para AI training)

---

## 🎯 Tipos de Pruebas Comunes

Basándome en la investigación y el enfoque de AI training de Work Vista, espera ver:

### 1. **Coding Challenges (40% de la prueba)**
   - Manipulación de datos con pandas
   - Implementación de algoritmos desde cero
   - Bug fixing y code optimization
   - Tiempo típico: 30-45 minutos

### 2. **Data Analysis Tasks (30%)**
   - EDA en datasets desconocidos
   - Statistical testing
   - Feature engineering
   - Tiempo típico: 20-30 minutos

### 3. **Machine Learning Problems (20%)**
   - Build & evaluate models
   - Model comparison
   - Hyperparameter tuning básico
   - Tiempo típico: 15-20 minutos

### 4. **Prompt Engineering / AI Training (10%)**
   - Escribir prompts efectivos
   - Evaluar calidad de respuestas AI
   - Crear preguntas de entrenamiento
   - Tiempo típico: 10-15 minutos

---

## 🔥 Temas Más Probables a Evaluar

### High Priority (>80% probabilidad):
1. **Pandas Operations**
   - GroupBy, aggregations
   - Merge, join operations
   - Handling missing data
   - Data type conversions

2. **NumPy Fundamentals**
   - Array operations
   - Broadcasting
   - Vectorización
   - Basic linear algebra

3. **Statistical Tests**
   - T-tests
   - Chi-square tests
   - A/B testing
   - Hypothesis testing

4. **Scikit-learn Pipelines**
   - Train/test split
   - Cross-validation
   - Model evaluation metrics
   - Feature scaling

5. **Feature Engineering**
   - Encoding categorical variables
   - Creating time-based features
   - Handling outliers
   - Feature selection

### Medium Priority (50-80% probabilidad):
6. **Algorithm Implementation**
   - K-means clustering
   - Linear/Logistic regression from scratch
   - Distance metrics (euclidean, cosine)
   - Simple classifiers

7. **Data Cleaning**
   - Outlier detection
   - Duplicate handling
   - Data validation
   - String manipulation

8. **Performance Optimization**
   - Vectorization vs loops
   - Memory efficiency
   - Time complexity

### Lower Priority pero Posible (20-50%):
9. **Time Series**
   - Lag features
   - Rolling statistics
   - Seasonality detection

10. **Deep Learning Basics**
    - Tensor operations
    - Basic PyTorch/TensorFlow
    - Neural network concepts

---

## 💡 Estrategias para la Prueba

### Antes de Empezar:
1. ✅ Lee TODAS las instrucciones primero
2. ✅ Identifica las partes más sencillas
3. ✅ Planifica tu tiempo (no más de X minutos por problema)
4. ✅ Ten a mano la documentación oficial (si permiten consultas)

### Durante la Prueba:
1. **Gestión del Tiempo**
   ```
   Problema fácil:   5-10 min
   Problema medio:   10-20 min
   Problema difícil: 15-30 min
   ```
   - Si te atascas >5 min, marca y sigue
   - Vuelve al final si sobra tiempo

2. **Orden de Resolución**
   - Primero: Problemas que sabes hacer (build confidence)
   - Segundo: Problemas de dificultad media
   - Tercero: Problemas difíciles
   - Último: Revisión y refinamiento

3. **Escribir Código**
   ```python
   # SIEMPRE incluye:
   # 1. Docstrings claros
   # 2. Type hints si es apropiado
   # 3. Comentarios en lógica compleja
   # 4. Manejo de edge cases
   
   def ejemplo_funcion(data: pd.DataFrame) -> dict:
       """
       Brief description of what this does.
       
       Parameters:
       -----------
       data : pd.DataFrame
           Description of input
       
       Returns:
       --------
       dict
           Description of output
       """
       # Validate input
       if data.empty:
           return {}
       
       # Main logic with comments
       # ...
       
       return result
   ```

4. **Testing Mental**
   - ¿Funciona con lista vacía?
   - ¿Funciona con un solo elemento?
   - ¿Maneja valores None/NaN?
   - ¿Qué pasa con valores negativos?

---

## 🚨 Errores Comunes a Evitar

### 1. **Pandas Anti-patterns**
```python
# ❌ MAL - Iterar fila por fila
for i in range(len(df)):
    df.loc[i, 'new_col'] = some_calculation(df.loc[i, 'old_col'])

# ✅ BIEN - Operaciones vectorizadas
df['new_col'] = df['old_col'].apply(some_calculation)
# o mejor aún
df['new_col'] = some_vectorized_operation(df['old_col'])
```

### 2. **División por Cero**
```python
# ❌ MAL
precision = true_positives / (true_positives + false_positives)

# ✅ BIEN
denominator = true_positives + false_positives
precision = true_positives / denominator if denominator != 0 else 0
```

### 3. **Memory Inefficiency**
```python
# ❌ MAL - Copia innecesaria
df_copy = df.copy()
df_copy['new'] = df_copy['old'] * 2

# ✅ BIEN - Modificación in-place cuando sea apropiado
df['new'] = df['old'] * 2
```

### 4. **No Validar Inputs**
```python
# ❌ MAL - Asumir que todo está bien
def process(data):
    return data.mean()

# ✅ BIEN - Validación
def process(data):
    if data is None or len(data) == 0:
        raise ValueError("Data cannot be empty")
    return data.mean()
```

---

## 📚 Cheat Sheet Rápido

### Pandas Essentials:
```python
# Reading
df = pd.read_csv('file.csv')
df.head(), df.info(), df.describe()

# Filtering
df[df['col'] > 10]
df.query('col > 10 and other_col == "value"')

# Grouping
df.groupby('category').agg({'sales': ['sum', 'mean', 'count']})

# Missing data
df.isnull().sum()
df.fillna(df.mean())
df.dropna()
df.interpolate()

# Merging
pd.merge(df1, df2, on='key', how='left')
pd.concat([df1, df2], axis=0)

# Apply functions
df['new'] = df['old'].apply(lambda x: x**2)
df['new'] = df.apply(lambda row: func(row['a'], row['b']), axis=1)
```

### Scikit-learn Quick Reference:
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# Predict
y_pred = model.predict(X_test_scaled)

# Evaluate
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

# Cross-validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
print(f"CV Score: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

### NumPy Quick Tricks:
```python
# Array operations
arr = np.array([1, 2, 3, 4, 5])
arr.mean(), arr.std(), arr.min(), arr.max()
np.percentile(arr, [25, 50, 75])

# Boolean indexing
arr[arr > 3]

# Broadcasting
arr + 10  # adds 10 to all elements

# Reshaping
arr.reshape(5, 1)

# Common functions
np.sqrt(arr)
np.exp(arr)
np.log(arr)
np.abs(arr)

# Statistics
np.corrcoef(x, y)
np.cov(x, y)
```

### Statistical Tests (scipy):
```python
from scipy import stats

# T-test
t_stat, p_value = stats.ttest_ind(group1, group2)

# Chi-square
chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)

# Normality test
stat, p_value = stats.shapiro(data)

# Correlation
corr, p_value = stats.pearsonr(x, y)
```

---

## 🎓 Prompt Engineering Tips (Específico para AI Training)

Como mencionan "write, review, and refine prompts", espera preguntas sobre:

### Principios de Buenos Prompts:
1. **Específico y Claro**
   ```
   ❌ "Analyze this data"
   ✅ "Calculate the mean, median, and standard deviation of the 'sales' 
      column, then identify any outliers using the IQR method"
   ```

2. **Contexto Suficiente**
   ```
   ❌ "Fix this code"
   ✅ "This Python function should calculate precision and recall metrics 
      for a binary classifier. It's currently failing with a ZeroDivisionError 
      when there are no positive predictions. Fix the error handling."
   ```

3. **Formato Esperado**
   ```
   ❌ "Show me the results"
   ✅ "Return results as a dictionary with keys 'accuracy', 'precision', 
      'recall', and 'f1_score', with values rounded to 3 decimal places"
   ```

4. **Ejemplos When Needed**
   ```
   "Extract dates from text. For example:
   Input: 'Meeting on Jan 15, 2024'
   Output: ['2024-01-15']"
   ```

---

## 🔍 Patrones de Código a Memorizar

### Pattern 1: Feature Engineering Template
```python
def engineer_features(df):
    """Standard feature engineering pipeline"""
    df = df.copy()
    
    # 1. Handle missing values
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    # 2. Encode categorical
    categorical_cols = df.select_dtypes(include=['object']).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    # 3. Scale numerical features
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df
```

### Pattern 2: Model Evaluation Template
```python
def evaluate_model(model, X_test, y_test):
    """Comprehensive model evaluation"""
    from sklearn.metrics import (
        accuracy_score, precision_score, recall_score, 
        f1_score, roc_auc_score, confusion_matrix
    )
    
    y_pred = model.predict(X_test)
    
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'recall': recall_score(y_test, y_pred, average='weighted'),
        'f1': f1_score(y_test, y_pred, average='weighted')
    }
    
    # Add ROC-AUC for binary classification
    if len(np.unique(y_test)) == 2:
        y_proba = model.predict_proba(X_test)[:, 1]
        metrics['roc_auc'] = roc_auc_score(y_test, y_proba)
    
    return metrics
```

### Pattern 3: Data Cleaning Template
```python
def clean_dataframe(df):
    """Standard data cleaning pipeline"""
    df = df.copy()
    
    # 1. Remove duplicates
    df = df.drop_duplicates()
    
    # 2. Handle missing values
    # Numeric: median imputation
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)
    
    # Categorical: mode imputation
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    # 3. Remove outliers (optional)
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[col] >= Q1 - 1.5*IQR) & (df[col] <= Q3 + 1.5*IQR)]
    
    return df
```

---

## ⏰ Timeline de Preparación Sugerido

### Si tienes 3+ días:
- **Día 1:** Practica todos los ejercicios del notebook (2-3 horas)
- **Día 2:** Revisa conceptos estadísticos y métricas ML (1-2 horas)
- **Día 3:** Simula una prueba completa con tiempo límite (1 hora)

### Si tienes 1-2 días:
- **Día 1:** Practica ejercicios básicos y medios del notebook (2 horas)
- **Día 2:** Repasa cheat sheet y haz ejercicio end-to-end (1 hora)

### Si tienes <1 día:
- Enfócate en: Pandas operations, scikit-learn basics, y statistical tests
- Practica 3-4 ejercicios clave del notebook
- Repasa el cheat sheet

---

## 🎯 Checklist Final Pre-Prueba

- [ ] Repasé operaciones básicas de pandas
- [ ] Practicé train/test split y cross-validation
- [ ] Sé calcular métricas de clasificación manualmente
- [ ] Puedo implementar un algoritmo simple desde cero
- [ ] Entiendo diferencias entre encoding methods
- [ ] Sé manejar valores faltantes de diferentes formas
- [ ] Practicé optimización de código (vectorización)
- [ ] Leí sobre prompt engineering best practices
- [ ] Tengo ejemplos de good vs bad prompts
- [ ] Preparé mi ambiente (si es prueba local)
- [ ] Descansé bien la noche anterior 😴

---

## 🌟 Recursos Adicionales

### Para Practicar Más:
1. **LeetCode** - Sección de Data Science
2. **HackerRank** - Python y Statistics tracks
3. **Kaggle** - Learn sections (todos son gratis)
4. **StrataScratch** - SQL y Data Science questions

### Documentación Oficial:
- Pandas: https://pandas.pydata.org/docs/user_guide/
- Scikit-learn: https://scikit-learn.org/stable/user_guide.html
- NumPy: https://numpy.org/doc/stable/user/
- SciPy Stats: https://docs.scipy.org/doc/scipy/reference/stats.html

### Repos de GitHub Útiles:
- "Data Science Interview Resources" - https://github.com/rbhatia46/Data-Science-Interview-Resources
- "Awesome Data Science" - https://github.com/academic/awesome-datascience

---

## 💪 Palabras Finales

**Recuerda:**
- Calidad > Cantidad en código
- Código legible > Código clever
- Si no sabes algo 100%, implementa lo que sabes y documéntalo
- No tengas miedo de usar funciones built-in (no tienes que reinventar todo)
- La comunicación clara es tan importante como el código correcto

**Durante la prueba:**
- Respira profundo si te sientes abrumado
- Lee cuidadosamente cada requerimiento
- Comenta tu pensamiento mientras codeas
- Deja código parcial mejor que nada
- Gestiona tu tiempo sabiamente

**¡Mucha suerte!** 🚀 Con tu experiencia de 6+ años en BPT y tus proyectos en Databricks/PySpark, tienes una base sólida. Esta prueba es solo para validar que puedes aplicar tus conocimientos en un formato de coding assessment.

---

## 📞 Contact & Follow-up

Después de la prueba:
1. Envía un follow-up email agradeciéndoles
2. Menciona 1-2 aspectos específicos que disfrutaste
3. Reitera tu interés y disponibilidad
4. Si te atascaste en algo, puedes mencionar cómo lo resolverías con más tiempo

**Template de Follow-up:**
```
Subject: Thank you - Data Scientist Coding Assessment

Hi [Recruiter Name],

I wanted to thank you for the opportunity to complete the coding assessment 
for the Data Scientist position. I found the [specific challenge] particularly 
interesting as it aligned well with my experience in [relevant area].

I'm very excited about the possibility of contributing to Work Vista's AI 
initiatives, especially given my background in [your relevant experience].

Please let me know if you need any additional information. I'm available 
for the next steps at your convenience.

Best regards,
[Your name]
```

¡Éxito en tu proceso! 🎉
