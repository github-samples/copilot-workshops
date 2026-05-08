#!/bin/bash

# Define color codes
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Store initial directory and script directory
INITIAL_DIR=$(pwd)
SCRIPT_DIR=$(dirname "$(realpath "$0")")
PROJECT_ROOT="$SCRIPT_DIR/.."

cd "$PROJECT_ROOT" || exit 1

echo "Starting API (ASP.NET Core) server..."

# Build and start the .NET API in the background
dotnet run --project server/TailspinToys.Api/TailspinToys.Api.csproj &
SERVER_PID=$!

echo "Starting client (Astro)..."
cd "$PROJECT_ROOT/client" || {
    echo "Error: client directory not found"
    cd "$INITIAL_DIR"
    exit 1
}
npm install
npm run dev -- --no-clearScreen &
CLIENT_PID=$!

# Sleep to allow servers to start
sleep 5

# Display the server URLs
echo -e "\n${GREEN}Server (ASP.NET Core) running at: http://localhost:5100${NC}"
echo -e "${GREEN}Client (Astro) server running at: http://localhost:4321${NC}\n"

echo "Ctl-C to stop the servers"

# Function to handle script termination
cleanup() {
    echo "Shutting down servers..."
    
    kill -TERM $SERVER_PID 2>/dev/null
    kill -TERM $CLIENT_PID 2>/dev/null
    
    sleep 2
    
    if ps -p $SERVER_PID > /dev/null 2>&1; then
        pkill -P $SERVER_PID 2>/dev/null
        kill -9 $SERVER_PID 2>/dev/null
    fi
    
    if ps -p $CLIENT_PID > /dev/null 2>&1; then
        pkill -P $CLIENT_PID 2>/dev/null
        kill -9 $CLIENT_PID 2>/dev/null
    fi
    
    cd "$INITIAL_DIR"
    exit 0
}

# Trap multiple signals
trap cleanup SIGINT SIGTERM SIGQUIT EXIT

# Keep the script running
wait
