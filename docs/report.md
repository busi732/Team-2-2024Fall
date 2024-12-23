<img width="906" alt="Screenshot 2024-12-23 at 1 56 07 AM" src="https://github.com/user-attachments/assets/228a781d-d0cf-4fbe-addb-daac5fc7e3fc" />

Developing a predictive maintenance strategy for EnergyCo's wind turbine in Texas. Using 2014 historical data, we analyzed patterns to build models that optimize maintenance strategy to maximize turbine uptime and improve energy production.

## Table of Contents
1. [Project Summary](#project-summary)
2. [Data Sources](#data-source)
3. [Maintenance Alternatives](#maintenance-alteratives)
4. [Feature Engineering](#feature-engineering)
5. [Linear Optimization](#linear-optimization-problem)
6. [Sensitivity Analysis](#sensitivity-analysis)
7. [Recommendations](#recommendations)
8. [Future Opportunities](#future-opportunities)



## Project Overview
EnergyCo's Wind Department manages a wind turbine in Texas as part of their Environmental, Social, and Governance (ESG) efforts. The department aims to optimize turbine operation, ensuring cost-effectiveness and high energy production through data-driven maintenance decisions.

### Project Goals

1. **Data Analysis:**

   - Analyze historical data to identify patterns and correlations in turbine operations and faults.

2. **Predictive Model Development:**
   - Develop models to anticipate maintenance needs based on historical fault data.

3. **Maintenance Optimization:**
   - Optimize the timing and type of maintenance to reduce costs and maximize turbine uptime and efficiency.


## Data Source
The data pertains to a single wind turbine located in Texas within the ERCOT region, covering the year 2014. Historical data includes fault occurrences, turbine status, and scada turbine operational data was provided. Utilized the ERCOT 2014 pricing data for the Houston Hub for energy prices.
- Fault Data
- Status Data
- SCADA Data
- ERCOT Pricing Data 2014 and 2015

### Data Assumptions
- EnergyCo pre-sold 80% of the expected energy generation based on a historical monthly ERCOT curve.

## Maintenance Alteratives

- **Internal Maintenance:**
  - Annual cost per fault type is $750,000 (inclusive of equipment, salaries, 401k contributions, and related expenses). 

- **External Vendor Maintenance:**
  - Normal Season: $50,000 per trip.
  - High Energy Demand Season: $150,000 per trip.

- **Preventative Maintenance:**
  - Has a 60% chance of preventing a particular type of failure.
## Feature Engineering
## Objective Function

## Maintenance Strategy 1 (Minimize Maintenance Cost)

### **MaintenanceStrategies_cost**

The `MaintenanceStrategies_cost` class is designed to determine the optimal maintenance strategy for minimizing total maintenance costs based on internal and external maintenance options. It incorporates factors such as fault rates, seasonal demand variations, and preventive maintenance effectiveness.

- **Parameters**:
  - `max_faults`: Maximum number of faults expected to occur.
  - `high_seasonality`: Proportion of faults occurring during the high-demand season (e.g., 0.7 indicates 70% faults happen in the high season).
  - `cost_internal`: Fixed cost for handling all faults internally.
  - `cost_external_normal`: Cost per fault for external maintenance during normal demand.
  - `cost_external_high_demand`: Cost per fault for external maintenance during high-demand seasons.
  - `prevention_effect`: Effectiveness of preventive maintenance in reducing fault occurrences.

- **Fault Distribution**:
  - Calculates the reduced number of faults after applying preventive measures (`faults_to_address`).
  - Splits faults into high-demand and normal seasons using the `high_seasonality` parameter.

#### Decision-Making (`maintenance_decsion` Method)
- **Cost Calculation**:
  - Compares the total cost of addressing faults externally (`total_external_cost`) with the fixed cost of internal maintenance (`cost_internal`).
  
- **Strategy Selection**:
  - If external maintenance is cheaper, faults are assigned to external providers, split across normal and high-demand seasons.
  - If internal maintenance is more cost-effective, all faults are addressed internally.

### **MaintenanceStrategy_LinearOpt_cost**


The `MaintenanceStrategy_LinearOpt_cost` class is a streamlined implementation of the `MaintenanceStrategies_cost` class. It is designed to **minimize maintenance costs** using a linear optimization approach with Pyomo and the Gurobi solver. This class determines the optimal maintenance strategy (internal vs. external) based on cost considerations.


- **Parameters**:
  - `max_faults`: Maximum number of faults expected to occur.
  - `high_seasonality`: Proportion of faults occurring during the high-demand season (e.g., 0.7 indicates 70% faults happen in the high season).
  - `cost_internal`: Fixed cost for handling all faults internally.
  - `cost_external_normal`: Cost per fault for external maintenance during normal demand.
  - `cost_external_high_demand`: Cost per fault for external maintenance during high-demand seasons.
  - `prevention_effect`: Effectiveness of preventive maintenance in reducing fault occurrences.


#### Optimization Model
- **Decision Variable**:
  - `x_internal`: A binary variable indicating whether internal maintenance is chosen (`1`) or not (`0`).
- **Objective Function**:
  - Minimizes the total cost of handling faults, which includes:
    - External maintenance costs for faults during normal and high-demand seasons.
    - Internal maintenance fixed costs if chosen.
- **Seasonal Fault Distribution**:
  - Splits faults into high-demand and normal seasons to calculate external maintenance costs.
- **Solver**
  - Uses the Gurobi solver to determine the optimal maintenance decision that minimizes total costs.

|           | **`MaintenanceStrategies_cost`**             | **`MaintenanceStrategy_LinearOpt_cost`**           |
|---------------------------|----------------------------------------------|---------------------------------------------------|
| **Implementation**         | Direct cost comparison.                     | Uses linear optimization with Pyomo and Gurobi.  |


## Maintenance Strategy 2 (Maximize Revenue)

### **MaintenanceStrategies_revenue**
The `MaintenanceStrategies_revenue` class focuses on **maximizing revenue** while managing faults through either internal or external maintenance strategies. It takes into account maintenance costs, downtime, and the impact of preventive maintenance on reducing faults. The class calculates the total revenue generated based on the maintenance strategy and selects the option that results in the **highest revenue**.


### Inputs and Parameters
- **Similar to `MaintenanceStrategies_cost`**:
  - `max_faults`: Maximum number of faults.
  - `high_seasonality`: Proportion of faults in high-demand seasons.
  - `cost_internal`: Fixed cost for internal maintenance.
  - `cost_external_normal`: Cost per fault for external maintenance in normal seasons.
  - `prevention_effect`: Reduction in faults due to preventive maintenance.

- **Additional Parameters**:
  - `repair_time_external_hr`: Time (in hours) to repair a fault using external maintenance.
  - `repair_time_internal_hr`: Time (in hours) to repair a fault using internal maintenance.
  - `operation_time_hr`: Total available operation time (in hours).
  - `max_revenue`: Maximum possible revenue achievable within the operation time.


### Decision Strategy (`maintenance_decision` Method)
- Compares the revenue generated by internal and external maintenance.
- Chooses the maintenance strategy that results in the **highest total revenue**.



## Comparison with `MaintenanceStrategies_cost`

| **Aspect**                       | **`MaintenanceStrategies_cost`**                     | **`MaintenanceStrategies_revenue`**                 |
|-----------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| **Objective**                     | Minimize total maintenance cost.                   | Maximize total revenue.                            |
| **Key Factors in Decision**       | Direct cost comparison between internal and external maintenance. | Considers both maintenance costs and downtime, factoring in revenue loss. |
| **Impact of Downtime**            | Downtime is not explicitly considered.             | Downtime directly affects revenue calculations and decision-making. |
| **Decision Metric**               | Chooses the cheaper option between internal and external maintenance. | Chooses the option that generates the highest revenue. |
| **Output Metrics**                | Total cost, faults addressed by each strategy.      | Total revenue, downtime, cost, and faults handled by each strategy. |
| **Focus**                         | Pure cost minimization.                            | Balances cost, downtime, and revenue generation.    |


## Key Differences in Decision-Making

1. **Consideration of Downtime**:
   - `MaintenanceStrategies_revenue` explicitly incorporates downtime and its revenue impact into the decision process, unlike `MaintenanceStrategies_cost`.

2. **Revenue Maximization vs. Cost Minimization**:
   - The `MaintenanceStrategies_cost` class prioritizes minimizing expenses, making it suitable when downtime costs are negligible or fixed.
   - The `MaintenanceStrategies_revenue` class prioritizes maximizing operational revenue, making it suitable when downtime has a significant financial impact.

3. **Complexity of Decision**:
   - `MaintenanceStrategies_cost` decisions are simpler, based solely on cost comparisons.
   - `MaintenanceStrategies_revenue` involves a more nuanced decision-making process, requiring calculations of downtime, operational hours, and revenue loss.



## Sensitivity Analysis

## Risks and Assumptions

The analysis conducted in this notebook relies on several key assumptions. These assumptions impact the thresholds and decisions illustrated in the sensitivity analysis graphs. If these assumptions change, the outcomes and interpretations could vary significantly.

1. **Fixed Cost of Maintenance**:
- The cost of **internal maintenance** is treated as a fixed expense, irrespective of the fault count.
- External maintenance costs are proportional to the number of faults and are split between normal and high-demand season costs.
- **Impact**: If these costs were dynamic (e.g., bulk discounts for external maintenance or variable internal costs), the decision thresholds would shift.



 2. **Repair Downtime**:
- **Internal Maintenance**:
  - Assumes a longer downtime due to in-house procedures and resource constraints.
- **External Maintenance**:
  - Assumes a shorter downtime due to specialization or external expertise.
-  **Impact**: Changes in the relative downtime between internal and external strategies would alter the preference for each strategy, particularly in the **Revenue Maximization** analysis where downtime directly affects revenue.



3. **Preventative Maintenance Cost is Missing**:
- Preventative maintenance is assumed to reduce faults by a fixed proportion (60% in the scenarios analyzed), but it has no impact in the cost.
- **Impact**: If the Preventative maintenance has a signifcant cost it would have impact both strategies in this analysis as it would affect cost and reveune. 


 4. **Fault Distribution**:
- Faults are distributed between high-demand and normal seasons based on a fixed `high_seasonality` proportion.
- No additional complexity, such as varying fault severity or clustering, is modeled.
- **Impact**: Changes in fault distribution or inclusion of fault severity levels would require adjustments to external and internal maintenance strategies, potentially affecting costs and preferences.



 5. **Revenue Impact of Downtime**:
- In the **Revenue Maximization** strategy, downtime directly reduces revenue in proportion to the total operation time and maximum possible revenue.
- Assumes that downtime scales linearly with the number of faults addressed.
- **Impact**: If downtime has nonlinear effects (e.g., compounding losses during peak demand periods), the thresholds and preferences would shift.


6. **Focus on Binary Maintenance Decisions**:
- Decisions are treated as binary (internal vs. external), with no intermediate options or shared responsibilities.
- **Impact**: Introducing mixed strategies (e.g., partial outsourcing) would make the decision-making process more complex and nuanced.

These assumptions simplify the analysis but also constrain the generalizability of the results. Future iterations of the analysis could incorporate dynamic costs, variable downtimes, or hybrid strategies to better reflect real-world scenarios. Acknowledging these assumptions highlights the sensitivity of the decisions to changes in key parameters and the importance of tailoring the analysis to specific operational contexts.


## Recommendations

## Future Opportunities
