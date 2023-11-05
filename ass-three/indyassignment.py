from os import environ
import time
from indy import anoncreds, did, ledger, pool, wallet
import json
import logging
from indy.error import ErrorCode, IndyError
import asyncio
from pathlib import Path
from tempfile import gettempdir

def get_pool_genesis_txn_path(pool_name):
    path_temp = Path(gettempdir()).joinpath("indy")
    path = path_temp.joinpath("{}.txn".format(pool_name))
    save_pool_genesis_txn_file(path)
    return path


def pool_genesis_txn_data():
    pool_ip = environ.get("TEST_POOL_IP", "127.0.0.1")

    return "\n".join([
        '{{"reqSignature":{{}},"txn":{{"data":{{"data":{{"alias":"Node1","blskey":"4N8aUNHSgjQVgkpm8nhNEfDf6txHznoYREg9kirmJrkivgL4oSEimFF6nsQ6M41QvhM2Z33nves5vfSn9n1UwNFJBYtWVnHYMATn76vLuL3zU88KyeAYcHfsih3He6UHcXDxcaecHVz6jhCYz1P2UZn2bDVruL5wXpehgBfBaLKm3Ba","blskey_pop":"RahHYiCvoNCtPTrVtP7nMC5eTYrsUA8WjXbdhNc8debh1agE9bGiJxWBXYNFbnJXoXhWFMvyqhqhRoq737YQemH5ik9oL7R4NTTCz2LEZhkgLJzB3QRQqJyBNyv7acbdHrAT8nQ9UkLbaVL9NBpnWXBTw4LEMePaSHEw66RzPNdAX1","client_ip":"{}","client_port":9702,"node_ip":"{}","node_port":9701,"services":["VALIDATOR"]}},"dest":"Gw6pDLhcBcoQesN72qfotTgFa7cbuqZpkX3Xo6pLhPhv"}},"metadata":{{"from":"Th7MpTaRZVRYnPiabds81Y"}},"type":"0"}},"txnMetadata":{{"seqNo":1,"txnId":"fea82e10e894419fe2bea7d96296a6d46f50f93f9eeda954ec461b2ed2950b62"}},"ver":"1"}}'.format(
            pool_ip, pool_ip),
        '{{"reqSignature":{{}},"txn":{{"data":{{"data":{{"alias":"Node2","blskey":"37rAPpXVoxzKhz7d9gkUe52XuXryuLXoM6P6LbWDB7LSbG62Lsb33sfG7zqS8TK1MXwuCHj1FKNzVpsnafmqLG1vXN88rt38mNFs9TENzm4QHdBzsvCuoBnPH7rpYYDo9DZNJePaDvRvqJKByCabubJz3XXKbEeshzpz4Ma5QYpJqjk","blskey_pop":"Qr658mWZ2YC8JXGXwMDQTzuZCWF7NK9EwxphGmcBvCh6ybUuLxbG65nsX4JvD4SPNtkJ2w9ug1yLTj6fgmuDg41TgECXjLCij3RMsV8CwewBVgVN67wsA45DFWvqvLtu4rjNnE9JbdFTc1Z4WCPA3Xan44K1HoHAq9EVeaRYs8zoF5","client_ip":"{}","client_port":9704,"node_ip":"{}","node_port":9703,"services":["VALIDATOR"]}},"dest":"8ECVSk179mjsjKRLWiQtssMLgp6EPhWXtaYyStWPSGAb"}},"metadata":{{"from":"EbP4aYNeTHL6q385GuVpRV"}},"type":"0"}},"txnMetadata":{{"seqNo":2,"txnId":"1ac8aece2a18ced660fef8694b61aac3af08ba875ce3026a160acbc3a3af35fc"}},"ver":"1"}}'.format(
            pool_ip, pool_ip),
        '{{"reqSignature":{{}},"txn":{{"data":{{"data":{{"alias":"Node3","blskey":"3WFpdbg7C5cnLYZwFZevJqhubkFALBfCBBok15GdrKMUhUjGsk3jV6QKj6MZgEubF7oqCafxNdkm7eswgA4sdKTRc82tLGzZBd6vNqU8dupzup6uYUf32KTHTPQbuUM8Yk4QFXjEf2Usu2TJcNkdgpyeUSX42u5LqdDDpNSWUK5deC5","blskey_pop":"QwDeb2CkNSx6r8QC8vGQK3GRv7Yndn84TGNijX8YXHPiagXajyfTjoR87rXUu4G4QLk2cF8NNyqWiYMus1623dELWwx57rLCFqGh7N4ZRbGDRP4fnVcaKg1BcUxQ866Ven4gw8y4N56S5HzxXNBZtLYmhGHvDtk6PFkFwCvxYrNYjh","client_ip":"{}","client_port":9706,"node_ip":"{}","node_port":9705,"services":["VALIDATOR"]}},"dest":"DKVxG2fXXTU8yT5N7hGEbXB3dfdAnYv1JczDUHpmDxya"}},"metadata":{{"from":"4cU41vWW82ArfxJxHkzXPG"}},"type":"0"}},"txnMetadata":{{"seqNo":3,"txnId":"7e9f355dffa78ed24668f0e0e369fd8c224076571c51e2ea8be5f26479edebe4"}},"ver":"1"}}'.format(
            pool_ip, pool_ip),
        '{{"reqSignature":{{}},"txn":{{"data":{{"data":{{"alias":"Node4","blskey":"2zN3bHM1m4rLz54MJHYSwvqzPchYp8jkHswveCLAEJVcX6Mm1wHQD1SkPYMzUDTZvWvhuE6VNAkK3KxVeEmsanSmvjVkReDeBEMxeDaayjcZjFGPydyey1qxBHmTvAnBKoPydvuTAqx5f7YNNRAdeLmUi99gERUU7TD8KfAa6MpQ9bw","blskey_pop":"RPLagxaR5xdimFzwmzYnz4ZhWtYQEj8iR5ZU53T2gitPCyCHQneUn2Huc4oeLd2B2HzkGnjAff4hWTJT6C7qHYB1Mv2wU5iHHGFWkhnTX9WsEAbunJCV2qcaXScKj4tTfvdDKfLiVuU2av6hbsMztirRze7LvYBkRHV3tGwyCptsrP","client_ip":"{}","client_port":9708,"node_ip":"{}","node_port":9707,"services":["VALIDATOR"]}},"dest":"4PS3EDQ3dW1tci1Bp6543CfuuebjFrg36kLAUcskGfaA"}},"metadata":{{"from":"TWwCRQRZ2ZHMJFn9TzLp7W"}},"type":"0"}},"txnMetadata":{{"seqNo":4,"txnId":"aa5e817d7cc626170eca175822029339a444eb0ee8f0bd20d3b0b76e566fb008"}},"ver":"1"}}'.format(
            pool_ip, pool_ip)
    ])


def save_pool_genesis_txn_file(path):
    data = pool_genesis_txn_data()

    path.parent.mkdir(parents=True, exist_ok=True)

    with open(str(path), "w+") as f:
        f.writelines(data)

async def create_wallet(identity):
    logging.info("\"{}\" -> Create wallet".format(identity['name']))
    try:
        await wallet.create_wallet(wallet_config("create", identity['wallet_config']),
                                   wallet_credentials("create", identity['wallet_credentials']))
    except IndyError as ex:
        if ex.error_code == ErrorCode.PoolLedgerConfigAlreadyExistsError:
            pass
    identity['wallet'] = await wallet.open_wallet(wallet_config("open", identity['wallet_config']),
                                                  wallet_credentials("open", identity['wallet_credentials']))

async def getting_verinym(from_, to):
    await create_wallet(to)

    (to['did'], to['key']) = await did.create_and_store_my_did(to['wallet'], "{}")

    from_['info'] = {
        'did': to['did'],
        'verkey': to['key'],
        'role': to['role'] or None
    }

    await send_nym(from_['pool'], from_['wallet'], from_['did'], from_['info']['did'],
                   from_['info']['verkey'], from_['info']['role'])


async def send_nym(pool_handle, wallet_handle, _did, new_did, new_key, role):
    nym_request = await ledger.build_nym_request(_did, new_did, new_key, None, role)
    await ledger.sign_and_submit_request(pool_handle, wallet_handle, _did, nym_request)

async def ensure_previous_request_applied(pool_handle, checker_request, checker):
    for _ in range(3):
        response = json.loads(await ledger.submit_request(pool_handle, checker_request))
        try:
            if checker(response):
                return json.dumps(response)
        except TypeError:
            pass
        time.sleep(5)

async def get_credential_for_referent(search_handle, referent):
    credentials = json.loads(
        await anoncreds.prover_fetch_credentials_for_proof_req(search_handle, referent, 10))
    return credentials[0]['cred_info']

async def prover_get_entities_from_ledger(pool_handle, _did, identifiers, actor, from_timestamp=None,
                                          to_timestamp=None):
    credential_defs = {}
    rev_states = {}
    schemas = {}
    for item in identifiers.values():
        print("\"{}\" -> Get Schema from Ledger".format(actor))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.", item['schema_id'])
        (received_schema_id, received_schema) = await get_schema(pool_handle, _did, item['schema_id'])
        schemas[received_schema_id] = json.loads(received_schema)

        print("\"{}\" -> Get Claim Definition from Ledger".format(actor))
        (received_cred_def_id, received_cred_def) = await get_cred_def(pool_handle, _did, item['cred_def_id'])
        credential_defs[received_cred_def_id] = json.loads(received_cred_def)

        if 'rev_reg_id' in item and item['rev_reg_id'] is not None:
            # Create Revocations States
            print("\"{}\" -> Get Revocation Registry Definition from Ledger".format(actor))
            get_revoc_reg_def_request = await ledger.build_get_revoc_reg_def_request(_did, item['rev_reg_id'])

            get_revoc_reg_def_response = \
                await ensure_previous_request_applied(pool_handle, get_revoc_reg_def_request,
                                                      lambda response: response['result']['data'] is not None)
            (rev_reg_id, revoc_reg_def_json) = await ledger.parse_get_revoc_reg_def_response(get_revoc_reg_def_response)

            print("\"{}\" -> Get Revocation Registry Delta from Ledger".format(actor))
            if not to_timestamp: to_timestamp = int(time.time())
            get_revoc_reg_delta_request = \
                await ledger.build_get_revoc_reg_delta_request(_did, item['rev_reg_id'], from_timestamp, to_timestamp)
            get_revoc_reg_delta_response = \
                await ensure_previous_request_applied(pool_handle, get_revoc_reg_delta_request,
                                                      lambda response: response['result']['data'] is not None)
            (rev_reg_id, revoc_reg_delta_json, t) = \
                await ledger.parse_get_revoc_reg_delta_response(get_revoc_reg_delta_response)

            tails_reader_config = json.dumps(
                {'base_dir': dirname(json.loads(revoc_reg_def_json)['value']['tailsLocation']),
                 'uri_pattern': ''})
            blob_storage_reader_cfg_handle = await blob_storage.open_reader('default', tails_reader_config)

            print('%s - Create Revocation State', actor)
            rev_state_json = \
                await anoncreds.create_revocation_state(blob_storage_reader_cfg_handle, revoc_reg_def_json,
                                                        revoc_reg_delta_json, t, item['cred_rev_id'])
            rev_states[rev_reg_id] = {t: json.loads(rev_state_json)}

    return json.dumps(schemas), json.dumps(credential_defs), json.dumps(rev_states)

async def run():

    pool_ = {
        'name': 'pool1'
    }
    logging.info("Open Pool Ledger: {}".format(pool_['name']))
    pool_['genesis_txn_path'] = get_pool_genesis_txn_path(pool_['name'])
    pool_['config'] = json.dumps({"genesis_txn": str(pool_['genesis_txn_path'])})
    print(pool_)

    await pool.set_protocol_version(2)

    try:
        await pool.create_pool_ledger_config(pool_['name'], pool_['config'])
    except IndyError as ex:
        if ex.error_code == ErrorCode.PoolLedgerConfigAlreadyExistsError:
            pass
    pool_['handle'] = await pool.open_pool_ledger(pool_['name'], None)

    steward = {
        'name': "Sovrin Steward",
        'wallet_config': json.dumps({'id': 'sovrin_steward_wallet'}),
        'wallet_credentials': json.dumps({'key': 'steward_wallet_key'}),
        'pool': pool_['handle'],
        'seed': '000000000000000000000000Steward1'
    }
    await create_wallet(steward)
    steward['did_info'] = json.dumps({'seed': steward['seed']})
    steward['did'], steward['key'] = await did.create_and_store_my_did(steward['wallet'], steward['did_info'])

    government = {
        'name': 'Government',
        'wallet_config': json.dumps({'id': 'government_wallet'}),
        'wallet_credentials': json.dumps({'key': 'government_wallet_key'}),
        'pool': pool_['handle'],
        'role': 'TRUST_ANCHOR'
    }

    await getting_verinym(steward, government)

    naa = {
        'name': 'NAA',
        'wallet_config': json.dumps({'id': 'naa_wallet'}),
        'wallet_credentials': json.dumps({'key': 'naa_wallet_key'}),
        'pool': pool_['handle'],
        'role': 'TRUST_ANCHOR'
    }

    await getting_verinym(steward, naa)

    cbdc = {
        'name': 'CBDC',
        'wallet_config': json.dumps({'id': 'cbdc_wallet'}),
        'wallet_credentials': json.dumps({'key': 'cbdc_wallet_key'}),
        'pool': pool_['handle'],
        'role': 'TRUST_ANCHOR'
    }

    await getting_verinym(steward, cbdc)

    logging.info("==============================")
    logging.info("=== Credential Schemas Setup ==")
    logging.info("------------------------------")

    logging.info("\"Government\" -> Create \"Property-Details\" Schema")

    property_details = {
        'name': 'PropertyDetails',
        'version': '1.2',
        'attributes': ['owner_first_name', 'owner_last_name',
        'address_of_property', 'residing_since_year', 'property_value_estimate',
        'realtion_to_applicant']
    }

    (government['property_details_schema_id'], government['property_details_schema']) = \
        await anoncreds.issuer_create_schema(government['did'], property_details['name'], property_details['version'],
                                             json.dumps(property_details['attributes']))
    property_details_schema_id = government['property_details_schema_id']

    logging.info("\"Government\" -> Send \"Property-Details\" Schema to Ledger")
    schema_request = await ledger.build_schema_request(government['did'], government['property_details_schema'])
    await ledger.sign_and_submit_request(government['pool'], government['wallet'], government['did'], schema_request)

    logging.info("\"Government\" -> Create \"Bonafide-Student\" Schema")

    bonafide_student = {
        'name': 'BonafideStudent',
        'version': '1.2',
        'attributes': ['student_first_name', 'student_last_name',
        'degree_name', 'student_since_year', 'cgpa']
    }

    (government['bonafide_student_schema_id'], government['bonafide_student_schema']) = \
        await anoncreds.issuer_create_schema(government['did'], bonafide_student['name'], bonafide_student['version'],
                                             json.dumps(bonafide_student['attributes']))
    bonafide_student_schema_id = government['bonafide_student_schema_id']

    logging.info("\"Government\" -> Send \"Bonafide-Student\" Schema to Ledger")
    schema_request = await ledger.build_schema_request(government['did'], government['bonafide_student_schema'])
    await ledger.sign_and_submit_request(government['pool'], government['wallet'], government['did'], schema_request)

    time.sleep(1)

    logging.info("==============================")
    logging.info("=== Government Property Details Definition Setup ==")
    logging.info("------------------------------")

    logging.info("\"Government\" -> Get \"Property Details\" Schema from Ledger")
    get_schema_request = await ledger.build_get_schema_request(government['did'], property_details_schema_id)
    get_schema_response = await ensure_previous_request_applied(
        government['pool'], get_schema_request, lambda response: response['result']['data'] is not None) 
    (government['property_details'], government['property_details_schema']) = \
        await ledger.parse_get_schema_response(get_schema_response)

    logging.info("\"Government\" -> Create and store in Wallet \"Property Details\" Credential Definition")
    property_details_def = {
        'tag': 'TAG1',
        'type': 'CL',
        'config': {"support_revocation": False}
    }
    (government['property_details_def_id'], government['property_details_def']) = \
        await anoncreds.issuer_create_and_store_credential_def(government['wallet'], government['did'],
                                                               government['property_details_schema'], property_details_def['tag'],
                                                               property_details_def['type'],
                                                               json.dumps(property_details_def['config']))

    logging.info("\"Government\" -> Send  \"Property Details\" Credential Definition to Ledger")
    cred_def_request = await ledger.build_cred_def_request(government['did'], government['property_details_def'])
    await ledger.sign_and_submit_request(government['pool'], government['wallet'], government['did'], cred_def_request)

    logging.info("\"NAA\" -> Get \"Bonafide Student\" Schema from Ledger")
    get_schema_request = await ledger.build_get_schema_request(naa['did'], bonafide_student_schema_id)
    get_schema_response = await ensure_previous_request_applied(
        naa['pool'], get_schema_request, lambda response: response['result']['data'] is not None) 
    (naa['bonafide_student'], naa['bonafide_student_schema']) = \
        await ledger.parse_get_schema_response(get_schema_response)

    logging.info("\"NAA\" -> Create and store in Wallet \"Bonafide Student\" Credential Definition")
    bonafide_student_def = {
        'tag': 'TAG1',
        'type': 'CL',
        'config': {"support_revocation": False}
    }
    (naa['bonafide_student_def_id'], naa['bonafide_student_def']) = \
        await anoncreds.issuer_create_and_store_credential_def(naa['wallet'], naa['did'],
                                                               naa['bonafide_student_schema'], bonafide_student_def['tag'],
                                                               bonafide_student_def['type'],
                                                               json.dumps(bonafide_student_def['config']))

    logging.info("\"NAA\" -> Send  \"Bonafide Student\" Credential Definition to Ledger")
    cred_def_request = await ledger.build_cred_def_request(naa['did'], naa['bonafide_student_def'])
    await ledger.sign_and_submit_request(naa['pool'], naa['wallet'], naa['did'], cred_def_request)
    
    logging.info("==============================")
    logging.info("=== Getting Bonafide Student certificate from NAA ===")
    logging.info("------------------------------")
    
    logging.info("== Rajesh setup ==")
    logging.info("------------------------------")

    Rajesh = {
        'name': 'Rajesh',
        'wallet_config': json.dumps({'id': 'Rajesh_wallet'}),
        'wallet_credentials': json.dumps({'key': 'Rajesh_wallet_key'}),
        'pool': pool_['handle'],
    }
    await create_wallet(Rajesh)
    (Rajesh['did'], Rajesh['key']) = await did.create_and_store_my_did(Rajesh['wallet'], "{}")

    # NAA creates bonafide certificate offer

    logging.info("\"NAA\" -> Create \"bonafide\" certificate Offer for Rajesh")
    naa['bonafide_student_offer'] = \
        await anoncreds.issuer_create_credential_offer(naa['wallet'], naa['bonafide_student_def_id'])

    logging.info("\"NAA\" -> Send \"bonafide\" certificate Offer to Rajesh")    
    Rajesh['bonafide_student_offer'] = naa['bonafide_student_offer']

    print(Rajesh['bonafide_student_offer'])

     # Rajesh prepares a bonafide certificate request

    bonafide_student_offer_object = json.loads(Rajesh['bonafide_student_offer'])

    Rajesh['bonafide_student_schema_id'] = bonafide_student_offer_object['schema_id']
    Rajesh['bonafide_student_def_id'] = bonafide_student_offer_object['cred_def_id']

    logging.info("\"Rajesh\" -> Create and store \"Rajesh\" Master Secret in Wallet")
    Rajesh['master_secret_id'] = await anoncreds.prover_create_master_secret(Rajesh['wallet'], None)

    logging.info("\"Rajesh\" -> Get \"naa Transcript\" Credential Definition from Ledger")
    (Rajesh['naa_bonafide_student_def_id'], Rajesh['naa_bonafide_student_def']) = \
        await get_cred_def(Rajesh['pool'], Rajesh['did'], Rajesh['naa_bonafide_student_def_id'])

    logging.info("\"Rajesh\" -> Create \"bonafide\" certificate Request for naa")
    (Rajesh['bonafide_student_request'], Rajesh['bonafide_student_request_metadata']) = \
        await anoncreds.prover_create_credential_req(Rajesh['wallet'], Rajesh['did'],
                                                     Rajesh['bonafide_student_offer'],
                                                     Rajesh['naa_bonafide_student_def'],
                                                     Rajesh['master_secret_id'])

    print("\"Rajesh\" -> Send \"bonafide\" certificate Request to naa")
    naa['bonafide_student_request'] = Rajesh['bonafide_student_request']

    # NAA issues credential to Rajesh ----------------
    print("\"NAA\" -> Create \"bonafide\" certificate for Rajesh")
    # encoded value of non-integer attribute is SHA256 converted to decimal
    naa['Rajesh_bonafide_student_values'] = json.dumps({
        "first_name": {"raw": "Rajesh", "encoded": "61128178701959270985030776464813634457025117419642008842185559604383054644572"},
        "last_name": {"raw": "Kumar", "encoded": "9628796848593399296846015413457437787688669743501058069201688673874032969253"},
        "degree_name": {"raw": "Pilot Training Programme", "encoded": "88808222341925514205595497221537271606006691185381008920976043208354606982292"},
        "student_since_year": {"raw": "2022", "encoded": "2022"},
        "cgpa": {"raw": "8", "encoded": "8"}
    })
    naa['bonafide_student_cred'], _, _ = \
        await anoncreds.issuer_create_credential(naa['wallet'], naa['bonafide_student_offer'],
                                                 naa['bonafide_student_request'],
                                                 naa['Rajesh_bonafide_student_values'], None, None)

    print("\"naa\" -> Send \"bonafide\" certificate to Rajesh")
    print(naa['bonafide_student'])
    Rajesh['bonafide_student'] = naa['bonafide_student']

    print("\"Rajesh\" -> Store \"bonafide\" certificate from naa")
    _, Rajesh['bonafide_student_def'] = await get_cred_def(Rajesh['pool'], Rajesh['did'],
                                                         Rajesh['bonafide_student_def_id'])

    await anoncreds.prover_store_credential(Rajesh['wallet'], None, Rajesh['bonafide_student_request_metadata'],
                                            Rajesh['bonafide_student'], Rajesh['bonafide_student_def'], None)
    
    print("\n\n>>>>>>>>>>>>>>>>>>>>>>.\n\n", Rajesh['bonafide_student_def'])



    logging.info("==============================")
    logging.info("=== Getting 'PropertyDetails' credential from government===")
    logging.info("------------------------------")
    

    # Government creates PropertyDetails credential offer

    logging.info("\"Government\" -> Create \"PropertyDetails\" credential Offer for Rajesh")
    government['property_details_offer'] = \
        await anoncreds.issuer_create_credential_offer(government['wallet'], government['property_details_def_id'])

    logging.info("\"Government\" -> Send \"PropertyDetails\" credential Offer to Rajesh")
    Rajesh['property_details_offer'] = government['property_details_offer']

    print(Rajesh['property_details_offer'])

    # Rajesh prepares a property details request

    property_details_offer_object = json.loads(Rajesh['property_details_offer'])

    Rajesh['property_details_schema_id'] = property_details_offer_object['schema_id']
    Rajesh['property_details_def_id'] = property_details_offer_object['cred_def_id']

    logging.info("\"Rajesh\" -> Create and store \"Rajesh\" Master Secret in Wallet")
    Rajesh['master_secret_id'] = await anoncreds.prover_create_master_secret(Rajesh['wallet'], None)

    logging.info("\"Rajesh\" -> Get \"government PropertyDetails\" Credential Definition from Ledger")
    (Rajesh['government_property_details_def_id'], Rajesh['government_property_details_def']) = \
        await get_cred_def(Rajesh['pool'], Rajesh['did'], Rajesh['government_property_details_def_id'])

    logging.info("\"Rajesh\" -> Create \"PropertyDetails\" credential Request for government")
    (Rajesh['property_details_request'], Rajesh['property_details_request_metadata']) = \
        await anoncreds.prover_create_credential_req(Rajesh['wallet'], Rajesh['did'],
                                                     Rajesh['property_details_offer'],
                                                     Rajesh['government_property_details_def'],
                                                     Rajesh['master_secret_id'])

    print("\"Rajesh\" -> Send \"PropertyDetails\" credential Request to government")
    government['property_details_request'] = Rajesh['property_details_request']

    # government issues credential to Rajesh ----------------
    print("\"Government\" -> Create \"PropertyDetails\" credential for Rajesh")
    # encoded value of non-integer attribute is SHA256 converted to decimal
    government['Rajesh_property_details_values'] = json.dumps({
        "first_name": {"raw": "Rajesh", "encoded": "61128178701959270985030776464813634457025117419642008842185559604383054644572"},
        "last_name": {"raw": "Kumar", "encoded": "9628796848593399296846015413457437787688669743501058069201688673874032969253"},
        "address_of_property": {"raw": "Malancha Road, Kharagpur", "encoded": "40124272564153356135322415401652142391558081737536971014701520100295852485629"},
        "property_value_estimate": {"raw": "2000000", "encoded": "2000000"},
        "residing_since_year": {"raw": "2010", "encoded": "2010"}
    })
    government['property_details_cred'], _, _ = \
        await anoncreds.issuer_create_credential(government['wallet'], government['property_details_offer'],
                                                 government['property_details_request'],
                                                 government['Rajesh_property_details_values'], None, None)

    logging.info("\"government\" -> Send \"PropertyDetails\" credential to Rajesh")
    print(government['property_details'])
    Rajesh['property_details'] = government['property_details']

    logging.info("\"Rajesh\" -> Store \"PropertyDetails\" credential from government")
    _, Rajesh['property_details_def'] = await get_cred_def(Rajesh['pool'], Rajesh['did'],
                                                         Rajesh['property_details_def_id'])

    await anoncreds.prover_store_credential(Rajesh['wallet'], None, Rajesh['property_details_request_metadata'],
                                            Rajesh['property_details'], Rajesh['property_details_def'], None)
    
    logging.info("\n\n-\n\n", Rajesh['property_details_def'])

    # Part d 

    # CBDC Bank creates loan application request 
    logging.info("\"CBDC Bank\" -> Create \"Loan-Application\" Proof Request")
    nonce = await anoncreds.generate_nonce()
    # have to change restrictions part
    cbdc['loan_application_proof_request'] = json.dumps({
        'nonce': nonce,
        'name': 'Loan-Application',
        'version': '0.1',
        'requested_attributes': {
            'attr1_referent': {
                'name': 'first_name'
            },
            'attr2_referent': {
                'name': 'last_name'
            },
            'attr3_referent': {
                'name': 'degree_name'
            },
            'attr4_referent': {
                'name': 'student_since_year',
                'restrictions': [
                    { 'cred_def_id': student_since_lower_CredDefId },
                    { 'cred_def_id': student_since_upper_CredDefId }
                ]
            },
            'attr5_referent': {
                'name': 'cgpa',
                'restrictions': [{'cred_def_id': naa['bonafide_student_def']}]
            },
            'attr6_referent': {
                'name': 'address_of_property'
            },
            'attr7_referent': {
                'name': 'property_value_estimate',
                'restrictions': [{'cred_def_id': government['property_details_def']}]
            },
            'attr8_referent': {
                'name': 'residing_since_year'
            }
        },
        'requested_predicates': {
            'predicate1_referent': {
                'name': 'student_since_lower_bound',
                'p_type': '>=',
                'p_value': 2019,
                'restrictions': [{'cred_def_id': student_since_lower_CredDefId}]
            },
            'predicate2_referent': {
                'name': 'student_since_upper_bound',
                'p_type': '<=',
                'p_value': 2023,
                'restrictions': [{'cred_def_id': student_since_upper_CredDefId}]
            },
            'predicate3_referent': {
                'name': 'cgpa_bound',
                'p_type': '>',
                'p_value': 6,
                'restrictions': [{'cred_def_id': naa['bonafide_student_def']}]
            },
            'predicate4_referent': {
                'name': 'property_value_bound',
                'p_type': '>',
                'p_value': 800000,
                'restrictions': [{'cred_def_id': government['property_details_def']}]
            }
        }
    })

    logging.info("\"cbdc\" -> Send \"Loan-Application\" Proof Request to Rajesh")
    Rajesh['loan_application_proof_request'] = cbdc['loan_application_proof_request']

    print(Rajesh['loan_application_proof_request'])

    # Rajesh prepares the presentation ===================================

    logging.info("\n\n->\n\n", Rajesh['loan_application_proof_request'])

    logging.info("\"Rajesh\" -> Get credentials for \"Loan-Application\" Proof Request")

    search_for_loan_application_proof_request = \
        await anoncreds.prover_search_credentials_for_proof_req(Rajesh['wallet'],
                                                                Rajesh['loan_application_proof_request'], None)
    
    logging.info("\nsearch_for_loan_application_proof_request\n")

    cred_for_attr1 = await get_credential_for_referent(search_for_loan_application_proof_request, 'attr1_referent')
    cred_for_attr2 = await get_credential_for_referent(search_for_loan_application_proof_request, 'attr2_referent')
    cred_for_attr3 = await get_credential_for_referent(search_for_loan_application_proof_request, 'attr3_referent')
    cred_for_attr4 = await get_credential_for_referent(search_for_loan_application_proof_request, 'attr4_referent')
    cred_for_attr5 = await get_credential_for_referent(search_for_loan_application_proof_request, 'attr5_referent')
    cred_for_attr6 = await get_credential_for_referent(search_for_loan_application_proof_request, 'attr6_referent')
    cred_for_attr7 = await get_credential_for_referent(search_for_loan_application_proof_request, 'attr7_referent')
    cred_for_attr8 = await get_credential_for_referent(search_for_loan_application_proof_request, 'attr8_referent')
    cred_for_predicate1 = \
        await get_credential_for_referent(search_for_loan_application_proof_request, 'predicate1_referent')
    cred_for_predicate2 = \
        await get_credential_for_referent(search_for_loan_application_proof_request, 'predicate2_referent')
    cred_for_predicate3 = \
        await get_credential_for_referent(search_for_loan_application_proof_request, 'predicate3_referent')
    cred_for_predicate4 = \
        await get_credential_for_referent(search_for_loan_application_proof_request, 'predicate4_referent')
    
    print(cred_for_attr1)
    print(cred_for_attr2)
    print(cred_for_attr3)
    print(cred_for_attr4)
    print(cred_for_attr5)
    print(cred_for_attr6)
    print(cred_for_attr7)
    print(cred_for_attr8)

    await anoncreds.prover_close_credentials_search_for_proof_req(search_for_loan_application_proof_request)

    Rajesh['creds_for_loan_application_proof'] = {cred_for_attr1['referent']: cred_for_attr1,
                                                cred_for_attr2['referent']: cred_for_attr2,
                                                cred_for_attr3['referent']: cred_for_attr3,
                                                cred_for_attr4['referent']: cred_for_attr4,
                                                cred_for_attr5['referent']: cred_for_attr5,
                                                cred_for_attr6['referent']: cred_for_attr6,
                                                cred_for_attr7['referent']: cred_for_attr7,
                                                cred_for_attr8['referent']: cred_for_attr8,
                                                cred_for_predicate1['referent']: cred_for_predicate1
                                                cred_for_predicate2['referent']: cred_for_predicate2
                                                cred_for_predicate3['referent']: cred_for_predicate3
                                                cred_for_predicate4['referent']: cred_for_predicate4}

    print(Rajesh['creds_for_loan_application_proof'])

    Rajesh['schemas_for_loan_application'], Rajesh['cred_defs_for_loan_application'], \
    Rajesh['revoc_states_for_loan_application'] = \
        await prover_get_entities_from_ledger(Rajesh['pool'], Rajesh['did'],
                                              Rajesh['creds_for_loan_application_proof'], Rajesh['name'])

    logging.info("\"Rajesh\" -> Create \"Loan-Application\" Proof")
    Rajesh['loan_application_requested_creds'] = json.dumps({
        'self_attested_attributes': {
            'attr1_referent': 'Rajesh',
            'attr2_referent': 'Kumar',
            'attr3_referent': 'Pilot Training Programme',
            'attr6_referent': 'Malancha Road, Kharagpur',
            'attr8_referent': '2010'
        },
        'requested_attributes': {
            'attr4_referent': {'cred_id': cred_for_attr4['referent'], 'revealed': True},
            'attr5_referent': {'cred_id': cred_for_attr5['referent'], 'revealed': True},
            'attr7_referent': {'cred_id': cred_for_attr7['referent'], 'revealed': True},
        },
        'requested_predicates': {'predicate1_referent': {'cred_id': cred_for_predicate1['referent']},
                                 'predicate2_referent': {'cred_id': cred_for_predicate2['referent']},
                                 'predicate3_referent': {'cred_id': cred_for_predicate3['referent']},
                                 'predicate4_referent': {'cred_id': cred_for_predicate4['referent']},
        }
    })

    Rajesh['loan_application_proof'] = \
        await anoncreds.prover_create_proof(Rajesh['wallet'], Rajesh['loan_application_proof_request'],
                                            Rajesh['loan_application_requested_creds'], Rajesh['master_secret_id'],
                                            Rajesh['schemas_for_loan_application'],
                                            Rajesh['cred_defs_for_loan_application'],
                                            Rajesh['revoc_states_for_loan_application'])
    print(Rajesh['loan_application_proof'])

    logging.info("\"Rajesh\" -> Send \"Loan-Application\" Proof to cbdc")
    cbdc['loan_application_proof'] = Rajesh['loan_application_proof']

    # Validating the verifiable presentation
    loan_application_proof_object = json.loads(cbdc['loan_application_proof'])

    cbdc['schemas_for_loan_application'], cbdc['cred_defs_for_loan_application'], \
    cbdc['revoc_ref_defs_for_loan_application'], cbdc['revoc_regs_for_loan_application'] = \
        await verifier_get_entities_from_ledger(cbdc['pool'], cbdc['did'],
                                                loan_application_proof_object['identifiers'], cbdc['name'])

    logging.info("\"cbdc\" -> Verify \"Loan-Application\" Proof from Rajesh")
    assert '2022' == \
           loan_application_proof_object['requested_proof']['revealed_attrs']['attr4_referent']['raw']
    assert '8' == \
           loan_application_proof_object['requested_proof']['revealed_attrs']['attr5_referent']['raw']
    assert '2000000' == \
           loan_application_proof_object['requested_proof']['revealed_attrs']['attr7_referent']['raw']

    assert 'Rajesh' == loan_application_proof_object['requested_proof']['self_attested_attrs']['attr1_referent']
    assert 'Kumar' == loan_application_proof_object['requested_proof']['self_attested_attrs']['attr2_referent']
    assert 'Pilot Training Programme' == loan_application_proof_object['requested_proof']['self_attested_attrs']['attr3_referent']
    assert 'Malancha Road, Kharagpur' == loan_application_proof_object['requested_proof']['self_attested_attrs']['attr6_referent']
    assert '2010' == loan_application_proof_object['requested_proof']['self_attested_attrs']['attr8_referent']

    assert await anoncreds.verifier_verify_proof(cbdc['loan_application_proof_request'], cbdc['loan_application_proof'],
                                                 cbdc['schemas_for_loan_application'],
                                                 cbdc['cred_defs_for_loan_application'],
                                                 cbdc['revoc_ref_defs_for_loan_application'],
                                                 cbdc['revoc_regs_for_loan_application'])


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
