from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import user_router as user
from routes.psychologist import psychologist_router as psychologist

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update when deploying
    allow_credentials=True,  # Allow tokens and cookies
    allow_methods=["*"],  # Restrict methods when deploying
    allow_headers=["*"],
)

# Routes
app.include_router(user)
app.include_router(psychologist)