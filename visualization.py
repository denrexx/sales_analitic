import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def price_distribution(df):
    plt.figure()
    sns.histplot(df["price"],bins=20,kde=True)
    plt.title("price distribution")
    plt.show()


def revenue_distribution(df):
    plt.figure()
    sns.histplot(df["revenue_after_discount"],bins=20,kde=True)
    plt.title("revenue distribution")
    plt.show()


def category_revenue_plot(cat_rev):
    plt.figure()
    sns.barplot(x="category",y="revenue_after_discount",data=cat_rev)
    plt.title("revenue by category")
    plt.show()


def platform_revenue_plot(platform_rev):
    plt.figure()
    sns.barplot(x="platform",y="revenue_after_discount",data=platform_rev)
    plt.title("revenue by platform")
    plt.show()


def weekday_revenue_plot(weekday_sales):
    plt.figure()
    sns.barplot(x="weekday",y="revenue_after_discount",data=weekday_sales)
    plt.title("revenue by weekday")
    plt.xticks(rotation=45)
    plt.show()


def price_boxplot(df):
    plt.figure()
    sns.boxplot(x=df["price"])
    plt.title("price boxplot")
    plt.show()


def price_quantity_scatter(df):
    plt.figure()
    sns.scatterplot(x="price",y="quantity",data=df)
    plt.title("price vs quantity")
    plt.show()


def correlation_heatmap(df):
    plt.figure()
    sns.heatmap(df[["price","quantity","revenue","revenue_after_discount"]].corr(),annot=True)
    plt.title("correlation heatmap")
    plt.show()


def interactive_category_plot(cat_rev):
    fig = px.bar(cat_rev,x="category",y="revenue_after_discount",title="revenue by category interactive")
    fig.show()


def visualize(df,cat_rev,platform_rev,weekday_sales):
    sns.set(style="whitegrid")
    price_distribution(df)
    revenue_distribution(df)
    category_revenue_plot(cat_rev)
    platform_revenue_plot(platform_rev)
    weekday_revenue_plot(weekday_sales)
    price_boxplot(df)
    price_quantity_scatter(df)
    correlation_heatmap(df)
    interactive_category_plot(cat_rev)