## 00_setup reasoning
<br>

### Step1: understanding the necessity of this folder

This `00_setup` folder is the foundation of the entire project. it does 3 things.<br>
1. helps to install everything this project needs
2. sets up secure environment variables
3. prepare a clean workspace for experiments or deployment

### step2: creating the requirements.txt

### step3: create an environment template

Here we will be creating variables for the API access, login detals or all the secrtes. However, we are not going to write the actual value in here. we wil be using `Secrets` to put the actual values. we will be creating `.env.example` here. The real `.env` will go into gitignore becuase we dont want people to have access to our secret keys.

### step4: create a conda env 

just a bit of explanation. in .sh files, we often see `#!/bin/bash`. this is called a `shebang` command.<br>
it essentially tells the system which interpreter should be running this script.<br>
`#!` is the shebang syntax
`/bin/bash` is the path to bash shell<br>

the system uses shebang to know how to execute it.

### step5: running the .sh file
after creating `setup_env.sh`, we go to the terminal and we change it's mode and make it executable. we do `chmod +x setup_env.sh`. once done, we run it. we put `./setup_env.sh`