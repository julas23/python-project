import os
import django
from fastapi import FastAPI
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

django_app = get_asgi_application()
app = FastAPI()

# Defina rotas do FastAPI como preferir
from .routes import router
app.include_router(router)

# Monte o Django na aplicação FastAPI
app.mount("/django", django_app)