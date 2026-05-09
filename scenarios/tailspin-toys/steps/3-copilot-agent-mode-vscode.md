## Scenario

As the list of games grows, Tailspin Toys wants to allow users to filter by publisher and category. This will require updating both the API and UI, and updating the tests for the API. With the help of Copilot Agent Mode you'll work with your AI pair programmer to add the new feature!

## Running the application

Before you make any changes, let's explore the Tailspin Toys website to understand its current functionality.

The website is a crowdfunding platform for board games with a developer theme. It allows users to list games and display details about them. The website has two main components: the front-end (written in Svelte) and the backend (written in Python using Flask).

### Starting the application

To make running the website easier, a script has been provided that will start both the front-end and back-end servers. You can run this script in your GitHub Codespace with the following instructions:

1. Return to your codespace. You'll continue working in your current branch.
2. Open a new terminal window inside your codespace by selecting <kbd>Ctl</kbd> + <kbd>\`</kbd>.
3. Run the following script to start the application:

   ```bash
   scripts/start-app.sh
   ```

   Once the script is running, you should see output indicating that both the front-end and back-end servers are running, similar to the below:

   ```bash
   Server (Flask) running at: http://localhost:5100
   Client (Astro) server running at: http://localhost:4321
   ```

> [!NOTE]
> If a dialog box opens prompting you to open a browser window for `http://localhost:5100` close it by selecting the **x**.

4. Open the website by using <kbd>Ctrl</kbd>-**Click** (or <kbd>Cmd</kbd>-**Click** on a Mac) on the client address `http://localhost:4321` in the terminal.

> [!NOTE]
> When using a codespace, selecting a link for the localhost URL from the Codespace terminal will automatically redirect you to `https://<your-codespace-name>-4321.app.github.dev/`. This is a private tunnel to your codespace, which is now hosting your web server!

### Exploring the application

Once the application is running, you can explore its functionality. The main features of the website include:

- **Home Page**: Displays a list of board games with their titles, images, and descriptions.
- **Game Details Page**: When you select a game, you'll be brought to a details page with more information about the game, including its title, description, publisher and category.
