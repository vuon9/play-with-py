# Play with Py

## Common commands
```bash
python -m venv venv
chmod +x venv/bin/*
source venv/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Install a specific package
pip install <package-name>

# Update the requirements.txt file
pip freeze -l --exclude tabulate --exclude termpdf.py --exclude cffi > requirements.txt
```
