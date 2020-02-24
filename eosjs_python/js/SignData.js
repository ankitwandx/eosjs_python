ecc = require('eosjs-ecc-eva');

const raw_data = process.argv[2];
const wif = process.argv[3];


function sign_data(raw_data, wif){
        try {
                let data = ecc.sign(raw_data, wif)
                console.log(data);
        } catch(error) {
      		console.error(error);
      		process.exit(1);
    	}
}
sign_data(raw_data, wif);

