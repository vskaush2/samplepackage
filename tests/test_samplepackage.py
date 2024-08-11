from samplepackage.script import *
import pytest
@pytest.mark.parametrize(
    "input_array_x, input_array_y, coefficient_a, coefficient_b, expected_output",
    [
        (np.array([1.0, 2.0]), np.array([3.0, 4.0]), 0, 0, np.array([0.0, 0.0])),
        (np.array([1.0, 2.0]), np.array([3.0, 4.0]), 1, 0, np.array([1.0, 2.0])),
        (np.array([1.0, 2.0]), np.array([3.0, 4.0]), 0, 1, np.array([3.0, 4.0])),
        (np.array([1.0, 2.0]), np.array([3.0, 4.0]), 1, 1, np.array([4.0, 6.0])),
    ]
)
def test_sample_method(input_array_x, input_array_y, coefficient_a, coefficient_b, expected_output):
    """Test sample method from SampleClass"""
    sample_class_instance = SampleClass(input_array_x, input_array_y)
    actual_output = sample_class_instance.sample_method(coefficient_a, coefficient_b)
    assert np.array_equal(actual_output, expected_output)
