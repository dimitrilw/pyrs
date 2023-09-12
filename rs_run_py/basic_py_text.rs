#!/usr/bin/env rust-script
// cargo-deps: rustpython-vm

// cSpell:ignore builtins

use rustpython_vm as vm;

fn main() -> vm::PyResult<()> {
    vm::Interpreter::without_stdlib(Default::default()).enter(|vm| {
        let scope = vm.new_scope_with_builtins();
        let source = r##"
print("start of script")

def hello():
    print("Hello from Python!")

x = 1
if x == 1:
    hello()
            
print("end of script")
        "##;
        let code_obj = vm
            .compile(source, vm::compiler::Mode::Exec, "<embedded>".to_owned())
            .map_err(|err| vm.new_syntax_error(&err, Some(source)))?;

        vm.run_code_obj(code_obj, scope)?;

        Ok(())
    })
}