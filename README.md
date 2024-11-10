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

## GitHub Actions Workflow

This repository includes a GitHub Actions workflow to automate the process of setting up the environment, installing dependencies, and running tests.

### Triggering the Workflow

The workflow is triggered on `push` and `pull_request` events for the `main` branch. To trigger the workflow, simply push your changes to the `main` branch or create a pull request targeting the `main` branch.
