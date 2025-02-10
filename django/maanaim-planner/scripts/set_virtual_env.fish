#!/usr/bin/fish

rm -rf .venv

python -m venv .venv

. .venv/bin/activate.fish

pip install --upgrade pip

pip install -r requirements.txt
