#!/bin/bash

# this script automated the conda environment creation

echo "🔧 Creating a conda environment called 'ci-cd-env'..."
conda create --name ci-cd-env python=3.10 -y

echo "✅ Conda environment created!"

echo "📦 Activating env and installing packages using pip..."
conda activate ci-cd-env
pip install -r requirements.txt

echo "🎉 The environment is ready!"