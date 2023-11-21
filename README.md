# Getting Started with JavaScript for Complete Beginners

Welcome to the world of web development! If you're new to JavaScript, follow these steps to set up a basic project on your computer.

## Step 1: Install a Text Editor

Choose a code editor to write your HTML, CSS, and JavaScript code. A recommended choice is:

-   [Visual Studio Code (VSCode)](https://code.visualstudio.com/)

## Step 2: Install Git, GitHub CLI, Node.js and Node Package Manager (npm)

Git is a version control system that helps you track changes in your code. Follow these steps to install Git:

1.  Download and install Git from [Git official website](https://git-scm.com/downloads).

2.  Verify the installation by running the following command in your terminal:

    ```sh
    git --version
    ```

    You should see the Git version printed in the terminal, confirming a successful installation.

GitHub CLI allows you to interact with GitHub from the command line. Follow these steps:

1.  Install GitHub CLI on macOS, Windows, or Linux. For more information, see [Installation](https://github.com/cli/cli#installation) in the GitHub CLI repository.

2.  Verify the installation by running the following command in your terminal:

    ```sh
    gh --version
    ```

    You should see the GitHub CLI version printed in the terminal, indicating a successful installation.

3.  Authenticate with GitHub by running this command from your terminal:

    ```sh
    gh auth login
    ```

4.  Follow the on-screen prompts.

    > GitHub CLI automatically stores your Git credentials for you when you choose HTTPS as your preferred protocol for Git operations and answer "yes" to the prompt asking if you would like to authenticate to Git with your GitHub credentials. This can be useful as it allows you to use git push, git pull, and so on, without needing to set up a separate credential manager or use SSH.

Node.js allows you to run JavaScript on your machine, and npm helps manage packages (libraries and tools). Follow these steps:

1. Download and install the LTS version of Node.js and npm from [Node.js website](https://nodejs.org/en/download).

2. Verify the installation by opening a terminal (command prompt) and running the following commands:

    ```sh
    node -v
    npm -v
    ```

    You should see versions printed in the terminal, indicating that Node.js and npm are installed.

## Step 3: Set Up Your Project

1. **Find the URL/CLI:**
   Look for the "Code" button (usually in green) on the repository page. Click on it, and a dropdown will appear.

2. **Clone the Repository:**
   Ensure that "GitHub CLI" is selected, and copy the CLI provided. It should look like:

    ```sh
    gh repo clone codersforcauses/vite-vanilla-js-{year}-{group}`
    ```

3. **Navigate to Project Directory:**
   Change your terminal's current directory to the project folder.

    ```sh
    cd vite-vanilla-js-{year}-{group}
    ```

4. **Install Dependencies:**
   Install the project dependencies using npm.

    ```sh
    npm install
    ```

## Step 4: Write Your HTML Code

Open the file named `index.html` in the project root directory and write basic HTML:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Your Web Page Title</title>
        <!-- Link to your CSS file (e.g., styles.css) -->
        <link rel="stylesheet" href="src/styles.css" />
    </head>
    <body>
        <!-- Your content goes here -->
        <script src="src/app.js"></script>
    </body>
</html>
```

## Step 5: Write Your JavaScript and CSS Code

In the `src` folder, there are two folders: `js` for JavaScript and `css` for CSS. Write your code in these files.

-   `src/js/main.js`:

    ```javascript
    // Your JavaScript code goes here
    console.log("Hello, World!");
    ```

-   `src/css/styles.css`:

    ```css
    /* Your CSS code goes here */
    body {
        font-family: "Arial", sans-serif;
        background-color: #f0f0f0;
    }
    ```

## Step 6: Run Your Frontend Project

1. **Development Mode:**
   Run the following command to compile and hot-reload for development:

    ```sh
    npm run dev
    ```

    Open [http://localhost:3000](http://localhost:3000) in your browser to view your project.

2. **Production Mode:**
   When you're ready to deploy your project, run the following command to compile and minify for production:

    ```sh
    npm run build
    ```

Congratulations! You've set up a basic JavaScript project. Experiment with your HTML, CSS, and JavaScript code to build exciting web applications.

Click [here](server/README.md) to set up the server-side of your project.

Once you've set up your project, you can run the frontend and backend simultaneously.

```sh
npm run dev:all
```

## Recommended Visual Studio Code Extensions

-   Prettier - Code formatter
-   ESLint (for JavaScript linting)
-   Thunder Client (for API testing)
-   GitHub Copilot
