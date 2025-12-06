# Top 50 Data Science Coding Questions - Quick Reference
## Work Vista Position Preparation

---

## 🔥 Sección 1: Pandas & Data Manipulation (15 Questions)

### Q1: ¿Cómo eliminar filas duplicadas basadas en columnas específicas?
```python
# Método 1: Mantener primera ocurrencia
df.drop_duplicates(subset=['col1', 'col2'], keep='first')

# Método 2: Mantener última ocurrencia
df.drop_duplicates(subset=['col1', 'col2'], keep='last')

# Método 3: Eliminar todas las duplicadas
df.drop_duplicates(subset=['col1', 'col2'], keep=False)
```

### Q2: ¿Cómo hacer pivot/unpivot de un DataFrame?
```python
# Pivot (wide format)
pivot_df = df.pivot_table(
    index='category',
    columns='date',
    values='sales',
    aggfunc='sum'
)

# Unpivot (long format)
melted_df = df.melt(
    id_vars=['category'],
    value_vars=['Jan', 'Feb', 'Mar'],
    var_name='month',
    value_name='sales'
)
```

### Q3: ¿Cómo manejar valores faltantes de diferentes formas?
```python
# 1. Eliminar
df.dropna()                          # cualquier NaN
df.dropna(subset=['important_col'])  # NaN en columna específica
df.dropna(thresh=5)                  # filas con <5 valores no-NaN

# 2. Rellenar
df.fillna(0)                         # con valor constante
df.fillna(df.mean())                 # con media
df.fillna(method='ffill')            # forward fill
df.fillna(method='bfill')            # backward fill
df.interpolate()                     # interpolación lineal

# 3. Indicador de missingness
df['was_missing'] = df['col'].isnull().astype(int)
```

### Q4: ¿Cómo combinar múltiples DataFrames?
```python
# Merge (SQL-like join)
pd.merge(df1, df2, on='key', how='left')   # left join
pd.merge(df1, df2, on='key', how='inner')  # inner join
pd.merge(df1, df2, on='key', how='outer')  # full outer join

# Concatenate
pd.concat([df1, df2], axis=0)              # vertical (stack rows)
pd.concat([df1, df2], axis=1)              # horizontal (side by side)

# Join (by index)
df1.join(df2, how='left')
```

### Q5: ¿Cómo hacer groupby con múltiples agregaciones?
```python
# Método 1: Diccionario de agregaciones
result = df.groupby('category').agg({
    'sales': ['sum', 'mean', 'count'],
    'profit': ['sum', 'mean'],
    'customer_id': 'nunique'
})

# Método 2: Named aggregations (más limpio)
result = df.groupby('category').agg(
    total_sales=('sales', 'sum'),
    avg_sales=('sales', 'mean'),
    num_transactions=('sales', 'count'),
    unique_customers=('customer_id', 'nunique')
)
```

### Q6: ¿Cómo aplicar una función a cada fila/columna?
```python
# Aplicar a columna (más rápido)
df['new_col'] = df['old_col'].apply(lambda x: x**2)

# Aplicar a fila
df['new_col'] = df.apply(
    lambda row: row['col1'] + row['col2'], 
    axis=1
)

# Aplicar función más compleja
def complex_function(row):
    if row['age'] < 30:
        return row['salary'] * 1.1
    else:
        return row['salary'] * 1.05

df['adjusted_salary'] = df.apply(complex_function, axis=1)
```

### Q7: ¿Cómo filtrar filas con múltiples condiciones?
```python
# AND conditions
filtered = df[(df['age'] > 25) & (df['salary'] > 50000)]

# OR conditions
filtered = df[(df['age'] < 25) | (df['salary'] > 100000)]

# Using query (más legible)
filtered = df.query('age > 25 and salary > 50000')

# NOT condition
filtered = df[~df['city'].isin(['NYC', 'LA'])]
```

### Q8: ¿Cómo crear bins/categorías de variables continuas?
```python
# Método 1: pd.cut (igual ancho)
df['age_group'] = pd.cut(
    df['age'],
    bins=[0, 18, 35, 50, 100],
    labels=['Teen', 'Young Adult', 'Adult', 'Senior']
)

# Método 2: pd.qcut (igual frecuencia)
df['income_quartile'] = pd.qcut(
    df['income'],
    q=4,
    labels=['Q1', 'Q2', 'Q3', 'Q4']
)

# Método 3: Custom bins
def categorize_age(age):
    if age < 18:
        return 'Minor'
    elif age < 65:
        return 'Adult'
    else:
        return 'Senior'

df['category'] = df['age'].apply(categorize_age)
```

### Q9: ¿Cómo trabajar con fechas/timestamps?
```python
# Convertir a datetime
df['date'] = pd.to_datetime(df['date_string'])

# Extraer componentes
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['dayofweek'] = df['date'].dt.dayofweek  # 0=Monday
df['is_weekend'] = df['date'].dt.dayofweek.isin([5, 6])

# Operaciones de fecha
df['days_since'] = (pd.Timestamp.now() - df['date']).dt.days
df['date_plus_week'] = df['date'] + pd.Timedelta(days=7)

# Resample para series temporales
df.set_index('date').resample('M').sum()  # agregar por mes
```

### Q10: ¿Cómo hacer rolling window calculations?
```python
# Rolling mean
df['rolling_mean_7d'] = df['sales'].rolling(window=7).mean()

# Rolling sum
df['rolling_sum_7d'] = df['sales'].rolling(window=7).sum()

# Rolling std
df['rolling_std_7d'] = df['sales'].rolling(window=7).std()

# Expanding window (desde el inicio)
df['cumulative_mean'] = df['sales'].expanding().mean()

# Con min_periods para evitar NaN
df['rolling_mean'] = df['sales'].rolling(window=7, min_periods=1).mean()
```

### Q11: ¿Cómo identificar y manejar outliers?
```python
def remove_outliers_iqr(df, column):
    """Remove outliers using IQR method"""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Z-score method
from scipy import stats
df['z_score'] = stats.zscore(df['value'])
df_no_outliers = df[df['z_score'].abs() < 3]

# Clip values (cap outliers)
df['value_clipped'] = df['value'].clip(lower=0, upper=100)
```

### Q12: ¿Cómo hacer one-hot encoding?
```python
# Método 1: pd.get_dummies
encoded = pd.get_dummies(df, columns=['category'], drop_first=True)

# Método 2: sklearn LabelEncoder (ordinal)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])

# Método 3: sklearn OneHotEncoder
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False)
encoded_array = ohe.fit_transform(df[['category']])
```

### Q13: ¿Cómo hacer target encoding?
```python
def target_encode(df, categorical_col, target_col):
    """Encode categorical variable by target mean"""
    # Calculate mean target per category
    encoding = df.groupby(categorical_col)[target_col].mean()
    
    # Map back to dataframe
    df[f'{categorical_col}_encoded'] = df[categorical_col].map(encoding)
    
    return df

# Uso
df = target_encode(df, 'city', 'purchase_rate')
```

### Q14: ¿Cómo optimizar operaciones en DataFrames grandes?
```python
# ❌ LENTO - Iteración fila por fila
for idx, row in df.iterrows():
    df.at[idx, 'new_col'] = row['col1'] * row['col2']

# ✅ RÁPIDO - Operaciones vectorizadas
df['new_col'] = df['col1'] * df['col2']

# ❌ LENTO - Append en loop
result = pd.DataFrame()
for chunk in chunks:
    result = result.append(process(chunk))

# ✅ RÁPIDO - Lista de DataFrames + concat
results = []
for chunk in chunks:
    results.append(process(chunk))
result = pd.concat(results, ignore_index=True)

# Usar categorías para strings repetitivos
df['category'] = df['category'].astype('category')
```

### Q15: ¿Cómo hacer multi-index operations?
```python
# Crear multi-index
df.set_index(['category', 'subcategory'], inplace=True)

# Acceder a datos
df.loc[('Electronics', 'Phones')]

# Agrupar por múltiples niveles
df.groupby(level=[0, 1]).sum()

# Reset index
df.reset_index(inplace=True)

# Stack/Unstack
stacked = df.stack()
unstacked = stacked.unstack()
```

---

## 📊 Sección 2: NumPy & Matemáticas (10 Questions)

### Q16: ¿Cómo calcular distancias entre vectores?
```python
# Euclidean distance
def euclidean_distance(vec1, vec2):
    return np.sqrt(np.sum((vec1 - vec2)**2))

# Manhattan distance
def manhattan_distance(vec1, vec2):
    return np.sum(np.abs(vec1 - vec2))

# Cosine similarity
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_product = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return dot_product / norm_product if norm_product != 0 else 0
```

### Q17: ¿Cómo normalizar/estandarizar arrays?
```python
# Min-Max normalization (0-1 range)
def min_max_normalize(arr):
    return (arr - arr.min()) / (arr.max() - arr.min())

# Z-score standardization (mean=0, std=1)
def standardize(arr):
    return (arr - arr.mean()) / arr.std()

# L2 normalization (unit vector)
def l2_normalize(arr):
    return arr / np.linalg.norm(arr)
```

### Q18: ¿Cómo hacer operaciones de matriz eficientemente?
```python
# Dot product
result = np.dot(matrix1, matrix2)
# o
result = matrix1 @ matrix2

# Element-wise multiplication
result = matrix1 * matrix2

# Matrix transpose
transposed = matrix.T

# Matrix inverse
inverse = np.linalg.inv(matrix)

# Eigenvalues/eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)
```

### Q19: ¿Cómo usar broadcasting efectivamente?
```python
# Suma de vector a cada fila de matriz
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])
result = matrix + vector  # [[11, 22, 33], [14, 25, 36]]

# Operación elemento a elemento
arr = np.array([1, 2, 3, 4, 5])
result = arr * 2  # [2, 4, 6, 8, 10]

# Reshape para broadcasting
arr = np.array([1, 2, 3])
arr_reshaped = arr.reshape(-1, 1)  # columna
```

### Q20: ¿Cómo generar datos sintéticos?
```python
# Números aleatorios uniformes
uniform = np.random.uniform(0, 1, size=100)

# Normal distribution
normal = np.random.normal(loc=0, scale=1, size=100)

# Integers aleatorios
integers = np.random.randint(0, 10, size=100)

# Sample from array
sample = np.random.choice([1, 2, 3, 4, 5], size=100, replace=True)

# Reproducibilidad
np.random.seed(42)
```

### Q21-Q25: Operaciones NumPy comunes
```python
# Q21: Encontrar índices de valores
indices = np.where(arr > 5)
indices = np.argmax(arr)  # índice del máximo
indices = np.argsort(arr)  # índices ordenados

# Q22: Operaciones condicionales
result = np.where(arr > 5, 'high', 'low')

# Q23: Unique values
unique, counts = np.unique(arr, return_counts=True)

# Q24: Percentiles
p25 = np.percentile(arr, 25)
p50 = np.percentile(arr, 50)  # median
p75 = np.percentile(arr, 75)

# Q25: Clipping values
clipped = np.clip(arr, 0, 100)  # values between 0 and 100
```

---

## 📈 Sección 3: Machine Learning (15 Questions)

### Q26: ¿Cómo dividir datos en train/validation/test?
```python
from sklearn.model_selection import train_test_split

# Simple train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train/val/test split
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, random_state=42  # 0.25 * 0.8 = 0.2
)
```

### Q27: ¿Cómo hacer cross-validation correctamente?
```python
from sklearn.model_selection import cross_val_score, KFold

# K-Fold CV
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')

print(f"CV Scores: {scores}")
print(f"Mean: {scores.mean():.3f} (+/- {scores.std():.3f})")

# Stratified K-Fold (para clasificación desbalanceada)
from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf)
```

### Q28: ¿Cómo calcular métricas de clasificación manualmente?
```python
def calculate_metrics(y_true, y_pred):
    """Calculate classification metrics from scratch"""
    tp = sum((yt == 1) and (yp == 1) for yt, yp in zip(y_true, y_pred))
    tn = sum((yt == 0) and (yp == 0) for yt, yp in zip(y_true, y_pred))
    fp = sum((yt == 0) and (yp == 1) for yt, yp in zip(y_true, y_pred))
    fn = sum((yt == 1) and (yp == 0) for yt, yp in zip(y_true, y_pred))
    
    # Avoid division by zero
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1
    }
```

### Q29: ¿Cómo manejar clases desbalanceadas?
```python
# Método 1: Class weights
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(class_weight='balanced')

# Método 2: SMOTE (oversampling minority class)
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Método 3: Undersampling majority class
from imblearn.under_sampling import RandomUnderSampler
rus = RandomUnderSampler(random_state=42)
X_resampled, y_resampled = rus.fit_resample(X_train, y_train)

# Método 4: Adjust decision threshold
y_proba = model.predict_proba(X_test)[:, 1]
y_pred = (y_proba > 0.3).astype(int)  # lower threshold
```

### Q30: ¿Cómo hacer feature selection?
```python
# Método 1: Correlation-based
corr_matrix = df.corr()
high_corr = corr_matrix[corr_matrix.abs() > 0.8]

# Método 2: Variance threshold
from sklearn.feature_selection import VarianceThreshold
selector = VarianceThreshold(threshold=0.01)
X_selected = selector.fit_transform(X)

# Método 3: SelectKBest (univariate)
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(f_classif, k=10)
X_selected = selector.fit_transform(X, y)

# Método 4: Feature importance from model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
importances = pd.Series(
    model.feature_importances_, 
    index=X.columns
).sort_values(ascending=False)
```

### Q31: ¿Cómo crear un pipeline de ML completo?
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

# Crear pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=10)),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Entrenar
pipeline.fit(X_train, y_train)

# Predecir
y_pred = pipeline.predict(X_test)

# Grid search sobre pipeline
from sklearn.model_selection import GridSearchCV
param_grid = {
    'pca__n_components': [5, 10, 15],
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [None, 10, 20]
}
grid_search = GridSearchCV(pipeline, param_grid, cv=5)
grid_search.fit(X_train, y_train)
```

### Q32: ¿Cómo evaluar un modelo de regresión?
```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# MAPE (Mean Absolute Percentage Error)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100

print(f"MAE: {mae:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"R²: {r2:.3f}")
print(f"MAPE: {mape:.2f}%")
```

### Q33: ¿Cómo implementar K-Nearest Neighbors desde cero?
```python
class KNN:
    def __init__(self, k=3):
        self.k = k
        
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
        
    def predict(self, X_test):
        predictions = []
        for test_point in X_test:
            # Calculate distances to all training points
            distances = [
                np.sqrt(np.sum((test_point - train_point)**2))
                for train_point in self.X_train
            ]
            
            # Get k nearest neighbors
            k_indices = np.argsort(distances)[:self.k]
            k_nearest_labels = self.y_train[k_indices]
            
            # Majority vote
            prediction = np.bincount(k_nearest_labels).argmax()
            predictions.append(prediction)
            
        return np.array(predictions)
```

### Q34: ¿Cómo implementar Logistic Regression desde cero?
```python
class LogisticRegressionScratch:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.lr = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for _ in range(self.n_iterations):
            # Forward pass
            linear_pred = np.dot(X, self.weights) + self.bias
            predictions = self.sigmoid(linear_pred)
            
            # Compute gradients
            dw = (1/n_samples) * np.dot(X.T, (predictions - y))
            db = (1/n_samples) * np.sum(predictions - y)
            
            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
    
    def predict(self, X):
        linear_pred = np.dot(X, self.weights) + self.bias
        y_pred = self.sigmoid(linear_pred)
        return (y_pred > 0.5).astype(int)
```

### Q35: ¿Cómo manejar categorical features con muchas categorías?
```python
# Método 1: Frequency encoding
def frequency_encode(df, column):
    freq = df[column].value_counts(normalize=True)
    df[f'{column}_freq'] = df[column].map(freq)
    return df

# Método 2: Target encoding con regularización
def target_encode_smooth(df, column, target, alpha=5):
    """Target encoding with smoothing"""
    global_mean = df[target].mean()
    agg = df.groupby(column)[target].agg(['mean', 'count'])
    
    # Smoothing formula
    smooth = (agg['count'] * agg['mean'] + alpha * global_mean) / (agg['count'] + alpha)
    
    df[f'{column}_encoded'] = df[column].map(smooth)
    return df

# Método 3: Keep top N, rest as "Other"
def reduce_categories(df, column, top_n=10):
    top_categories = df[column].value_counts().head(top_n).index
    df[f'{column}_reduced'] = df[column].apply(
        lambda x: x if x in top_categories else 'Other'
    )
    return df
```

### Q36-Q40: Conceptos ML importantes
```python
# Q36: Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)

# Q37: ROC Curve and AUC
from sklearn.metrics import roc_curve, roc_auc_score
fpr, tpr, thresholds = roc_curve(y_true, y_proba)
auc = roc_auc_score(y_true, y_proba)

# Q38: Learning curves
from sklearn.model_selection import learning_curve
train_sizes, train_scores, val_scores = learning_curve(
    model, X, y, cv=5, scoring='accuracy',
    train_sizes=np.linspace(0.1, 1.0, 10)
)

# Q39: Handle outliers en predictions
def remove_prediction_outliers(y_pred, threshold=3):
    z_scores = np.abs(stats.zscore(y_pred))
    return y_pred[z_scores < threshold]

# Q40: Ensemble voting
from sklearn.ensemble import VotingClassifier
voting_clf = VotingClassifier(
    estimators=[
        ('lr', LogisticRegression()),
        ('rf', RandomForestClassifier()),
        ('svm', SVC(probability=True))
    ],
    voting='soft'  # or 'hard'
)
```

---

## 📊 Sección 4: Statistical Testing (10 Questions)

### Q41: ¿Cómo realizar un t-test?
```python
from scipy import stats

# One-sample t-test
t_stat, p_value = stats.ttest_1samp(sample, popmean=100)

# Two-sample t-test (independent)
t_stat, p_value = stats.ttest_ind(group1, group2)

# Paired t-test
t_stat, p_value = stats.ttest_rel(before, after)

# Interpretación
alpha = 0.05
if p_value < alpha:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")
```

### Q42: ¿Cómo hacer un A/B test?
```python
def ab_test(control, treatment, alpha=0.05):
    """
    Perform A/B test for conversion rates
    """
    from scipy.stats import chi2_contingency
    
    # Create contingency table
    conversions_control = sum(control)
    conversions_treatment = sum(treatment)
    
    table = [
        [conversions_control, len(control) - conversions_control],
        [conversions_treatment, len(treatment) - conversions_treatment]
    ]
    
    # Chi-square test
    chi2, p_value, dof, expected = chi2_contingency(table)
    
    # Calculate conversion rates
    rate_control = conversions_control / len(control)
    rate_treatment = conversions_treatment / len(treatment)
    
    # Calculate lift
    lift = (rate_treatment - rate_control) / rate_control * 100
    
    return {
        'control_rate': rate_control,
        'treatment_rate': rate_treatment,
        'lift_percentage': lift,
        'p_value': p_value,
        'statistically_significant': p_value < alpha
    }
```

### Q43: ¿Cómo testear normalidad?
```python
from scipy.stats import shapiro, normaltest, anderson

# Shapiro-Wilk test
stat, p_value = shapiro(data)

# D'Agostino's K² test
stat, p_value = normaltest(data)

# Anderson-Darling test
result = anderson(data)

# Visual tests
import matplotlib.pyplot as plt

# Q-Q plot
from scipy.stats import probplot
probplot(data, plot=plt)

# Histogram
plt.hist(data, bins=30, density=True, alpha=0.7)
```

### Q44: ¿Cómo calcular intervalos de confianza?
```python
from scipy import stats

def confidence_interval(data, confidence=0.95):
    """Calculate confidence interval for mean"""
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)
    
    # t-distribution for small samples
    margin = std_err * stats.t.ppf((1 + confidence) / 2, n - 1)
    
    return (mean - margin, mean + margin)

# Bootstrap confidence interval
def bootstrap_ci(data, n_bootstrap=10000, confidence=0.95):
    """Bootstrap confidence interval"""
    bootstrap_means = []
    
    for _ in range(n_bootstrap):
        sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_means.append(np.mean(sample))
    
    alpha = (1 - confidence) / 2
    lower = np.percentile(bootstrap_means, alpha * 100)
    upper = np.percentile(bootstrap_means, (1 - alpha) * 100)
    
    return (lower, upper)
```

### Q45: ¿Cómo calcular correlaciones y sus p-values?
```python
from scipy.stats import pearsonr, spearmanr

# Pearson correlation (linear relationship)
corr, p_value = pearsonr(x, y)

# Spearman correlation (monotonic relationship)
corr, p_value = spearmanr(x, y)

# Correlation matrix with p-values
def correlation_matrix_with_pvalues(df):
    """Calculate correlation matrix with p-values"""
    from scipy.stats import pearsonr
    
    cols = df.select_dtypes(include=[np.number]).columns
    n = len(cols)
    
    corr_matrix = np.zeros((n, n))
    p_values = np.zeros((n, n))
    
    for i, col1 in enumerate(cols):
        for j, col2 in enumerate(cols):
            corr, p_val = pearsonr(df[col1], df[col2])
            corr_matrix[i, j] = corr
            p_values[i, j] = p_val
    
    return pd.DataFrame(corr_matrix, index=cols, columns=cols), \
           pd.DataFrame(p_values, index=cols, columns=cols)
```

### Q46-Q50: Tests estadísticos adicionales
```python
# Q46: Chi-square test para independencia
from scipy.stats import chi2_contingency
contingency_table = pd.crosstab(df['var1'], df['var2'])
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Q47: ANOVA (comparar múltiples grupos)
from scipy.stats import f_oneway
f_stat, p_value = f_oneway(group1, group2, group3)

# Q48: Mann-Whitney U test (no paramétrico)
from scipy.stats import mannwhitneyu
stat, p_value = mannwhitneyu(group1, group2)

# Q49: Kolmogorov-Smirnov test
from scipy.stats import ks_2samp
stat, p_value = ks_2samp(sample1, sample2)

# Q50: Calculate effect size (Cohen's d)
def cohens_d(group1, group2):
    """Calculate Cohen's d effect size"""
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    d = (np.mean(group1) - np.mean(group2)) / pooled_std
    
    return d
```

---

## 🎯 Tips Finales

### Para cada pregunta en la prueba:
1. ✅ **Lee cuidadosamente** los requerimientos
2. ✅ **Valida inputs** (None, empty, tipos incorrectos)
3. ✅ **Maneja edge cases** (división por cero, listas vacías)
4. ✅ **Comenta** tu código cuando la lógica es compleja
5. ✅ **Testea mentalmente** con ejemplos simples

### Priorización durante la prueba:
1. **Primero:** Funcionalidad correcta
2. **Segundo:** Manejo de edge cases
3. **Tercero:** Optimización (si hay tiempo)
4. **Cuarto:** Clean code y comments

### Recursos para memorizar:
- **Pandas:** groupby, merge, apply, fillna
- **Sklearn:** train_test_split, cross_val_score, metrics
- **Scipy.stats:** ttest_ind, chi2_contingency, pearsonr
- **NumPy:** vectorization, broadcasting, basic math

---

¡Buena suerte! 🚀

Con este quick reference, deberías poder resolver el 80% de las preguntas comunes de coding interviews para Data Scientist.
