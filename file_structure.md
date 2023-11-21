# Project Structure Overview

```
📦vite-vanilla-js
 ┣ 📂public
 ┃ ┣ 📂favicon
 ┃ ┃ ┗ 📜logo.svg
 ┃ ┗ 📂svg
 ┃ ┃ ┣ 📜javascript.svg
 ┃ ┃ ┗ 📜vite.svg
 ┣ 📂server
 ┃ ┣ 📂api
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜get_function.py
 ┃ ┃ ┗ 📜post_function.py
 ┃ ┣ 📜README.md
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜main.py
 ┃ ┗ 📜requirements.txt
 ┣ 📂src
 ┃ ┣ 📂css
 ┃ ┃ ┗ 📜style.css
 ┃ ┗ 📂js
 ┃ ┃ ┣ 📜counter.js
 ┃ ┃ ┣ 📜main.js
 ┃ ┃ ┗ 📜testAPI.js
 ┣ 📜.gitignore
 ┣ 📜README.md
 ┣ 📜index.html
 ┣ 📜package.json
 ┗ 📜vite.config.js
```

## Project Components

### 1. `public` Directory

-   Contains static assets served by the frontend.
-   `favicon`: Store your favicon images here.
-   `svg`: SVG images used in the project.

### 2. `server` Directory

-   Backend implementation using FastAPI.
-   `api`: Directory for API-related modules.
-   `main.py`: Entry point for the FastAPI application.
-   `requirements.txt`: Python dependencies for the backend.

### 3. `src` Directory

-   Frontend source code.
-   `css`: Stylesheet files.
-   `js`: JavaScript files.
    -   `counter.js`, `main.js`, `testAPI.js`: Example JavaScript files.

### 4. Other Project Files

-   `.gitignore`: Specifies files and directories to be ignored by Git.
-   `index.html`: Main HTML file for the frontend.
-   `package.json`: Configuration file for Node.js and npm packages.
-   `vite.config.js`: Configuration file for Vite.
