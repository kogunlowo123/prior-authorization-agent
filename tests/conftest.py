"""Test configuration for Prior Authorization Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "prior-authorization-agent", "category": "Healthcare"}
