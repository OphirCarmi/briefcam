import generator
import estimator

generator.main("config.json", "generator_output.json", True)
estimator.main("generator_output.json", "estimator_output.json", True)
