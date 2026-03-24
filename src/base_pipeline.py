import pyodbc
import logging
from abc import ABC, abstractmethod

class BasePipeline(ABC):
    """
    Abstract Base Class for SAP to SQL pipelines.
    Handles connections, logging, and batch processing.
    """

    def __init__(self, hana_conn_str, sql_conn_str):
        self.hana_conn_str = hana_conn_str
        self.sql_conn_str = sql_conn_str
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(f"{self.__class__.__name__}.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def connect_hana(self):
        try:
            self.logger.info("Connecting to SAP HANA...")
            conn = pyodbc.connect(self.hana_conn_str)
            self.logger.info("Connected to SAP HANA.")
            return conn
        except Exception as e:
            self.logger.error(f"Failed to connect to SAP HANA: {e}")
            raise

    def connect_sql(self):
        try:
            self.logger.info("Connecting to SQL Server...")
            conn = pyodbc.connect(self.sql_conn_str)
            self.logger.info("Connected to SQL Server.")
            return conn
        except Exception as e:
            self.logger.error(f"Failed to connect to SQL Server: {e}")
            raise

    @abstractmethod
    def extract(self, hana_conn):
        """
        Extract data from SAP HANA.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def transform(self, data):
        """
        Transform the extracted data.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def load(self, sql_conn, data):
        """
        Load the transformed data into SQL Server.
        Must be implemented by subclasses.
        """
        pass

    def run(self):
        """
        Execute the pipeline: Extract -> Transform -> Load.
        """
        try:
            hana_conn = self.connect_hana()
            sql_conn = self.connect_sql()

            self.logger.info("Starting ETL process...")
            data = self.extract(hana_conn)
            transformed_data = self.transform(data)
            self.load(sql_conn, transformed_data)
            self.logger.info("ETL process completed successfully.")
        except Exception as e:
            self.logger.error(f"Pipeline execution failed: {e}")
            raise