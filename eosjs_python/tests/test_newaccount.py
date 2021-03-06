from eosjs_python import Eos

eos = Eos({
	'http_address': 'http://localhost:8888',
	'key_provider': '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3'
})

test = eos.newaccount({
	'creator': 'eosio',
	'name': 'mytestacc14',
	'owner_public_key': 'EOS7aJDVdDjcpjAXS53sFoVMHQJdFTMhaS3mThnXE3okFEtvxmQov',
	'active_public_key': 'EOS7aJDVdDjcpjAXS53sFoVMHQJdFTMhaS3mThnXE3okFEtvxmQov',
	'buyrambytes_bytes': 8192,
	'delegatebw_stake_net_quantity': '100.0000 SYS',
	'delegatebw_stake_cpu_quantity': '100.0000 SYS',
	'delegatebw_transfer': 0
})

print(test)
