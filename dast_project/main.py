from attacks.sql_injection import sql_injection_attack
from attacks.xss import xss_attack
from attacks.blind_sql_injection import blind_sql_injection_attack
import os

def main():
    print("Welcome to the DAST Project")
    url_file = "config/urls.txt"
    sql_log_file = "logs/sql_injection.log"
    xss_log_file = "logs/xss.log"
    blind_sql_log_file = "logs/blind_sql_injection.log"

    sql_injection_attack(url_file, sql_log_file)
    xss_attack(url_file, xss_log_file)
    blind_sql_injection_attack(url_file, blind_sql_log_file)

if __name__ == "__main__":
    main()
