import generator
import estimator
import tester

generator.main("config.json", "generator_output.json", False)

estimator.main("generator_output.json", "estimator_output.json", False)

tester.main("generator_output.json", "estimator_output.json", "tester_output.json", False)
