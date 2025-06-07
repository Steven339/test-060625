from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["System"])
def health_check():
    return {
        "data": {
            "type": "health",
            "id": "status",
            "attributes": {
                "status": "ok"
            }
        }
    }