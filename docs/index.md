# apiminio <!-- omit in toc -->

[![docs.apimin.io](https://img.shields.io/badge/apimin.io-docs-blue
)](https://docs.apimin.io)
[![Release](https://img.shields.io/github/v/release/raederan/apiminio
)](https://github.com/raederan/apiminio/releases)
[![PyPI Version](https://img.shields.io/pypi/v/apiminio)](https://pypi.org/project/apiminio/)
[![Build status](https://img.shields.io/github/actions/workflow/status/raederan/apiminio/main.yml?branch=main)](https://github.com/raederan/apiminio/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/raederan/apiminio/branch/main/graph/badge.svg)](https://codecov.io/gh/raederan/apiminio)
[![Commit activity](https://img.shields.io/github/commit-activity/m/raederan/apiminio)](https://img.shields.io/github/commit-activity/m/raederan/apiminio)
[![License](https://img.shields.io/github/license/raederan/apiminio)](https://img.shields.io/github/license/raederan/apiminio)

[![apiminio banner](https://raw.githubusercontent.com/raederan/apiminio/018c35c90a1cc772611bc2ca17dc926832e3612b/img/apiminio_banner.svg)](https://docs.apimin.io)

apiminio is a Python package that provides a ready-to-use REST API for interacting with MinIO S3 storage, built with FastAPI and the MinIO Python client. It enables seamless file uploads, downloads, and bucket management via HTTP interface ideal for integrating MinIO S3 into your applications with minimal setup.

Additionally, wrapped AI agent tools via MCP are now supported to provide an interface for LLMs to S3 bucket objects ✨

🔜 Customization of your own endpoints!

- **Github repository** <https://github.com/raederan/apiminio/>
- **Documentation** <https://docs.apimin.io/>

## 📄 Table of Contents <!-- omit in toc -->

- [💡 Project](#-project)
- [🚦 Prerequisites](#-prerequisites)
- [🚀 Install](#-install)
- [💥 Usage 🌰🐿️](#-usage-️)
  - [✔️ Minimal Example](#️-minimal-example)
  - [🐍 Run the Server](#-run-the-server)
- [Support](#support)
- [🥐 Kubernetes](#-kubernetes)
- [🛞 Commands](#-commands)
- [📜 License](#-license)
- [🦥 Authors](#-authors)

## 💡 Project

1. [ ] At 1st basic implementation of apiminio, handling buckets and files will be focused.
   1. [x] Create buckets
   2. [x] List buckets
   3. [x] Delete buckets
   4. [x] Upload files
   5. [ ] Download files
   6. [x] Delete files
2. [x] MCP (Model Context Protocol) wrapped endpoints to enable usage for AI agent tools
3. [ ] Customization of additional endpoints and MCP tools
4. [ ] Security will be at the 2nd development stage using authenticated sessions by credentials as well as tokens.
5. [ ] Certificate handling and TLS will be the 3rd level.

## 🚦 Prerequisites

- [minio](https://min.io/docs/minio/kubernetes/upstream/index.html) endpoint, access key, and secret key
- Recommended Dev Setup
  - [Kubernetes](https://github.com/tomhuang12/awesome-k8s-resources)
  - [kubectl](https://kubernetes.io/de/docs/tasks/tools/install-kubectl/)
  - [Skaffold](https://skaffold.dev/docs/)

## 🚀 Install

Recommended

```bash
uv add apiminio
```

or use pip

```bash
pip install apiminio
```

## 💥 Usage 🌰🐿️

Create your python file, e.g., ``apiminio_server.py``, configure your S3 server and run it.
You can use the following examples as a starting point.

### ✔️ Minimal Example

```python
from apiminio import Apiminio, MinioConfig
from pydantic import SecretStr

app = Apiminio(
    minio_config=MinioConfig(
        endpoint="localhost:9000",
        access_key="minioadmin",
        secret_key=SecretStr("minioadmin"),
        secure=False
    )
)

if __name__ == "__main__":
    # Serve FastAPI using Uvicorn
    import uvicorn

    uvicorn.run("minimal:app", host="0.0.0.0", port=8000, reload=True)
```

### 🐍 Run the Server

Either just run ``python apiminio_server.py`` or use ``fastapi run apiminio_server.py``.

> You can use flags and parmeters inherited from ``FastAPI`` to deploy your ``apiminio`` server via ``Uvicorn`` 🦄🐍
> Open [apiminio docs](http://localhost:8000/docs) and explore your new API on [http://localhost:8000](http://localhost:8000/docs) 🔬

## Support

Thats it! Please leave me a ⭐ if you like the projekt 🤗
More features coming soon!

## 🥐 Kubernetes

This repository has a [skaffold.yaml](https://raw.githubusercontent.com/raederan/apiminio/refs/heads/main/skaffold.yaml) configuration with a working minio as well as the apiminio service to bootstrap the development 😎🙌

## 🛞 Commands

To clone this repository, run:

```bash
git clone https://github.com/raederan/apiminio.git
```

To instantly provide minio with apiminio, e.g., run:

```bash
skaffold dev --no-prune=false --cache-artifacts=false --default-repo localhost:32000/apiminio --port-forward
```

## 📜 License

This project is licensed under the terms of the Apache License 2.0.

The [banner file](https://github.com/raederan/apiminio/blob/main/img/apiminio_banner.svg) is based on an original png generated using Microsoft Copilot and subsequently modified further as svg by the initial author of this repository.

## 🦥 Authors

[Andreas Räder](https://github.com/raederan)
