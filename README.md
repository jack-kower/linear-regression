# linear-regression
# Steps to start viewing data and models
#
# 1. Clone repo with the "git clone <https> command"
# 2. start a virtual environment by either activating a current virtual environment or by creating a new one
#    a. To create a new one, run the command virtualenv <name of env>
#        i. example would be virtualenv venv
#    b. This is optional. Only to keep downloaded packages contained in one environment
#    c. To activate an already made environement:
#       i. On Windows: <name of environment folder>/Scripts/activate
#       ii. On Mac or Linux: source <name_of_environment>/bin/activate
# 3. ⚠️To install all needed packages, run pip install -r requirements.txt⚠️
# 4. cd into linear-regression/linear-regression-model
# 5. run python3 (on linux or mac) or python (on windows) models.py
#    a. so the command on windows is python models.py
# 6. Here you can see the data plotted.
# 7. If you installed any new packages, add them by running the command pip freeze > requirements.txt
# If you wish to develop, learn, or test on jupyter notebook, type the command: jupyter lab
#   a. Reminder: jupyter notebooks are stored in .ipynb files, so save under this file extension. 
#
# To see the models themselves, look into linear-regression/linear-regression-model
# To look into a web application of using linear regression models, look into linear-regression/linear-regression-application. This feature is still under maintenance.  
#
# Note: Working on jupyter notebook automatically saves the work into the directory specified

# If you need data to use to practice regression, scikit learn has many free open source data sets
#    a. To use these data sets, install pip scikit learn
#    b. import "from sklearn.datasets import <name of data set>"
#    c. For regression, two very popular datasets are load_boston about Boston houring prices and load_diabetes for medical research data on diabetes. 
