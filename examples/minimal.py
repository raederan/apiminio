from pydantic import SecretStr

from apiminio import Apiminio, MinioConfig

app = Apiminio(
    config=MinioConfig(
        endpoint="localhost:9000",
        access_key="minioadmin",
        secret_key=SecretStr("minioadmin"),
        secure=False,
    )
)

if __name__ == "__main__":
    # Serve FastAPI using Uvicorn
    import uvicorn

    uvicorn.run("minimal:app", host="localhost", port=8000, reload=True)
