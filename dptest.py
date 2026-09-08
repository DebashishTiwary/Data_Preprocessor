from IPython.display import display, HTML

def EDA(data):
    # 1. Perform your Exploratory Data Analysis logic here
    columns_count = len(data.columns)
    row_count = len(data)
    
    # 2. Design your document-style clickable HTML output
    html_content = f"""
    <div style="font-family: 'Arial', sans-serif; line-height: 1.6; max-width: 600px; padding: 15px; border: 1px solid #e0e0e0; border-radius: 5px; background-color: #f9f9f9;">
        <h3 style="color: #2c3e50; margin-top: 0;">📊 Exploratory Data Analysis Report</h3>
        <p style="margin: 5px 0;">Your dataset contains <strong>{columns_count} columns</strong> and <strong>{row_count} rows</strong>.</p>
        
        <hr style="border: 0; border-top: 1px solid #ccc; margin: 15px 0;">
        
        <!-- Clickable actions styled like a document index -->
        <p style="margin: 8px 0;">
            👉 <a href="#dataframe_preview" style="color: #1a73e8; text-decoration: none; font-weight: bold;">[View Dataframe Preview]</a>
        </p>
        <p style="margin: 8px 0;">
            👉 <a href="https://pydata.org" target="_blank" style="color: #1a73e8; text-decoration: none; font-weight: bold;">[Open External Pandas Documentation]</a>
        </p>
    </div>
    """
    
    # 3. Use display(HTML()) instead of a standard return or print statement
    display(HTML(html_content))
