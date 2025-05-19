#!/bin/bash

VENV_DIR=".venv"

if [ ! -d "$VENV_DIR" ]; then
    sudo apt install python3.12-venv
    python3 -m venv "$VENV_DIR"
    echo "Virtual environment created at $VENV_DIR"
else
    echo "Virtual environment already exists at $VENV_DIR"
fi
#/home/beiop/Desktop/mcpil2/mcpil-1/.venv/bin/python3 -m pip install python-tk
/home/beiop/Desktop/mcpil2/mcpil-1/.venv/bin/python3 -m pip install ttkbootstrap