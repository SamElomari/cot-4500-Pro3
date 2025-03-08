import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from main.assignment_3 import f, euler_method, runge_kutta_method

def test_euler_method():
    t0, y0, t_end, iterations = 0, 1, 2, 10
    expected_output = 1.2446380979332121
    result = euler_method(f, t0, y0, t_end, iterations)
    assert np.isclose(result, expected_output), f"Euler Method failed: got {result}, expected {expected_output}"
    print(f"Euler Method Passed: {result}")

def test_runge_kutta_method():
    t0, y0, t_end, iterations = 0, 1, 2, 10
    expected_output = 1.251316587879806
    result = runge_kutta_method(f, t0, y0, t_end, iterations)
    assert np.isclose(result, expected_output), f"Runge-Kutta Method failed: got {result}, expected {expected_output}"
    print(f"Runge-Kutta Method Passed: {result}")

if __name__ == "__main__":
    test_euler_method()
    test_runge_kutta_method()
