"""Prior Authorization Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_check_auth_required():
    """Test Check if prior authorization is required for a service."""
    tools = AgentTools()
    result = await tools.check_auth_required(service_code="test", payer_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_submit_authorization():
    """Test Submit prior authorization request with clinical documentation."""
    tools = AgentTools()
    result = await tools.submit_authorization(patient_id="test", service_code="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_check_status():
    """Test Check status of a pending prior authorization."""
    tools = AgentTools()
    result = await tools.check_status(auth_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_prepare_appeal():
    """Test Prepare an appeal for a denied prior authorization."""
    tools = AgentTools()
    result = await tools.prepare_appeal(auth_id="test", denial_reason="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.prior_authorization_agent_agent import PriorAuthorizationAgentAgent
    agent = PriorAuthorizationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
