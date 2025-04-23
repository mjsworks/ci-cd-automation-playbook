import optuna
import json

def objective(trial):
    x = trial.suggest_float("x", -10, 10)
    return (x-2) ** 2

study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=10)

# save summary
summary = {
    "best_params": study.best_params,
    "best_value": study.best_value,
    "n_trials": len(study.trials)
}

with open("optuna_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("✅ Training complete. Summary saved to optuna_summary.json")