# %%
from rdflib import Graph, URIRef

# Create a Graph
g = Graph()

# Parse in an RDF file hosted on the Internet
g.parse('examples/turtle format/mensa.ttl', format='ttl')

# Loop through each triple in the graph (subj, pred, obj)
for subj, pred, obj in g:
    # Check if there is at least one triple in the Graph
    if (subj, pred, obj) not in g:
       raise Exception("It better be!")


# %%
# Print the number of "triples" in the Graph
print(f"Graph g has {len(g)} statements.")
# Prints: Graph g has 86 statements.


# %%
# Print out the entire Graph in the RDF Turtle format
print(g.serialize(format="turtle"))


# %%
triplet = (URIRef('http://example.org/#JerryRed'),
           URIRef('http://www.perceive.net/schemas/relationship/enemyOf'),
           URIRef('http://example.org/#MichaelBrown'))
g.add(triplet)


# %%
g.serialize(destination='examples/turtle format/mensa-plus.ttl')