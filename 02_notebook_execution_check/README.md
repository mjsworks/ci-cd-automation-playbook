### ✅ Module 2 Summary: Notebook Execution with CI/CD

**Objective**: Automatically run and validate Jupyter notebooks using GitHub Actions.

- Created `.github/workflows/02-test-notebook-execution.yml`
- Used `nbconvert` to execute `.ipynb` and catch runtime errors
- Fixed common errors:
  - YAML spacing and quoting (python-version: "3.10")
  - Missing `jupyter` CLI in `requirements.txt`
  - Invalid notebook content (empty or uncommitted)
- Final result: Workflow runs on push and confirms that my notebooks don’t break in CI


![Notebook Execution](https://github.com/mjsworks/ci-cd-automation-playbook/actions/workflows/02-test-notebook-execution.yml/badge.svg)
