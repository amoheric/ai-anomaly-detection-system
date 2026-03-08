from sklearn.ensemble import IsolationForest


class AnomalyDetector:
    def __init__(self, n_estimators=100, contamination=0.001, random_state=42):
        """
        Isolation Forest based anomaly detection model.
        """
        self.model = IsolationForest(
            n_estimators=n_estimators,
            contamination=contamination,
            random_state=random_state
        )

    def train(self, X):
        """
        Train the model on feature matrix X.
        """
        self.model.fit(X)

    def predict(self, X):
        """
        Predict anomalies in dataset.
        Returns:
        1 = anomaly
        0 = normal
        """
        preds = self.model.predict(X)
        return [1 if p == -1 else 0 for p in preds]