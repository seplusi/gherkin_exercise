import os.path
import json

GOOD_RESPONSE_FILE_NAME = "good_response_json_payload.json"
BAD_RESPONSE_FILE_NAME = "bad_response_json_payload.json"


def before_scenario(context, scenario):
    print('Before scenario\n')

    context.good_json_payload = read_json_from_file(GOOD_RESPONSE_FILE_NAME)
    context.bad_json_payload = read_json_from_file(BAD_RESPONSE_FILE_NAME)


def after_scenario(context, scenario):
    print('After scenario\n')
    context.after = 'done'

def read_json_from_file(filename):
    file = os.path.dirname(__file__) + '/../test_data/%s' %filename
    with open(file) as f:
        data = json.load(f)

    return data
