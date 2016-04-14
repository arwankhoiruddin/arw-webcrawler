from nltk.tag.stanford import NERTagger

st = NERTagger('/home/x300/Downloads/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz', '/home/x300/Downloads/stanford-ner/stanford-ner.jar')

tags = st.tag('Applied Graphene Materials (AGM), a world-leading UK Manufacturer of graphene, appointed  Hudson Sandler to support its IPO.  We firmly put AGM on the map with one of the most high profile AIM IPOs of the year in November 2013.  The float saw the shares twice oversubscribed and triple in value in their first year of listing.'.split())


organizations = []
for tag in tags:
    found = False
    for word in tag:
        if 'ORGANIZATION' in word and not found:
            name = []
            name.append(word[0])
            found = True
        elif 'ORGANIZATION' in word and found:
            name.append(word[0])
        elif 'ORGANIZATION' not in word and found:
            organization = ' '.join(name)
            organizations.append(organization)
            found = False

for organization in organizations:
    print(organization)
