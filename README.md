# fsimport
Import source file from the file system for Python

This library is a very simple wrapper around

```python
spec = importlib.util.spec_from_file_location('module', str('/full/path/to/module'))
module_inst = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module_inst)
```

It allows for a convenient way to import files based on the file system path. The path is relative to the caller script.

Usage:

```python
import fsimport

include_lv0 = fsimport('../../include_lv0')
include_lv1 = fsimport('../include_lv1')
include_lv2 = fsimport('./include_lv2')
include_lv3 = fsimport('./lv3/include_lv3')
```
