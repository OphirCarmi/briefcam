# Briefcam assignment
## installation
Tested on Ubuntu 18.04 and with python 3.6.9
1. Download this github project zip file by pressing the green "Code" button -> Download zip.
1. Unzip the file: `unzip briefcam-main.zip`
1. Get to the directory with all the ".py" files: `cd briefcam-main`
1. Create python virtual environment in this directory. see tutorial [here](https://towardsdatascience.com/a-data-scientists-guide-to-python-virtual-environments-858841922f14 "here")
basically it's:
```bash
python3 -m venv env
source env/bin/activate
```
5. install dependencies: `pip install -r requirements.txt `
## run
Each of the three scripts, `generator.py`, `estimator.py`, `tester.py` has usage printed when adding `--help`
for example use:
`python3 generator.py --help`

You can use the example `main.py` script and change it for your convenience.
`python3 main.py`
