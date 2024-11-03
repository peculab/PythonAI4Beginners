import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna() 
    return df

def top_items_bar_plot(df, output_file='001.jpg'):
    df1 = df.groupby("Item").sum().sort_values(by="Amount", ascending=False).head(10)
    df1 = df1.reset_index()
    sns.barplot(data=df1, x=df1.Item, y=df1.Amount)
    plt.xlabel("Item")
    plt.ylabel("Total Amount Spent")
    plt.savefig(output_file)  
    #plt.show() 

    highest_spending_item = df1.iloc[0]
    print(f"Item with the highest spending is {highest_spending_item['Item']}")
    print(f"Total amount spent is {highest_spending_item['Amount']}\n")

def analyze_and_weekday_pie_plot(df, output_file='002.jpg'):
    df2 = df.groupby("day").sum().sort_values(by="Amount",ascending=False)
    df2 = df2.reset_index()
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)  
    df['Weekday'] = df['Date'].dt.day_name() 

    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    df3 = df.groupby(['day', 'Weekday'])['Amount'].sum().reset_index()
    highest_per_weekday = df3.loc[df3.groupby('Weekday')['Amount'].idxmax()]

    plt.clf()
    plt.pie(data=df2, labels=df2.day, x="Amount",autopct='%.0f%%')
    plt.savefig(output_file)  
    #plt.show() 

    highest_per_weekday = df.loc[df.groupby('Weekday')['Amount'].idxmax()]

    for day in weekday_order:
        row = highest_per_weekday[highest_per_weekday['Weekday'] == day]
        if not row.empty:
            print(f"Highest spending day on {day} is {row['Date'].dt.date.values[0]}")
           
file_path = 'myExpenses1.csv' 
df = load_and_clean_data(file_path)
top_items_bar_plot(df)  
analyze_and_weekday_pie_plot(df)  