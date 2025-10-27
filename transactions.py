import pandas as pd
import os
from datetime import datetime

class TransactionManager:
    def __init__(self, csv_file='user_transactions.csv'):
        self.csv_file = csv_file
        self.columns = ['date', 'username', 'type', 'category', 'amount', 'description']
        
        if not os.path.exists(self.csv_file):
            df = pd.DataFrame(columns=self.columns)
            df.to_csv(self.csv_file, index=False)
    
    def add_transaction(self, username, trans_type, category, amount, description=''):
        """Add a new transaction (expense or income)"""
        try:
            df = pd.read_csv(self.csv_file)
            new_transaction = {
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'username': username,
                'type': trans_type,
                'category': category,
                'amount': float(amount),
                'description': description
            }
            df = pd.concat([df, pd.DataFrame([new_transaction])], ignore_index=True)
            df.to_csv(self.csv_file, index=False)
            return True, "Transaction added successfully"
        except Exception as e:
            return False, f"Error adding transaction: {str(e)}"
    
    def get_transactions(self, username, trans_type=None):
        """Get all transactions for a user"""
        try:
            df = pd.read_csv(self.csv_file)
            user_transactions = df[df['username'] == username]
            
            if trans_type:
                user_transactions = user_transactions[user_transactions['type'] == trans_type]
            
            return user_transactions
        except Exception as e:
            return pd.DataFrame()
    
    def edit_transaction(self, username, index, category=None, amount=None, description=None):
        """Edit an existing transaction"""
        try:
            df = pd.read_csv(self.csv_file)
            user_transactions = df[df['username'] == username]
            
            if index >= len(user_transactions):
                return False, "Invalid transaction index"
            
            actual_index = user_transactions.index[index]
            
            if category:
                df.at[actual_index, 'category'] = category
            if amount:
                df.at[actual_index, 'amount'] = float(amount)
            if description is not None:
                df.at[actual_index, 'description'] = description
            
            df.to_csv(self.csv_file, index=False)
            return True, "Transaction updated successfully"
        except Exception as e:
            return False, f"Error editing transaction: {str(e)}"
    
    def remove_transaction(self, username, index):
        """Remove a transaction"""
        try:
            df = pd.read_csv(self.csv_file)
            user_transactions = df[df['username'] == username]
            
            if index >= len(user_transactions):
                return False, "Invalid transaction index"
            
            actual_index = user_transactions.index[index]
            df = df.drop(actual_index)
            df.to_csv(self.csv_file, index=False)
            return True, "Transaction removed successfully"
        except Exception as e:
            return False, f"Error removing transaction: {str(e)}"
    
    def get_total_income(self, username):
        """Calculate total income"""
        df = self.get_transactions(username, 'income')
        return df['amount'].sum() if not df.empty else 0
    
    def get_total_expenses(self, username):
        """Calculate total expenses"""
        df = self.get_transactions(username, 'expense')
        return df['amount'].sum() if not df.empty else 0
    
    def get_expenses_by_category(self, username):
        """Get expenses grouped by category"""
        df = self.get_transactions(username, 'expense')
        if df.empty:
            return {}
        return df.groupby('category')['amount'].sum().to_dict()