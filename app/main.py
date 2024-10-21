import sentry_sdk
from sentry_sdk.integrations.starlette import StarletteIntegration
from sentry_sdk.integrations.fastapi import FastApiIntegration
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.core.config import settings
from app.router import router

root_path = f"/api/{settings.BASE_API_PATH}"

sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    environment=settings.ENVIRONMENT,
    release=settings.API_VERSION,
    integrations=[
        StarletteIntegration(),
        FastApiIntegration(),
    ],
)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{root_path}/openapi.json",
    version=settings.API_VERSION,
    description=settings.PROJECT_DESCRIPTION,
    docs_url=f"{root_path}/swagger",
)

# Define allowed origins based on the environment
if settings.ENVIRONMENT == "PROD":
    allowed_origins = [
        "185.22.110.31",
        "127.0.0.1",
        "https://www.siamo.app",
        "https://siamo.app",
    ]
else:
    allowed_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        workers=4,
        reload=settings.ENVIRONMENT == "DEV",
    )
