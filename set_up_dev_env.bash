

conda remove --name wvu_dev_env --all --yes
conda env create -f wvu_dev_env.yaml
conda activate wvu_dev_env
pip install --no-deps -e "$(pwd)/pkg"  # sym link to source files


