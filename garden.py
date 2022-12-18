# Import spaCy
import spacy

garden_path_sentences = [u"The old man the boat", 
                        u"The horse raced past the barn fell",
                        u"The complex houses married and single soldiers and their families",
                        u"The farmers warned about the floods planted other crops in the Himalayan Mountains",
                        u"The man who whistles tunes pianos"]

nlp = spacy.load("en_core_web_sm")

doc_tags = set()
gloss = spacy.glossary.GLOSSARY

for sent in garden_path_sentences:
    sent_NLP = nlp(sent)
    print(sent.upper())
    print("Entities: " + str([(i, i.label_) for i in sent_NLP.ents]))
    print("Tokens: " + str([(i.orth_, i.tag_) for i in sent_NLP]))

print("\033[93mI think these sentences have no entities since there are no words of the following classes:")
print("""Organisation
Place
Money
Date
Person\033[0m\n\nSee the following website for details: 
https://www.analyticsvidhya.com/blog/2021/06/nlp-application-named-entity-recognition-ner-in-python-with-spacy/#:~:text=Spacy%20is%20an%20open-source,very%20easily%20for%20NER%20tasks.
""")

# Let's use another sentence that does return entities:
sent_NLP = nlp("The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well.")

# Glossary section containing NER-related terms - these are classes of entities
ent_rec_dict = {"PERSON": "People, including fictional",
                "NORP": "Nationalities or religious or political groups",
                "FACILITY": "Buildings, airports, highways, bridges, etc.",
                "FAC": "Buildings, airports, highways, bridges, etc.",
                "ORG": "Companies, agencies, institutions, etc.",
                "GPE": "Countries, cities, states",
                "LOC": "Non-GPE locations, mountain ranges, bodies of water",
                "PRODUCT": "Objects, vehicles, foods, etc. (not services)",
                "EVENT": "Named hurricanes, battles, wars, sports events, etc.",
                "WORK_OF_ART": "Titles of books, songs, etc.",
                "LAW": "Named documents made into laws.",
                "LANGUAGE": "Any named language",
                "DATE": "Absolute or relative dates or periods",
                "TIME": "Times smaller than a day",
                "PERCENT": 'Percentage, including "%"',
                "MONEY": "Monetary values, including unit",
                "QUANTITY": "Measurements, as of weight or distance",
                "ORDINAL": '"first", "second", etc.',
                "CARDINAL": "Numerals that do not fall under another type"}

for ent in sent_NLP.ents:
    print((ent, ent.label_, spacy.explain(ent.label_)))

# This shows us the entity in the sentence, as well as the category it falls under
