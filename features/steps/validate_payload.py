from behave import then


@then("I verify the json content has not found")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert list(context.bad_json_payload.keys()) == ['detail']
    assert context.bad_json_payload['detail'] == 'Not found.'


@then("I verify the json content")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert list(context.good_json_payload.keys()) == ['id', 'name', 'state', 'bank_type', 'family_ids', 'reader_enabled', 'transfer_enabled', 'bank_codes', 'country', 'features', 'details', 'parameters']
    assert context.good_json_payload['id'] == 98
    assert context.good_json_payload['name'] == "Copito Bank - Empresas"
    assert context.good_json_payload['state'] == 1
    assert context.good_json_payload['bank_type'] == 2
    assert context.good_json_payload['family_ids'] == [98]
    assert context.good_json_payload['reader_enabled'] == context.good_json_payload['transfer_enabled'] == True
    assert isinstance(context.good_json_payload['id'], int)
