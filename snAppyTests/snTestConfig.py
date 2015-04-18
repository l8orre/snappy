#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" this is a configuration repo. this is th eplace where as much as possible of the configuration data is supposed
to be placed in order to NOT hardcode it into the code.
 """#


LISTEN_PORT_SNT = 7800 #


environ = {}
# Note: this dict has currently four levels of nesting.
# The top level contains immediate configuraiton informatin for launching the app,
#
# It also contains UC_schedules that contain info for timer driven looping calls.
# These Have three nesting levels to accommodate flexibility in UC design.
#
# This dict can also contain informatin on XML data sources.
# It can be extended t use an sqlite db later.

##################################################################
#
# SuperNET configuration

STONEFISH_IP = '178.62.185.131'
BOXFISH_IP   = 'localhost'

SNET_port = '7777'
SNET_url = 'http://' + STONEFISH_IP + ":" + SNET_port
#SNET_url = 'http://' + BOXFISH_IP + ":" + SNET_port

#SERVER_ADDR_jl777 = BOXFISH_IP
#SERVER_ADDR_jl777 =  STONEFISH_IP

SERVER_PORT_SUPERNETHTTP = 7777 # http  14632 twisted wants int

SCHEME = 'http://'
#FULL_URL = SCHEME + SERVER_ADDR_jl777 + ":" + str(SERVER_PORT_SUPERNETHTTP)
POSTHEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


##################################################################
#
# BitcoinDarkd configuration

SERVER_PORT_BTCD_RPC = 14632    # going thorugh BTCT RPC
BitcoinDarkRPCCreds = {'user' : 'azure', 'rpcPw' : 'Ir9qDmicntTxH8C'}
environ['BitcoinDarkRPCCreds'] = BitcoinDarkRPCCreds


###################################################################
#
#
#
# The top environ {dict} contains all configuration information.
# 
#  environ['whatIsNeeded'] = 'whatIsNeeded'
#
#


CACHE_DIR = '/localCache/' # use dedicated install subdir later

environ['CACHE_DIR'] = CACHE_DIR
environ['CACHE_FILENAMES'] = {
                                'soccer_schedule' : 'soccer_schedule.xml',\
                                'other_schedule' : 'other_schedule.xml',\
                                'more' : 'more.csv'
                                }

###################################################################



NXTASSETS = [
    {
        "name": "1000BURST",
        "asset": "251006016744564741",
        "description": "Each one 1000BURST asset represents 1000 (one thousand) BURST coins. To obtain these assets just send your BURST coins to the BURTS Gateaway address BURST-MCHC-LBKK-ZLZY-C3XL5 _and_ send an Arbitrary Message containing your NXT address (in alpha-numeric format) to the same address. To withdraw your 1000BURST assets you should transfer them to this issuing account (NXT-VVTV-U25N-U2FY-2V35H) _and_ in the attached message place your BURST address (in alpha-numeric format). More info can be found here: https://bitcointalk.org/index.php?topic=731923.msg8381305#msg8381305"
    },
    {
        "name": "1000FIM",
        "asset": "12404894802398759379",
        "description": "Each 1000FIM asset represents 1000 FIM coins. To obtain these assets send your FIM coins to FIM-SESR-CDCR-F86V-A2ABQ _and_ send an Arbitrary Message containing your NXT address (in Reed Solomon format) to the same address (FIM-SESR-CDCR-F86V-A2ABQ). In order to guarantee smooth withdrawals, the amount of the 1000FIM assets in circulation will always be less then the balance of FIM-SESR-CDCR-F86V-A2ABQ. To withdraw your 1000FIM assets transfer them to NXT-M667-6GVL-3JNZ-GRN96 _and_ in the attached message place your FIM address (in Reed Solomon format). More info can be found here: https://bitcointalk.org/index.php?topic=633304.msg8097620#msg8097620"
    },
    {
        "name": "ATOMIC",
        "asset": "11694807213441909013",
        "description": "Atomic is a NXTventure project with the official thread at https://bitcointalk.org/index.php?topic=780833.msg8800442#msg8800442"
    },
    {
        "name": "AutoDiv",
        "asset": "1434237137246193127",
        "description": "A steady stream of automatic dividends paid daily. Details here: http://tiny.cc/91oisx"
    },
    {
        "name": "AutoDiv3",
        "asset": "6924643464789677166",
        "description": "AutoDiv3 is a weekly income fund. Objective (3.0%-6.5%) Details here: http://tiny.cc/91oisx"
    },
    {
        "name": "BGCAFFE",
        "asset": "2978798152942226372",
        "description": "The first Buongiorno Caffe opened November 2013 in Pretoria, South Africa. We are committed to providing high quality food for our customers in a \r\nsustainable way, doing our best to improve both their well-being and the planet we all live on. Part of this journey is sourcing the best possible ingredients from local producers, ensuring our staff are part of the business and benefit from their energy and creativity and most importantly building a better community.\r\n\r\nWe would love you all to become part of our community and listing on NextCoin AE is the first step in that direction. Lets take this exciting step together and see where our journey takes us :)\r\n\r\nPlease see Buongiorno Caffe's website for more detail: http://www.buongiorno-caffe.co.za\r\n\r\nSPECIAL THANKS!\r\nThe team at Buongiorno Caffe would like to send a heartfelt thanks to the NextCoin developers and community for working so hard to bring the amazing possibilities of crypto currencies into the hands of the people!"
    },
    {
        "name": "BearMining",
        "asset": "16866116529232450550",
        "description": "No-fee direct mining asset. Please see our discussion thread on the forums for more information."
    },
    {
        "name": "Bithaus",
        "asset": "13926712251908664867",
        "description": "Each asset represents .0001% of bithaus profits. As profits from bithaus come in, they will be distributed to asset holders. please refer to bithaus themselves for info on their business.\r\nThere are a total of 40% bithaus profit assets issued for a total of 400000, but most are parked in the Parkinglot account 6917879084634468097\r\nThe only bithaus assets that are released from the parkinglot acct are the ones bound to actual bithaus profit shares. Initially it will be comprised of my personal 1.8% (18000) and also some of aldrin's shares. contact jl777 if you want to bind your bithaus profit sharing with this bithaus asset"
    },
    {
        "name": "CBOOKING",
        "asset": "13159456840724391314",
        "description": "CoinBooking.net - Vacation Rental Listings platform | List your property for cryptocurrency. This project is developed by CoinEvolve.com. Note that this project is separated from SuperNET Partnerhip. This project does not share profit with SuperNET"
    },
    {
        "name": "CELL",
        "asset": "18212211773827322818",
        "description": "https://asset.cryptomining.farm"
    },
    {
        "name": "CNTROPOLIS",
        "asset": "17321741837176104160",
        "description": "ConnectTropolis by CoinTropolis is the combination of 4 different services that not only grow our exposure to all 300+ coin communities, but help us work with businesses that could use guidance in marketing, project management or business development.This will also allow us to showcase how Nxt can become the basis for a stable and relevant platform from which to build upon.\r\n\r\nConnectTropolis virtual token holders will be rewarded a percentage based on the number of tokens held. The reward pool will consist of 50% of the coins earned by the ConnectTropolis services outlined in detail in the links below.\r\n\r\nDetails about virtual tokens:\r\nhttps://nxtforum.org/assets-board/official-cointropolis-launch-1pm-today-us-eastern/\r\n\r\nAbout CoinTropolis:\r\nhttp://www.cointropolis.com/"
    },
    {
        "name": "CoinoUSD",
        "asset": "12982485703607823902",
        "description": "CoinoUSD is a non-dividend paying asset tied to US dollar, one CoinoUSD equals one dollar. In- and out-exchange of it is carried out at Coinomat.com. The objective of CoinoUSD is to create NXT/USD market directly on NXT asset exchange. Besides, it allows for value transfer in USD on NXT blockchain."
    },
    {
        "name": "Coinomat",
        "asset": "6220108297598959542",
        "description": "Coinomat.com is an instant cryptocurrency exchange service. Coinomat.com seeks external funding through virtual IPO to enhance its operating capital and implement several new services aimed at transaction volume and revenue growth.   IPO is carried out at several platforms, including NXT platform. Our mission consists in offering frictionless customer experience in the area of cryptocurrency transactions. Our business model is built on offering fixed rate services for cryptocurrency exchanges and charging premium for the transaction speed and comfort. Our competitive advantage is the current lack of similar services and our clear profit structure, based on hedging cryptocurrency volatility effects. \r\n\r\nCoinomat.com offers its shareholders profits equal to 1.5% of the total transaction amount. Users can have access to our transactions stats here: http://coinomat.com/globalstat.php\r\n\r\nThe dividend payments are made weekly."
    },
    {
        "name": "Coinomat1",
        "asset": "7474435909229872610",
        "description": "This is the secondary offering of Coinomat asset. \r\nCoinomat.com is an instant cryptocurrency exchange service. in July of 2014 NXT cryptocurrency transactions have been integrated in Coinomat.com services, including NXT withdrawals to bank cards.\r\n\r\nTotal volume of the initial and secondary IPO is equal to 7000000 NXT.\r\nCoinomat.com offers its shareholders profit equal to 1.5% of the total transaction amount. Users can have access to our transactions stats here: http://coinomat.com/globalstat.php. The dividend payments are made weekly on Mondays."
    },
    {
        "name": "ColdHash",
        "asset": "11632121299907478243",
        "description": "Diversified cloud mining asset. Details at https://nxtforum.org/asset-exchange-general/(ann)-coldhash/"
    },
    {
        "name": "DORCS",
        "asset": "2318361924203311027",
        "description": "1. DORCS ASSETS are bearer assets issued via a digitally signed certificate\r\non the NXT AE.\r\n2. The issuer maintains no records of who owns the assets.\r\n3. Ownership is transferred by transferring the digital certificate\r\nrepresenting a particular asset.\r\n4. Whoever can demonstrate ownership of the private-key securing the\r\ncertificate is presumed to own the asset.\r\nFor a more detailed description of the Asset, please refer to http://www.dorcsgames.com/nxtaedescription/"
    },
    {
        "name": "DeBuNe",
        "asset": "6926770479287491943",
        "description": "DeBuNe, the Decentrilised Business Network, combines the power of Nxt blockchain and powerful software frameworks to a modular, agile, worldwide business network beneficial to both members and clients. Some non core DeBuNe functionalities (centralised in external websites) will require a fee to be used. Dividends will be paid starting July 2015. Info on http://debune.org"
    },
    {
        "name": "DroneMine",
        "asset": "4087414277501042216",
        "description": "Create drones to mine raw materials from Earth, Ocean & Space. An interactive online overlay environment will be created to allow the drones to be directed by users and interact with the real world.Concept: Interface environ to interact with drones by site users.Drones will be developed to function in a sandbox environment during the alpha. Release C&C centers, Manufacturing Facilities and Material Drop-off point locations. % of raw material sales will be kept as a fee for providing the Drop-off points. Dividends will be paid out to all shareholders after each sale. Shareholders will have voting rights in the company. No other shares will be created unless voted and approved by the majority of shareholders using the voting system in the DAC. Goal is to create a DAC in the NXT ecosystem. Each share of DroneMine represents of 1/1,000,000th of 30% of yearly profits to be paid out as dividends. Initial IPO funds will be used for liquidity.Profit Split: 30% R&D/40% reinvest/30% dividends"
    },
    {
        "name": "EVOLVE",
        "asset": "3574526501061878636",
        "description": "http://coinevolve.com - A group of developers working full time on developing various services for cryptocurrency. We aim to make your cryptocurrency a bit more useful and generate some profit in the same time"
    },
    {
        "name": "EVOLVE2",
        "asset": "3643966800021258206",
        "description": "EVOLVE Shares for latecomers - http://coinevolve.com - A group of developers working full time on developing various services for cryptocurrency. We aim to make your cryptocurrency a bit more useful and generate some profit in the same time"
    },
    {
        "name": "FIMventure",
        "asset": "8501115346481349929",
        "description": "FIMventure makes private investments in promising enterprises and adds value to each investment. FIMventure forging and trading FIM (fork NXT). FIMventure will pay 3-5% monthly dividends in the assets or NXT it acquires, net of trading activities during the all period. Send Message NXT-USCH-VC7D-4EX3-272SG if you are seeking investment."
    },
    {
        "name": "ForgeCoin",
        "asset": "5934798443252900551",
        "description": "Mine with cheap electricity! \r\nTotal 175 Slots at this phase. 145 Slots (83%) selling at IPO.\r\nEach Asset (Slot) is a 180 GH/s S1 AntMiner in a country with about $0.01/KWh.\r\nROI is about 4 Months from IPO Date. Dividends will pay Weekly. \r\nYou can pay or receive dividends in BTC or NXT.\r\nMore info: http://forgeco.in"
    },
    {
        "name": "FreeMarket",
        "asset": "134138275353332190",
        "description": "FreeMarket is a decentralized marketplace that supports physical items for an initial fixed listing cost of 7.77 NXT. Please check the official website http://nxtfreemarket.com and the official thread https://nxtforum.org/index.php?topic=5408.0 for any changes and updates. A 20% revenue sharing agreement with SuperNET allows for 80% of the listing fees to be distributed as dividends."
    },
    {
        "name": "Freebsrvrs",
        "asset": "784050511394255426",
        "description": "Freebieservers is hereby issuing 1 million shares for 5 percent profit shares of freebieservers.com's net profit. Dividends will be paid out on the 15th of every month , 6 months from now. With a clientele that spans across the globe, Freebie Servers is one of the hottest start-ups to be involved in the Nxt Ecosystem. \r\n\r\n\r\nRead more at : https://nxtforum.org/asset-exchange-general/freebieservers-com-75-000-users-and-growing!/"
    },
    {
        "name": "FunBotReve",
        "asset": "3930224606324455741",
        "description": "This asset will receive 30% of all profits generated through the FunBotV1 project asset: 502090591603781088. More details can be found here: https://nxtforum.org/index.php?topic=5638.0"
    },
    {
        "name": "FunBotV1",
        "asset": "502090591603781088",
        "description": "This is the official FunBotV1 asset. An automated trading bot is used to generate profits, that are distributed as dividends. More details can be found here: https://nxtforum.org/index.php?topic=5638.0"
    },
    {
        "name": "HRLTCGear",
        "asset": "10890135065820123998",
        "description": "Hashrate.org LTCGear Shares\r\nPlease see: http://tinyurl.com/HRLTCGear for asset information."
    },
    {
        "name": "HRNXTPool",
        "asset": "17166680677145186899",
        "description": "Each asset represents .001% fractional ownership of the private Hashrate.org NXT mining pool. Up to date details can be found at http://tiny.cc/9m1yix"
    },
    {
        "name": "InstantDEX",
        "asset": "15344649963748848799",
        "description": "There are a total of 1 million InstantDEX assets. The goal of InstantDEX is to offer realtime trading of NXT, NXT assets and other cryptos. It will earn fees from commissions on the trades. By keeping costs low by using a decentralized infrastructure, it is expected to be able to distribute approximately half of revenues to asset holders.\r\n\r\nplease refer to nxtforum.org for up to date details"
    },
    {
        "name": "Jinn",
        "asset": "3061160746493230502",
        "description": "www.jinnlabs.com"
    },
    {
        "name": "KPS",
        "asset": "10941619155761914846",
        "description": "Kongzi Print Shop"
    },
    {
        "name": "LAND",
        "asset": "11225580336549701867",
        "description": "Borzalom ! Virtual world turns into reality.\r\nThis is an area developer game.\r\nA total of 33 million shares are released.\r\nA LAND asset is equal to 1 x 1 cm of real land area.\nBefore purchasing read the terms and conditions and up to date details located at borzalom.hu"
    },
    {
        "name": "LIQUID",
        "asset": "4630752101777892988",
        "description": "Liquid Technologies implements custom software solutions for trading cryptocurrency markets.  Please see http://www.liquidtech.info for more details. LIQUID ASSETS are bearer assets issued via a digitally signed certificate on the NXT AE. The issuer maintains no records of who owns the assets. Ownership is transferred by transferring the digital certificate representing a particular asset. Whoever can demonstrate ownership of the private-key securing the certificate is presumed to own the asset."
    },
    {
        "name": "LOVE",
        "asset": "12358227497921853690",
        "description": "Love is one of the first and best virtual goods ever! Spend it generously with your loved ones. Love is specifically not for getting rich. It's for spreading, baby! Love is available in huge quantities but still you need to search for it. If you find it you will be amazed by its value."
    },
    {
        "name": "LTCshare2G",
        "asset": "2128300325778905751",
        "description": "LTCshare2G provides affordable, reliable Scrypt cloud mining and will INCREASE payouts and hashrate over time. Initial hashrate is 2 GH/s mining LTC. 35% of profits will be re-invested to increase hashrate and 65% will be paid out in dividends weekly. This gives the majority of income back to investors for fast ROI and increases hashrate faster than the projected difficulty increase of LTC. This ratio could be adjusted by majority vote. 0.1 MH/s per share at launch, increasing each week. Please see https://nxtforum.org/asset-exchange-general/ann-ltcshares/ for more information and weekly profitability/dividend reports."
    },
    {
        "name": "MGW",
        "asset": "10524562908394749924",
        "description": "each MGW asset represents .0001% of multigateway\r\nmultigateway will generate minimal fees from deposits and withdraws of cryptos into NXT AE. It uses a separate multisig acct for each depositor. It will have ongoing server costs and to minimize the cost of depositing and withdrawing crypto assets into NXT, it will keep fees as low as possible. Currently its projected revenue source will be via auctions for listing altcoins and altcoin giveaways. Such revenues received net of operating costs will be distributed to asset holders.\r\nmultigateway isnt a non-profit, but it also isnt designed to be a massive profit generator. Any investment in multigateway will help cover operating costs and help the NXT community."
    },
    {
        "name": "MIC",
        "asset": "4469670021276890463",
        "description": "The most interesting coin in the world"
    },
    {
        "name": "MMNXT",
        "asset": "979292558519844732",
        "description": "Market-making fund for NXT AE: https://nxtforum.org/assets-board/mmnxt-market-making-and-arbitrage-fund-for-nxt-ae/"
    },
    {
        "name": "NEMstake",
        "asset": "12465186738101000735",
        "description": "A NEMstake token represents one million NEM receivable after the official launch of NEM blockchain. The token can be traded down to one digit after zero (minimum unit is 1/10 of a token). Our website is www.ournem.com. Please read about NEM, NEMstake token and the conversion rules in our dedicated thread before buying NEMstake. The issuing account is NXT-J62B-CNAR-34YW-4RCFN."
    },
    {
        "name": "NHZ",
        "asset": "3733170523104676119",
        "description": "This is the (first) official NHZ ( http://nhzcrypto.org ) Asset. \r\n\r\nNHZ is a fork of NXT. The NHZ blockchain started on 03-22-2014. It has the same parameters as NXT and follows NXT releases after a small delay. Our own features will be added over time. \r\n\r\nNHZ is distributed by a bounty system. The current distribution state can be seen on the block explorer. If you want to earn NHZ, take a look at the bounties on our forum. You can of course also come with your own ideas how you could be useful for NHZ.\r\n\r\nWe don't expect all NHZ to end up here, so there are only 100M units of the asset, each worth 1 NHZ.\r\nTo withdraw, send your assets to NXT-S7CP-4FZC-5T8B-H7UPF and add your numeric NHZ account ID - and nothing else! - to the comment field.\r\nFor deposits and further information about the asset as well as the current fee go to http://asx.nhzcrypto.org \r\n\r\nAlways check the issuer and asset ID! Be sure not to buy assets from copycats! The asset issuer account will never sell assets!"
    },
    {
        "name": "NNG",
        "asset": "1013693125509851736",
        "description": "NNG (NewNxtGames) develops browser games on top of Nxt. For more information visit www.NewNxtGames.com or contact NewNxtGames on NXTforum.org."
    },
    {
        "name": "NSC",
        "asset": "6775372232354238105",
        "description": "[NSC]\r\nNXT Security Coin:\r\nNSC is created to help securing the network by adding more value to forging fees. NSC is distributed weekly to every Block Generator. Payout is 1 NSC for every forged block by an accout ID. Every account ID have a cap of x NSC per 1440 Blocks, Public Forging Pools don't have a cap! The future value of this first tradeable AE-Coin depends on the community, the more value the more forgers secure the network. The Asset Holder will only sell NSC to cover the Asset transfer fees. To all stake holders, please help to give this Coin a value, thank you! The start value should be around 0.10 EUR. More information on https://nxtforum.org"
    },
    {
        "name": "NXTCS",
        "asset": "12658817572699179955",
        "description": "NXTCS is a callback service for developers. We will watch your account and call your defined URLs at specific events like receiving payments. You get all infos for processing in a JSON posted to your script. More details at: https://nxtforum.org/index.php?topic=6982.0"
    },
    {
        "name": "NXTInspect",
        "asset": "14273984620270850703",
        "description": "This asset is represents the right to a share in the profits from the activities of NXTinspect, you can find more information about it here https://nxtforum.org/index.php?topic=5655.msg109465#msg109465"
    },
    {
        "name": "NXTMINING",
        "asset": "15953898000415537360",
        "description": "Only 18250 virtual tokens issued. Each virtual token corresponds to a value equivalent to a qasic share on ltcgear.com. “NXTMINING\" tokens are redeemable for actual qasic shares on the site. just message me here https://nxtforum.org/index.php?action=profile;area=summary;u=2333. These shares will be sold at 25 NXT each until they are all sold out. Lowest fees on the asset exchange! \"NXTMINING\" tokens are not stocks, bonds or any other kind of financial instrument or security. Investors are expected to perform due diligence."
    },
    {
        "name": "NXTautoDAC",
        "asset": "14347250558295845059",
        "description": "NXTautoDAC assets represent .0001% of revenues from the family of autoDACs that bluemeanie1 and his team will create. NXTventure has made a private investment and assetized 75% of revenues. Development costs will be funded by the remaining 25% of revenues.\r\n\r\nOnce deployed the automatic Digital Autonomous Corporations will continue to operate in an open and transparent manner with transactions enforced by the NXT blockchain. Due to their automated nature the fees charged to people can be dramatically less than real world equivalents. The much lower fees are expected to entice enough people to try this new technology and thus increasing the customer base.\r\n\r\nThe ability to easily utilize autoDACs will be integrated into NXTservices and this will encourage adoption. While autoDAC's have a tremendous potential, it is still in its infancy and it is expected that it will take a while for people to become comfortable with using autoDACs\r\n\r\nPlease follow updates on the NXTventure section"
    },
    {
        "name": "NXTcoinsco",
        "asset": "17571711292785902558",
        "description": "There are a total of 1 million NXTcoinsco assets. NXTcoinsco will be creating coins that run on top of NXT, starting with nodecoin. After that it will make SVMcoin and also create a NXTcoins development kit to enable others to make coins easily.\r\nFor internally created coins, NXTcoinsco asset holders will receive 10% of the coins. The percentage for externally developed coins will vary.\r\n\r\nplease refer to nxtforum.org for up to date details"
    },
    {
        "name": "NXTmovie",
        "asset": "2240155853020376741",
        "description": "Loosely based on real life events, the NXT Film Project (nxtmovie.org) narrates the subversive and often vicious attacks that are conducted using technology. It further aims to educate and inform the masses about these new technologies.\r\n\r\nCurrent round is for pre-production on the NXT Film Project screenplay. All proceeds from the sale or licensing of said screenplay will be distributed to token holders at the time of sale. Token holders will also receive site advertising revenues, which will ensure an early source of ROI. Holders of 5% or more get access to contributors circle.\r\n\r\n*Added Perk*\r\nA substantial portion of the proceeds from the NXTmovie Project will go towards rewarding community member Cadence Jean Morton (aka CobaltSkky) as a form of reparation for the vicious harassment she received while confronting cyberbulling and cyberstalking in our community; this will show that the community rewards such members who stand against acts of cruelty and the invasion of our privacy."
    },
    {
        "name": "NXTprivacy",
        "asset": "17911762572811467637",
        "description": "NXTprivacy will contain various privacy related projects. It will hold significant percentages of several other privacy related assets, like Privatebet and NXTcard, and it will also create privacyServer software for server hosts to run. Any dividends NXTprivacy receives from assets it holds, will be redistributed to its assetholders on a prorata basis. The privacyServer software will provide services for customers that will allow server hosts to recoup some or all of their costs in maintaining a NXT node. Additionally, NXTprivacy will make a market in privateNXT. Please follow the nxtforum.org section on NXTprivacy for more information."
    },
    {
        "name": "NXTventure",
        "asset": "16212446818542881180",
        "description": "NXTventure makes private investments in promising enterprises and adds value to each investment by proactively integrating it into NXTservices to add a valuable new service for the NXTcommunity. \r\n\r\nNXTventure will pay monthly dividends in the assets it acquires, net of trading activities during the launch period. This means NXTventure asset will generate a stream of new assets as it launches them. contact jl777 if you are seeking investment"
    },
    {
        "name": "NeoDICE",
        "asset": "18184274154437352348",
        "description": "100% of the neoDICE revenues will be distributed to assetholders.\r\n\r\nNeoDICE revives the instantaneous gaming experience of the legendary SatoshiDice and brings it to NXT. The game is playable via any NXT client supporting asset transfer and does not require any additional software.\r\n\r\nNeoDice is a provably fair game relying on mathematically verifiable cryptographic hash calculations. To ensure the game's integrity the entire betting history is permanently stored on the NXT blockchain.\r\n\r\nMore info at http://neodice.com"
    },
    {
        "name": "NxtAT",
        "asset": "16365311175761675972",
        "description": "NxtAT (automated transaction) is a decentralised business that will provide AT solutions for clients wanting to gain the benefits of \"Turing complete\" transactions in the Nxt ecosystem without the complexity of having to understand every detail about how AT works"
    },
    {
        "name": "Nxttycoin",
        "asset": "18128686802152832026",
        "description": "The official cryptocurrency of the Nxt Mobile Applications Company.  \r\n\r\nOfficial newsfeed: https://twitter.com/cryptomessenger"
    },
    {
        "name": "OPALTKN",
        "asset": "5326942574002986149",
        "description": "OpalTKN represents a holding in the future earnings of opal products.  Learn more at http://www.opal-coin.com"
    },
    {
        "name": "ORA",
        "asset": "16194910134118257692",
        "description": "ORA is a leaderless, decentralised 'starfish' community software development project announced on May 22, 2014. 889 people initially registered between June 24 - July 8, 2014 for a FREE stake of 166,666 assets each. The remaining ORA assets were held in trust for later distribution to community members & future developers. ORA asset tokens are issued as bearer assets. Whoever controls the  private keys for an amount of ORA asset tokens will be eligible to redeem an equivalent amount of ORA 'coins' if/when the ORA software and P2P network is completed. The asset issuer is unable to guarantee either the completion of ORA software, or the exchange of ORA asset tokens into ORA coins. Please research the ORA project before purchasing ORA assets. The terms & conditions and date of the redemption will be finalised after community consultation. Total assets: 1,000,000,000. For more details : http://ora.to. Issuing account : NXT-7FPB-3K2S-M9FL-ARP4G"
    },
    {
        "name": "Pangea",
        "asset": "6883271355794806507",
        "description": "Pangea is SuperNET's decentralized poker that uses provably random numbers and will take advantage of the built in privacy features of SuperNET. 80% of revenues will be distributed to assetholders. 20% of revenues will go to marketing affiliates, with Privatebet handling the SuperNET players for Pangea.\r\n\r\nhttps://nxtforum.org/nxtventures/pangea-poker/ will have the latest information"
    },
    {
        "name": "Privatebet",
        "asset": "17083334802666450484",
        "description": "Privatebet will allow people to make bets directly with each other in a decentralized way. It will let people create their own personal bet with a designated arbiter in addition to automatically supporting a range of standard events with betting interest, like sports betting. Privatebet will only accept crypto and no personal information will be required from its customers. It will have a fee of 1% to begin with, subject to change to adapt to market forces. The goal is to automate as much of Privatebet as possible and it is expected to be able to payout about 80% of the fees it collects as dividends. Please follow the NXTforum for more detals and up to date information."
    },
    {
        "name": "RGDO",
        "asset": "17140378927644056619",
        "description": "HK Rigid Petroleum Chemical Group Limited was founded in 2003, the company set the lubricating oil research and development, sales, business wide coverage, Taiwan, Macao, Hongkong, the country, and exported to Japan, India, South Korea and other overseas areas. Fusion leading the world's outstanding enterprise management mode and China efficient kind spirit of service in a body, not only can let the customers use to lubricating material of high end, more be able to enjoy real first-class service. Over the years, we have been committed to the development of new products, long-term close cooperation with scientific research units of international NAC, Institute of petroleum, coal science research institute and other institutions. http://www.rigidlube.com"
    },
    {
        "name": "RSUnit",
        "asset": "14285820955872321553",
        "description": "RSUnit is the NXT asset that holds the place of RSU, allowing early trading of it, until the Beta release of the Reserve Share wallet. Reserve Share is a cryptocurrency, based on Proof of Reserve block generation method, having a Unique Source Code, which allows the users to keep their Units in reserve, by which they increase their Shares. For detailed information check our White Paper and official thread at Bitcointalk."
    },
    {
        "name": "SAAS",
        "asset": "14225517118742712534",
        "description": "Scrypt Asic Advanced Shares (SAAS) aims to correct 2 significant drawbacks of mining shares/contracts. 1) diminishing returns and 2) decreasing share value.  50% of revenue generated by SAAS will be re-invested to increasing Hash rate, the other 50% will go back to shareholders via dividend payouts.  As hash rates in SAAS increase so does your dividend and therefore your share value.  All funds generated by initial share offering go directly to purchasing more Hash rate.  As of September 1st the Pool owns 211 MH Scrypt.  First dividend payout is scheduled for Monday September 15th 2014 and every Monday after.  Regular updates on Twitter @SAASonNXTAE"
    },
    {
        "name": "STSH",
        "asset": "2504568464748765731",
        "description": "STSH is a crypto-currency diversified fund that aims to provide its shareholders above average steady dividends with minimal downside . \r\n\r\n3 income Sources:\r\n\r\nArbitrage Trading\r\nScrypt and SHA-256 Mining\r\nSolid Dividend paying Crypto-stocks\r\n\r\nThree rounds of assets listing on NXT AE\r\n1- 2500 Assets @ 10 NXT\r\n2- 5000 Assets @ 30 NXT\r\n3- 7500 Assets @ 50 NXT\r\nOur weekly guaranteed Dividend is .1 NXT per week for each NXT shareholder.\r\nPlease check our website for latest updates.\r\nwww.satosh1.com"
    },
    {
        "name": "SafeHash",
        "asset": "12699150877111554426",
        "description": "https://nxtforum.org/asset-exchange-general/safehash/"
    },
    {
        "name": "ShortNXT",
        "asset": "7297711024038530345",
        "description": "twitter.com/shortnxt\r\n\r\nProtect the value of your NXT holdings and hedge your transaction exposure. If NXT goes down, ShortNXT goes up (and vice versa).\r\n\r\nInitial Price: 100 NXT\r\n\r\nShortNXT aims to generate a daily percentage gain inverse to that of NXT. Issuer will support price target with buy and sell orders on the Asset Exchange.\r\n\r\nShortNXT Target Price equals the most recent ShortNXT Daily Reference Price minus the percentage change in NXT from the most recent NXT Daily Reference Price (in USD). ShortNXT Daily Reference Price is set daily at or around 10 am ET to current ShortNXT Target Price. NXT Daily Reference Price is a weighted average as reported at coinmarketcap.com or comparable substitute, at issuer's discretion, at or around 10 am ET.\r\n\r\nIssuer will maintain price support on a best effort basis and makes no assurances of timeliness or accurate calculation or reporting of involved prices.\r\n\r\nUpdates and reference price history at @shortnxt."
    },
    {
        "name": "Sianote",
        "asset": "11593659039925686857",
        "description": "Convertible to Siastock upon completion of Sia. 1 Sianote converts to 0.01% siastock. Only 1500 will be sold during pre-IPO."
    },
    {
        "name": "SkyNET",
        "asset": "6854596569382794790",
        "description": "SkyNET will develop decentralized AI technology using neural nets, SVM and other methods, combined with blockchain technology to create real world solutions that can be monetized. More details available at: https://nxtforum.org/index.php?topic=6826"
    },
    {
        "name": "SuperNET",
        "asset": "12071612744977229797",
        "description": "Official SuperNET asset, trading symbol on exchanges is UNITY \r\n\r\nOfficial BTT thread is https://bitcointalk.org/index.php?topic=762346.0 \r\n\r\nOfficial website http://supernet.org"
    },
    {
        "name": "SuperNETx2",
        "asset": "13502152099823770958",
        "description": "SuperNETx2 is backed 1:1 with SuperNET assets in NXT-7HAS-3W8H-BTDY-99BJE account. It will receive passthrough asset and revshare dividends that the SuperNET backing the x2 gets. Additionally it will receive an extra 5% revshare dividends, which doubles the revshare that x2 gets since there are 40803.05 x2 assets, which is 5% of SuperNET assets"
    },
    {
        "name": "Supercell",
        "asset": "15008504503343850630",
        "description": "Supercell Investments is a diverse investments venture offering multitudes of financial services and investment opportunities. Shares offered here are a total 10 Million shares; They represents 50% of Supercell Investments and entitles the owners to 50% of the revenue."
    },
    {
        "name": "TOKEN",
        "asset": "15641806960898178066",
        "description": "thesupernet.org Official SuperNET TOKEN, latest info at https://bitcointalk.org/index.php?topic=762346"
    },
    {
        "name": "TXTCoinNow",
        "asset": "17874206509705745796",
        "description": "What we offer:\r\n\r\n1) Safe and secure online storage of all your coins. Transfers of coins require phone call verification and PIN request.\r\n\r\n2) Simple SMS transfer system opens up mico-payments in local currencies using crypto-coins. Merchants create an account and can instantly start taking payments in any of our supported crypto-coins.\r\n www.txtcoinsnow.com"
    },
    {
        "name": "USDbitfnx",
        "asset": "10294386916428132892",
        "description": "Each 1 USDbitfnx asset represents 1 USD deposited at bitfinex.com . The USD deposited at bitfinex will be used to provide liquidity to margin traders that pay a fee for that service. This interest is paid daily into our account and is currently hovering at about 0.16% per day(~60% yearly return). This dividend will be distributed proportionally to USDbitfnx holders every two weeks. Details about fees, risks and how to deposit and withdraw, can be found in this thread on nxtforum.org: https://nxtforum.org/index.php?topic=3884.0"
    },
    {
        "name": "VULTMINING",
        "asset": "12419839393546948696",
        "description": "VULTMINING Labs."
    },
    {
        "name": "XDFB",
        "asset": "288267136544646747",
        "description": "Domains have been considered digital property for 2 decades now. Every business in the modern world needs it's own estate in cyberspace and that is exactly what domains are. In today’s world new businesses pop up all the time. Every second of every minute of every hour of every day: a new business starts it's journey. Some are good and some are bad, some fail and some succeed, but they all have one thing in common: they all need a domain name. \r\n \r\nDomains were the first assets of the internet, and with the ever rapid and enormous growth of both cryptocurrencies and the domain market, it is almost poetically natural for the two to be joined together. This is exactly what DotsforBits will do!\r\n \r\nCheck out the infographic and prospectus for all the details and FAQ!\r\n\r\nhttps://www.youtube.com/watch?v=_9JAK4TAUvE\r\n\r\nAsset Exchange - Ticker symbol - XDFB\r\n\r\nINFO : http://dotsforbits.com/DfB_VIPO.pdf"
    },
    {
        "name": "ach",
        "asset": "6789385243274909976",
        "description": "Altcoin Herald is a leading alternative cryptocurrency news website known for its’ well-balanced coverage. Our mission is to continue to offer high-quality coverage of cryptocurrency while growing our revenues and profits at a healthy rate. Each ACH purchased entitles the holder to 40% of our net revenues, as explained here. https://alth.co/rDPPI Dividends will be paid bi-weekly. 5000000 ACH are available for sale. Each ACH costs 1 NXT. Learn more here:"
    },
    {
        "name": "cryptocard",
        "asset": "7110939398145553585",
        "description": "NXTprivacy is proud to issue the cryptocard asset which will distribute 1% of processed transaction volumes to the assetholders. This card does not require any personal information. All of the processing and handling is outsourced to coinomat.com. Please check NXTprivacy.org for the latest details on fees and limits. Standard ATM fees will apply for cash withdrawals."
    },
    {
        "name": "cyberShare",
        "asset": "18349167062458849940",
        "description": "cyber•Shares are protoshares which create industry of Polymorphic Decentralised Applications. Official site: http://cybershares.net. Read http://paper.cybershares.net. Get involved http://cybertalks.org. Major news http://blog.cyber.fund. Created by http://cyber.fund. 1000000 cyber•Shares ever existed. Proof-of-Origin cybershares.net/explorer. In accordance with shareholders agreement 148158 cyber•Shares was placed on NXT AE burning 148158 cyber•Shares from Open Assets Protocol. cyber•Shares polymorphic blockchain - is the mailing list for sharedrops to community who build cyber•Shares technology. cyber•Shares is your share in all future industry of decentralized applications."
    },
    {
        "name": "fuzon",
        "asset": "5053136014193078855",
        "description": "A concoction of carefully selected cryptocurrencies which have been identified as long-term investments. Strong performing cryptocurrencies are being added continuously to the assets holdings. Perfect for investors who are looking for a well rounded investment with diversification. More information can be found at fuzon.io or follow @fuzonXFN on twitter."
    },
    {
        "name": "iHash",
        "asset": "9560963759586239947",
        "description": "iHash is a 0.2 GH/s Virtual Bitcoin Mining Bond valued at 10 NXT each. At the time of launch, Sep 3, 2014 iHash projected APR is more than 90%. With iHash you can start generating Bitcoin immediately. Your payout rate is pegged to Bitcoin Mining difficulty so there are no  downtimes, power failure or any other surprise expenses.\r\nDividends will be calculated every Friday 00:00 UTC and distributed at Friday 10:00 UTC.\r\nProof of solvency: We will accumulate 6 months future dividends on NXT AE. \r\nFor latest details please check our website <a href=\"http://ihash.biz”>iHash.biz</a>"
    },
    {
        "name": "jl777hodl",
        "asset": "6932037131189568014",
        "description": "This asset will not pay dividends. It will contain portions of almost all of the assets that I issue, the target percentage is 10%, but actual percentage will vary. Some issues will have more than 10%, some assets I wont be able to put here. Once the assets are in this account they will probably stay there long term, but occasional changes will be made at then current market prices. You can see current hodlings at 18323612891099439610 NXT-2AHU-UXZW-K9Q2-HENLW"
    },
    {
        "name": "ltc2nXt",
        "asset": "8670004015468655281",
        "description": "ltc2nxt.ihash.biz :: Each virtual token corresponds to a value equivalent to a qasic share on ltcgear.com. ltc2nXt tokens are not redeemable for actual qasic shares.\r\nltc2nXt tokens are not stocks, bonds or any other kind of financial instrument or security. Investors are expected to perform due diligence. For uptodate information please check the official website: http://ltc2nxt.ihash.biz/"
    },
    {
        "name": "ltc2nXt3",
        "asset": "7658325674657936242",
        "description": "http://ltc2nxt3.ihash.biz :: only 50,000 ltc2nXt3 virtual tokens issued. 100% of your initial NXT purchase is protected. 0% fees and 100% multiplication shares during 100% ROI period. “ltc2nXt3\" tokens are not redeemable for actual qasic shares. “ltc2nXt3\" tokens are not stocks, bonds or any other kind of financial instrument or security. Investors are expected to perform due diligence. For up-to-date information please check the official website: http://ltc2nxt3.ihash.biz"
    },
    {
        "name": "ltc2nxt2",
        "asset": "2388153394586381152",
        "description": "http://ltc2nXt.net :: only 18250 virtual tokens issued. Each virtual token corresponds to a value equivalent to a qasic share on ltcgear.com. “ltc2nXt2\" tokens are not redeemable for actual qasic shares. “ltc2nXt2\" tokens are not stocks, bonds or any other kind of financial instrument or security. Investors are expected to perform due diligence. For up-to-date information please check the official website: http://ltc2nxt.net/"
    },
    {
        "name": "mgwBTC",
        "asset": "17554243582654188572",
        "description": "Production Multigateway BTC (mgwBTC) is backed 100% by deposits in the custom multi-signature accounts generated for each user in the Multigateway production servers. Deposits made to the multi-signature accounts will automatically transfer the corresponding amount of mgwBTC assets to the associated NXT account. Withdraws are automatically processed serially only when all Multigateway servers are in agreement. The balances in the multi-signature accounts will change internally and do not represent the amount of BTC in your NXT account, the mgwBTC assets you own do. See https://multigateway.org for more information."
    },
    {
        "name": "mgwBTC",
        "asset": "4551058913252105307",
        "description": "multigateway BTC is backed 100% by deposits in the custom multisig accounts generated for each user. Deposits made to the multisig account will automatically transfer the corresponding amount of BTC assets to the associated NXT account. Withdraws are automatically processed serially only when all multigateway servers are in agreement. The balances in the multisig accounts will change and do not represent the amount of BTC in your account, the BTC assets do. See forum for more details and fee structure. By configuring NXTservices to monitor multigateway, any NXT node will be able to track the current status of all multigateway transactions and balances."
    },
    {
        "name": "mgwBTCD",
        "asset": "11060861818140490423",
        "description": "multigateway BTCD is backed 100% by deposits in the custom multisig accounts generated for each user. Deposits made to the multisig account will automatically transfer the corresponding amount of BTCD assets to the associated NXT account. Withdraws are automatically processed serially only when all multigateway servers are in agreement. The balances in the multisig accounts will change and do not represent the amount of BTCD in your account, the BTCD assets do. See forum for more details and fee structure. By configuring NXTservices to monitor multigateway, any NXT node will be able to track the current status of all multigateway transactions and balances. Amounts are rounded down to 4 decimals."
    },
    {
        "name": "nXtGenGHS",
        "asset": "9312536843540017349",
        "description": "nXtGen Mining is offering mining assets available immediately. Each asset is equivalent to 1 GHS worth of processing power. We will use the profits from mining to buy NXT and distribute it through dividends to all asset holders. By placing an order on this Site for Our Services, You agree to be bound by these Terms and Conditions of Service [ http://nxtmining.com/terms ]. We collect an ongoing variable hosting charge from the virtual currency product produced by all of Our Services. See Terms and Conditions for hosting charges and also for general risk information. WE RESERVE THE RIGHT TO TERMINATE ANY SERVICES WHEN IT BECOMES UNECONOMICAL FOR US OR YOU (IN OUR SOLE DECISION MAKING DISCRETION) TO CONTINUE ON WITH SUCH SERVICES BECAUSE OF CHANGES IN THE VIRTUAL CURRENCY MARKETPLACE, THE FACT MINING EQUIPMENT HAS BECOME OBSOLETE, ETC., EVEN THOUGH THERE IS NO STATED TERMINATION OR EXPIRY DATE ON ‘ASSETS’ or 'SHARES' (ALL SERVICES) WHICH YOU PURCHASE."
    },
    {
        "name": "nXtGenGHS",
        "asset": "12984255659001987157",
        "description": "nXtGen Mining is offering mining shares valued at 1 GHS per share. nXtGen Mining will be partnering with Knights of the Satoshi Ltd. to facilatate hosting of the equipment at a very competitive rate. This will allow for a more profitable venture. We will merge mine SHA-256 coins on a decentralized pool which will allow us to make a larger ROI. We will use the profits from mining to buy NXT and distrubute it through dividends to all shareholders. There will be a 3% fee to cover expenses such as electricity, hosting, etc. Dividends will be paid on a weekly basis. Further information will be found through the alias nXtGenMining or the website http://nxtmining.com"
    },
    {
        "name": "nXtGenKHS",
        "asset": "12178299813760950396",
        "description": "nXtGen Mining is offering mining shares valued at 1 KHS per share. nXtGen Mining will be partnering with Knights of the Satoshi Ltd. to facilatate hosting of the equipment at a very competitive rate. This will allow for a more profitable venture. We will merge mine Scrypt coins on a decentralized pool which will allow us to make a larger ROI. We will use the profits from mining to buy NXT and distrubute it through dividends to all shareholders. There will be a 3% fee to cover expenses such as electricity, hosting, etc. Dividends will be paid on a weekly basis. Further information will be found through the alias nXtGenMining or the website http://nxtmining.com"
    },
    {
        "name": "nxtegregor",
        "asset": "15363532072961781727",
        "description": "Этот актив будет получать прибыль от краткосрочных и среднесрочных инвестиций в Nxt Asset Exchange активы. А также от инвестиций в другие финансовые рынки.\r\nДля успешного старта проекта,держателям этого актива,первоначально будут выплачены высокие дивиденды:\r\n21.12.2014-22.12.2014-будет выплачено 100% прибыли от вложенных средств,т.е.  количество активов nxtegregor  удвоится.\r\n29.12.2014-03.01.2014-будет выплачено 100% \r\nВ январе 2015 года,планируется выплата 50%"
    },
    {
        "name": "sharkfund0",
        "asset": "3006420581923704757",
        "description": "Each purchased sharkfund0 asset represents a proportional share of the fund's crypto holdings. NXTsharks will actively manage sharkfund0 to maximize its market value. 25% of profits are assetized by the NXTsharks assets, the rest compounds in sharkfund0. The sharkfund0 assets held by NXTsharks are unpurchased assets and are not bound to anything, NXTsharks will never sell unpurchased assets via AE. Initially, the value is set to 10000 NXT per asset. After the initial funding, additions are made at the marked to the market value of all previously purchased sharkfund0 assets. Purchases using non-NXT crypto is done manually on a case by case basis, minimum 10 BTC. It is preferred to make withdrawals simply by selling the asset using AE, but NXTsharks can accomodate requests of larger cashouts manually.\r\nplease check the NXT forum for up to date details"
    },
    {
        "name": "silver",
        "asset": "7819056276221630295",
        "description": "Before purchasing read the terms and conditions located at alias SilverTerms. - The act of purchasing one of these tokens shall constitute the expression of consent to the terms expressed at alias SilverTerms. - These tokens act as warehouse receipts for 999 Silver Bullion stored in my facilities and may be redeemed for physical silver. For more details read the information located at alias SilverDetails or send me a personal message."
    },
    {
        "name": "theRealDAX",
        "asset": "10014539005191342474",
        "description": "The Real DAX is not a Game but a real Trade based on Real DAX Rates.every Day in the Morning (Mo-Fr) we cancel our old Sell Orders from the previous Day and make new Sell Orders based on the closing Rates from the previous Day.a certain Sell Orders below the current Rates we will buy to provide a fair Trade of course we can not all Sell Orders buy! All DAX Rates are based on the official Closing Rates from www.finanzen.net/dax  You can also make Real Profits! All Rates are dividends thru Thousend! Happy Trading"
    },
    {
        "name": "topDISTR",
        "asset": "1007341094739630837",
        "description": "The aim of this asset is to achieve the highest distribution at the NXT AE. I’m putting the funds and the effort to distribute 10000 packages of 1000 shares to whoever has an account on nxtforum.org or on bitcointalk.org, created before 2014-07-30. The priority is on a first come first served basis. The issuing account will never trade a single share and will only have outgoing transactions of 1000 shares and one incoming initial transaction of 11000 NXT for creating and distributing the asset. I will not send shares to the same NXT account twice. Post your account number to the corresponding thread on either forum."
    }
    ]

COINS = [
	    { 'id':"5527630" },
	    { 'id':"17554243582654188572" },
	    { 'id':"4551058913252105307" },
	    { 'id':"12659653638116877017" },
	    { 'id':"11060861818140490423"},
	    { 'id':"6918149200730574743" },
	    { 'id':"13120372057981370228" },
	    { 'id':"2303962892272487643" },
	    { 'id':"16344939950195952527"},
	    { 'id':"6775076774325697454" },
	    { 'id':"7734432159113182240" },
	    { 'id':"9037144112883608562" },
	    { 'id':"1369181773544917037" },
	    { 'id':"17353118525598940144" },
	    { 'id':"2881764795164526882" },
	    { 'id':"7117580438310874759" },
	    { 'id':"275548135983837356" },
	]

