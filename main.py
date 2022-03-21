import generator
import estimator
import tester

generator.main("config.json", "generator_output.json", True)
estimator.main("generator_output.json", "estimator_output.json", True)
tester.main("generator_output.json", "estimator_output.json", True)
