from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import public_svc_profile, private_svc_builds

app = FastAPI(swagger_ui_parameters={"operationsSorter": "method"})
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


app.include_router(public_svc_profile.router)
app.include_router(private_svc_builds.router)
