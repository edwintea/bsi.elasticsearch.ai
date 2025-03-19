from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.routers import (
    media,
    media_ocrs,
    part_categories,
    part_groups,
    part_has_vehicle_has_model_years,
    part_has_vehicle_has_production_years,
    part_has_vehicle_has_variants,
    part_has_vehicles,
    part_image_ocr_has_part_number_cars,
    part_image_ocrs,
    part_images,
    part_number_car_has_variants,
    part_number_cars,
    parts,
    vehicle_has_model_years,
    vehicle_has_production_years,
    vehicle_has_source_of_truths,
    vehicle_has_variants,
    vehicles,
    search,
    suggestion
)

app = FastAPI()
app.mount("/static", StaticFiles(directory="./app/static"), name="static")
templates = Jinja2Templates(directory="./app/static")

# CORS configuration

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify your frontend origin)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


# Include routers with the /api prefix
app.include_router(media.router, prefix="/api/media", tags=["media"])
app.include_router(media_ocrs.router, prefix="/api/media_ocrs", tags=["media_ocrs"])
app.include_router(part_categories.router, prefix="/api/part_categories", tags=["part_categories"])
app.include_router(part_groups.router, prefix="/api/part_groups", tags=["part_groups"])
app.include_router(part_has_vehicle_has_model_years.router, prefix="/api/part_has_vehicle_has_model_years", tags=["part_has_vehicle_has_model_years"])
app.include_router(part_has_vehicle_has_production_years.router, prefix="/api/part_has_vehicle_has_production_years", tags=["part_has_vehicle_has_production_years"])
app.include_router(part_has_vehicle_has_variants.router, prefix="/api/part_has_vehicle_has_variants", tags=["part_has_vehicle_has_variants"])
app.include_router(part_has_vehicles.router, prefix="/api/part_has_vehicles", tags=["part_has_vehicles"])
app.include_router(part_image_ocr_has_part_number_cars.router, prefix="/api/part_image_ocr_has_part_number_cars", tags=["part_image_ocr_has_part_number_cars"])
app.include_router(part_image_ocrs.router, prefix="/api/part_image_ocrs", tags=["part_image_ocrs"])
app.include_router(part_images.router, prefix="/api/part_images", tags=["part_images"])
app.include_router(part_number_car_has_variants.router, prefix="/api/part_number_car_has_variants", tags=["part_number_car_has_variants"])
app.include_router(part_number_cars.router, prefix="/api/part_number_cars", tags=["part_number_cars"])
app.include_router(parts.router, prefix="/api/parts", tags=["parts"])
app.include_router(vehicle_has_model_years.router, prefix="/api/vehicle_has_model_years", tags=["vehicle_has_model_years"])
app.include_router(vehicle_has_production_years.router, prefix="/api/vehicle_has_production_years", tags=["vehicle_has_production_years"])
app.include_router(vehicle_has_source_of_truths.router, prefix="/api/vehicle_has_source_of_truths", tags=["vehicle_has_source_of_truths"])
app.include_router(vehicle_has_variants.router, prefix="/api/vehicle_has_variants", tags=["vehicle_has_variants"])
app.include_router(vehicles.router, prefix="/api/vehicles", tags=["vehicles"])
app.include_router(search.router, prefix="/api/search", tags=["search"])
app.include_router(suggestion.router, prefix="/api/suggestion", tags=["suggestion"])

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})