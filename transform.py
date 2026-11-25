import duckdb

split = duckdb.sql("""SELECT
    DISTINCT
        session_id,
        session_date,
        customer_id,
        store_id,
        device_type,
        browser_os,
        SPLIT_PART(browser_os, ' ', 1) AS browser,
        SPLIT_PART(browser_os, ' ', 2) AS os,
        session_purchase_made,
        session_duration_minutes,
        session_pages_visited,
        COALESCE(session_quality_score, avg(session_quality_score) over() ) as cleaned_seassion_quality_score
        FROM 'output.parquet'
""")
print(split)  


duckdb.sql("""
COPY (
    SELECT
        DISTINCT
            session_id,
            session_date,
            customer_id,
            store_id,
            device_type,
            browser_os,
            SPLIT_PART(browser_os, '|', 1) AS browser,
            SPLIT_PART(browser_os, '|', 2) AS os,
            session_purchase_made,
            session_duration_minutes,
            session_pages_visited,
            COALESCE(session_quality_score, avg(session_quality_score) over() ) as cleaned_sq_score
    FROM 'output.parquet'
)
TO 'transformed_output.parquet'
(FORMAT PARQUET);
""")