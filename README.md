# Play with Py

## Common commands
```bash
python -m venv .
chmod +x ./bin/activate ./bin/deactivate

# Activate the virtual environment
source .venv/bin/activate.fish
source .venv/bin/deactivate.fish

# Install the dependencies
pip install -r requirements.txt
pip install <package-name>

# Update the requirements.txt file
pip freeze -l --exclude tabulate --exclude termpdf.py --exclude cffi > requirements.txt
```
