from fastapi import FastAPI, status
from pydantic import BaseModel
from app.core.config import settings
from app.router import router

root_path = f"/api/{settings.BASE_API_PATH}"

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{root_path}/openapi.json",
    version=settings.API_VERSION,
    description=settings.PROJECT_DESCRIPTION,
    docs_url=f"{root_path}/swagger",
)


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: str = "OK"


@app.get(
    "/health",
    tags=["Health Check"],
    summary="Perform a health check.",
    description="Endpoint to check the status of the application.",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def health_check() -> HealthCheck:
    """Health check endpoint.

    HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck(status="OK")


app.include_router(router, prefix=root_path)


# Run the application with Uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
