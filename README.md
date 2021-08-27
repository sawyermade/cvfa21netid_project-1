# Project 1: Transformations

## Clone GitHub Repo
```
# Clone
git clone https://github.com/sawyermade/cvfa21netid_project-1.git

# Change directory name to your netid, example using my netid
# You can also use file explorer, right-click, and rename
mv cvfa21netid_project-1 danielsawyer_project-1

# Enter directory, again using my netid as example
cd danielsawyer_project-1
```

## How To Run

### Anaconda Setup
```
# Install Anaconda Environment
conda env create -f environment.yml
conda activate cvpj1
```

OR

### Pip Setup
```
# Install Modules Pip
pip3 install -r requirements.txt
```

### Run program
```
# Runs program, will write output images to output directory
python3 project.py
```

## How To Submit
For submission replace the cvfa21netid part of the directory with you netid. In my case, my netid is danielsawyer so the directory name would be danielsawyer_project-1.

The whole project should be contained within that directory. Then, zip the directory and only that directory and save it as netid_project-1.zip, where netid is replaced by your netid. In my case, it would be danielsawyer_project-1.zip

DO NOT INCLUDE OUTPUT DIRECTORY!!!

Here is an example tree of the directory structure
```
danielsawyer_project-1.zip contains...

danielsawyer_project-1
├── data
│      ├── baboon.png
│      ├── boat.png
│      ├── building.png
│      ├── girl.png
│      └── tulips.png
├── environment.yml
├── project.py
├── README.md
└── requirements.txt
```