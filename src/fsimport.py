import os
import sys
import inspect
import importlib
from pathlib import Path


def fsimport(rel_path: str) -> any:
    """Return module loaded from file. File path is relative. Example: mod = fsimport('../utils/mod')"""
    call_stack = inspect.stack()

    # prevent infinite loop
    if len(call_stack) > 400:
        raise Exception(f'call stack too large: {len(call_stack)}. Maybe circular dependency.')

    filename = call_stack[1].filename
    parent_folder = Path(os.path.abspath(filename)).parent

    # resolve relative to caller
    target_file_path = Path(os.path.join(parent_folder, os.path.normpath(rel_path))).resolve()

    # if file not found try with .py extension
    if not target_file_path.is_file():
        if not rel_path.endswith('.py'):
            rel_path += '.py'
            target_file_path = Path(os.path.join(parent_folder, os.path.normpath(rel_path))).resolve()

    if not target_file_path.is_file():
        raise Exception(f'cannot find file: {str(target_file_path)}')

    # get file name without extension
    target_name = str(target_file_path.stem)
    spec = importlib.util.spec_from_file_location(target_name, str(target_file_path))
    module_inst = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module_inst)
    return module_inst


sys.modules[__name__] = fsimport