# **ADR : Code Editor(VSCode) and Extension Configuration**

## **Status**: Accepted

## **Date**: 2024-12-16

### **Context**

To efficiently develop, debug, and maintain our optimization models, our team believe a well-configured development environment is essential. Therefore, we intend to deploy IDE with the following requirements to conduct our project:

1. Virtual environments (e.g., Anaconda environments).
2. Python debugging.
3. Integration with version control systems like Git/GitHub.

Visual Studio Code (**VSCode**) has emerged as the preferred choice due to its lightweight nature, cross-platform compatibility, and rich ecosystem of extensions.

---

### **Decision**

We will use **VSCode** as the primary Integrated Development Environment (IDE) for this project with the following extensions:

#### **Extensions**

Install the following extensions from the Visual Studio Code Marketplace:

- **Python**: Official Microsoft extension for Python development.
    - Features: IntelliSense (auto-completion), debugging, linting, formatting, and support for virtual environments.
- **Jupyter**: Enables running, editing, and debugging Jupyter Notebooks directly in VSCode.
- **GitLens** (optional): Enhances version control visibility with Git features like blame annotations, commit history, and diffs.
- **Gurobi Optimization Tools** (optional): For team members integrating Gurobi's optimization tools directly.

### **Rationale**

- VSCode is lightweight, free, and offers excellent Python development support.
- Extensions such as **Python** and **Jupyter** provide seamless integration with Pyomo models and Jupyter notebooks.
- GitLens ensures better visibility for team collaboration and version control.
- Gurobi offers instant optimization of our objective functions and constraints.


---

### **Impact**

- Faster, more productive development workflow with IntelliSense and debugging.
- Consistent coding practices using linting and formatting tools.
- Improved collaboration with GitLens and shared workspace configurations. 
---

### **Consequences**

- Team members need to install VSCode and required extensions.
- Team members can cooperate on the same project independently.
