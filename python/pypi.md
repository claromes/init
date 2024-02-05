```shell
python setup.py develop

pip3 install setuptools
pip3 install wheel
pip3 install twine

python3 setup.py sdist bdist_wheel
twine upload dist/*
```