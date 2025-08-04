import matplotlib.pyplot as plt

def plot_total_units(units_dict):
    fig, ax = plt.subplots()
    ax.bar(units_dict.keys(), units_dict.values(), color=['#FF5733', '#33C3FF', '#6AFF33', '#FFC133'])
    ax.set_title("Total Units Sold per Product")
    ax.set_ylabel("Units")
    ax.set_xlabel("Products")
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    return fig

def plot_monthly_revenue(df):
    grouped = df.groupby(['Year', 'Month'])['Total_Revenue'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    for year in grouped['Year'].unique():
        monthly = grouped[grouped['Year'] == year]
        ax.plot(monthly['Month'], monthly['Total_Revenue'], marker='o', label=str(year))
    ax.set_title("Monthly Revenue Trend by Year")
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax.set_ylabel("Revenue")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.5)
    return fig

def plot_category_pie(revenue_dict):
    fig, ax = plt.subplots()
    ax.pie(
        revenue_dict.values(),
        labels=revenue_dict.keys(),
        autopct='%1.1f%%',
        startangle=90,
        colors=["#ff9999","#66b3ff","#99ff99","#ffcc99"]
    )
    ax.set_title("Revenue Contribution by Product")
    ax.axis('equal')
    return fig
