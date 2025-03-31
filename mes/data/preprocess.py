import pandas as pd
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

# Load the CSV file
df = pd.read_csv('MES-2.csv')

# Create the root element
root = ET.Element("sentences")

# Iterate through each row in the dataframe
for _, row in df.iterrows():
    # Create a sentence element with an id attribute
    sentence_elem = ET.SubElement(root, "sentence", id=str(row['index']))

    # Add the text element
    text_elem = ET.SubElement(sentence_elem, "text")
    text_elem.text = row['sentence']

    # Add the aspectTerms element
    aspect_terms_elem = ET.SubElement(sentence_elem, "aspectTerms")
    for i in range(1, 5):
        label = row.get(f'label_{i}', None)
        if pd.notna(label):
            aspect_term_elem = ET.SubElement(aspect_terms_elem, "aspectTerm", term="None", polarity=label, implicit_sentiment="True")

    # Add the aspectCategories element
    aspect_categories_elem = ET.SubElement(sentence_elem, "aspectCategories")
    aspect_category_elem = ET.SubElement(aspect_categories_elem, "aspectCategory", category="None", polarity="None")

# Convert the tree to a string
tree = ET.ElementTree(root)
xml_str = ET.tostring(root, encoding='unicode')

# Pretty print the XML string
def pretty_print_xml(xml_str):
    dom = minidom.parseString(xml_str)
    return dom.toprettyxml(indent="    ")

# Pretty print the XML string and save it
pretty_xml_str = pretty_print_xml(xml_str)

# Save the XML to a file
xml_file_path = 'mes_implicit.xml'
with open(xml_file_path, 'w', encoding='utf-8') as f:
    f.write(pretty_xml_str)
    
