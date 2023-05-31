import os
import re
import xml.etree.ElementTree as ET
import pyodbc
import unittest
from io import StringIO


class TestXMLProcessing(unittest.TestCase):

    def setUp(self):
        self.xml_root = ET.fromstring(
            """
            <Invoice>
                <Header UUID="1234567890">
                    <Date>2023-05-05</Date>
                </Header>
                <Items>
                    <Item UUID="0987654321">
                        <Name>Item 1</Name>
                        <Price>100.00</Price>
                    </Item>
                </Items>
            </Invoice>
            """
        )

    def test_get_child_elements(self):
        elements = get_child_elements(self.xml_root)
        self.assertEqual(len(elements), 5)

    def test_create_table(self):
        conn_str = "your_connection_string_here"
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        table_name = "TestTable"
        attributes = {"UUID": "1234567890", "Name": "Test"}

        create_table(cursor, table_name, attributes)
        cursor.execute(f"DROP TABLE {table_name}")

        conn.close()

    def test_insert_element_attributes(self):
        conn_str = "your_connection_string_here"
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        table_name = "TestTable"
        attributes = {"UUID": "1234567890", "Name": "Test"}

        create_table(cursor, table_name, attributes)

        test_element = ET.Element("TestElement")
        test_element.attrib = attributes

        insert_element_attributes(cursor, table_name, test_element)

        cursor.execute(f"DELETE FROM {table_name} WHERE UUID = '1234567890'")
        cursor.execute(f"DROP TABLE {table_name}")

        conn.close()

    def test_process_elements(self):
        conn_str = "your_connection_string_here"
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        elements = get_child_elements(self.xml_root)
        elements.append(self.xml_root)

        process_elements(elements, cursor)

        cursor.execute("DELETE FROM Header WHERE UUID = '1234567890'")
        cursor.execute("DELETE FROM Item WHERE UUID = '0987654321'")

        conn.close()

    def test_process_xml_file(self):
        conn_str = "your_connection_string_here"
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        xml_file_path = "test.xml"

        with open(xml_file_path, "w") as xml_file:
            xml_file.write(self.xml_root.tostring().decode("utf-8"))

        process_xml_file(xml_file_path, cursor)

        cursor.execute("DELETE FROM Header WHERE UUID = '1234567890'")
        cursor.execute("DELETE FROM Item WHERE UUID = '0987654321'")

        conn.close()


if __name__ == "__main__":
    unittest.main()
