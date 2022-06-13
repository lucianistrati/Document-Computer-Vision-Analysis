# default class, cdep, senat, prezi
import spacy
import re
nlp = spacy.load("ro_core_news_sm")

counties_list = []
abbreviations_da = ["DA", "ICON", "ANI", "integritate", "analysis", "Declaratie",
                 "de", "avere", "institutia", "prefectului", "cep", "VVA",
                 "cdep", "GA", "eu", "ABO", "RVC", "decl", "incetare", "mandat",
                 "biroul", "electoral", "central", "candidati", "deputati",
                 "senatori", "ambulantasj", "IB", "ORG", "APIA", "CATRE", "PLATI",
                 "Av", "cd", "sm"]

abbreviations_da = [abb.lower() for abb in abbreviations_da]



def get_nume(filename: str):
    words = re.split('[^a-zA-Z]', filename)


get_nume("AchimasÌ¦-Cadariu Patriciu-Andrei  DA_2013_06_14_ANI_ACPA_analysis.json")
