#!/bin/bash

sudo apt update

VENV_DIR=".venv"

if [ ! -d "$VENV_DIR" ]; then
    sudo apt install python3.12-venv
    python3 -m venv "$VENV_DIR"
    echo "Virtual environment created at $VENV_DIR"
else
    echo "Virtual environment already exists at $VENV_DIR"
fi
#/home/beiop/Desktop/mcpil2/mcpil-1/.venv/bin/python3 -m pip install python-tk
echo $VENV_DIR
"$VENV_DIR"/bin/python3 -m pip install ttkbootstrap

#apparently needed for tkextrafont:
"$VENV_DIR"/bin/python3 -m pip install scikit-build && sudo apt install cmake && sudo apt install tk-dev tcl-dev

"$VENV_DIR"/bin/python3 -m pip install tkextrafont