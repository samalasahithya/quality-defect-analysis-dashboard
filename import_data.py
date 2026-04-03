import pandas as pd
import psycopg2

df = pd.read_csv('C:/Users/samala sahithya/Desktop/Quality_defect.csv')

# Keep only these 9 exact columns
df = df[['defect_id', 'product_id', 'defect_type', 'defect_date', 
         'defect_location', 'severity', 'inspection_method', 
         'repair_cost', 'year_month']]

# Fix date format
df['defect_date'] = pd.to_datetime(df['defect_date'], dayfirst=True).dt.strftime('%Y-%m-%d')

df = df.where(pd.notnull(df), None)

conn = psycopg2.connect(
    host="localhost",
    database="quality_defect_analysis",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO quality_data 
        (defect_id, product_id, defect_type, defect_date, 
         defect_location, severity, inspection_method, 
         repair_cost, year_month)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()
cur.close()
conn.close()
print("Data imported successfully!")