from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


def calculate_metrics(y_true, y_pred):
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(
            y_true,
            y_pred,
            zero_division=0
        ),
        "recall": recall_score(
            y_true,
            y_pred,
            zero_division=0
        ),
        "f1_score": f1_score(
            y_true,
            y_pred,
            zero_division=0
        ),
        "confusion_matrix": confusion_matrix(
            y_true,
            y_pred
        ).tolist()
    }


if __name__ == "__main__":
    actual = [0, 1, 1, 0, 1]
    predicted = [0, 1, 0, 0, 1]

    print(calculate_metrics(actual, predicted))
