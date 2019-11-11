import string
from pathlib import Path
import itertools
import stanfordnlp
import pygephi


def start_nlp():
    return stanfordnlp.Pipeline(processors='tokenize,lemma,pos', lang='da')


def process(text, nlp, lang, wanted_pos):
    try:
        text = text.translate(str.maketrans('', '', string.punctuation))
        token = nlp(text)
        words = {word for sent in token.sentences for word in sent.words}
        wanted_words = set(filter(lambda word: word.upos in wanted_pos, words))
        wanted_words = [word.lemma for word in wanted_words if word]
        wanted_words = [word.lower() for word in wanted_words]
        return wanted_words
    except:
        return []


def draw_nodes(text, nlp):
    nouns = process(text=text, nlp=nlp, lang='da', wanted_pos={'NOUN'})

    # Add nodes
    for noun in nouns:
        node_attributes = {"label": noun, "size": 10,
                           'r': 1.0, 'g': 0.0, 'b': 0.0, 'x': 1}
        g.add_node(noun, **node_attributes)

    # Add edges
    combos = list(itertools.combinations(nouns, r=2))
    for i, combo in enumerate(combos):
        g.add_edge(id=f'{combo[0]}-{combo[1]}', source=combo[0],
                   target=combo[1], directed=False)


# Download model for nlp.
stanford_path = Path.home() / 'stanfordnlp_resources' / f'da_ddt_models'
if not stanford_path.exists():
    stanfordnlp.download('da')

# Set up Gephi client
g = pygephi.GephiClient('http://localhost:8080/workspace1', autoflush=True)
g.clean()
