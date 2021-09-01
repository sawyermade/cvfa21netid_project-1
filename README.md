# Project 1: Transformations

## Assignment Info
[Assignment 1 Info](Assignment_1.pdf)

## Clone GitHub Repo
```
# Clone
git clone https://github.com/sawyermade/cvfa21netid_project-1.git

# Change directory name to your netid, example using my netid
# You can also use file explorer, right-click, and rename
mv cvfa21netid_project-1 danielsawyer_project-1

# Enter directory, again using my netid as an example
cd danielsawyer_project-1
```

## How To Run: Python

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

## How To Run: Colab
Open project.py in a text editor and then copy/paste into a new Colab Notebook.

DO NOT ADD ANY NEW CODE CELLS OR TEXT CELLS!!!

Also, do not use any inline "!" bash commands in your code. You wont need it and it will mess up the grading process, which will lose you points since you cant follow instructions.

Once coding is complete go to the File tab in Colab, then Download, choose ".py", save as project.py, and overwrite the original project.py in the original directory you cloned/downloaded earlier. Then submit according to the section below.

## How To Submit
For submission replace the cvfa21netid part of the directory with you netid. In my case, my netid is danielsawyer so the directory name would be danielsawyer_project-1

The whole project should be contained within that directory. Then zip the directory, and only that directory, then save it as netid_project-1.zip where netid is replaced by your netid. In my case, it would be danielsawyer_project-1.zip

DO NOT INCLUDE OUTPUT DIRECTORY!!!

So either delete or move the output directory.

ALSO include your 2 PAGE REPORT as report.pdf in the main directory.

After creating the zip file, upload it to Canvas by the submission due date.

Here is an example tree of the directory structure you should be turning in with the netid being danielsawyer.

danielsawyer_project-1.zip contains...

```
danielsawyer_project-1
├── data
│   ├── batch
│   │   ├── 0.jpg
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   ├── 3.jpg
│   │   ├── 4.jpg
│   │   ├── 5.jpg
│   │   ├── 6.jpg
│   │   ├── 7.jpg
│   │   ├── 8.jpg
│   │   └── 9.jpg
│   ├── baboon.png
│   ├── boat.png
│   ├── building.png
│   ├── girl.png
│   └── tulips.png
├── environment.yml
├── Project_1.pdf
├── project.py
├── README.md
├── report.pdf
├── requirements.txt
└── transformations.txt
```
