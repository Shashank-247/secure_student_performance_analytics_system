# from fastapi import FastAPI
# from app.routes import auth
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# app.include_router(auth.router)


# # CORS for frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # production me frontend URL dalna
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(auth.router)


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.routes import auth

# app = FastAPI(title="Secure Student Performance Analytics System", version="1.0.0")

# # CORS for frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Production me frontend URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Include routers
# app.include_router(auth.router)


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth
from app.routes import test_db




app = FastAPI(
    title="Secure Student Performance Analytics System",
    version="1.0.0"
)

app.include_router(test_db.router)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Testing: * , Production: frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(auth.router)


# ye naya test-db router include karo
app.include_router(test_db.router)
