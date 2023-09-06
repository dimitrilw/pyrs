// rustimport:pyo3

use pyo3::prelude::*;

#[pyfunction]
fn gcd(a: u128, b: u128) -> u128 {
    if b == 0 { return a };
    if b > a { return gcd(a, b % a) };
    gcd(b, a % b)
}