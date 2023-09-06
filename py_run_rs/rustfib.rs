// rustimport:pyo3

use pyo3::prelude::*;

#[pyfunction]
fn fib(n: u128) -> u128 {
    if n == 0 {
        return 0;
    }
    if n == 1 {
        return 1;
    }
    let mut p_prev: u128 = 0;
    let mut prev: u128 = 1;
    let mut cur: u128 = 1;
    for _ in 0..(n - 1) {
        cur = p_prev + prev;
        p_prev = prev;
        prev = cur;
    }
    cur
}