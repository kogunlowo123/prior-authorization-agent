# Prior Authorization Agent

[![CI](https://github.com/kogunlowo123/prior-authorization-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/prior-authorization-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Healthcare | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Prior authorization agent that automates insurance pre-authorization requests, checks coverage eligibility, submits clinical documentation, tracks authorization status, and manages appeals for denials.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `check_auth_required` | Check if prior authorization is required for a service |
| `submit_authorization` | Submit prior authorization request with clinical documentation |
| `check_status` | Check status of a pending prior authorization |
| `prepare_appeal` | Prepare an appeal for a denied prior authorization |
| `track_turnaround` | Track prior authorization turnaround times and approval rates |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/prior-authorization/process` | Process request |
| `POST` | `/api/v1/prior-authorization/query` | Query data |
| `POST` | `/api/v1/prior-authorization/validate` | Validate |
| `POST` | `/api/v1/prior-authorization/report` | Generate report |
| `GET` | `/api/v1/prior-authorization/audit` | Get audit trail |

## Features

- Prior
- Authorization
- Compliance
- Interoperability

## Integrations

- Epic Ehr
- Cerner Ehr
- Allscripts
- Fhir Server
- Clearinghouse

## Architecture

```
prior-authorization-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── prior_authorization_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**EHR + Healthcare Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
