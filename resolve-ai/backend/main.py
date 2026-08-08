from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Enterprise CX Intelligence & Autonomous Dispute Resolution API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


def analyze_complaint(message):
    text = message.lower()

    # Duplicate payment
    if "duplicate" in text or "charged twice" in text or "charged two times" in text:
        return {
            "category": "duplicate_payment",
            "confidence": 0.95
        }

    # Delivery
    if (
        "delivery" in text
        or "delayed" in text
        or "late" in text
    ):
        return {
            "category": "DELIVERY",
            "confidence": 0.90
        }

    # Fraud
    if (
        "fraud" in text
        or "unauthorized" in text
        or "don't recognize" in text
    ):
        return {
            "category": "FRAUD",
            "intent": "UNAUTHORIZED_TRANSACTION",
            "confidence": 0.95
        }

    # General — MUST BE LAST
    return {
        "category": "general",
        "confidence": 0.50
    }
    # Unknown
    return {
        "category": "OTHER",
        "intent": "UNKNOWN",
        "confidence": 0.60,
        "action": "REQUEST_INFORMATION",
        "status": "PENDING",
        "resolution": "Additional information is required."
    }


@app.get("/")
def home():

    return {
        "message": "ResolveAI is running"
    }


@app.post("/analyze")
def analyze(data: dict):

    message = data.get("message", "")

    if not message:

        return {
            "error": "Please enter a complaint"
        }

    result = analyze_complaint(message)

    return {
        "complaint": message,
        "analysis": result
    }