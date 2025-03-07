import matplotlib.pyplot as plt
import seaborn as sns

# Function to create a data analytics dashboard
def create_dashboard(stats):
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle("Website Traffic Summary Statistics Dashboard", fontsize=16)

    # Metrics to visualize
    metrics = [
        ("Page Views", "page_views_mean", "page_views_median", "page_views_min", "page_views_max"),
        ("Site Sessions", "site_sessions_mean", "site_sessions_median", "site_sessions_min", "site_sessions_max"),
        ("Unique Visitors", "unique_visitors_mean", "unique_visitors_median", "unique_visitors_min", "unique_visitors_max"),
        ("Bounce Rate", "bounce_rate_mean", "bounce_rate_median", "bounce_rate_min", "bounce_rate_max"),
        ("Session Duration", "session_duration_mean", "session_duration_median", "session_duration_min", "session_duration_max"),
    ]

    # Colors for visualization
    colors = ["blue", "green", "red", "purple", "orange"]

    for ax, (title, mean_key, median_key, min_key, max_key), color in zip(axes.flat, metrics, colors):
        values = [stats[min_key], stats[median_key], stats[mean_key], stats[max_key]]
        labels = ["Min", "Median", "Mean", "Max"]
        
        sns.barplot(x=labels, y=values, ax=ax, palette=color)
        ax.set_title(title)
        ax.set_ylabel("Value")

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

# Create and display the dashboard
create_dashboard(traffic_statistics)
