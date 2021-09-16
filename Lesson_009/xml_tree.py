import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type = "intl">
    +1 354654 146546531
    </phone>
    <email hide = "yes"/>
    </person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print('Phone:', tree.find('phone').text)
print('Phone:', tree.find('phone').get('type'))
