"""
postgres-client - PostgreSQL utilities and connection management

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import PostgresClient, query, process, main

__all__ = ["PostgresClient", "query", "process", "main"]
