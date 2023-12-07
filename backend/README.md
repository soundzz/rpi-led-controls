# Raspberry Pi LED Controls (Backend)

Made with Python+FastAPI

## Installation
Prerequisites:
- Python 3.10
- pip

Create a virtual environment and install the required packages.
```bash
python -m venv backend-env
source backend-env/bin/activate
pip install -r requirements.txt
```

Create a copy of `env.example` and rename it to `.env`, adjust values according to your setup.

## Usage

Start server using

```bash
uvicorn main:app --host 0.0.0.0
```
or
```bash
uvicorn main:app --reload --host 0.0.0.0
```
for automatic reloads on file change.

The backend is now available at http://127.0.0.1:8000 locally, and at http://your.rpi.ip:8000 with the Swagger UI at http://127.0.0.1:8000/docs accordingly.