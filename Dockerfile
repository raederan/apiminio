# Install uv
FROM python:3.12-alpine

WORKDIR /app

RUN pip install --upgrade pip

COPY pyproject.toml ./
COPY README.md ./
RUN pip install .

WORKDIR /app/src/apiminio
COPY src/apiminio/ ./

CMD ["fastapi", "run", "--port", "7676"]
