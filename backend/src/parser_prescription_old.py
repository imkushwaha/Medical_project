from backend.src.parser_generic import MedicalDocParser
import re

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {

            'patient_name': self.get_name(),
            'address': self.get_address(),
            'medicines': self.get_medicines(),
            'directions': self.get_directions(),
            'refill': self.get_refill()
        }

    def get_field(self, field_name):
        pattern = ''
        flags = None

        pattern_dict = {
            'patient_name': {'pattern': 'Name:(.*)Date', 'flags': 0},
            'patient_address': {'pattern': 'Address:(.*)\n', 'flags': 0},
            'medicines': {'pattern': 'Address[^\n]*(.*)Directions', 'flags': re.DOTALL},
            'directions': {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL},
            'refills': {'pattern': 'Refill:(.*)times', 'flags': 0}
        }
        pattern_object = pattern_dict.get(field_name)



    def get_name(self):
        pattern = "Name:(.*)Date"
        matches = re.findall(pattern, self.text)
        if len(matches) > 0:
            return matches[0].strip()

    def get_address(self):
        pattern = "Address:(.*)\n"
        matches = re.findall(pattern, self.text)
        if len(matches) > 0:
            return matches[0].strip()

    def get_medicines(self):
        pattern = "Address[^\n]*(.*)Directions"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches[0].strip()

    def get_directions(self):
        pattern = "Directions:(.*)Refill"
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches[0].strip()

    def get_refill(self):
        pattern = "Refill:(.*)times"
        matches = re.findall(pattern, self.text)
        if len(matches) > 0:
            return matches[0].strip()

if __name__ = '__main__':
    PrescriptionParser('abc')

