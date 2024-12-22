from pyomo.environ import *
from pyomo.opt import SolverFactory
from pyomo.environ import ConcreteModel, Var, Objective, Binary, minimize, SolverFactory
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Define the logistic function
def logistic_function(x, a, b, c):
    """
    Compute the logistic function.

    This function calculates the logistic function, which is commonly used to model 
    growth processes. The logistic function is defined as:
    c / (1 + exp(-a * (x - b)))

    Parameters:
    x (float or array-like): The input value(s) for which to calculate the logistic function.
    a (float): The steepness of the curve.
    b (float): The x-value of the sigmoid's midpoint.
    c (float): The maximum value of the curve.

    Returns:
    float or array-like: The value(s) of the logistic function evaluated at x.
    """
    return c / (1 + np.exp(-a * (x - b)))




class MaintenanceStrategies_cost:
    def __init__(self, max_faults, high_seasonality, cost_internal=750000, cost_external_normal=50000, cost_external_high_demand=150000, prevention_effect=0.6):
        """
        Initialize the MaintenanceStrategies_cost class with relevant parameters.

        Parameters:
        - max_faults: int, The maximum number of faults expected.
        - high_seasonality: float, Proportion of faults expected during the high-demand season (0 to 1).
        - cost_internal: int, Fixed cost for performing all maintenance internally.
        - cost_external_normal: int, Cost per fault for external maintenance during normal season.
        - cost_external_high_demand: int, Cost per fault for external maintenance during high-demand season.
        - prevention_effect: float, Effectiveness of preventive measures in reducing faults (0 to 1).
        """
        self.max_faults = max_faults
        self.prevention_effect = prevention_effect
        self.high_seasonality = high_seasonality
        self.cost_internal = cost_internal
        self.cost_external_normal = cost_external_normal
        self.cost_external_high = cost_external_high_demand

        # Calculate the number of faults to address after applying preventive measures.
        self.faults_to_address = round((1 - self.prevention_effect) * self.max_faults)

        # Split the faults into high and normal seasonality based on the high_seasonality proportion.
        self.high_seasonality_faults = round(self.high_seasonality * self.faults_to_address)
        self.normal_seasonality_faults = self.faults_to_address - self.high_seasonality_faults

        # Calculate the total cost of addressing faults externally.
        self.total_external_cost = (
            (self.high_seasonality_faults * self.cost_external_high) +
            (self.normal_seasonality_faults * self.cost_external_normal)
        )
    
    def maintenance_decsion(self):
        """
        Decide the optimal maintenance strategy based on the costs.

        Returns:
        - total_cost: int, The total cost of the chosen maintenance strategy.
        - total_internal_maintenance: int, The number of faults addressed internally.
        - total_external_normal_maintenance: int, The number of faults addressed externally during the normal season.
        - total_external_high_maintenance: int, The number of faults addressed externally during the high-demand season.
        """
        # Initialize variables for tracking maintenance decisions and costs.
        total_cost = 0
        total_internal_maintenance = 0
        total_external_normal_maintenance = 0
        total_external_high_maintenance = 0

        # Choose the cost-effective strategy based on internal vs. external maintenance costs.
        if self.total_external_cost <= self.cost_internal:
            # External maintenance is cheaper; assign faults to external providers.
            total_external_normal_maintenance = self.normal_seasonality_faults
            total_external_high_maintenance = self.high_seasonality_faults
            total_cost = self.total_external_cost
        else:
            # Internal maintenance is cheaper; address all faults internally.
            total_internal_maintenance = self.faults_to_address
            total_cost = self.cost_internal

        return total_cost, total_internal_maintenance, total_external_normal_maintenance, total_external_high_maintenance





class MaintenanceStrategy_LinearOpt_cost:
    def __init__(self, max_faults, high_seasonality, cost_internal=750000, cost_external_normal=50000, cost_external_high_demand=150000, prevention_effect=0.6):
        """
        Initialize the maintenance strategy parameters.

        Parameters:
        - max_faults (int): The maximum number of faults expected.
        - high_seasonality (float): The proportion of faults occurring in high-demand seasons (0 to 1).
        - cost_internal (float): Fixed cost for performing internal maintenance.
        - cost_external_normal (float): Cost per fault for external maintenance during normal seasons.
        - cost_external_high_demand (float): Cost per fault for external maintenance during high-demand seasons.
        - prevention_effect (float): Proportion of faults reduced due to preventive measures (0 to 1).
        """
        self.max_faults = max_faults
        self.prevention_effect = prevention_effect
        # Calculate the faults that remain after applying preventive measures
        self.faults_to_address = round((1.0 - self.prevention_effect) * self.max_faults)
        
        self.high_seasonality = high_seasonality
        self.cost_internal = cost_internal  # Fixed cost for internal maintenance
        self.cost_external_normal = cost_external_normal  # Cost per fault for external maintenance (normal season)
        self.cost_external_high = cost_external_high_demand  # Cost per fault for external maintenance (high-demand season)
        self.solver = SolverFactory('gurobi')  # Specify Gurobi as the solver

        # Calculate the seasonal fault distribution
        self.high_seasonality_faults = round(self.high_seasonality * self.faults_to_address)
        self.normal_seasonality_faults = self.faults_to_address - self.high_seasonality_faults
    
    def solve(self):
        """
        Build and solve the Pyomo optimization model.

        Returns:
        - dict: A dictionary containing the optimal decision and total maintenance cost.
        """
        # Create a Pyomo model
        model = ConcreteModel()
        
        # Decision Variable
        model.x_internal = Var(domain=Binary)  # Binary variable: 1 if internal maintenance is chosen, 0 otherwise

        # Objective Function: Minimize total cost
        def total_cost_rule(model):
            """
            Define the total cost calculation.
            - Includes external costs during both normal and high-demand seasons if external maintenance is chosen.
            - Includes fixed internal maintenance cost if internal maintenance is chosen.
            """
            external_cost = (
                self.cost_external_normal * self.normal_seasonality_faults +
                self.cost_external_high * self.high_seasonality_faults
            ) * (1 - model.x_internal)  # Apply only if external maintenance is chosen

            internal_cost = self.cost_internal * model.x_internal  # Apply only if internal maintenance is chosen
            return external_cost + internal_cost
        
        model.obj = Objective(rule=total_cost_rule, sense=minimize)  # Define the objective function
        
        # Solve the model
        results = self.solver.solve(model, tee=True)  # Solve using Gurobi solver and display output
        
        # Check if a feasible solution is found
        x_internal_value = model.x_internal.value  # Retrieve the value of the decision variable
        if x_internal_value is None:
            # If no solution is found, assume all faults are handled externally
            x_internal_value = 0
            total_cost = (
                self.cost_external_normal * self.normal_seasonality_faults +
                self.cost_external_high * self.high_seasonality_faults
            )
        else:
            # Calculate the total cost based on the solution
            total_cost = model.obj()
        
        # Determine maintenance decisions
        x_internal = x_internal_value * self.faults_to_address  # Faults handled internally
        x_external_normal = self.normal_seasonality_faults * (1 - x_internal_value)  # Faults handled externally (normal season)
        x_external_high = self.high_seasonality_faults * (1 - x_internal_value)  # Faults handled externally (high-demand season)
        
        # Store results in a dictionary
        results_dict = {
            "Max Faults": self.max_faults,
            "High Seasonality": self.high_seasonality,
            "Internal Maintenance": x_internal,
            "External Maintenance (Normal)": x_external_normal,
            "External Maintenance (High-Demand)": x_external_high,
            "Total Cost": total_cost
        }
        
        return results_dict


class MaintenanceStrategies_revenue:
    def __init__(self, max_faults, high_seasonality, cost_internal=750000, cost_external_normal=50000, cost_external_high_demand=150000, prevention_effect=0.6, repair_time_external_hr=6, repair_time_internal_hr=8, operation_time_hr=5000, max_revenue=223992786.65):
        """
        Initialize the maintenance strategy parameters for revenue analysis.

        Parameters:
        - max_faults (int): Maximum number of faults expected.
        - high_seasonality (float): Proportion of faults occurring in high-demand seasons (0 to 1).
        - cost_internal (float): Fixed cost for internal maintenance.
        - cost_external_normal (float): Cost per fault for external maintenance during normal seasons.
        - cost_external_high_demand (float): Cost per fault for external maintenance during high-demand seasons.
        - prevention_effect (float): Proportion of faults reduced due to preventive measures (0 to 1).
        - repair_time_external_hr (float): Repair time per fault for external maintenance (in hours).
        - repair_time_internal_hr (float): Repair time per fault for internal maintenance (in hours).
        - operation_time_hr (float): Total operation time in hours.
        - max_revenue (float): Maximum possible revenue.
        """
        self.max_faults = max_faults
        self.prevention_effect = prevention_effect
        self.high_seasonality = high_seasonality
        self.total_internal_cost = cost_internal  # Fixed cost for internal maintenance
        self.cost_external_normal = cost_external_normal  # Cost per fault for external maintenance (normal season)
        self.cost_external_high = cost_external_high_demand  # Cost per fault for external maintenance (high-demand season)

        self.repair_time_external_hr = repair_time_external_hr
        self.repair_time_internal_hr = repair_time_internal_hr
        self.operation_time_hr = operation_time_hr

        # Calculate the faults to address after applying preventive measures
        self.faults_to_address = round((1 - self.prevention_effect) * self.max_faults)

        # Distribute faults across high and normal seasonality
        self.high_seasonality_faults = round(self.high_seasonality * self.faults_to_address)
        self.normal_seasonality_faults = self.faults_to_address - self.high_seasonality_faults

        # Calculate total external maintenance cost
        self.total_external_cost = (
            (self.high_seasonality_faults * self.cost_external_high) +
            (self.normal_seasonality_faults * self.cost_external_normal)
        )

        # Calculate revenue parameters
        self.max_possible_revenue = max_revenue
        self.revenue_generated_per_hour = self.max_possible_revenue / self.operation_time_hr

        # Calculate total downtime and revenue for external maintenance
        self.total_downtime_external_maintenance = self.repair_time_external_hr * self.faults_to_address
        self.revenue_external_maintenance = self.max_possible_revenue - (
            self.total_external_cost + (self.total_downtime_external_maintenance * self.revenue_generated_per_hour)
        )

        # Calculate total downtime and revenue for internal maintenance
        self.total_downtime_internal_maintenance = self.repair_time_internal_hr * self.faults_to_address
        self.revenue_internal_maintenance = self.max_possible_revenue - (
            self.total_internal_cost + (self.total_downtime_internal_maintenance * self.revenue_generated_per_hour)
        )

    def maintenance_decision(self):
        """
        Decide the optimal maintenance strategy based on maximizing revenue.

        Returns:
        - total_revenue (float): The total revenue achieved.
        - total_downtime (float): Total downtime incurred.
        - total_cost (float): Total cost incurred.
        - total_internal_maintenance (int): Number of faults addressed by internal maintenance.
        - total_external_normal_maintenance (int): Number of faults addressed by external maintenance during normal seasons.
        - total_external_high_maintenance (int): Number of faults addressed by external maintenance during high-demand seasons.
        """
        # Initialize results
        total_revenue = 0
        total_downtime = 0
        total_cost = 0
        total_internal_maintenance = 0
        total_external_normal_maintenance = 0
        total_external_high_maintenance = 0

        # Compare revenues for external and internal maintenance
        if self.revenue_external_maintenance > self.revenue_internal_maintenance:
            # Choose external maintenance
            total_revenue = self.revenue_external_maintenance
            total_downtime = self.total_downtime_external_maintenance
            total_cost = self.total_external_cost
            total_external_normal_maintenance = self.normal_seasonality_faults
            total_external_high_maintenance = self.high_seasonality_faults
        else:
            # Choose internal maintenance
            total_revenue = self.revenue_internal_maintenance
            total_downtime = self.total_downtime_internal_maintenance
            total_cost = self.total_internal_cost
            total_internal_maintenance = self.faults_to_address

        return (
            total_revenue,
            total_downtime,
            total_cost,
            total_internal_maintenance,
            total_external_normal_maintenance,
            total_external_high_maintenance
        )
