# G2M Insight for Cab Investment Firm

## Project Overview
XYZ, a private firm in the US, is considering an investment in the cab industry. As part of their **Go-to-Market (G2M) strategy**, they seek data-driven insights to evaluate the **profitability, customer preferences, and operational efficiency** of two cab companies—**Yellow Cab and Pink Cab**—to determine the best investment opportunity.

## Objectives
This project aims to:
- Compare the **profitability** of Yellow Cab vs. Pink Cab.
- Analyze **customer preferences** and **loyalty trends**.
- Identify the **geographic distribution** of revenue and market dominance.
- Examine **price sensitivity** and its impact on demand.
- Provide an investment recommendation based on data insights.

## Dataset Information
The project utilizes the following datasets:

| **Dataset**      | **Description**                                   | **Format** | **Size**  |
|-----------------|---------------------------------------------------|-----------|----------|
| **Cab_Data**    | Contains details of transactions for both cab companies. | `.csv`     | 20.1 MB  |
| **Customer_ID** | Links customer demographics to transactions.     | `.csv`     | 1 MB     |
| **Transaction_ID** | Maps transactions to customers and payment methods. | `.csv`     | 8.58 MB  |
| **City**        | Lists US cities with population and cab users.    | `.csv`     | 759 Bytes |

## Exploratory Data Analysis (EDA)
The **EDA.ipynb** notebook explores key aspects of cab usage trends, customer behavior, and company performance:

### 1. **Demographic Influence**
- Yellow Cab outperforms Pink Cab in both total revenue and number of orders.
- Medium and high-income customers prefer **Pink Cab**.

### 2. **Geographic Analysis**
- Yellow Cab is more **profitable** in every city.
- Pink Cab has more orders only in **San Diego, Sacramento, and Nashville**.

### 3. **Customer Loyalty and Segmentation**
- Loyal customers are defined as the **top 10% most frequent riders**.
- **Yellow Cab** has more loyal customers than Pink Cab.
- Major hubs for loyal customers: **New York, Chicago, Los Angeles, and Washington, DC**.

### 4. **Price Sensitivity**
- Yellow Cab charges a higher **price per kilometer** than Pink Cab.
- The higher price suggests **Yellow Cab is a premium service**.

### 5. **Profitability Analysis**
- **Formula:**  
  \[
  \text{Profitability} = \frac{\text{Price Charged} - \text{Cost of Trip}}{\text{Cost of Trip}}
  \]
- **Yellow Cab** has a **higher profitability ratio** than Pink Cab.
- It converts a greater portion of revenue into profit.

## Key Findings & Investment Recommendation
| **Question**                                    | **Insight**                                      | **Preferred Cab** |
|------------------------------------------------|-------------------------------------------------|-----------------|
| Which company has higher profitability?       | **Yellow Cab** generates more profit.          | **Yellow Cab** |
| Do customers prefer Yellow Cab to Pink Cab?   | Customers prefer **Yellow Cab**, especially medium and high-income riders. | **Yellow Cab** |
| Which company has more loyal customers?       | **Yellow Cab** has a higher number of repeat customers. | **Yellow Cab** |
| Which company dominates in most cities?       | **Yellow Cab dominates all cities** except for a few. | **Yellow Cab** |
| Will Yellow Cab be more profitable in the future? | Yes. Given its **higher profitability, pricing power, and loyal customer base**, Yellow Cab is a better long-term investment. | **Yellow Cab** |

### **Final Recommendation: Invest in Yellow Cab.**

## Repository Structure
