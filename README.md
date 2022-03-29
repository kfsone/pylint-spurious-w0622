# Pylint W0622 bug demonstration
(tested with python 3.8, 2.12.2<=pylint<=2.13.3)

A simple repro of Pylint under Linux ignoring a disable=redefined-builtin. The same does not
occur under Windows or MacOS with 3.8<=Python<=3.10 and the same range of pylints.

# Summary
Pylint disregards "disable=redefined-builtin" in some cases in files that were
"found" as opposed to being explicitly specified.

```
	--- testme.py ---
	# pylint: disable=redefined-builtin
	...
	def fn():
	...
		something.globals = None  # pylint: disable=redefined-builtin
	--- testme.py ---
```

Will still report the redefined builtin on the last line when pylint is run with a
search path rather than specifying the file directly.


# Usage:

```
$ python3.8 -m venv venv38
$ . venv38/bin/activate
$ hash -r
$ pip install pylint==2.13.3
$ pylint --rcfile=pylintrc --persistent=no src/Testme.py src/__init__.py src/test_Testme.py
# passes without errors
$ pylint --rcfile=pylintrc --persistent=no src
# produces an error in test_Testme.py
$ pylint --rcfile=pylintrc --persistent=no src/test_Testme.py src src/test_Testme.py
# still produces an error
```

## Expected outcome:
No errors

## Error outcome:

```
************* Module src.test_Testme
src/test_Testme.py:7: [W0622(redefined-builtin), setUp] Redefining built-in 'globals'
```

## Notes
- `src/test_Testme.py` has a global and line-specific `# pylint: disable=redefined-builtin`,
- error only occurs when a search path is used, even if the file is explicitly named,
