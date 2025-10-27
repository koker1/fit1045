class BudgetTracker:
    def __init__(self):
        self.needs_percent = 0.50  # 50%
        self.wants_percent = 0.30  # 30%
        self.savings_percent = 0.20  # 20%
    
    def calculate_budget(self, total_income):
        """Calculate 50/30/20 budget breakdown"""
        return {
            'needs': total_income * self.needs_percent,
            'wants': total_income * self.wants_percent,
            'savings': total_income * self.savings_percent
        }
    
    def get_category_type(self, category):
        """Map category to budget type (needs/wants/savings)"""
        needs_categories = ['rent', 'groceries', 'utilities', 'transportation', 'insurance', 'healthcare']
        wants_categories = ['entertainment', 'dining', 'shopping', 'hobbies', 'vacation']
        savings_categories = ['savings', 'investment', 'emergency fund', 'debt payment']
        
        category_lower = category.lower()
        
        if category_lower in needs_categories:
            return 'needs'
        elif category_lower in wants_categories:
            return 'wants'
        elif category_lower in savings_categories:
            return 'savings'
        else:
            return 'other'
    
    def analyze_spending(self, expenses_by_category, total_income):
        """Analyze spending against 50/30/20 rule"""
        budget = self.calculate_budget(total_income)
        
        actual_spending = {
            'needs': 0,
            'wants': 0,
            'savings': 0,
            'other': 0
        }
        
        for category, amount in expenses_by_category.items():
            budget_type = self.get_category_type(category)
            actual_spending[budget_type] += amount
        
        analysis = {
            'budget': budget,
            'actual': actual_spending,
            'difference': {
                'needs': budget['needs'] - actual_spending['needs'],
                'wants': budget['wants'] - actual_spending['wants'],
                'savings': budget['savings'] - actual_spending['savings']
            }
        }
        
        return analysis
    
    def get_recommendations(self, analysis):
        """Provide budget recommendations"""
        recommendations = []
        
        for category, diff in analysis['difference'].items():
            if diff < 0:
                recommendations.append(
                    f"⚠️  You're overspending on {category.upper()} by ${abs(diff):.2f}"
                )
            else:
                recommendations.append(
                    f"✓ You have ${diff:.2f} remaining in your {category.upper()} budget"
                )
        
        return recommendations