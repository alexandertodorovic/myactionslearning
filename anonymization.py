import spacy
from faker import Faker

def anonymize_text(text):
    fake = Faker()
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    # Mapping spaCy entity types to Faker methods
    entity_replacements = {
        'PERSON': lambda: fake.name(),
        'DATE': lambda: fake.date_between(start_date='-30y', end_date='today').strftime('%B %d, %Y'),
        'GPE': lambda: fake.city(),
        'ORG': lambda: fake.company(),
        'MONEY': lambda: fake.currency_symbol() + fake.numerify(text="#####.##"),
        'EMAIL': lambda: fake.email(),
        'PHONE': lambda: fake.phone_number(),
        'ADDRESS': lambda: fake.address().replace('\n', ', '),
    }

    anonymized_tokens = []

    for token in doc:
        if token.ent_type_ in entity_replacements:
            replacement = entity_replacements[token.ent_type_]()
            anonymized_tokens.append(replacement)
        else:
            anonymized_tokens.append(token.text)

    return ' '.join(anonymized_tokens)

# Example usage
if __name__ == "__main__":
    text = (
        "John Doe visited 123 Main St. in New York on September 10th, 2021. "
        "He spent $500 on a new laptop. Contact him at john.doe@example.com or 555-123-4567."
    )
    anonymized_text = anonymize_text(text)
    print(anonymized_text)
