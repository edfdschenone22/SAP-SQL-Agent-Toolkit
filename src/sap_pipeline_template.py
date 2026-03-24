from base_pipeline import BasePipeline
import pandas as pd

class SapPipelineTemplate(BasePipeline):
    """
    Template for SAP to SQL pipelines.
    Inherit from this class and implement the extract, transform, and load methods.
    """

    def extract(self, hana_conn):
        """
        Extract data from SAP HANA.
        Replace the query below with the actual query for your task.
        """
        query = "SELECT * FROM YOUR_TABLE WHERE CONDITIONS"
        self.logger.info(f"Executing query: {query}")
        try:
            data = pd.read_sql(query, hana_conn)
            self.logger.info(f"Extracted {len(data)} rows.")
            return data
        except Exception as e:
            self.logger.error(f"Failed to extract data: {e}")
            raise

    def transform(self, data):
        """
        Transform the extracted data.
        Replace the transformation logic below with the actual logic for your task.
        """
        self.logger.info("Starting data transformation...")
        try:
            # Example transformation: Drop null values
            transformed_data = data.dropna()
            self.logger.info("Data transformation completed.")
            return transformed_data
        except Exception as e:
            self.logger.error(f"Failed to transform data: {e}")
            raise

    def load(self, sql_conn, data):
        """
        Load the transformed data into SQL Server.
        Replace the table name below with the actual table name for your task.
        """
        table_name = "YOUR_TARGET_TABLE"
        self.logger.info(f"Loading data into {table_name}...")
        try:
            data.to_sql(table_name, sql_conn, if_exists="replace", index=False)
            self.logger.info("Data loaded successfully.")
        except Exception as e:
            self.logger.error(f"Failed to load data: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    HANA_CONN_STR = "Your HANA connection string here"
    SQL_CONN_STR = "Your SQL Server connection string here"

    pipeline = SapPipelineTemplate(HANA_CONN_STR, SQL_CONN_STR)
    pipeline.run()