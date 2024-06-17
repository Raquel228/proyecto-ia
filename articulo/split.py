from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Utilizar cross_val_score para la validación cruzada
rf_model = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42)
scores = cross_val_score(rf_model, X_resampled, y_resampled, cv=10, scoring='accuracy')

# Calcular la mediana de las precisiones
median_accuracy = np.median(scores)

print("Mediana de la precisión en la validación cruzada:", median_accuracy)
