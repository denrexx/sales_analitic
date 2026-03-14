from analysis import load_data, clean_data, add_features, run_analysis
from visualization import visualize


def main():
    df = load_data("db.csv")
    df = clean_data(df)
    df = add_features(df)

    cat_rev,platform_rev,weekday_sales,users = run_analysis(df)

    visualize(df,cat_rev,platform_rev,weekday_sales)

    cat_rev.to_csv("category_report.csv",index=False)
    platform_rev.to_csv("platform_report.csv",index=False)
    users.to_csv("top_users.csv",index=False)


if __name__ == "__main__":
    main()