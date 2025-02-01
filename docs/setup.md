# Setup everything related to the project

## Clone the repo:
````commandline
mkdir ~/Workspace && cd ~/Workspace
git clone https://github.com/IEPiXI/NiRo_AI.git && cd NiRo_AI
````

## Create a Python 3.10 env and install python package

### Create the niro env
````commandline
conda create -n niro python=3.10 -y
````
Activate it:
````commandline
conda activate niro
````

Install the NiRo_AI python package:
````commandline
pip install .
````
