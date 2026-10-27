import pandas as pd

def clean_columns(df):
    """Columns have mulitple rows of names. We will flatten 'multi-index' columns and clean column names."""
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = ['_'.join(col).strip() for col in df.columns.values]
    return df



def vix_segments(df):
    """Categorize VIX close prices into Low, Normal, Elevated, High and X-treme volatility segments."""
    vix_col = [c for c in df.columns if 'VIX' in c and 'Close' in c][0]
    
    def get_segment(val):
        if val <= 15:
            return 'Low (0-15)'
        elif val <= 20:
            return 'Normal (15-20)'
        elif val <= 25:
            return 'Elevated(20-25)'
        elif val <= 30:
            return 'High (25-30)'
        else:
            return 'X-Treme! (30+)'
            
    df['VIX_Segments'] = df[vix_col].apply(get_segment)
    return df

def missing_values(df):
    """Missing values replaced or dropped by forward filling and/or dropping null values. 
    Using this since this is time series data."""
    return df.ffill()