import pandas as pd
import numpy as np
from scipy import stats


def load_data(path):
    df = pd.read_csv(path)
    print(df.head())
    print(df.info())
    print(df.describe())
    return df


def clean_data(df):
    df.drop_duplicates(inplace=True)
    df["date"] = pd.to_datetime(df["date"])
    df["discount"] = df["discount"].fillna(0)
    df["quantity"] = df["quantity"].astype(int)
    return df


def audit_price(df):
    s = df["price"]
    print("count:",s.count())
    print("mean:",s.mean())
    print("median:",s.median())
    print("var:",s.var())
    print("std:",s.std())
    print("q50:",s.quantile(0.5))
    print("quartiles:")
    print(s.quantile([0.25,0.5,0.75]))


def add_features(df):
    df["revenue"] = df["price"] * df["quantity"]
    df["revenue_after_discount"] = df["revenue"] * (1 - df["discount"]/100)
    df["weekday"] = df["date"].dt.day_name()
    return df


def filters(df):
    print(df[df["price"] > 300])
    print(df[df["platform"] == "Mobile"])
    print(df[(df["price"] > 100) & (df["quantity"] >= 2)])
    print(df.loc[10:15])


def sorting(df):
    print(df.sort_values("revenue_after_discount",ascending=False))


def aggregation(df):
    cat_rev = df.groupby("category").agg({"revenue_after_discount":"sum","price":"mean","user_id":"count"}).reset_index()
    platform_rev = df.groupby("platform").agg({"revenue_after_discount":"sum","price":"median"}).reset_index()
    weekday_sales = df.groupby("weekday").agg({"revenue_after_discount":"sum"}).reset_index()
    print(cat_rev)
    print(platform_rev)
    print(weekday_sales)
    return cat_rev,platform_rev,weekday_sales


def user_analytics(df):
    users = df.groupby("user_id").agg({"revenue_after_discount":"sum","price":"median","quantity":"sum"}).reset_index()
    print(users.sort_values("revenue_after_discount",ascending=False))
    return users


def numpy_analysis(df):
    arr = np.array(df["revenue_after_discount"])
    max_i = np.argmax(arr)
    print(df.loc[max_i])
    print(arr[max_i])
    print(arr[arr > 200])
    return arr


def stats_tests(df,arr):
    t_stat,p_value = stats.ttest_1samp(arr,150)
    print(t_stat,p_value)

    mobile = np.array(df[df["platform"]=="Mobile"]["revenue_after_discount"])
    web = np.array(df[df["platform"]=="Web"]["revenue_after_discount"])

    stat,p_value = stats.mannwhitneyu(mobile,web)
    print(stat,p_value)


def run_analysis(df):
    audit_price(df)
    filters(df)
    sorting(df)
    cat_rev,platform_rev,weekday_sales = aggregation(df)
    users = user_analytics(df)
    arr = numpy_analysis(df)
    stats_tests(df,arr)
    return cat_rev,platform_rev,weekday_sales,users