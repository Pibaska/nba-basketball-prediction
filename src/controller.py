from core.validation.run import run_validation
from core.main import run_gen_alg
from core.web.control import activate_web_scraping
import argparse

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument(
    "-d", "--date", help="Specifies a date for the program to run with in the format YYYY-MM-DD", type=str)

arg_parser.add_argument("-g", "--genetic", "--genetic-algorithm",
                        help="Runs an genetic algorithm", action="store_true")

arg_parser.add_argument("-v", "--validation",
                        help="Runs the validation script", action="store_true")

arg_parser.add_argument("-w", "--web-scraping",
                        help="Collects data via web scraping", action="store_true")

args = arg_parser.parse_args()

print(args)

if(args.web_scraping):
    activate_web_scraping()

if(args.genetic):
    run_gen_alg()

if(args.validation):
    run_validation()
