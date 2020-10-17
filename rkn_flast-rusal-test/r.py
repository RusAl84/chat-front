from rutermextract import TermExtractor
from typing import List


term_extractor = TermExtractor()
text="Военкомат представляет собой орган местного самоуправления. Он отвечает за учетно-призывную и военно-мобилизационную деятельность. путешествие по России, страховка ВЗР поможет чувствовать себя уверенно."
definition_list: List[str] = list()
for term in term_extractor.__call__(text, nested=True):
    definition_list.append(term.normalized)
    print(str(term.normalized.split(' ')))
# print(definition_list)

