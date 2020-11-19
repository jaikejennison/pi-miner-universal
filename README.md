# pi-miner-universal
ARM 32/64 bit (v6/v8) build of geth for arm v6 &amp; arm v8 with run scripts and remote API support for Raspberry Pi Devices

## Configurations
In the `piminer_genesis.json` file
- change `"chainId": 0`
- change `"coinbase": "0x0000000000000000000000000000000000000000"`

For Raspberry Pi 4 devices running `buster 64` run
```bash
./piMiner64.sh
```
For Raspberry Pi 4 devices running `buster 32` or for Raspberry Pi 1,2 &amp; 3 devices run
```bash
./piMiner32.sh
```

## License
The go-ethereum library (i.e. all code outside of the `bin` &amp; `bin64` directories) is licensed under the
[GNU Lesser General Public License v3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html).
The go-ethereum binaries (i.e. all code outside of the `bin` &amp; `bin64` directories) is licensed under the
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

### Special Thank You
The [Go Ethereum](https://github.com/ethereum/go-ethereum) Team!
