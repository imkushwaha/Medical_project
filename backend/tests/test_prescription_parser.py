from backend.src.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc_1_Marta():
    document_text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222
Name: Marta Sharapova Date: 5/11/2022
Address: 9 tennis court, new Russia, DC
Prednisone 20 mg
Lialda 2.4 gram
Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month
Refill: 2 times
'''
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_2_Virat():
    document_text = ''''
Dr John >mith, M.D
2 Non-Important street,
New York, Phone (900)-323- ~2222
    
Name:  Virat Kohli Date: 2/05/2022
    
Address: 2 cricket blvd, New Delhi
    
Omeprazole 40 mg
    
Directions: Use two tablets daily for three months
    
Refill: 3 times
'''
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_3_empty():
    return PrescriptionParser('')

def test_get_name(doc_1_Marta, doc_2_Virat,doc_3_empty):
    assert doc_1_Marta.get_field('patient_name') == "Marta Sharapova"
    assert doc_2_Virat.get_field('patient_name') == "Virat Kohli"
    assert doc_3_empty.get_field('patient_name') == None


def test_get_address(doc_1_Marta, doc_2_Virat, doc_3_empty):
    assert doc_1_Marta.get_field('patient_address') == "9 tennis court, new Russia, DC"
    assert doc_2_Virat.get_field('patient_address') == "2 cricket blvd, New Delhi"
    assert doc_3_empty.get_field('patient_address') == None

def test_get_medicines(doc_1_Marta, doc_2_Virat, doc_3_empty):
    assert doc_1_Marta.get_field('medicines') == 'Prednisone 20 mg\nLialda 2.4 gram'
    assert doc_2_Virat.get_field('medicines') == 'Omeprazole 40 mg'
    assert doc_3_empty.get_field('medicines') == None

def test_get_directions(doc_1_Marta, doc_2_Virat, doc_3_empty):
    assert doc_1_Marta.get_field('directions') == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month'
    assert doc_2_Virat.get_field('directions') == 'Use two tablets daily for three months'
    assert doc_3_empty.get_field('directions') == None

def test_get_refill(doc_1_Marta, doc_2_Virat, doc_3_empty):
    assert doc_1_Marta.get_field('refills') == '2'
    assert doc_2_Virat.get_field('refills') == '3'
    assert doc_3_empty.get_field('refills') == None

def test_parse(doc_1_Marta, doc_2_Virat, doc_3_empty):
    record_Marta = doc_1_Marta.parse()
    assert record_Marta['patient_name'] == 'Marta Sharapova'
    assert record_Marta['patient_address'] == '9 tennis court, new Russia, DC'
    assert record_Marta['medicines'] == 'Prednisone 20 mg\nLialda 2.4 gram'
    assert record_Marta['directions'] == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month'
    assert record_Marta['refills'] == '2'

    record_Virat = doc_2_Virat.parse()
    assert record_Virat == {
        'patient_name': 'Virat Kohli',
        'patient_address': '2 cricket blvd, New Delhi',
        'medicines': 'Omeprazole 40 mg',
        'directions': 'Use two tablets daily for three months',
        'refills': '3'
    }

    record_empty = doc_3_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'patient_address': None,
        'medicines': None,
        'directions': None,
        'refills': None
    }

