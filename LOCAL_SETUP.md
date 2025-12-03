# Local Development Setup Guide

This guide will help you set up and run the Tailspin Toys crowdfunding platform on your local machine without using GitHub Codespaces.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

### Required Software

1. **Python 3.12 or higher**
   - **Windows**: Download from [python.org](https://www.python.org/downloads/)
   - **macOS**: Install via [Homebrew](https://brew.sh/): `brew install python@3.12`
   - **Linux**: Install via your package manager:
     ```bash
     # Ubuntu/Debian
     sudo apt update
     sudo apt install python3.12 python3.12-venv python3-pip
     
     # Fedora
     sudo dnf install python3.12
     ```

2. **Node.js 18.x or higher** (includes npm)
   - Download from [nodejs.org](https://nodejs.org/) (LTS version recommended)
   - Or use [nvm (Node Version Manager)](https://github.com/nvm-sh/nvm):
     ```bash
     nvm install --lts
     nvm use --lts
     ```

3. **Git**
   - **Windows**: Download from [git-scm.com](https://git-scm.com/download/win)
   - **macOS**: Install via Homebrew: `brew install git` or use Xcode Command Line Tools
   - **Linux**: Install via your package manager: `sudo apt install git` (Ubuntu/Debian)

### Verify Installation

Run these commands to verify your installations:

```bash
python3 --version  # Should show 3.12 or higher
node --version     # Should show v18.x or higher
npm --version      # Should show 9.x or higher
git --version      # Should show 2.x or higher
```

## Getting Started

### 1. Clone the Repository

If you're working with the original template:

```bash
git clone https://github.com/github-samples/agents-in-sdlc.git
cd agents-in-sdlc
```

Or if you've already created your own copy from the template:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

### 2. Set Up the Development Environment

The repository includes a setup script that will:
- Create a Python virtual environment
- Install Python dependencies
- Install Node.js dependencies
- Install Playwright browsers for testing

Run the setup script:

```bash
# On macOS/Linux
./scripts/setup-env.sh

# On Windows (using Git Bash or WSL)
bash ./scripts/setup-env.sh
```

> **Note**: The setup script may take several minutes to complete as it downloads and installs all dependencies.

### 3. Start the Application

Once the setup is complete, you can start both the backend API server and the frontend development server:

```bash
./scripts/start-app.sh
```

The script will:
- Start the Flask backend API server on `http://localhost:5100`
- Start the Astro frontend development server on `http://localhost:4321`

You should see output similar to:

```
Starting API (Flask) server...
Starting client (Astro)...

Server (Flask) running at: http://localhost:5100
Client (Astro) server running at: http://localhost:4321
```

### 4. Access the Application

Open your web browser and navigate to:

```
http://localhost:4321
```

You should see the Tailspin Toys crowdfunding platform homepage!

### 5. Stop the Application

To stop both servers, press `Ctrl+C` in the terminal where the application is running.

## Running Tests

### Backend (Python) Tests

To run the Flask API tests:

```bash
./scripts/run-server-tests.sh
```

This script will:
- Set up the Python environment (if not already set up)
- Run all Python unit tests using unittest

### Frontend (End-to-End) Tests

To run the Playwright end-to-end tests:

```bash
cd client
npm run test:e2e
```

> **Note**: Make sure both the backend and frontend servers are running before executing end-to-end tests.

## Project Structure

```
agents-in-sdlc/
├── client/                 # Astro/Svelte frontend
│   ├── src/
│   │   ├── components/    # Svelte components
│   │   ├── layouts/       # Astro layout templates
│   │   ├── pages/         # Astro page routes
│   │   └── styles/        # CSS and Tailwind configuration
│   ├── e2e-tests/         # Playwright end-to-end tests
│   └── package.json       # Node.js dependencies
├── server/                # Flask backend
│   ├── models/           # SQLAlchemy ORM models
│   ├── routes/           # API endpoints
│   ├── tests/            # Python unit tests
│   ├── utils/            # Utility functions
│   ├── app.py           # Flask application entry point
│   └── requirements.txt  # Python dependencies
├── scripts/              # Development scripts
│   ├── setup-env.sh     # Environment setup
│   ├── start-app.sh     # Start both servers
│   └── run-server-tests.sh  # Run Python tests
├── data/                 # SQLite database files
└── docs/                # Workshop documentation
```

## Development Workflow

### Making Code Changes

1. **Backend Changes**: Edit files in the `server/` directory
   - The Flask server runs in debug mode and will auto-reload on changes
   
2. **Frontend Changes**: Edit files in the `client/src/` directory
   - The Astro dev server supports hot module replacement (HMR)
   - Changes will automatically refresh in your browser

### Database

The application uses SQLite for the database, which is stored in the `data/` directory. The database is automatically created when you first run the application.

## Troubleshooting

### Port Already in Use

If you see an error about ports 4321 or 5100 already being in use:

1. Find and stop the process using the port:
   ```bash
   # On macOS/Linux
   lsof -ti:4321 | xargs kill -9
   lsof -ti:5100 | xargs kill -9
   
   # On Windows
   netstat -ano | findstr :4321
   netstat -ano | findstr :5100
   taskkill /PID <PID> /F
   ```

2. Or change the port in the respective configuration files

### Python Virtual Environment Issues

If you encounter issues with the Python virtual environment:

1. Delete the `venv` directory:
   ```bash
   rm -rf venv
   ```

2. Re-run the setup script:
   ```bash
   ./scripts/setup-env.sh
   ```

### Node Modules Issues

If you encounter issues with Node.js dependencies:

1. Delete the `node_modules` directory and `package-lock.json`:
   ```bash
   cd client
   rm -rf node_modules package-lock.json
   ```

2. Reinstall dependencies:
   ```bash
   npm install
   ```

### Permission Denied on Scripts

If you get a "permission denied" error when running scripts:

```bash
chmod +x scripts/*.sh
```

### Playwright Browser Installation

If Playwright browsers are not installed correctly:

```bash
cd client
npx playwright install
```

## Additional Resources

- **Flask Documentation**: https://flask.palletsprojects.com/
- **SQLAlchemy Documentation**: https://www.sqlalchemy.org/
- **Astro Documentation**: https://docs.astro.build/
- **Svelte Documentation**: https://svelte.dev/
- **Tailwind CSS Documentation**: https://tailwindcss.com/

## Workshop Documentation

If you're following the workshop, please refer to the [workshop documentation](./docs/README.md) for guided exercises on using GitHub Copilot and related features.

## Getting Help

If you encounter any issues not covered in this guide:

1. Check the GitHub Issues in the repository for similar problems
2. Review the workshop documentation in the `docs/` directory
3. Open a new issue with details about your environment and the error message

## License

This project is licensed under the terms of the MIT open source license. Please refer to [LICENSE](./LICENSE) for the full terms.
