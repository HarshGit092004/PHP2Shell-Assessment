
import requests
import logging
import argparse
from datetime import datetime
from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Logging configuration
log_file = LOG_DIR / "php2shell_poc.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def check_target(url):
    """Check HTTP connectivity and collect basic response details."""

    print(f"\n[*] Checking target: {url}")

    try:
        response = requests.get(url, timeout=10)

        result = {
            "timestamp": datetime.now().isoformat(),
            "url": url,
            "http_status": response.status_code,
            "server": response.headers.get("Server", "Not disclosed"),
            "content_type": response.headers.get("Content-Type", "Unknown"),
            "response_size": len(response.content),
            "php_fingerprint": response.json()
        }

        logging.info("HTTP check successful: %s", result)

        print("\n[+] HTTP connection successful")
        for key, value in result.items():
            print(f"{key}: {value}")

        return result

    except requests.RequestException as error:
        logging.error("Connection failed: %s", error)
        print(f"\n[!] Connection failed: {error}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="PHP2Shell assessment - safe HTTP reconnaissance"
    )

    parser.add_argument(
        "--url",
        required=True,
        help="Authorized test endpoint"
    )

    args = parser.parse_args()
    check_target(args.url)


if __name__ == "__main__":
    main()
