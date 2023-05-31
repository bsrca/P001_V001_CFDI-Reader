#Program to parse the xml file and extract the data

#import Libriaries
import xml.etree.ElementTree as ET
import pandas as pd
import re


#this defined function eventually will be on a separate file

def get_child_elements(xml_root):
    # Create a list to store all child elements
    elements = []
    #append xml root to elements list
    #elements.append(xml_root)
    # Get all child elements of a given xml element
    for child in xml_root:
        elements.append(child)
        elements.extend(get_child_elements(child))
    return elements


# Define file to read
#xml_file_path = r"C:\Users\Roberto\OneDrive\cargoIabono\Proyectos y Desarrollos\P001_V001_CFDI-Reader\01_Inputs\Nomina\EMS2103108P3_Pago de nómina_20220815_N_AOAR951019842.xml"
xml_file_path = r"C:\Users\Roberto\OneDrive\cargoIabono\Proyectos y Desarrollos\P001_V001_CFDI-Reader\01_Inputs\Facturas\0F23FE0D-8324-4BCE-AFAC-68CB67E89714.xml"
xml_tree = ET.parse(xml_file_path)
xml_root = xml_tree.getroot()
print(xml_root.tag)

#Read XML Child elements
elements = get_child_elements(xml_root)

#add xml root to read it with their child elements
elements.append(xml_root)

#print child elements
for element in elements:
    print(element.tag, element.attrib)