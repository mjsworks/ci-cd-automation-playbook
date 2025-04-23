# 🚀 Module 3: Train and Log a Model with GitHub Actions

This module shows how to run a model training script inside GitHub Actions and save the result to a JSON file.

- 🧠 Uses Optuna to train a toy model
- 📁 Output file: `optuna_summary.json`
- ⚙️ Workflow: `.github/workflows/03-trigger-optuna-run.yml`
- 🧪 Trigger: Runs on push to this folder or the workflow file

## 📝 Output Example

```json
{
  "best_params": {"x": 2.01},
  "best_value": 0.0001,
  "n_trials": 10
}


![Model Training](https://github.com/mjsworks/ci-cd-automation-playbook/actions/workflows/03-trigger-optuna-run.yml/badge.svg)