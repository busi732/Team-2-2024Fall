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

## Recommendations

## Future Opportunities
