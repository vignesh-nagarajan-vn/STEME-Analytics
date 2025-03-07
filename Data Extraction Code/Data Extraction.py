# Function to extract summary statistics as variables
def extract_statistics(df):
    stats = {}
    
    # Extracting mean, median, min, max for key metrics
    stats["page_views_mean"] = df["Page views"].mean()
    stats["page_views_median"] = df["Page views"].median()
    stats["page_views_min"] = df["Page views"].min()
    stats["page_views_max"] = df["Page views"].max()
    
    stats["site_sessions_mean"] = df["Site sessions"].mean()
    stats["site_sessions_median"] = df["Site sessions"].median()
    stats["site_sessions_min"] = df["Site sessions"].min()
    stats["site_sessions_max"] = df["Site sessions"].max()

    stats["unique_visitors_mean"] = df["Unique visitors"].mean()
    stats["unique_visitors_median"] = df["Unique visitors"].median()
    stats["unique_visitors_min"] = df["Unique visitors"].min()
    stats["unique_visitors_max"] = df["Unique visitors"].max()

    stats["bounce_rate_mean"] = df["Bounce rate"].mean()
    stats["bounce_rate_median"] = df["Bounce rate"].median()
    stats["bounce_rate_min"] = df["Bounce rate"].min()
    stats["bounce_rate_max"] = df["Bounce rate"].max()

    stats["session_duration_mean"] = df["Avg. session duration"].mean()
    stats["session_duration_median"] = df["Avg. session duration"].median()
    stats["session_duration_min"] = df["Avg. session duration"].min()
    stats["session_duration_max"] = df["Avg. session duration"].max()

    return stats

# Store statistics in variables
traffic_statistics = extract_statistics(df)

# Display the extracted statistics
traffic_statistics
