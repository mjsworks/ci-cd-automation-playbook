# 🛠️  Setup Guide 

This folder sets up the machine for the CI/CD Automation Playbook project using Anaconda or Miniconda.

---

## 📦 What's Included?

| File              | Purpose                                |
|-------------------|----------------------------------------|
| `requirements.txt` | List of Python packages for pip       |
| `.env.example`     | Template for environment variables    |
| `setup_env.sh`     | Script to create a Conda environment  |

---

## 🚀 Setup Instructions 

1. Make sure you have Miniconda or Anaconda installed.
2. Open terminal and run:

```bash
cd 00_setup
chmod +x setup_env.sh
./setup_env.sh
```