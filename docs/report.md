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
### Objective Function

## Sensitivity Analysis

### Risks and Assumptions

The analysis conducted in this notebook relies on several key assumptions. These assumptions impact the thresholds and decisions illustrated in the sensitivity analysis graphs. If these assumptions change, the outcomes and interpretations could vary significantly.

1. **Fixed Cost of Maintenance**:
   - The cost of **internal maintenance** is treated as a fixed expense, irrespective of the fault count.
   - External maintenance costs are proportional to the number of faults and are split between normal and high-demand season costs.
   -  **Impact**: If these costs were dynamic (e.g., bulk discounts for external maintenance or variable internal costs), the decision thresholds would shift.



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
