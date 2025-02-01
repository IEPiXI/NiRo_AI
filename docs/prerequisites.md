# Install Everything:

## WSL Ubuntu 24.04 for Windows

Install Ubuntu 24.04 and follow the instructions:
````commandline
wsl --install --d Ubuntu-24.04
````

Check if the installation was completed:
````commandline
wsl -v
````

Activate Ubuntu with WSL
````commandline
wsl
````

Make sure everything is up to date:
````commandline
sudo apt update && sudo apt upgrade
````

## Git and GitHub
Within WSL now install Git and setup GitHub:
````commandline
sudo apt install git -y
````

### Setup Git username & email
````commandline
git config --global user.name <username>
git config --global user.email <user@email.com>
````

### Setup new SSH authentication so you don't need password everytime
````commandline
ssh-keygen -t ed25519 -C <user@email.com>
````
Press enter 3 times

### Copy new public SSH Key to GitHub page, settings > SSH and GPG Keys (https://github.com/settings/keys)
On the website use your ``<user@email.com>`` as **'Title'** and Key type should be **'Authentication Key'** then paste following line:
````commandline
cat ~/.ssh/id_ed25519.pub
````
Test you ssh connection:
````commandline
ssh -T git@github.com
````

## Install Miniconda for python environments
````commandline
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
````
Activate miniconda and init:
````commandline
source ~/miniconda3/bin/activate
````

Update conda just in case:
````commandline
conda update conda -y
````
