# CodeAlpha_DataVisualization

## Task
Transform raw sales data into clear charts, graphs, and a combined dashboard using Python (Matplotlib and Seaborn), and use them to tell a data-driven story.

## Objective
To convert raw, row-level sales data into visual formats that reveal trends and patterns clearly, and to build a small "portfolio-style" dashboard that supports business decision-making.

## Tools & Libraries Used
- Python 3
- `pandas` – data loading and aggregation (group by category/region/month)
- `matplotlib` – base plotting engine, used for the combined dashboard
- `seaborn` – styled statistical charts (bar chart, heatmap, scatter plot)

## Dataset Used
`sales_data.csv` — a sample sales dataset (480 rows) covering:
- 24 months (Jan 2024 – Dec 2025)
- 5 product categories: Electronics, Clothing, Groceries, Furniture, Toys
- 4 regions: North, South, East, West
- Columns: `Month`, `Category`, `Region`, `Sales`, `Profit`

This is a realistic, synthetic dataset built to include a genuine seasonal pattern and a slow upward growth trend, so the charts show meaningful, explainable insights rather than random noise. It is included directly in this repo — no download needed.

## Folder Structure
```
CodeAlpha_DataVisualization/
│
├── visualize_sales.py               # Main visualization script
├── sales_data.csv                    # Sample sales dataset
├── README.md                         # Project description
└── requirements.txt                  # Required libraries
```

## How to Run
1. Clone this repository:
   ```
   git clone https://github.com/ramprasadshinde9834-star/CodeAlpha_DataVisualization.git
   cd CodeAlpha_DataVisualization
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the script:
   ```
   python visualize_sales.py
   ```
4. Output: 5 individual chart images + 1 combined dashboard image (all `.png`), plus key insights printed in the terminal.

## Charts Generated
| File | Chart Type | What it shows |
|---|---|---|
| chart1_monthly_sales_trend.png | Line chart | Overall sales trend and seasonality over 24 months |
| chart2_sales_by_category.png | Bar chart | Total sales ranked by product category |
| chart3_sales_share_by_region.png | Pie chart | Percentage share of sales contributed by each region |
| chart4_profit_vs_sales.png | Scatter plot | Relationship between sales and profit, split by category |
| chart5_category_region_heatmap.png | Heatmap | Sales performance across every category-region combination |
| dashboard_sales_overview.png | Combined dashboard | All key charts in one single report-ready image |

## Sample Output (Console)
```
Dataset loaded successfully.
Shape: (480, 5)

--- KEY INSIGHTS ---
Best-selling category: Electronics
Top-performing region: North
Sales growth from first to last month: 7.5%

Visualization completed! 5 charts + 1 dashboard image saved in this folder.
```

## Data Story / Key Insights
- Sales show a clear **seasonal pattern** — dipping mid-year and peaking around January-February each year.
- **Electronics** is the top-performing category by a wide margin, followed by Groceries.
- **North region** contributes the largest share of total sales (~29%), while South contributes the least (~21%).
- Profit does **not scale perfectly with sales** — some lower-sales categories have a higher profit margin, visible clearly in the scatter plot.
- The heatmap shows **Electronics + North** as the single best-performing category-region combination — a useful pointer for where to focus marketing budget.

## Real-World Applications
- Business dashboards for tracking monthly revenue and category performance
- Marketing teams identifying which region/category to focus campaigns on
- Retail inventory planning based on seasonal demand patterns
- Executive reporting — a single dashboard image summarizing performance for leadership

## Internship
This project was completed as part of the **CodeAlpha Internship Program**.
