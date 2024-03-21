import argparse  # Step 1

parser = argparse.ArgumentParser(description="Run the game in debug mode.")
parser.add_argument('-d', '--debug', action='store_true', help="Enable debug mode")  # Step 3
args = parser.parse_args()  # Parse arguments