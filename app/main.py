import uvicorn

from app.infrastructure.environment import get_settings
from app.app import init_app


_SETTINGS = get_settings()

app = init_app(_SETTINGS)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)


