#!/usr/bin/env python3
import requests
import os
import sys
import logging

# Configure logging
logging.basicConfig(
    filename='/var/log/test_server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_server():
    url = "http://localhost/test/index.php"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if 'success' in data and data['success'] == False:
            logging.warning("Status is false. Restarting server...")
            restart_mysql_server()
        else:
            logging.info("Server status is OK.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error connecting to server: {e}")
        logging.info("Attempting to restart server...")
        restart_server()
    except ValueError:
        logging.error("Invalid JSON response.")
        logging.info("Attempting to restart server...")
        restart_server()

def restart_server():
    try:
        os.system("sudo systemctl restart apache2")
        logging.info("Server restarted successfully.")
    except Exception as e:
        logging.critical(f"Error restarting server: {e}")
        sys.exit(1)

def restart_mysql_server():
    try:
        os.system("sudo systemctl restart mysql")
        logging.info("Server restarted successfully.")
    except Exception as e:
        logging.critical(f"Error restarting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_server()
