## 02_notebook_execution_check reasoning
<br>
📁 Folder: 02_notebook_execution_check/<br>
🔧 Workflow: .github/workflows/02-test-notebook-execution.yml<br>
🎯 Purpose: Ensure all .ipynb notebooks run successfully from top to bottom on a clean machine.

## Learning Objectives
1. This helps us to learn how to automate the execution of notebook using `GitHub Actions`.
2. Understand how to fail a CI job when notebook fails to execute
3. how nbconvert tests ipynb fikes programmatically.
4. gain confidence that the code works on a clean machine (`GitHub Runner`)

## why this matters
Sometimes notebooks run perfectly on one machine but does not run in another machine. The reason might be due to missing packages, bad cell ordering or skipped cells.

The workflow works as a safety net. it ensures that the notebook:
1. Runs cleanly from top to bottom
2. does not rely on any hidden state
3. can be trusted by collaborators, employers or automated systems.


### step1: Create a test notebook

### step2: create a github workflow file
we will be creating this into our 📄 File: `.github/workflows/02-test-notebook-execution.yml` <br>

at first it might be overwheming to learn how to generate thesw files. however, we dont need to essentially memorize these thing. Instead of memorizing, we will break it into modular mental blocks

`block 1: when should this run?`
```
text
on:
    push:
        paths: 
            - 'some/folder/**'
            - '.github/workflows/this-workflow.yml'
    pull_request:
```