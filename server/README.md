# FastAPI Project README

## Project Setup

### 1. Create Virtual Environment and activate it

```sh
python -m venv ./venv
```

For Windows:

```sh
.\venv\Scripts\activate
```

For Linux/Mac:

```sh
source ./venv/bin/activate
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

## Running the Server

```sh
uvicorn main:app --reload
```

This will start the FastAPI server with automatic reloading enabled.

## Project Structure

```
📦server
 ┣ 📂api
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜get_function.py
 ┃ ┗ 📜post_function.py
 ┣ 📜README.md
 ┣ 📜__init__.py
 ┣ 📜main.py
 ┗ 📜requirements.txt
```

-   **api/**: This folder is intended for storing your API modules. Create your API modules within this directory.

-   **main.py**: The entry point for your FastAPI application. Include your API modules here.

## Creating Your API

1. Create a new Python module (e.g., `your_api_module.py`) in the `api/` directory.

2. Define your FastAPI router in the module. Example:

    ```python
    from fastapi import APIRouter

    router = APIRouter()

    @router.get("/read_root")
    def read_root():
        return {"message": "Hello, FastAPI!"}
    ```

3. Include your newly created API module in the `main.py` file:

    ```python
    from fastapi import FastAPI
    from api import your_api_module

    app = FastAPI()

    app.include_router(your_api_module.router)
    ```

    Replace `your_api_module` with the actual name of your module.

4. Run the server using the command mentioned in the "Running the Server" section.

## Explore APIs

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive documentation and to explore the existing APIs. This page provides detailed information about each API endpoint, request parameters, and allows you to make requests directly from your browser.
