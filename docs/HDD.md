### Wind Turbine Case Study



We aim to **minimize the total cost** of maintenance and failures, with a focus on deciding between **internal** and **external** maintenance options. Internal maintenance is more expensive per instance but has a higher preventive success rate. In contrast, external maintenance can be cheaper during normal periods but becomes more costly during high-demand seasons. Considering the pros and cons of both methods, our goal is to balance total cost, preventive effectiveness, and operational impact.



### Variables



#### Costs:


**Internal Maintenance Cost:** $C_{\text{internal}} = \$750,000$ per fault type.

**External Maintenance Cost:**
  - During Normal Season: $C_{\text{external\_normal}} = \$50,000$ per trip.
  - During High Demand Season: $C_{\text{external\_high\_demand}} = \$150,000$ per trip.


#### Decision Variables:

- **$x_{\text{internal}}$**: Number of internal maintenance actions chosen (How many fault types to address?).
- **$x_{\text{external\_normal}}$**: Number of external maintenance actions chosen during the normal season (Number of trips of external maintenance needed in normal seasons).
- **$x_{\text{external\_high\_demand}}$**: Number of external maintenance actions chosen during the high-demand season (Number of trips of external maintenance needed in high-demand seasons).



#### Additional Parameters:
- **Preventive Success Rate** $p_{\text{internal}}$: 60% for internal maintenance.
- **Failure Cost** $D_{\text{failure}}$: Downtime cost per failure occurrence (varies by failure type).
- **Failure Frequency** $F_{\text{freq}}$: Typical frequency of faults that could be prevented.
- **Production Requirement** $U_{\text{required}}$: Required uptime to meet energy production commitments.


### Objective Function

To minimize the total cost, including maintenance and failure costs, the function is:

$$
\text{Minimize } \text{TotalCost} = C_{\text{internal}} \cdot x_{\text{internal}} + C_{\text{external\_normal}} \cdot x_{\text{external\_normal}} + C_{\text{external\_high\_demand}} \cdot x_{\text{external\_high\_demand}} + D_{\text{failure}} \cdot F_{\text{occur}}
$$

where $F_{\text{occur}}$ represents the number of failures that occur due to unprevented issues.

### Constraints

The following hypothetical constraints reflect real-world assumptions about wind turbine operations. For an optimization model, select the most critical constraints.

1. **Failure Prevention Model:**
   Each internal maintenance action reduces failure occurrence by 60%:

   $$F_{\text{occur}} = F_{\text{freq}} \cdot (1 - 0.6 \cdot x_{\text{internal}})$$

2. **Uptime Constraint - Production:**
   Total downtime from maintenance and failures should not reduce uptime below the required production threshold. This threshold should satisfy the 80% pre-sold power commitment.

   $$U_{\text{total}} - (\text{downtime from maintenance and failures}) \geq U_{\text{required}}$$

3. **Budget Constraint:**
   Assume there’s a budget $B$ for maintenance costs.

   $$C_{\text{internal}} \cdot x_{\text{internal}} + C_{\text{external\_normal}} \cdot x_{\text{external\_normal}} + C_{\text{external\_high\_demand}} \cdot x_{\text{external\_high\_demand}} \leq B$$

4. **Non-Negativity Constraints:**
   All decision variables must be non-negative.

   $$x_{\text{internal}} \geq 0, \quad x_{\text{external\_normal}} \geq 0, \quad x_{\text{external\_high\_demand}} \geq 0$$