import matplotlib.pyplot as plt
import pandas as pd

class Visualizer:
    @staticmethod
    def plot_expenses_pie_chart(expenses_by_category, username):
        """Create a pie chart of expenses by category"""
        if not expenses_by_category:
            print("No expenses to display")
            return
        
        categories = list(expenses_by_category.keys())
        amounts = list(expenses_by_category.values())
        
        plt.figure(figsize=(10, 7))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title(f'Expense Distribution for {username}')
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig(f'expenses_{username}.png')
        plt.show()
    
    @staticmethod
    def plot_budget_comparison(analysis):
        """Create a comparison chart for 50/30/20 budget"""
        categories = ['Needs (50%)', 'Wants (30%)', 'Savings (20%)']
        budget_values = [
            analysis['budget']['needs'],
            analysis['budget']['wants'],
            analysis['budget']['savings']
        ]
        actual_values = [
            analysis['actual']['needs'],
            analysis['actual']['wants'],
            analysis['actual']['savings']
        ]
        
        x = range(len(categories))
        width = 0.35
        
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.bar([i - width/2 for i in x], budget_values, width, label='Budget', color='skyblue')
        ax.bar([i + width/2 for i in x], actual_values, width, label='Actual', color='salmon')
        
        ax.set_xlabel('Categories')
        ax.set_ylabel('Amount ($)')
        ax.set_title('Budget vs Actual Spending (50/30/20 Rule)')
        ax.set_xticks(x)
        ax.set_xticklabels(categories)
        ax.legend()
        
        plt.tight_layout()
        plt.savefig('budget_comparison.png')
        plt.show()