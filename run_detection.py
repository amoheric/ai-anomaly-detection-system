import pandas as pd
from src.anomaly_model import AnomalyDetector


def main():
    print("Loading dataset...")

    data = pd.read_csv("data/creditcard.csv")
    X = data.drop("Class", axis=1)

    print("Training anomaly detection model...")
    detector = AnomalyDetector()
    detector.train(X)

    print("Detecting anomalies...")
    predictions = detector.predict(X)

    anomalies = sum(predictions)
    print(f"Total anomalies detected: {anomalies}")


if __name__ == "__main__":
    main()