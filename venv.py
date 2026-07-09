# =====================================================================
# PYTHON VIRTUAL ENVIRONMENT (VENV) 
# =====================================================================

# What is a Virtual Environment?
# It is an isolated folder that contains its own Python installation 
# and its own independent packages (via PIP).
# It prevents version conflicts between different projects.

# =====================================================================
# THE WORKFLOW COMMANDS (Run these in your Terminal)
# =====================================================================

# STEP 1: Create the virtual environment (named 'venv')
# command: python -m venv venv

# STEP 2: Activate the virtual environment
# Windows command:      venv\Scripts\activate
# Mac/Linux command:    source venv/bin/activate

# STEP 3: Install packages safely inside the environment
# command: pip install requests

# STEP 4: Save your environment packages list for GitHub
# command: pip freeze > requirements.txt

# STEP 5: Deactivate and leave the environment
# command: deactivate


# =====================================================================
# 3. HOW TO CREATING A .gitignore FILE FOR YOUR PROJECT
# =====================================================================
# To prevent Git from tracking and uploading your heavy virtual environment,
# follow these professional steps:
#
# STEP 1: Create a new file in your project root directory.
#         Name it EXACTLY: .gitignore (Notice the dot at the beginning!)
#
# STEP 2: Open the '.gitignore' file and write the following lines:
#
#         # Ignore Python virtual environments
#         venv/
#         ENV/
#         .env
#
#         # Ignore Python cache files
#         __pycache__/
#         *.pyc
#
# STEP 3: Save the file. Now, Git will automatically ignore the 'venv' 
#         folder, and it will never be uploaded to GitHub!



# =====================================================================
# CRITICAL GIT & GITHUB RULE:
# Never upload the 'venv' folder to GitHub! It contains thousands of 
# heavy files. Always add 'venv/' to your .gitignore file.
# Share 'requirements.txt' instead!
# =====================================================================