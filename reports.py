import pandas as pd
import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

@st.cache_data
def load_data():
    return pd.read_csv("Telco-Customer-Churn.csv")


def create_report_pdf(
    total_customers,
    churned_customers,
    retained_customers,
    churn_rate
):

    file_name = "Churn_Analysis_Report.pdf"

    doc = SimpleDocTemplate(
        file_name,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    normal_style = styles["BodyText"]

    story = []

    story.append(
        Paragraph(
            "Telecom Customer Churn Analysis Report",
            title_style
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Executive Summary",
            heading_style
        )
    )

    story.append(Spacer(1, 10))

    kpi_data = [
        ["Metric", "Value"],
        ["Total Customers", f"{total_customers:,}"],
        ["Churned Customers", f"{churned_customers:,}"],
        ["Retained Customers", f"{retained_customers:,}"],
        ["Churn Rate", f"{churn_rate:.2f}%"]
    ]

    kpi_table = Table(
        kpi_data,
        colWidths=[250, 150]
    )

    kpi_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("ALIGN", (1, 1), (1, -1), "CENTER"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 8)
        ])
    )

    story.append(kpi_table)
    story.append(Spacer(1, 25))

    story.append(
        Paragraph(
            "Key Findings",
            heading_style
        )
    )

    story.append(Spacer(1, 10))

    findings = [
        "Month-to-month customers have the highest churn rate at 42.71%, "
    "compared with 11.27% for one-year contracts and 2.83% for two-year contracts.",

    "Customers with 0-12 months of tenure have the highest churn rate "
    "at 47.68%. Churn decreases as customer tenure increases.",

    "Customers paying 61-90 per month have the highest churn rate "
    "at 33.91%, followed by customers paying 91-120 per month at 32.78%.",

    "Month-to-month customers using Fiber Optic internet have the "
    "highest observed churn rate at 54.60%."
  ]
    

    for finding in findings:

        story.append(
            Paragraph(
                f"• {finding}",
                normal_style
            )
        )

        story.append(Spacer(1, 6))

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "Business Recommendations",
            heading_style
        )
    )

    story.append(Spacer(1, 10))

    story.append(Spacer(1, 15))

    story.append(
    Paragraph(
        "High-Risk Customer Segments",
        heading_style
    )
)

    story.append(Spacer(1, 10))

    risk_data = [
    ["Customer Segment", "Churn Rate"],
    ["Month-to-month contract", "42.71%"],
    ["0-12 months tenure", "47.68%"],
    ["Monthly charges 61-90", "33.91%"],
    ["Month-to-month + Fiber Optic", "54.60%"],
]

    risk_table = Table(
    risk_data,
    colWidths=[280, 120]
)

    risk_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ALIGN", (1, 1), (1, -1), "CENTER"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
    ])
)

    story.append(risk_table)

    story.append(Spacer(1, 10))

    story.append(
    Paragraph(
        "These customer segments should receive priority in "
        "customer retention campaigns because they show relatively "
        "high churn rates.",
        normal_style
    )
)

    recommendations = [
        "Encourage month-to-month customers to choose long-term contracts.",
        "Create retention offers for new customers.",
        "Target high-risk Fiber Optic customers with special offers.",
        "Provide loyalty benefits to long-term customers."
    ]

    for recommendation in recommendations:

        story.append(
            Paragraph(
                f"• {recommendation}",
                normal_style
            )
        )

        story.append(Spacer(1, 6))


    story.append(Spacer(1, 15))

    story.append(
    Paragraph(
        "Machine Learning Model Performance",
        heading_style
    )
)

    story.append(Spacer(1, 10))

    model_data = [
    ["Metric", "Score"],
    ["Accuracy", "83.81%"],
    ["Precision", "78.79%"],
    ["Recall", "93.58%"],
    ["F1 Score", "85.55%"],
]

    model_table = Table(
     model_data,
     colWidths=[250, 150]
)

    model_table.setStyle(
      TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ALIGN", (1, 1), (1, -1), "CENTER"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
    ])
)

    story.append(model_table)

    story.append(Spacer(1, 10))

    story.append(
    Paragraph(
        "The churn prediction model uses an XGBoost classifier. "
        "The model achieved an accuracy of 83.81% and a recall of "
        "93.58%, indicating strong performance in identifying "
        "customers who are likely to churn.",
        normal_style
    )
)

    # Conclusion

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Conclusion",
            heading_style
        )
    )

    story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            "The analysis shows that customer churn is strongly associated "
            "with contract type, customer tenure, monthly charges, and "
            "internet service.",
            normal_style
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            "Month-to-month customers have a significantly higher churn "
            "rate compared with customers on long-term contracts. "
            "Customers in their first 12 months are also more likely to "
            "leave, indicating that early customer experience and onboarding "
            "are important for retention.",
            normal_style
        )
    )
    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            "The analysis identifies month-to-month Fiber Optic customers "
            "as the highest-risk segment, with a churn rate of 54.60%. "
            "In contrast, customers with 61-72 months of tenure have a "
            "much lower churn rate of 6.61%.",
            normal_style
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            "Based on these findings, the company should focus on early-stage "
            "customer retention, long-term contract incentives, targeted "
            "offers for high-risk Fiber Optic customers, and loyalty "
            "programs for existing customers.",
            normal_style
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            "Overall, the analysis can help the telecom company identify "
            "high-risk customer segments and develop data-driven strategies "
            "to reduce churn and improve customer retention.",
                  normal_style
        )
    )


    # Build PDF AFTER adding all content

    doc.build(story)

    return file_name


def report_summary():

    dataset = load_data()

    st.title("📑 Churn Analysis Report")

    st.subheader("📊 Executive Summary")

    total_customers = len(dataset)
    churned_customers = (dataset["Churn"] == "Yes").sum()
    retained_customers = (dataset["Churn"] == "No").sum()

    churn_rate = (churned_customers / total_customers)*100

    col1,col2= st.columns(2)

    with col1:
        st.metric("👥 Total Customers", total_customers)

    with col2:
        st.metric("❌ Churned Customer",churned_customers)

    col3,col4 = st.columns(2)

    with col3:
        st.metric("✅ Retained Customers",retained_customers)

    with col4:
        st.metric("📈 Churn Rate",f"{churn_rate:.2f}%")

    st.subheader("📌 Overall Insight")

    st.write(
     f"""
    The telecom dataset contains **{total_customers:,} customers**.
    Out of these, **{churned_customers:,} customers have churned**, while
    **{retained_customers:,} customers have remained with the company**.

    The overall customer churn rate is **{churn_rate:.2f}%**.
    This indicates that approximately **1 out of every 4 customers**
    has left the company.
    """
   )

    st.subheader("🔍 Key Findings")

    contract = pd.DataFrame(
        {
            "Contract": ["Month-to-month", "One year", "Two year"],
            "Churn Rate": [42.71, 11.27, 2.83]

        }
    )
    contract.columns = ["Contract","Churn Rate"]

    tenure = pd.DataFrame(
            {
            "Tenure": [
             "0-12 months",
             "13-24 months",
             "25-36 months",
             "37-48 months",
             "49-60 months",
             "61-72 months"
         ],
         "Churn Rate": [
             47.68,
             28.71,
             21.63,
             19.03,
             14.42,
             6.61
         ]
            }
        )
    tenure.columns = ["Tenure","Churn Rate"]

    monthly_charges = pd.DataFrame(
        {
            "Monthly Charges": [
            "0-30",
            "31-60",
            "61-90",
            "91-120"
    ],
          "Churn Rate": [
           9.80,
           25.93,
           33.91,
           32.78
    ]
    
            }
        )

    contract_internet = pd.DataFrame(
            {
        "Contract + Internet": [
           "Month-to-month-DSL",
           "Month-to-month-Fiber Optic",
           "Month-to-month-No",
           "One-Year-DSL",
           "One-Year-Fiber Optic",
           "One-Year-No",
           "Two-Year-DSL",
           "Two-Year-Fiber Optic",
           "Two-Year-No"
    ],
        "Churn Rate": [
           32.21,
           54.60,
           18.89,
           9.28,
           19.29,
           2.47,
           1.91,
           7.22,
           0.78
      ]
    
     }
    )

    st.dataframe(contract)
    st.dataframe(tenure)
    st.dataframe(monthly_charges)
    st.dataframe(contract_internet)

    st.markdown("""
    ### 🔴 Contract Type

    Month-to-month customers have the highest churn rate at **42.71%**,
    compared with **11.27%** for one-year contracts and only **2.83%**
    for two-year contracts.

    ### 🔴 Customer Tenure

    Customers with **0-12 months of tenure** have the highest churn rate
    of **47.68%**. Churn decreases significantly as customer tenure increases.

    ### 🟠 Monthly Charges

    Customers paying **61-90** per month have the highest churn rate
    at **33.91%**, followed by customers paying **91-120** at **32.78%**.

    ### 🔴 Contract + Internet Service

    The highest churn rate is among customers with **month-to-month
    contracts and Fiber Optic internet**, with a churn rate of **54.60%**.

    ### 🟢 Long-Term Customers

    Customers with **61-72 months of tenure** have a much lower churn rate
    of only **6.61%**, indicating that long-term customers are more likely
    to remain with the company.
    """)

    st.subheader("💡 Business Recommendations")

    st.markdown("""
    ### 1. 📄 Encourage Long-Term Contracts
    Offer discounts or additional benefits to month-to-month customers
    to encourage them to switch to one-year or two-year contracts.

    ### 2. 👋 Focus on New Customers
    Customers in their first 12 months have the highest churn rate.
    Create onboarding and retention programs for new customers.

    ### 3. 🌐 Target Fiber Optic Customers
    Month-to-month Fiber Optic customers have the highest churn rate.
    Offer targeted plans and incentives to this customer segment.

    ### 4. 💰 Review High Monthly Charges
    Customers with higher monthly charges show higher churn.
    Consider personalized plans, discounts, or additional value.

    ### 5. 🏆 Reward Loyal Customers
    Long-term customers have much lower churn.
    Introduce loyalty rewards to encourage them to stay.
    """)

    st.subheader("🎯 Conclusion")

    st.markdown("""
    The analysis shows that customer churn is strongly associated with 
    **contract type, customer tenure, monthly charges, and internet service**.

    **Month-to-month customers** have a significantly higher churn rate 
    compared with customers on long-term contracts. Customers in their 
    **first 12 months** are also more likely to leave, indicating that 
    early customer experience and onboarding are important for retention.

    The analysis also identifies **month-to-month Fiber Optic customers** 
    as the highest-risk segment, with a churn rate of **54.60%**. In 
    contrast, customers with **61-72 months of tenure** have a much lower 
    churn rate of **6.61%**, showing the importance of long-term customer 
    relationships.

    Based on these findings, the company should focus on **early-stage 
    customer retention, long-term contract incentives, targeted offers 
    for high-risk Fiber Optic customers, and loyalty programs for existing 
    customers**.

    Overall, the analysis can help the telecom company identify high-risk 
    customer segments and develop **data-driven strategies to reduce 
    churn and improve customer retention**.
    """)

        # Generate PDF Report
    report_file = create_report_pdf(
        total_customers,
        churned_customers,
        retained_customers,
        churn_rate
    )

    # Download Button
    with open(report_file, "rb") as file:
        st.download_button(
            label="📥 Download Churn Analysis Report",
            data=file,
            file_name="Churn_Analysis_Report.pdf",
            mime="application/pdf"
        )