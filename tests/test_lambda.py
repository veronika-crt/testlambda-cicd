from src.lambda_function import handler
import types

def test_handler_runs():
    event = {}
    context = types.SimpleNamespace(function_name="test")
    result = handler(event, context)
    assert result is not None