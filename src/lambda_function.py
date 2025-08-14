from src.lambda_function import lambda_handler
import types

def test_lambda_handler_runs():
    event = {}
    context = types.SimpleNamespace(function_name="test")
    result = lambda_handler(event, context)
    assert result is not None
    assert result['statusCode'] == 200
