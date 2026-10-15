1. Purpose
    i. To get hands on knowlegde with virtual environment and git/github.
    ii. The project is to manage employee and data is in .json format.

2. For running the project
    i. First clone it and after that create virtual environment and run command as "pip install -r requirements.txt", because I stored required library there.
    ii.. Now we are in our project folder which is "empmgr-project" and when we are trying run out project file with "python empmgr/cli.py". We are getting an error as "ImportError : attempted relative import with no known parent package".
    iii. Here we didn't specify the parent folder for imported modules for example "from .validators import parse_salary" which is relative imports, so here .validators need the parent directory or package to run.
    iv. And when we are trying to run our code as "python -m empmgr.cli", it is working because we are specifying parent package as "empmgr".

3. For setting virtual environment
    i. To manage the versions of libraries for each different project we have virtual environment
    ii. To create virtual environment, we have command as "python -m venv package_name".
    iii. For e.g., if we have package name as .venv we can perform command as "python -m venv .venv".
    iv. After creating virtual environment, we need to check execution policy via "get-executionpolicy".
    v. If it is restricted then use command as "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force".
    vi. And then to activate virtual environment we have command as "package_name\Scripts\activate", in our example it will be like ".venv\Scripts\activate".

4.  History
        (.venv) PS F:\Sushant\Training\python-bootcamp\day06\empmgr-project> git log --oneline --graph --all
        * 94b482f (HEAD -> main, feature/report) Added summary report
        * a0eb1b6 (feature/validation) Update for negative salary and check email
        * e210d51 Added rich library in virtual environment with display data in table
        * aa7c751 Add salary validation
        * aa1207f Add storage module with JSON load/save
        * 653387e models for handling employee operations
        * 42c919b first commit

5.  Peer test: Suraj Kohle
    The code run on first. 
