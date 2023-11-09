const crypto = require('crypto');
const readline = require('readline');

const chaveSecreta = '#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista';

//Metódo AES
function encryptAndDecryptWithAES(text, key) {
  const iv = crypto.randomBytes(16);
  const cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');

  const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
  let decrypted = decipher.update(encrypted, 'hex', 'utf8');
  decrypted += decipher.final('utf8');

  return { encrypted, decrypted };
}

//Metódo DES
function encryptAndDecryptWithDES(text, key) {
  const iv = crypto.randomBytes(8);
  const cipher = crypto.createCipheriv('des-ede3-cbc', key, iv);
  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');

  const decipher = crypto.createDecipheriv('des-ede3-cbc', key, iv);
  let decrypted = decipher.update(encrypted, 'hex', 'utf8');
  decrypted += decipher.final('utf8');

  return { encrypted, decrypted };
}

//Metódo Camellia
function encryptAndDecryptWithCamellia(text, key) {
  const iv = crypto.randomBytes(16);
  const cipher = crypto.createCipheriv('camellia-256-cfb', key, iv);
  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');

  const decipher = crypto.createDecipheriv('camellia-256-cfb', key, iv);
  let decrypted = decipher.update(encrypted, 'hex', 'utf8');
  decrypted += decipher.final('utf8');

  return { encrypted, decrypted };
}

const chaveAES = crypto.createHash('sha256').update(chaveSecreta).digest();
const chaveDES = Buffer.from(chaveSecreta.substring(0, 24));
const chaveCamellia = crypto.createHash('sha256').update(chaveSecreta).digest();

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question('Digite a primeira senha: ', (senha1) => {
  rl.question('Digite a segunda senha: ', (senha2) => {
    rl.question('Digite a terceira senha: ', (senha3) => {

      const aesResult = encryptAndDecryptWithAES(senha1, chaveAES);
      const desResult = encryptAndDecryptWithDES(senha2, chaveDES);
      const camelliaResult = encryptAndDecryptWithCamellia(senha3, chaveCamellia);

      console.log('AES - Senha Criptografada:', aesResult.encrypted);
      console.log('AES - Senha Descriptografada:', aesResult.decrypted);

      console.log('DES - Senha Criptografada:', desResult.encrypted);
      console.log('DES - Senha Descriptografada:', desResult.decrypted);

      console.log('Camellia - Senha Criptografada:', camelliaResult.encrypted);
      console.log('Camellia - Senha Descriptografada:', camelliaResult.decrypted);

      rl.close();
    });
  });
});