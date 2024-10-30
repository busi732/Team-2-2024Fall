---

# Team-2-2024Fall: Wind Turbine Data Science Project  
This repository is dedicated to **Team 2** in BUSI 732, Fall 2024. The project intends to identify **opportunities for optimization** in wind turbine operations with IIOT (Industrial Internet of Things) data.

---

## 📋 Table of Contents  
1. [Mission](#mission)  
2. [Getting Started](#getting-started)  
3. [Project Setup Instructions](#project-setup-instructions)  
4. [Environment Usage](#environment-usage)  
5. [Updating the Environment](#updating-the-environment)  
6. [Contributing to the Project](#contributing-to-the-project)  
7. [Getting Help](#getting-help)  
8. [Who We Are](#who-we-are)  

---

## 🎯 Mission  
The mission of this project is to **explore the IIOT data from EnergyCo’s wind turbines** and identify areas where operations can be optimized. The analysis will focus on **performance efficiency, predictive maintenance**, and **cost reduction opportunities**. The objective is to build a data science framework that delivers actionable insights to improve turbine uptime and productivity.

---

## 🚀 Getting Started  
This section will guide you on what you need to employ in this project. We mainly work locally in **VS Code** with the **Conda environment**. The next section will teach you how to set up the environment for the project after satisfying the following required software.

- **Prerequisites**:  
    - Install **Git**, **Conda**, and **Python 3.8.x or later**.
    - Ensure that **VS Code** is installed with the **Python** and **Jupyter** extensions enabled.  

---

## 🛠️ Project Setup Instructions  
This section allows you to set up an isolated environment containing all the necessary software for this project.  First, you clone the repository from GitHub, and then you set up the environment, some in-use packages, with the environment.yml file. By doing so, you can ensure compatibility and avoid conflicts with other projects

### 1. **Clone the Repository**  
Open the **terminal** in VS Code and enter:  
```bash
git clone https://github.com/busi732/Team-2-2024Fall.git  
cd Team-2-2024Fall  
```  

💡 **Tip**: Use  (`Ctrl + \``) to call VS Code’s integrated terminal to execute the commands.

---

### 2. **Create the Conda Environment**  
The environment is defined in the `environment.yml` file. Run the following command:  
```bash
conda env create -f environment.yml  
```  

---

### 3. **Activate the Environment**  
After creating the environment, activate it:  
```bash
conda activate turbine_env  
```  

💡 **Tip**: Set VS Code to use the active Conda environment. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS), type **Python: Select Interpreter**, and select the **turbine** environment.

---

## 🌍 Environment Usage  
Once the environment is activated, you can install additional packages as needed using either conda or pip. For example, we install Jupyter Notebook and common data science libraries as following to help us process data in the future.

1. **Installing Packages**  
Install packages using either **conda** or **pip** under the activated environment:  
```bash
conda install <package_name>  
pip install <package_name>  
```  

2. **Example**:  
To install **Jupyter Notebook** and common data science libraries, run:  
```bash
pip install notebook ipython numpy pandas matplotlib seaborn  
```  

3. **Updating All Packages**:  
Keep the environment up-to-date:  
```bash
conda update --all  
```  

---

## 🔄 Updating the Environment  

If new packages are added during development, follow these steps to ensure all team members can stay in sync.  

### Method 1: Create a New Environment File  
```bash
conda env export > new_environment_filename.yml  
```  

### Method 2: Update the Existing `environment.yml` File  
```bash
conda env update --file environment.yml --prune  
```  
💡 **Note**: The `--prune` flag ensures any removed packages are also deleted locally.  

---

## 🔗 Contributing to the Project  
To contribute to the project, commit and push your changes to the main branch. If the environment.yml file is updated, use conda env update to synchronize your local environment. After installing new packages, update the environment.yml file to maintain a clean and efficient environment.
1. **After Making Changes**:  
Use the following commands to update your work on **GitHub**:  
```bash
git add .  
git commit -m "Add new files and update the environment"  
git push origin main  
```  

2. **Collaborative Workflow**:  
- When a team member pulls the latest changes, including an updated `environment.yml` file, they must update their environment:  
    ```bash
    conda env update --file environment.yml --prune  
    ```  
💡 **Note**: The `--prune` flag ensures any packages removed from the environment are also removed locally, keeping everyone’s environment consistent.

3. **Updating the Environment File**:  
After installing any new packages:
```bash
conda env export --no-builds > environment.yml  
```  
This keeps the `environment.yml` clean and avoids unnecessary dependencies.

---

## ❓ Getting Help  

If you encounter any issues:  
- **Open an issue** in the repository’s issue tracker.  
- **Check the `test/` folder** for troubleshooting tips and test notebooks.  
- Reach out to teammates on the project’s communication channel (e.g., Slack or email).  

---

## 👥 Who We Are  

This project is maintained by **Team 2** in **BUSI 732**.  

| Team Member       | Task                   |  
|-------------------|------------------------|  
| ZiYi Huang         |  Analyst     |  
| Javier          | Analyst                |  
| AJ          | Analyst                |  
| Radhey Ruparel         | Developer              |  

---
