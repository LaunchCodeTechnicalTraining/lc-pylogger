## Installing Dependencies

This project depends on the pynput package, which itself has a couple of dependencies.

You will need to load the dependencies found in the `requirements.txt` file into your python3 environment.

### Virtualenv Instructions

If you are using virtualenv to control your virtual python environments you can create a new virtual environment for this project with:

```
virtualenv --python=python3 env_pylogger
```

You can then activate the new environment with:

```
source env_pylogger/bin/activate
```

After your environment is activated you can load the dependencies into this environment with:

```
pip3 install -r requirements.txt
```

Your `/env_pylogger` will now have Python3, and the dependencies necessary for running this project.


## Running project

Simply executing `python3 main.py` while the configured environment has the necessary dependencies should start the task attached to your current terminal.

### Detach from terminal

You can run the command and detach it from your terminal with:

```
python3 path/to/main.py &
```

Now the logger is running in the background. YOu can kill it with:

```
kill -9 [PID]
```

Where `[PID]` is the process id your terminal displayed to STDOUT when you ran the command and detached.
