#!/bin/bash
set -euo pipefail
echo "Setting up Prior Authorization Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
