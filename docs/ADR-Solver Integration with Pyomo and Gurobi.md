# Solver Integration with Pyomo and Gurobi

## **Status**: Accepted

## **Date**: 2024-12-11

## **Context**

Our optimization models involve solving complex Mixed-Integer Programming (MIP) and Linear Programming (LP) problems. A reliable and efficient solver is essential for handling real-world constraints, large datasets, and achieving accurate results.

We have chosen to model our problem using **Pyomo**, a flexible Python-based optimization modeling library. To solve the models, we will integrate the **Gurobi Solver**, which is one of the fastest and most robust solvers for MIP and LP problems.

---

### **Decision**

We will use **Gurobi** as the solver for Pyomo-based optimization models. The integration involves:

#### **1. Installing Gurobi**

- Download and install Gurobi from [Gurobi’s official website](https://www.gurobi.com/).
- Apply for a Gurobi license and activate it by following the manual on Gurobi.    

#### **2. Solver Integration in Pyomo**

Ensure the Gurobi solver is correctly called from Pyomo:

```python
from pyomo.environ import SolverFactory

# Define the solver
solver = SolverFactory('gurobi')

# Solve the model
results = solver.solve(model, tee=True)
```

#### **3. License Configuration**

- Store the Gurobi license file (`gurobi.lic`) in a secure, shared location.
- Each team member must configure for their local license path.


---

### **Rationale**

- **Gurobi** is industry-standard for optimization problems, providing exceptional performance for MIP/LP models.
- **Pyomo** offers a Python-based framework that is highly flexible for constraint modeling and solver integrations.
- Gurobi’s advanced algorithms reduce computation time for large-scale problems.

---

### **Impact**

- Solve larger, more complex optimization models efficiently.
- Ensure accurate and reliable solutions to support decision-making.
- Facilitate our project by testing out more possible objective functions and contraints.

---

### **Consequences**

- Despite efficiency of deploying the Gurobi, it requires a valid license, which could introduce costs for team members without academic access.
- Some team members may need training for Gurobi solver options.

---

### **References**

- [Gurobi Documentation](https://www.gurobi.com/documentation/)
- [Pyomo Documentation](http://www.pyomo.org/)
