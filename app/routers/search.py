# routers/search.py
from fastapi import APIRouter, Query
from ..es_client import search_global

router = APIRouter()
@router.get("/", response_model=dict)
def global_search(q: str, page: int = Query(1, ge=1), page_size: int = Query(10, ge=1)):
    """Global search for vehicles and parts with suggestions."""
    results = search_global(q, page, page_size)
    return results