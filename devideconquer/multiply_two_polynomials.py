from typing import List


p = [0] * 5

def multiply_two_polynomials(m: List, n: List, m_length: int, n_length: int):
    prod = [0] * (m_length+n_length-1)
