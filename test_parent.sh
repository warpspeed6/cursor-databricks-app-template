#!/bin/bash

echo "Running setup.sh in new terminal..."

# Create a temporary file for communication
temp_file=$(mktemp)
echo "Parent: Using temp file: $temp_file"

# Launch setup.sh with auto-close flag in new terminal and activate it
osascript -e 'tell application "Terminal" to do script "cd '"$(pwd)"' && ./setup.sh --auto-close '$temp_file'"' -e 'tell application "Terminal" to activate'

echo "Setup launched in new terminal window"
echo "Parent: Waiting for setup to complete..."

# Wait for the setup to complete by monitoring the temp file
while [ ! -s "$temp_file" ]; do
    sleep 1
done

# Clean up temp file
rm "$temp_file"

echo "Parent: Setup completed!"