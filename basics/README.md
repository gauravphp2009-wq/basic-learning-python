# Basics — Python Command Reference

A concise reference of basic Python commands, useful terminal utilities, and quick examples for working in this project.

**Quick Start**
- **Run script:** `python script.py` — runs a Python file.
- **Run module:** `python -m module_name` — run a module as a script.
- **REPL:** `python` or `python -i script.py` — interactive prompt (or run script then drop to REPL).

**Virtual Environments**
- **Create venv:** `python -m venv venv` — create `venv` folder.
- **Activate (Windows PowerShell):** `venv\Scripts\Activate.ps1`
- **Activate (Windows CMD):** `venv\Scripts\activate.bat`
- **Activate (bash):** `source venv/bin/activate` or `venv/Scripts/activate` on WSL.
- **Install deps:** `pip install -r requirements.txt`
- **Freeze deps:** `pip freeze > requirements.txt`

**Package Management**
- **Install package:** `pip install package_name`
- **Show installed:** `pip list`
- **Upgrade pip:** `python -m pip install --upgrade pip`

**Testing & Linting (quick commands)**
- **Run tests (pytest):** `pytest` (if `pytest` installed).
- **Run flake8:** `flake8 .` — lint project.

**Common `python -m` Utilities**
- **Simple HTTP server:** `python -m http.server 8000` — serve current dir on port 8000.
- **Module runner:** `python -m pip install .` — install local package in editable mode if applicable.
- **Profile a script:** `python -m cProfile -s time script.py`

**Debugging**
- **Run with pdb:** `python -m pdb script.py` — run under debugger.
- **Set breakpoints:** Insert `import pdb; pdb.set_trace()` in code.
- **Verbose import tracing:** `python -v script.py` — verbose mode.

**File & IO Helpers**
- **Read file lines:** `python -c "print(open('file.txt').read())"`
- **One-liner JSON pretty print:** `python -m json.tool input.json > pretty.json`

**Useful Shell Shortcuts / Tips**
- **Run with specific interpreter:** `path\to\python.exe script.py` (useful for multiple Python installs).
- **Check Python path:** `python -c "import sys; print(sys.executable); print(sys.version)"`
- **Use `-u` for unbuffered output:** `python -u script.py` — useful for logs in CI.

**Git & Python**
- **Check python in PATH:** `where python` (Windows) or `which python` (bash)

**Examples from this project**
- Run the main app: `python main.py`
- Insert demo data: `python insert_category.py`
- Create DB table: `python create_table.py`

**Notes & Best Practices**
- Always use a virtual environment per project.
- Pin dependencies in `requirements.txt` for reproducibility.
- Use `python -m venv` rather than third-party tools unless needed.

**VS Code Run Configurations**
- Use `Run Python File` to execute the active file.
- Use `Python: Select Interpreter` to choose the project virtual environment.
- Create a `.vscode/launch.json` for repeatable debugging and run tasks.
- Example `launch.json` snippet:
  ```json
  {
    "version": "0.2.0",
    "configurations": [
      {
        "name": "Python: Run main.py",
        "type": "python",
        "request": "launch",
        "program": "${workspaceFolder}/main.py",
        "console": "integratedTerminal"
      }
    ]
  }
  ```

**Windows PowerShell Commands**
- Activate virtual environment: `& .\venv\Scripts\Activate.ps1`
- Install requirements: `pip install -r requirements.txt`
- Check interpreter path: `python -c "import sys; print(sys.executable)"`
- Run a script: `python .\main.py`
- Deactivate environment: `deactivate`

**Project files added**
- `requirements.txt` lists `fastapi`, `psycopg2-binary`, and `requests`.
- Use `pip install -r requirements.txt` after activating the virtual environment.
