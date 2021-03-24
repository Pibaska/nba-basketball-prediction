from core.validation.run import run_validation
from core.main import run_gen_alg, run_web_scraping, predict_score
import argparse

arg_parser = argparse.ArgumentParser()

command_subparser = arg_parser.add_subparsers(dest="subparser",
                                              help="Operation to be executed with the program.")

gen_parser = command_subparser.add_parser("genetic")
gen_parser.add_argument("-d", "--day", type=int, default=20,
                        help="Day to run the genetic algorithm at.")
gen_parser.add_argument("-m", "--month", type=int, default=6,
                        help="Month to run the genetic algorithm at.")
gen_parser.add_argument("-y", "--year", type=int, default=2018,
                        help="Year to run the genetic algorithm at.")

ws_parser = command_subparser.add_parser("scrape")


prediction_parser = command_subparser.add_parser("predict")
prediction_parser.add_argument(
    "-at", "--away", type=str, default="Orlando Magic", help="The name of the away team.")
prediction_parser.add_argument(
    "-ht", "--home", type=str, default="Miami Heat", help="The name of the home team.")
prediction_parser.add_argument("-d", "--day", type=int, default=20,
                               help="Day to predict the results at.")
prediction_parser.add_argument("-m", "--month", type=int, default=6,
                               help="Month to predict the results at.")
prediction_parser.add_argument("-y", "--year", type=int, default=2018,
                               help="Year to predict the results at.")

validation_parser = command_subparser.add_parser("validate")
validation_parser.add_argument("-c", "--cycles", type=int, default=10, help="Number of cycles ran in the validation. \
    Equates to how many fitness values will be compared for each generator function.")

args = arg_parser.parse_args()

if(args.subparser == "genetic"):
    run_gen_alg(date=[args.year, args.month, args.day])
elif(args.subparser == "scrape"):
    run_web_scraping()
elif(args.subparser == "predict"):
    predict_score(args.home, args.home, [args.year, args.month, args.day])
elif(args.subparser == "validate"):
    run_validation(test_cycles=args.cycles)
else:
    print("""
    NBA PREDICTION
    Thanks for using NBA prediction. Please run this command with a `-h` to see available options.
    """)
