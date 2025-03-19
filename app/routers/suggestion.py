# routers/search.py
from fastapi import APIRouter, Query
from ..es_client import suggestion_global
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()
# CORS configuration
@router.get("/", response_model=dict)
def global_suggestion(q: str, page: int = Query(1, ge=1), page_size: int = Query(10, ge=1)):
    """Global search for vehicles and parts with suggestions."""
    results = suggestion_global(q, page, page_size)
    return results