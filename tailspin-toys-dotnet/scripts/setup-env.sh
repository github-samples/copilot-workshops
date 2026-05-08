#!/bin/bash

# Setup environment: .NET dependencies and Node.js client dependencies

# Determine project root
SCRIPT_DIR=$(dirname "$(realpath "$0")")
PROJECT_ROOT="$SCRIPT_DIR/.."
cd "$PROJECT_ROOT" || exit 1

echo "Restoring .NET dependencies..."
dotnet restore server/TailspinToys.sln

echo "Installing client dependencies..."
cd client || exit 1
npm install

# Return to project root
cd "$PROJECT_ROOT"
echo "Environment setup complete."
