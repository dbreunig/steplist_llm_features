import pytest
import dspy

from steplist_ai_features.modules.emojifier_predict import EmojifierPredict


@pytest.fixture
def module():
    """Create a module instance for testing."""
    return EmojifierPredict()


def test_module_instantiation(module):
    """Test that the module can be instantiated."""
    assert isinstance(module, dspy.Module)
    assert hasattr(module, 'forward')


def test_module_forward(module):
    """Test the module's forward method."""
    # TODO: Add your test cases here
    # Example:
    # result = module(question="What is 2+2?")
    # assert hasattr(result, 'answer')
    # assert isinstance(result.answer, str)
    pass
