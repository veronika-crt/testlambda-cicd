
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


# Regression Tests
def test_greet_handler_default_name():
    """Regression: greet_handler should default to 'Guest' if no name provided"""
    event = {}
    context = types.SimpleNamespace(function_name="test")
    result = lambda_function.greet_handler(event, context)
    assert "Guest" in result["body"]

def test_lambda_handler_unexpected_event():
    """Regression: lambda_handler should handle unexpected event keys gracefully"""
    event = {"unexpected": "value"}
    context = types.SimpleNamespace(function_name="test")
    result = lambda_function.lambda_handler(event, context)
    assert result["statusCode"] == 200
    assert "Hello from Lambda!" in result["body"]

def test_greet_handler_non_string_name():
    """Regression: greet_handler should handle non-string name values"""
    event = {"name": 12345}
    context = types.SimpleNamespace(function_name="test")
    result = lambda_function.greet_handler(event, context)
    assert "12345" in result["body"]