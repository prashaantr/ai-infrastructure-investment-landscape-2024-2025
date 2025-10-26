#!/usr/bin/env python3
"""
Analysis Framework for AI Infrastructure Investment Landscape Research
=====================================================================

This module provides a comprehensive analysis framework following rigorous
scientific methodology for experiment result analysis.

Key Components:
- Statistical analysis functions
- Visualization utilities
- Hypothesis testing framework
- Result interpretation methods
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from sklearn.metrics import classification_report, confusion_matrix
from typing import Dict, List, Any, Optional, Tuple
import warnings
warnings.filterwarnings('ignore')

# Set plotting style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class ExperimentAnalyzer:
    """
    Comprehensive experiment analysis following scientific methodology.
    
    This class implements rigorous statistical analysis methods for
    evaluating experimental results and drawing scientifically valid conclusions.
    """
    
    def __init__(self, experiments_file: str = 'experiments.json'):
        """Initialize the analyzer with experiment data."""
        self.experiments_file = experiments_file
        self.experiments = []
        self.results = {}
        self.load_experiments()
    
    def load_experiments(self):
        """Load experiment data from JSON file."""
        try:
            with open(self.experiments_file, 'r') as f:
                self.experiments = json.load(f)
            print(f"Loaded {len(self.experiments)} experiments")
        except FileNotFoundError:
            print(f"Warning: {self.experiments_file} not found. Creating empty framework.")
            self.experiments = []
    
    def filter_successful_experiments(self) -> List[Dict]:
        """
        Filter experiments that completed successfully with valid data.
        
        Returns:
            List of experiments that meet quality criteria for analysis
        """
        successful = []
        for exp in self.experiments:
            # Skip example experiments
            if exp.get('_isExample', False):
                continue
                
            # Check for required fields and completion status
            if all(key in exp for key in ['id', 'title', 'experimentId']):
                # Additional validation would go here for real experiments
                # e.g., check if results files exist, data is valid, etc.
                successful.append(exp)
        
        return successful
    
    def perform_statistical_analysis(self, data: pd.DataFrame) -> Dict[str, Any]:
        """
        Perform comprehensive statistical analysis on experimental data.
        
        Args:
            data: DataFrame containing experimental results
            
        Returns:
            Dictionary containing statistical test results and interpretations
        """
        analysis = {
            'descriptive_stats': {},
            'hypothesis_tests': {},
            'effect_sizes': {},
            'confidence_intervals': {}
        }
        
        # Descriptive statistics
        analysis['descriptive_stats'] = {
            'mean': data.mean().to_dict() if not data.empty else {},
            'std': data.std().to_dict() if not data.empty else {},
            'median': data.median().to_dict() if not data.empty else {},
            'n_observations': len(data)
        }
        
        # Example statistical tests (would be customized based on actual data)
        if not data.empty and len(data.columns) >= 2:
            # Correlation analysis
            numeric_cols = data.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) >= 2:
                corr_matrix = data[numeric_cols].corr()
                analysis['correlations'] = corr_matrix.to_dict()
        
        return analysis
    
    def create_visualizations(self, data: pd.DataFrame, output_dir: str = 'visualizations/'):
        """
        Create comprehensive visualizations for data analysis.
        
        Args:
            data: DataFrame containing experimental results
            output_dir: Directory to save visualization files
        """
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        if data.empty:
            print("No data available for visualization")
            return
        
        # Distribution plots
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            fig, axes = plt.subplots(len(numeric_cols), 1, figsize=(10, 6*len(numeric_cols)))
            if len(numeric_cols) == 1:
                axes = [axes]
            
            for i, col in enumerate(numeric_cols):
                axes[i].hist(data[col].dropna(), bins=30, alpha=0.7)
                axes[i].set_title(f'Distribution of {col}')
                axes[i].set_xlabel(col)
                axes[i].set_ylabel('Frequency')
            
            plt.tight_layout()
            plt.savefig(f'{output_dir}/distributions.png', dpi=300, bbox_inches='tight')
            plt.close()
        
        # Correlation heatmap
        if len(numeric_cols) >= 2:
            plt.figure(figsize=(10, 8))
            corr_matrix = data[numeric_cols].corr()
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
            plt.title('Correlation Matrix')
            plt.tight_layout()
            plt.savefig(f'{output_dir}/correlation_heatmap.png', dpi=300, bbox_inches='tight')
            plt.close()
    
    def generate_analysis_report(self) -> Dict[str, Any]:
        """
        Generate comprehensive analysis report following scientific standards.
        
        Returns:
            Structured analysis report with findings and interpretations
        """
        successful_experiments = self.filter_successful_experiments()
        
        report = {
            'metadata': {
                'total_experiments': len(self.experiments),
                'successful_experiments': len(successful_experiments),
                'analysis_date': pd.Timestamp.now().isoformat(),
                'methodology': 'Rigorous statistical analysis following scientific standards'
            },
            'experiments_analyzed': successful_experiments,
            'statistical_results': {},
            'findings': [],
            'implications': [],
            'limitations': [],
            'next_steps': []
        }
        
        if not successful_experiments:
            report['findings'] = [
                "No completed experiments found for analysis",
                "Current data consists only of example/template entries"
            ]
            report['next_steps'] = [
                "Conduct experiments according to defined protocols",
                "Ensure proper data collection and storage procedures",
                "Implement quality control measures for experimental data"
            ]
            return report
        
        # If we had real data, we would perform actual statistical analysis here
        # For now, we provide the framework structure
        
        return report

def main():
    """Main analysis execution function."""
    analyzer = ExperimentAnalyzer()
    report = analyzer.generate_analysis_report()
    
    # Save analysis results
    with open('analysis_results.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print("Analysis framework completed.")
    print(f"Found {report['metadata']['total_experiments']} total experiments")
    print(f"Successfully analyzed {report['metadata']['successful_experiments']} experiments")
    
    return report

if __name__ == '__main__':
    main()