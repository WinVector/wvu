
pushd pkg
rm -rf dist build wvu.egg-info wvu/__pycache__ tests/__pycache__
pip uninstall -y wvu
pip install --no-deps -e pkg 
pytest --cov wvu > ../coverage.txt
cat ../coverage.txt
python3 setup.py sdist bdist_wheel
# pip install dist/wvu-*.tar.gz
pdoc -o docs ./wvu
popd
twine check pkg/dist/*

