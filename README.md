# cypherbabies
DApp created at ETH Waterloo2 using Proxy Reencryption and NFTs for a fictitious Donation of Human Eggs Program

Cypherbabies is a DApp aplication to empower women to take control of their digital data related to health and human egg donation.

The App uses non-fungible tokens as examples of smart contracts that save unique information about an Egg Donation program. Each non-fungible token representing a uEggie with its unique characteristics.

Because of the complexities of an egg donation program include many confidentiality agreements, legal documentation, payments, and physical, mental, and genetic examinations, this data should be protected by strong encryption technologies.

The App intends to apply nuCypher's TPRE (Threshold Proxy Re-Encryption) scheme to re-encrypt the medical data using the Umbral Network and dividing the encryption keys in fragments among the network participants. Data could only be accessed by "Bob" once he recovers the encryption keys from the network.  Data is divided in k fragments into N participants. Using Shamir Secret Sharing scheme, data is recovered if the majority (M) of the N participants is recovered. 

The encryptor character, represented at nuCypher's network as Enrico, has no access to the data, only to cyphertext produced by "GisAlice". GisAlice is the character that grants and revokes access to the encryption policy. She encrypts the medical data FOR the policy key and not for Bob's public key. She can specify one Bob, or many Bobs in the policy. GisAlice encrypts her message (or in our case, a PDF file containing blood cholesterol examinations) for the policy public key, not for Bob. Bob can retrieve the policy with his public key and then decrypt the message (or data PDF file) and access it.

The App will use IPFS to store the health data in decentralized nodes, so that gisAlice doesn't need to be available and online at the moment Bob needs to access the data. (IPFS hash: 	
QmTLA69jDBQRP6QDa3qgQbyby1ExNx69bYbKb6rsrXvthE and Pinata API Key: 8d721abbafb07d336bd3) 
To access the file, please request juliana@itsencrypted.com for the password mentioning Eth Waterloo 2 on your email.

uEggies are the actual non-fungible tokens that were deployed on Görli testnet for this project. They were part of gisAlice's ficticious 3rd round of Egg Donations, and in the CypherBabies Program she was able to collect 33 human eggs. They are gisAlice's property (hereby represented as _donor variable) and can be accessible on Görli Network under the following Smart Contract Addresses:

uEggie #25
0x55Da75AFb321aE47F5429feC110D14476799c981

uEggie #26
0x4d7c5Ad3bD2e56f6EcFe847fA6df9F0D83937011

uEggie #27
0xA5Bf4Be0b1707B24CB1844DCCF28Bc4981455973

uEggie #28
0xf0e9dE6DC4176190E06E678C6e34e07911c41b7B

uEggie #29
0xf13Ed788c5De83522E69e6A120ae88707EAE7922

uEggie #30
0x84Ffd7BAB6CE48Ad9088d3290f52f0F6842606D9

uEggie #31
0x41f3FbFe45d3d86C80cdE0f5c49897B7e5261e69

uEggie #32
0xAfb44393F9083900D8f7b9Fb1F5D6175ac985410

uEggie #33
0x804622a7fbBc1a11f66F8cb3D65c603556c29B78

Each uEggie was collected at the WaterlooFertilityClinic on 09.October.2019 between 17:50-17:59 (each one collected in a different minute of time) and each one is part of gisAlice's 3rd Round of Donations.

The Visual representation of the cypherbabies App and NFT Wallet can be seen using the prototype Adobe XD aplication. The user has a human friendly interface, mostly in pastel colors, where user can also inform herself about the latest news and developments in human egg donation programs and relevant fertility news. 

Genetic Engineering is a promising field, and the dApp should be able to empower more women to have control of their health and mental data, and in this case, sensitive genetic information data. In the future, users could capitalize and sell the data to Universities and research centers globally without revealing their identities in a secure and reliable fashion. Pharmaceutical industries and Hospitals might be interested in buying the exams of anonymous users.
