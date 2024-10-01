from src.train_model import train_model
import matplotlib.pyplot as plt
import os
import pandas as pd

def visualize_results(y_test, y_pred):
    print("Saving Actual vs Predicted visualization...")
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # 45-degree line
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Actual vs Predicted Values for Python Popularity')
    plt.xlim(y_test.min() - 10, y_test.max() + 10)
    plt.ylim(y_test.min() - 10, y_test.max() + 10)
    plt.grid()

    # Create the visuals folder if it doesn't exist
    visuals_folder = 'visuals'
    os.makedirs(visuals_folder, exist_ok=True)

    # Save the plot as a PNG file
    plt.savefig(os.path.join(visuals_folder, 'actual_vs_predicted.png'))
    plt.close()
    print("Visualization saved.")

def visualize_trends(df):
    print("Saving trends visualization...")
    plt.figure(figsize=(10, 6))
    for column in df.columns[1:]:  # Skip 'Month'
        plt.plot(df['Month'], df[column], label=column)
    plt.xlabel('Year')
    plt.ylabel('Popularity (%)')
    plt.title('Programming Language Popularity Over Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()

    plt.savefig(os.path.join('visuals', 'trends.png'))
    plt.close()
    print("Trends visualization saved.")

def visualize_histogram(df):
    print("Saving histogram visualization...")
    plt.figure(figsize=(10, 6))
    for column in df.columns[1:]:  # Skip 'Month'
        plt.hist(df[column], alpha=0.5, bins=20, label=column)
    plt.xlabel('Popularity (%)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Programming Language Popularity')
    plt.legend()
    plt.grid()

    plt.savefig(os.path.join('visuals', 'histogram.png'))
    plt.close()
    print("Histogram visualization saved.")

def visualize_individual_language_trends(df):
    print("Saving individual language trends visualizations...")
    for column in df.columns[1:]:  # Skip 'Month'
        plt.figure(figsize=(10, 6))
        plt.plot(df['Month'], df[column], label=column)
        plt.xlabel('Year')
        plt.ylabel('Popularity (%)')
        plt.title(f'{column} Popularity Over Time')
        plt.xticks(rotation=45)
        plt.grid()
        plt.savefig(os.path.join('visuals', f'{column}_trend.png'))
        plt.close()
        print(f"Saved visualization for {column}.")

if __name__ == "__main__":
    df, y_test, y_pred = train_model()  # Get DataFrame, actual and predicted values
    visualize_results(y_test, y_pred)  # Call visualization function
    visualize_trends(df)  # Visualize overall trends
    visualize_histogram(df)  # Visualize histogram of popularity
    visualize_individual_language_trends(df)  # Visualize individual language trends






