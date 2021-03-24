from core.validation.run import run_validation
from core.main import run_gen_alg, run_web_scraping, predict_score
import argparse
from datetime import datetime

arg_parser = argparse.ArgumentParser()

command_subparser = arg_parser.add_subparsers(dest="subparser",
                                              help="Operation to be executed with the program.")


gen_parser = command_subparser.add_parser("genetic")
gen_parser.add_argument("-d", "--day", type=int, default=24,
                        help="Day to run the genetic algorithm at.")
gen_parser.add_argument("-ggg", "--gen-good-generations", type=int, default=3,
                        help="Sets how many consecutive good generations will interrupt and finish the algorithm execution.")
gen_parser.add_argument("-gwr", "--gen-weight-range", type=tuple, default=(-100, 1000),
                        help="Sets the minimum and maximum value for newly created individuals' genes.")
gen_parser.add_argument("-gmc", "--gen-mutation-chance", type=float, default=1,
                        help="Percentage that indicates the chance of a gene being mutated during reproduction.")
gen_parser.add_argument("-gmm", "--gen-mutation-magnitude", type=tuple, default=(-10, 10),
                        help="Sets the magnitude of the value added to a gente during mutation.")
gen_parser.add_argument("-gcs", "--gen-chromosome-size", type=int, default=10,
                        help="Sets how many genes are in a chromosome. WARNING: Editing this value might yield some strange results from the algorithm without prior setup.")
gen_parser.add_argument("-gps", "--gen-population-size", type=int, default=100,
                        help="Sets how many individuals are going to be in any given generation")
gen_parser.add_argument("-gmg", "--gen-max-generations", type=int, default=99999,
                        help="Sets the maximum number of generations for the algorithm to run for it to break automatically.")
gen_parser.add_argument("-gpi", "--gen-persistent-individuals", type=int, default=10,
                        help="Sets how many of the parents (ordered by the highest fitness) will continue existing in the children generation.")
gen_parser.add_argument("-m", "--month", type=int, default=3,
                        help="Month to run the genetic algorithm at.")
gen_parser.add_argument("-y", "--year", type=int, default=2021,
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
    print(args)
    run_gen_alg(date=[args.year, args.month, args.day], good_generations=args.gen_good_generations,
                weight_range=args.gen_weight_range, mutation_chance=args.gen_mutation_chance,
                mutation_magnitude=args.gen_mutation_magnitude, chromosome_size=args.gen_chromosome_size,
                population_size=args.gen_population_size, max_generations=args.gen_max_generations,
                persistent_individuals=args.gen_persistent_individuals, timestamp=datetime.now())
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
