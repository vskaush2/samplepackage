## Publishing 

```bash
$ pip install build twine
$ python3 -m build
$ twine check dist/*
$ twine upload -r testpypi dist/* # Upload to TestPyPi
$ twine upload dist/* # Upload to PyPi
```