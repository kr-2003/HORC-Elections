from clean_candidates import clean_candidates
from clean_residents import clean_residents
from create_import_data import create_import_data

CANDIDATES_RAW = "Hos. Candidate List.csv"
RESIDENTS_RAW  = "Hos. Res List.csv"

POST_NAMES = ['Cultural Secretary','Dining Secretary','Hall Secretary','Science and Technology Secretary','Sports Secretary']
HOSTEL_NAMES = ["APJ","CVR","DA","HJB","VSB"]

clean_candidates(CANDIDATES_RAW,POST_NAMES,HOSTEL_NAMES)
clean_residents(RESIDENTS_RAW,HOSTEL_NAMES)
create_import_data()

