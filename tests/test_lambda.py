
import types
import pytest
from src import lambda_function

def test_lambda_handler_status_code():
    """Smoke test: Lambda handler returns 200 status code"""
    event = {}
    context = types.SimpleNamespace(function_name="test")
    result = lambda_function.lambda_handler(event, context)
    assert result["statusCode"] == 200

def test_lambda_handler_body():
    """Smoke test: Lambda handler returns expected body"""
    event = {}
    context = types.SimpleNamespace(function_name="test")
    result = lambda_function.lambda_handler(event, context)
    assert result["body"] == "Hello from Lambda!"

def test_greet_handler_status_code():
    """Smoke test: greet_handler returns 200 status code"""
    event = {"name": "Veronika"}
    context = types.SimpleNamespace(function_name="test")
    result = lambda_function.greet_handler(event, context)
    assert result["statusCode"] == 200

def test_greet_handler_body():
    """Smoke test: greet_handler returns correct greeting"""
    event = {"name": "Veronika"}
    context = types.SimpleNamespace(function_name="test")
    result = lambda_function.greet_handler(event, context)
    assert "Veronika" in result["body"]