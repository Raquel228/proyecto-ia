num_splits = 10
accuracies = []

for _ in range(num_splits):
    # Dividir el dataset
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

    # Entrenar el modelo Random Forest
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)

    # Predecir y calcular la precisión
    y_pred_rf = rf_model.predict(X_test)
    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    accuracies.append(accuracy_rf)

# Calcular la mediana de las precisiones
median_accuracy = np.median(accuracies)

print("Mediana de la precisión en 10 splits:", median_accuracy)
