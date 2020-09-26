ecc = require('eosjs-ecc-eva');

const signature = process.argv[2];
const raw_data = process.argv[3];
const public_key = process.argv[4];


function verify(signature, raw_data, public_key){
        try {
            // ecc.verify(signature, 'I am alive', pubkey)
            let data = ecc.verify(signature, raw_data, public_key)
            console.log(data);
        } catch(error) {
      		console.error(error);
      		process.exit(1);
    	}
}
verify(signature, raw_data, public_key);
