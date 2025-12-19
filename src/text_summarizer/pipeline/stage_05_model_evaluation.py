from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.logging import logger
from text_summarizer.components.model_evaluation import ModelEvaluation

class ModelEvaluationTrainPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
    
    def main(self):
        model_evaluation_config = self.config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()