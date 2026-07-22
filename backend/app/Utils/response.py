from datetime import datetime


def success(prediction, confidence):
    return {
        "status": "success",
        "prediction": prediction,
        "confidence": round(confidence, 4),
        "timestamp": datetime.now().isoformat()
    }


def failure(message):
    return {
        "status": "error",
        "message": message,
        "timestamp": datetime.now().isoformat()
    }
