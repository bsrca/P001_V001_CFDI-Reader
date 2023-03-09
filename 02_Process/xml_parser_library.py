#xml library

#**get_child_elements**
#This code defines a recursive function get_child_elements that takes a root element and 
# returns a list of all child elements (including nested child elements) of that root element.
# It does this by iterating over each child element of the root element and appending it to the 
# elements list, # and then recursively calling the get_child_elements function on each child 
# element and extending the elements list with the result

def get_child_elements(xml_root):
    elements = []
    for child in xml_root:
        elements.append(child)
        elements.extend(get_child_elements(child))
    return elements