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
    logger.info("\"{}\" -> Create wallet".format(identity['name']))
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

async def run():

    pool_ = {
        'name': 'pool1'
    }
    logger.info("Open Pool Ledger: {}".format(pool_['name']))
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

    logger.info("==============================")
    logger.info("=== Credential Schemas Setup ==")
    logger.info("------------------------------")

    logger.info("\"Government\" -> Create \"Property-Details\" Schema")

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

    logger.info("\"Government\" -> Send \"Property-Details\" Schema to Ledger")
    schema_request = await ledger.build_schema_request(government['did'], government['property_details_schema'])
    await ledger.sign_and_submit_request(government['pool'], government['wallet'], government['did'], schema_request)

    logger.info("\"Government\" -> Create \"Bonafide-Student\" Schema")

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

    logger.info("\"Government\" -> Send \"Bonafide-Student\" Schema to Ledger")
    schema_request = await ledger.build_schema_request(government['did'], government['bonafide_student_schema'])
    await ledger.sign_and_submit_request(government['pool'], government['wallet'], government['did'], schema_request)

    time.sleep(1)

    logger.info("==============================")
    logger.info("=== Government Property Details Definition Setup ==")
    logger.info("------------------------------")

    logger.info("\"Government\" -> Get \"Property Details\" Schema from Ledger")
    get_schema_request = await ledger.build_get_schema_request(government['did'], property_details_schema_id)
    get_schema_response = await ensure_previous_request_applied(
        government['pool'], get_schema_request, lambda response: response['result']['data'] is not None) 
    (government['property_details'], government['property_details_schema']) = \
        await ledger.parse_get_schema_response(get_schema_response)

    logger.info("\"Government\" -> Create and store in Wallet \"Property Details\" Credential Definition")
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

    logger.info("\"Government\" -> Send  \"Property Details\" Credential Definition to Ledger")
    cred_def_request = await ledger.build_cred_def_request(government['did'], government['property_details_def'])
    await ledger.sign_and_submit_request(government['pool'], government['wallet'], government['did'], cred_def_request)

    logger.info("\"NAA\" -> Get \"Bonafide Student\" Schema from Ledger")
    get_schema_request = await ledger.build_get_schema_request(naa['did'], bonafide_student_schema_id)
    get_schema_response = await ensure_previous_request_applied(
        naa['pool'], get_schema_request, lambda response: response['result']['data'] is not None) 
    (naa['bonafide_student'], naa['bonafide_student_schema']) = \
        await ledger.parse_get_schema_response(get_schema_response)

    logger.info("\"NAA\" -> Create and store in Wallet \"Bonafide Student\" Credential Definition")
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

    logger.info("\"NAA\" -> Send  \"Bonafide Student\" Credential Definition to Ledger")
    cred_def_request = await ledger.build_cred_def_request(naa['did'], naa['bonafide_student_def'])
    await ledger.sign_and_submit_request(naa['pool'], naa['wallet'], naa['did'], cred_def_request)
    
    logger.info("==============================")
    logger.info("=== Getting Bonafide Student certificate from NAA ===")
    logger.info("------------------------------")
    
    logger.info("== Rajesh setup ==")
    logger.info("------------------------------")

    Rajesh = {
        'name': 'Rajesh',
        'wallet_config': json.dumps({'id': 'Rajesh_wallet'}),
        'wallet_credentials': json.dumps({'key': 'Rajesh_wallet_key'}),
        'pool': pool_['handle'],
    }
    await create_wallet(Rajesh)
    (Rajesh['did'], Rajesh['key']) = await did.create_and_store_my_did(Rajesh['wallet'], "{}")

    # NAA creates bonafide certificate offer

    logger.info("\"NAA\" -> Create \"bonafide\" certificate Offer for Rajesh")
    naa['bonafide_student_offer'] = \
        await anoncreds.issuer_create_credential_offer(naa['wallet'], naa['bonafide_student_def_id'])

    logger.info("\"NAA\" -> Send \"bonafide\" certificate Offer to Rajesh")
    
    # Over Network 
    Rajesh['bonafide_student_offer'] = naa['bonafide_student_offer']

    print(Rajesh['bonafide_student_offer'])

     # Rajesh prepares a bonafide certificate request

    bonafide_student_offer_object = json.loads(Rajesh['bonafide_student_offer'])

    Rajesh['bonafide_student_schema_id'] = bonafide_student_offer_object['schema_id']
    Rajesh['bonafide_student_def_id'] = bonafide_student_offer_object['cred_def_id']

    logger.info("\"Rajesh\" -> Create and store \"Rajesh\" Master Secret in Wallet")
    Rajesh['master_secret_id'] = await anoncreds.prover_create_master_secret(Rajesh['wallet'], None)

    logger.info("\"Rajesh\" -> Get \"naa Transcript\" Credential Definition from Ledger")
    (Rajesh['naa_bonafide_student_def_id'], Rajesh['naa_bonafide_student_def']) = \
        await get_cred_def(Rajesh['pool'], Rajesh['did'], Rajesh['naa_bonafide_student_def_id'])

    logger.info("\"Rajesh\" -> Create \"bonafide\" certificate Request for naa")
    (Rajesh['bonafide_student_request'], Rajesh['bonafide_student_request_metadata']) = \
        await anoncreds.prover_create_credential_req(Rajesh['wallet'], Rajesh['did'],
                                                     Rajesh['bonafide_student_offer'],
                                                     Rajesh['naa_bonafide_student_def'],
                                                     Rajesh['master_secret_id'])

    print("\"Rajesh\" -> Send \"bonafide\" certificate Request to naa")

    # Over Network
    naa['bonafide_student_request'] = Rajesh['bonafide_student_request']

    # NAA issues credential to Rajesh ----------------
    print("\"NAA\" -> Create \"bonafide\" certificate for Rajesh")
    # can use any type of encoding scheme according to documentation
    naa['Rajesh_bonafide_student_values'] = json.dumps({
        "first_name": {"raw": "Rajesh", "encoded": "1139481716457488690172217916278103335"},
        "last_name": {"raw": "Kumar", "encoded": "5321642780241790123587902456789123452"},
        "degree_name": {"raw": "Pilot Training Programme", "encoded": "12434523576212321"},
        "student_since_year": {"raw": "2022", "encoded": "2022"},
        "cgpa": {"raw": "8", "encoded": "8"}
    })
    naa['bonafide_student_cred'], _, _ = \
        await anoncreds.issuer_create_credential(naa['wallet'], naa['bonafide_student_offer'],
                                                 naa['bonafide_student_request'],
                                                 naa['Rajesh_bonafide_student_values'], None, None)

    print("\"naa\" -> Send \"bonafide\" certificate to Rajesh")
    print(naa['bonafide_student'])
    # Over the network
    Rajesh['bonafide_student'] = naa['bonafide_student']

    print("\"Rajesh\" -> Store \"bonafide\" certificate from naa")
    _, Rajesh['bonafide_student_def'] = await get_cred_def(Rajesh['pool'], Rajesh['did'],
                                                         Rajesh['bonafide_student_def_id'])

    await anoncreds.prover_store_credential(Rajesh['wallet'], None, Rajesh['bonafide_student_request_metadata'],
                                            Rajesh['bonafide_student'], Rajesh['bonafide_student_def'], None)
    
    print("\n\n>>>>>>>>>>>>>>>>>>>>>>.\n\n", Rajesh['bonafide_student_def'])



    logger.info("==============================")
    logger.info("=== Getting 'PropertyDetails' credential from government===")
    logger.info("------------------------------")
    

    # Government creates PropertyDetails credential offer

    logger.info("\"Government\" -> Create \"PropertyDetails\" credential Offer for Rajesh")
    government['property_details_offer'] = \
        await anoncreds.issuer_create_credential_offer(government['wallet'], government['property_details_def_id'])

    logger.info("\"Government\" -> Send \"PropertyDetails\" credential Offer to Rajesh")
    
    # Over Network 
    Rajesh['property_details_offer'] = government['property_details_offer']

    print(Rajesh['property_details_offer'])

     # Rajesh prepares a property details request

    property_details_offer_object = json.loads(Rajesh['property_details_offer'])

    Rajesh['property_details_schema_id'] = property_details_offer_object['schema_id']
    Rajesh['property_details_def_id'] = property_details_offer_object['cred_def_id']

    logger.info("\"Rajesh\" -> Create and store \"Rajesh\" Master Secret in Wallet")
    Rajesh['master_secret_id'] = await anoncreds.prover_create_master_secret(Rajesh['wallet'], None)

    logger.info("\"Rajesh\" -> Get \"government PropertyDetails\" Credential Definition from Ledger")
    (Rajesh['government_property_details_def_id'], Rajesh['government_property_details_def']) = \
        await get_cred_def(Rajesh['pool'], Rajesh['did'], Rajesh['government_property_details_def_id'])

    logger.info("\"Rajesh\" -> Create \"PropertyDetails\" credential Request for government")
    (Rajesh['property_details_request'], Rajesh['property_details_request_metadata']) = \
        await anoncreds.prover_create_credential_req(Rajesh['wallet'], Rajesh['did'],
                                                     Rajesh['property_details_offer'],
                                                     Rajesh['government_property_details_def'],
                                                     Rajesh['master_secret_id'])

    print("\"Rajesh\" -> Send \"PropertyDetails\" credential Request to government")

    # Over Network
    government['property_details_request'] = Rajesh['property_details_request']

    # government issues credential to Rajesh ----------------
    print("\"Government\" -> Create \"PropertyDetails\" credential for Rajesh")
    # change this encoding. can use any type of encoding scheme according to documentation
    government['Rajesh_property_details_values'] = json.dumps({
        "first_name": {"raw": "Rajesh", "encoded": "1139481716457488690172217916278103335"},
        "last_name": {"raw": "Kumar", "encoded": "5321642780241790123587902456789123452"},
        "address_of_property": {"raw": "Malancha Road, Kharagpur", "encoded": "12434523576212321"},
        "property_value_estimate": {"raw": "2000000", "encoded": "2000000"},
        "residing_since_year": {"raw": "2010", "encoded": "2010"}
    })
    government['property_details_cred'], _, _ = \
        await anoncreds.issuer_create_credential(government['wallet'], government['property_details_offer'],
                                                 government['property_details_request'],
                                                 government['Rajesh_property_details_values'], None, None)

    print("\"government\" -> Send \"PropertyDetails\" credential to Rajesh")
    print(government['property_details'])
    # Over the network
    Rajesh['property_details'] = government['property_details']

    print("\"Rajesh\" -> Store \"PropertyDetails\" credential from government")
    _, Rajesh['property_details_def'] = await get_cred_def(Rajesh['pool'], Rajesh['did'],
                                                         Rajesh['property_details_def_id'])

    await anoncreds.prover_store_credential(Rajesh['wallet'], None, Rajesh['property_details_request_metadata'],
                                            Rajesh['property_details'], Rajesh['property_details_def'], None)
    
    print("\n\n>>>>>>>>>>>>>>>>>>>>>>.\n\n", Rajesh['property_details_def'])


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
