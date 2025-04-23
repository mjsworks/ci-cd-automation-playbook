# ✅ CI/CD Module 2: Notebook Execution Check

📁 **Folder:** `02_notebook_execution_check/`  
🔧 **Workflow File:** `.github/workflows/02-test-notebook-execution.yml`  
🎯 **Goal:** Automatically test that all `.ipynb` notebooks run top-to-bottom on a clean GitHub-hosted machine.

---

## 🎓 Learning Objectives

1. Learn how to automate notebook execution using **GitHub Actions**.
2. Understand how to **fail a CI job** if any notebook cell fails.
3. Explore how `nbconvert` can be used to test notebooks programmatically.
4. Gain confidence that notebooks run correctly in a **clean environment** (like a GitHub Runner).

---

## 🧠 Why This Matters

Notebooks often work **locally** but fail elsewhere due to:
- Missing packages
- Hidden variable states
- Bad cell execution order

This workflow ensures notebooks:
- ✅ Run from top to bottom without error
- ✅ Do not depend on hidden state
- ✅ Are trusted by collaborators, employers, or automation systems

---

## 🪜 Step-by-Step Breakdown

### 🔹 Step 1: Create a Test Notebook

Create a minimal notebook inside:

```
02_notebook_execution_check/test_notebook.ipynb
```

---

### 🔹 Step 2: Create GitHub Workflow File

Create the workflow at:

```
.github/workflows/02-test-notebook-execution.yml
```

We’ll break this down into 6 clear mental blocks:

---

### 🧱 Block 1: Define Triggers

```yaml
on:
  push:
    paths:
      - '02_notebook_execution_check/**'
      - '.github/workflows/02-test-notebook-execution.yml'
  pull_request:
```

- ✅ Runs when notebooks or the workflow are changed  
- 💡 **Remember:** Watch specific folders or files to control when CI runs

---

### 🧱 Block 2: Define the Machine

```yaml
runs-on: ubuntu-latest
```

- ✅ Uses Ubuntu for consistency and speed  
- 💡 **Remember:** Stick to `ubuntu-latest` unless you need Windows/macOS

---

### 🧱 Block 3: Checkout the Repository

```yaml
- name: ⬇️ Checkout repository
  uses: actions/checkout@v3
```

- ✅ Downloads your repository to the GitHub runner  
- 💡 **Remember:** Always include this in any GitHub Actions workflow

---

### 🧱 Block 4: Set Up Conda Environment

```yaml
- name: Setup Miniconda
  uses: conda-incubator/setup-miniconda@v2
  with:
    auto-update-conda: true
    python-version: 3.10
    activate-environment: ci-cd-env
```

- ✅ Sets up Python and Conda environment  
- 💡 **Remember:** Set your required Python version and environment name

---

### 🧱 Block 5: Install Dependencies

```yaml
- name: Install dependencies
  run: |
    pip install -r 00_setup/requirements.txt
```

- ✅ Installs required Python packages  
- 💡 **Remember:** Keep your dependencies in a `requirements.txt` file

---

### 🧱 Block 6: Run the Notebook

```yaml
- name: Run the notebook
  run: |
    jupyter nbconvert --to notebook --execute 02_notebook_execution_check/test_notebook.ipynb --output executed.ipynb
```

- ✅ Executes the notebook from top to bottom  
- 💡 **Remember:** You can replace this with any other test logic (`pytest`, `streamlit`, etc.)

---

## ✅ Full Example Workflow

```yaml
name: 🚀 Test Notebook Execution

on:
  push:
    paths:
      - '02_notebook_execution_check/**'
      - '.github/workflows/02-test-notebook-execution.yml'
  pull_request:

jobs:
  run-notebook:
    runs-on: ubuntu-latest
    steps:
      - name: ⬇️ Checkout repository
        uses: actions/checkout@v3

      - name: Setup Miniconda
        uses: conda-incubator/setup-miniconda@v2
        with:
          auto-update-conda: true
          python-version: 3.10
          activate-environment: ci-cd-env

      - name: Install dependencies
        run: |
          pip install -r 00_setup/requirements.txt

      - name: Run the notebook
        run: |
          jupyter nbconvert --to notebook --execute 02_notebook_execution_check/test_notebook.ipynb --output executed.ipynb
```

---


