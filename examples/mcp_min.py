"""Minimal example of an MCP server using Apiminio with MinIO."""

# Example mcp.json in .vscode directory:
#
# {
# 	"servers": {
# 		"apiminio-mcp": {
# 			"url": "http://localhost:8000/mcp",
# 			"type": "http"
# 		},
# 	},
# 	"inputs": []
# }

from pydantic import SecretStr

from apiminio import Apiminio, McpConfig, MinioConfig

app = Apiminio(
    minio_config=MinioConfig(
        endpoint="localhost:9000",
        access_key="minioadmin",
        secret_key=SecretStr("minioadmin"),
        secure=False,
    ),
    mcp_config=McpConfig(
        enable_mcp=True,  # Default is True
        transport="http",  # Default http, (sse is also supported)
    ),
)

if __name__ == "__main__":
    # Serve FastAPI using Uvicorn
    import uvicorn

    uvicorn.run("mcp_min:app", host="localhost", port=8000, reload=True)
