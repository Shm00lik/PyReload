# 🔥PyReload

Automatically reloads your python scripts when you save them!

## 🔮 How To Use

Just run `python main.py <file_path>` where `<file_path>` is the path to the file you want to reload.

> You can also pass arguments to the script, as you would when running it normally: `python main.py <file_path> <arg1> <arg2> ...`.

## ⚒️ How To Install

Create a new `.bat` file that includes the following code:

```bat
@echo off

IF EXIST "%CD%\venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call "%CD%\venv\Scripts\activate.bat"
) ELSE (
    echo No virtual environment found, proceeding without activation.
)

@echo on

python <PATH TO PYRELOAD'S MAIN FILE> %*
```

> replace the `<PATH TO PYRELOAD'S MAIN FILE>` with the path to PyReload's main file

Then, add the folder containing the `.bat` file to your `PATH` environment variable.

Now you can run your script using the `.bat` file.

## 🚧 TODO

-   [x] Installation Script
-   [ ] Reload when one of the imported modules is changed
-   [ ] Add logging
