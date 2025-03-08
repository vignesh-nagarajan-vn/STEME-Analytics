import pandas as pd
# Importing pandas to use the .agg() function instead of calling .mean(), .median(), .min(), and .max() separately
# Improves program resource utilization and effeciency

def extract_statistics(df):
    # Selecting relevant columns
    metrics = ["Page views", "Site sessions", "Unique visitors", "Bounce rate", "Avg. session duration"]
    
    # Compute summary statistics in one go
    stats_df = df[metrics].agg(["mean", "median", "min", "max"])
    
    # Convert DataFrame to dictionary for easy access
    stats = stats_df.to_dict()
    
    return stats

# Example usage
traffic_statistics = extract_statistics(df)

# Display the extracted statistics
traffic_statistics
