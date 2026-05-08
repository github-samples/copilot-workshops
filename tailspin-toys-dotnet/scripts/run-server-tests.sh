#!/bin/bash

# Run the ASP.NET Core server tests using dotnet test

# Determine project root
SCRIPT_DIR=$(dirname "$(realpath "$0")")
PROJECT_ROOT="$SCRIPT_DIR/.."
cd "$PROJECT_ROOT" || exit 1

echo "Running server tests..."
dotnet test server/TailspinToys.Tests/TailspinToys.Tests.csproj --verbosity normal
