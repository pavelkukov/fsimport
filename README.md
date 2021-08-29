# fsimport
Import source file from the file system for Python

This library is a simple wrapper around

```python
spec = importlib.util.spec_from_file_location('module', str('/full/path/to/module'))
module_inst = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module_inst)
```

It is a convenient way to import files based on the file system path. The path is relative to the caller script.

## Usage:

```python
import fsimport

include_two_levels_up = fsimport('../../file.py')
include_level_up = fsimport('../another_py_file_without_ext')
include_same_level = fsimport('./include_me')
include_level_down = fsimport('./lv3/include_me.py')
```

## Install

`pip install fsimport`


## Links
PyPI - https://pypi.org/project/fsimport/0.0.3/
