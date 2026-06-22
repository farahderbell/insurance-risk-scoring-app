# 🏦 Maghrebia Insurance Scoring System

## Overview

This project is a decision-support system designed for **insurance risk assessment**.  
It focuses on evaluating the **solvency and payment reliability** of new insurance clients.

The goal is to help insurers estimate whether a new client is likely to:
- Pay premiums regularly
- Default on payments
- Represent low or high financial risk

---

## 🎯 Objective

In insurance, not all clients have the same financial reliability.

This system aims to:
- Predict the **risk level of a new insured client**
- Estimate their **solvency (ability to pay over time)**
- Support underwriters in decision-making
- Reduce financial loss due to non-payment

---

## 📊 What is “Scoring”?

The scoring system assigns a **risk score** to each client based on available data.

The score represents:

- 🟢 **Low risk (good payer)** → financially stable client
- 🟡 **Medium risk** → uncertain payment behavior
- 🔴 **High risk (bad payer)** → high probability of default

---

## 🧠 What is Solvency?

**Solvency** refers to a client's ability to meet financial obligations over time.

In insurance terms, a solvent client is someone who:
- Has stable income
- Has low debt ratio
- Has consistent payment behavior
- Is unlikely to miss premium payments

---

## 📌 How the System Thinks (Conceptually)

The scoring model evaluates risk using factors such as:

- Income stability
- Employment type
- Age group
- Financial history (if available)
- Past insurance behavior
- Debt / obligations ratio

These inputs are combined to produce a **final risk score**.

---

## 📈 Output of the System

For each new client, the system provides:

- Risk category (Low / Medium / High)
- Numerical score (probability-based or weighted index)
- Recommendation (Accept / Review / Reject)

---

## 🧩 Use in Insurance Workflow

This system helps:

- Underwriters → faster decision-making
- Actuaries → better risk segmentation
- Company → reduce claim and default risk

---

## 🚀 Future Improvements

- Machine Learning model for predictive scoring
- Integration with real insurance databases
- Automated risk dashboards
- Historical claim behavior analysis
- Explainable AI (why a client is high risk)

---

## 🏢 Context

This project is designed in the context of **Assurance Maghrebia** internal risk evaluation processes, focusing on improving underwriting decisions for new insured clients.

---
