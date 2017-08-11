# Pythosphere

Pythosphere is a demo application built on Flask and Angular.

## Installation

### Install Python 3

Assuming you have Homebrew installed, `brew install python3` should do the job.

### Create your virtual environment

Get the virtualenv tool; note the `pip3` command for Python 3 packages.

`pip3 install virtualenv`

After checking out this repository, go to the top-level Pythosphere directory and create your environment:

`virtualenv venv`

Your environment doesn't have to be called `venv`, but it's conventional and what .gitignore is expecting. You should see a message along the lines of:

`Using base prefix '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6'`

This indicates that your Homebrew-installed Python 3 is being used. Now activate your environment for further work.

`source venv/bin/activate`

### Install Oracle Instant Client

You'll need Oracle libraries (as of writing, available at http://www.oracle.com/technetwork/topics/intel-macsoft-096467.html) to drive the Python Oracle client.
- Choose the two downloads labeled "Instant Client Package - Basic" and "Instant Client Package - SDK".
- Unzip the downloads into a local directory of your choice, say `/usr/local/share/oracle`. Move them up from any intermediate directory created by unzipping.
- Provide version-agnostic symlinks for a couple of the included files. As of writing, the relevant commands are:
  ```
  ln -s libclntsh.dylib.12.1 libclntsh.dylib
  ln -s libocci.dylib.12.1 libocci.dylib
  ```
- Set a couple of env variables; consider adding them to your shell profile.
  ```
  export ORACLE_HOME=/usr/local/share/oracle
  export DYLD_LIBRARY_PATH=/usr/local/share/oracle
  ```

### Install back-end dependencies

From the top-level Pythosphere directory:

`pip install -r requirements.txt`

Now that your virtual environment is activated, you'll use `pip` rather than `pip3`. (You can use `which pip` to verify that the command is pointing to the virtual environment.) Dependencies are installed into `venv/bin` and `venv/lib/python3.6/site-packages`.

### Install front-end dependencies

`bower install`

Dependencies are installed into `app/static/lib`.

### Create database from schema.sql

TBD

### Create local configurations.

Canvas configuration goes in the `tenants` table; Postgres and EDO Oracle configuration goes into a local config file (`config/development-local.py`). You'll also need an SSH tunnel set up to talk to EDO Oracle.

## Usage

`python run.py` will start a development server on port 5000.