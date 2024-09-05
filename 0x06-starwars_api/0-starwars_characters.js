#!/usr/bin/node


const request = require('request');
const util = require('util');

if (process.argv[2] === undefined) {
  console.log('Usage: node <FILENAME> <id>');
} else {
  (async () => {
    const promis_req = util.promisify(request);
    const _url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
    const body = (await promis_req(_url)).body;
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      const character = (await promis_req(characters[i])).body;
      console.log(JSON.parse(character).name);
    }
  })();
}
