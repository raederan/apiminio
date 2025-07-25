# apiminio <!-- omit in toc -->

[![Release](https://img.shields.io/github/v/release/raederan/apiminio)](https://img.shields.io/github/v/release/raederan/apiminio)
[![Build status](https://img.shields.io/github/actions/workflow/status/raederan/apiminio/main.yml?branch=main)](https://github.com/raederan/apiminio/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/raederan/apiminio/branch/main/graph/badge.svg)](https://codecov.io/gh/raederan/apiminio)
[![Commit activity](https://img.shields.io/github/commit-activity/m/raederan/apiminio)](https://img.shields.io/github/commit-activity/m/raederan/apiminio)
[![License](https://img.shields.io/github/license/raederan/apiminio)](https://img.shields.io/github/license/raederan/apiminio)

🚧🚧🚧 apiminio package is under construction 🚧🚧🚧

apiminio is a Python package that provides a ready-to-use REST API for interacting with MinIO S3 storage, built with FastAPI and the MinIO Python client. It enables seamless file uploads, downloads, and bucket management via HTTP interface ideal for integrating MinIO S3 into your applications with minimal setup.

- **Github repository**: <https://github.com/raederan/apiminio/>
- **Documentation** <https://raederan.github.io/apiminio/>

## 📄 Table of Contents <!-- omit in toc -->

- [📚 Project](#-project)
- [🚦 Prerequisites](#-prerequisites)
- [🚀 Install](#-install)
- [✔️ Usage](#️-usage)
- [🥐 Recommended Dev Setup Kubernetes](#-recommended-dev-setup-kubernetes)
  - [🛞 Commands](#-commands)
- [📜 License](#-license)
- [🦥 Authors](#-authors)

## 📚 Project

1. At 1st basic implementation of apiminio, handling buckets and files will be focused.
2. Security will be at the 2nd development stage using authenticated sessions by credentials as well as tokens.
3. Certificate handling and TLS will be the 3rd level.

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

## ✔️ Usage

TBD

## 🥐 Recommended Dev Setup Kubernetes

This repository has a [skaffold.yaml](./skaffold.yaml) configuration with a working minio as well as the apiminio service to bootstrap the development 😎🙌

### 🛞 Commands

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

## 🦥 Authors

[Andreas Räder](https://github.com/raederan)
