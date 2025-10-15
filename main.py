import uvicorn
from app import create_app
from config import ENV_CONFIG


app = create_app()


if __name__ == "__main__":
    uvicorn.run(
        'main:app', host=ENV_CONFIG.host, port=ENV_CONFIG.port,
        reload=ENV_CONFIG.debug, workers=ENV_CONFIG.workers
    )
