from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine


analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()


def analyze_pii(text):

    results = analyzer.analyze(
        text=text,
        language="en"
    )

    entities = [r.entity_type for r in results]

    anonymized = anonymizer.anonymize(
        text=text,
        analyzer_results=results
    )

    return entities, anonymized.text