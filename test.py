from rouge_score import rouge_scorer

scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
actual_summary = "The user expresses surprise and amusement at the situation, mentioning the CEO and COO selling many shares without lockout agreements, contrasting it with their experience during an IPO where major shareholders were required to sign such agreements. Despite their heavy use of the platform, they show a lack of concern. The user also includes humorous elements like lol and expresses discontent towards the CEO."

generated_summary="lmao went through an IPO once and all major shareholders were _required_ to sign six month lockout agreements . its amazing how little i care about this platform for how much i use it ."


scores = scorer.score(actual_summary, generated_summary)
for key in scores:
    print(f'{key}: {scores[key]}')



# from deepeval.metrics import SummarizationMetric
# from deepeval.test_case import LLMTestCase
# import openai


# from deepeval import evaluate
# from deepeval.test_case import LLMTestCase
# from deepeval.metrics import SummarizationMetric

# test_case = LLMTestCase(
#   input=input, 
#   actual_output=actual_output
# )
# # summarization_metric = SummarizationMetric()
# # evaluate([test_case], [summarization_metric])



# test_case = LLMTestCase(input=input, actual_output=actual_output)
# metric = SummarizationMetric(threshold=0.5)

# metric.measure(test_case)
# print(metric.score)