df = pd.read_excel(filepath)

    # Date column
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date

    # datetime column
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce').dt.floor('S')

    # Cash_type column
    df['cash_type'] = df['cash_type'].astype('category').str.strip()
    
    df['cash_type'].unique()

    # Card colum 
    df['card'] = df['card'].astype(str).str.strip().replace('nan', 'no_card').fillna('no_card')

    # Money column
    df['money'] = pd.to_numeric(df['money'], errors='coerce')
     df['money'].describe()

    # Cofee_name column
    df['coffee_name'] = df['coffee_name'].astype('category').str.strip()
    df['coffee_name'] = df['coffee_name'].str.replace(r'[^a-zA-Z\s]', '', regex=True)

   
df.to_excel("coffee_sales.xlsx", index=False)

