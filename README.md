# pyrs

Python (py) + Rust (rs)

This is a learning repo for experimenting with Python and Rust interoperability.

## py_run_rs: using Python to call Rust code

Folder `py_run_rs` contains Rust code that can be called from Python.

I am following [this writeup](https://pythonspeed.com/articles/easiest-rust-python/)
to get started with Python and Rust interoperability.

This is basically the same "speed up Python" method as the classic
"write a custom module in C/C++" method, but using Rust instead.

And [rustimport](https://github.com/mityax/rustimport) makes it easy. Very easy.
Like "I can't believe it's not butter" easy. Even on-demand compiling when the
script is first run. Wow.

The result is a 10.6x speedup for the Fibonacci + GCD function combo -- not bad.

![results of running run_both.py script](./static/10.6x_improvement.png "10.6x improvement")

Note: rather standard VS-Code Python extension settings will be unhappy with
importing a `.so` file.

![VS-Code Python extension error](./static/vscode-not-happy.png "VS-Code Python extension error")

This happens despite the `.so` files being in the CWD and the Python code
itself imports them & runs them just fine.

![files are in directory](./static/compiled-so-files-are-in-dir.png "files are in directory")

There are multiple methods to fix this behavior, such as adjusting the Python Path,
adding a `.env` file, editing the VS-Code Pylance settings, etc. And I am not
demo'ing that here. :wink:
