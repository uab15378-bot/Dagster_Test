from dagster import asset
import snowflake.connector

@asset
def ctas_source_to_target():
    conn = snowflake.connector.connect(
        user="DBTEXPLORER",
        password="Copperbrigade.123@",
        account="FISEJZV-BY00378",
        warehouse="COMPUTE_WH",
        database="PRACTICEDB",
        schema="PRACTICE_SCHEMA"
    )

    cur = conn.cursor()
    cur.execute("""
        CREATE OR REPLACE TABLE TARGET_TABLE AS
        SELECT * FROM SOURCE_TABLE;
    """)
    conn.commit()
    cur.close()
    conn.close()
