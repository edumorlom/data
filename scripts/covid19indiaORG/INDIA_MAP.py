# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# The places' dcids are resolved by wikidataId.
# The wikidataId for each place was found using the place_resolver.go as well as so manual checks.
# Please see README.md for more information.

# State ISO Code -> District Name -> WikidataId

DISTRICTS = {
   "WB":{
      "Alipurduar":"Q4726845",
      "Bankura":"Q2088458",
      "Birbhum":"Q2088440",
      "Cooch Behar":"Q2728658",
      "Dakshin Dinajpur":"Q533839",
      "Darjeeling":"Q1134759",
      "Hooghly":"Q548518",
      "Howrah":"Q1478937",
      "Jalpaiguri":"Q1351487",
      "Jhargram":"Q29168456",
      "Kalimpong":"Q28769140",
      "Kolkata":"Q2088496",
      "Malda":"Q2049820",
      "Murshidabad":"Q1546240",
      "Nadia":"Q1143880",
      "North 24 Parganas":"Q338425",
      "Paschim Bardhaman":"Q808023",
      "Paschim Medinipur":"Q1855537",
      "Purba Bardhaman":"Q29257278",
      "Purba Medinipur":"Q1431920",
      "Purulia":"Q307474",
      "South 24 Parganas":"Q2308319",
      "Uttar Dinajpur":"Q2019766"
   },
   "UT":{
      "Almora":"Q1805066",
      "Bageshwar":"Q1815313",
      "Chamoli":"Q1797372",
      "Champawat":"Q288278",
      "Dehradun":"Q1815740",
      "Haridwar":"Q2270438",
      "Nainital":"Q1797306",
      "Pauri Garhwal":"Q2085474",
      "Pithoragarh":"Q1945425",
      "Rudraprayag":"Q1805059",
      "Tehri Garhwal":"Q1357107",
      "Udham Singh Nagar":"Q1805082",
      "Uttarkashi":"Q1773437"
   },
   "UP":{
      "Agra":"Q606343",
      "Aligarh":"Q766918",
      "Ambedkar Nagar":"Q456764",
      "Amethi":"Q1071494",
      "Amroha":"Q1891677",
      "Auraiya":"Q1812533",
      "Ayodhya":"Q1814132",
      "Azamgarh":"Q793553",
      "Baghpat":"Q1797363",
      "Bahraich":"Q1812548",
      "Ballia":"Q584644",
      "Balrampur":"Q1948380",
      "Banda":"Q2131759",
      "Barabanki":"Q633114",
      "Bareilly":"Q1797378",
      "Basti":"Q715267",
      "Bhadohi":"Q127533",
      "Bijnor":"Q1937865",
      "Budaun":"Q1815262",
      "Bulandshahr":"Q1752328",
      "Chandauli":"Q2733369",
      "Chitrakoot":"Q2089141",
      "Deoria":"Q731746",
      "Etah":"Q1773429",
      "Etawah":"Q1815288",
      "Farrukhabad":"Q1897251",
      "Fatehpur":"Q1946829",
      "Firozabad":"Q1946950",
      "Gautam Buddha Nagar":"Q1785950",
      "Ghaziabad":"Q1773444",
      "Ghazipur":"Q1287993",
      "Gonda":"Q1937857",
      "Gorakhpur":"Q1144349",
      "Hamirpur":"Q2019757",
      "Hapur":"Q5653340",
      "Hardoi":"Q1772822",
      "Hathras":"Q1814892",
      "Jalaun":"Q2089115",
      "Jaunpur":"Q1356060",
      "Jhansi":"Q1937885",
      "Kannauj":"Q627979",
      "Kanpur Dehat":"Q610612",
      "Kanpur Nagar":"Q2089152",
      "Kasganj":"Q890800",
      "Kaushambi":"Q1946937",
      "Kushinagar":"Q1840355",
      "Lakhimpur Kheri":"Q1755447",
      "Lalitpur":"Q1947336",
      "Lucknow":"Q1773416",
      "Maharajganj":"Q1356139",
      "Mahoba":"Q1815322",
      "Mainpuri":"Q1816657",
      "Mathura":"Q1773422",
      "Mau":"Q1518847",
      "Meerut":"Q1764627",
      "Mirzapur":"Q1143894",
      "Moradabad":"Q1345006",
      "Muzaffarnagar":"Q2365710",
      "Pilibhit":"Q2980705",
      "Pratapgarh":"Q1473962",
      "Prayagraj":"Q1773426",
      "Rae Bareli":"Q1321157",
      "Rampur":"Q1815331",
      "Saharanpur":"Q1797326",
      "Sambhal":"Q3000436",
      "Sant Kabir Nagar":"Q1945445",
      "Shahjahanpur":"Q1812557",
      "Shamli":"Q2999938",
      "Shrawasti":"Q1945458",
      "Siddharthnagar":"Q1815339",
      "Sitapur":"Q1812539",
      "Sonbhadra":"Q607798",
      "Sultanpur":"Q1356154",
      "Unnao":"Q1937875",
      "Varanasi":"Q1321140"
   },
   "TR":{
      "Dhalai":"Q2086546",
      "Gomati":"Q16086497",
      "Khowai":"Q16086680",
      "North Tripura":"Q1920978",
      "Sipahijala":"Q16086076",
      "South Tripura":"Q1822159",
      "Unokoti":"Q16087996",
      "West Tripura":"Q1947570"
   },
   "TN":{
      "Ariyalur":"Q15112",
      "Chengalpattu":"Q65976177",
      "Chennai":"Q15116",
      "Coimbatore":"Q15136",
      "Cuddalore":"Q15150",
      "Dharmapuri":"Q15152",
      "Dindigul":"Q15154",
      "Erode":"Q15155",
      "Kallakurichi":"Q60493360",
      "Kancheepuram":"Q15157",
      "Kanyakumari":"Q15158",
      "Karur":"Q15182",
      "Krishnagiri":"Q15183",
      "Madurai":"Q15184",
      "Nagapattinam":"Q15185",
      "Namakkal":"Q15187",
      "Nilgiris":"Q15188",
      "Perambalur":"Q15186",
      "Pudukkottai":"Q15190",
      "Ramanathapuram":"Q15191",
      "Ranipet":"Q66659623",
      "Salem":"Q15192",
      "Sivaganga":"Q15195",
      "Tenkasi":"Q75094121",
      "Thanjavur":"Q15194",
      "Theni":"Q15196",
      "Thiruvallur":"Q15204",
      "Thiruvarur":"Q15197",
      "Thoothukkudi":"Q15198",
      "Tiruchirappalli":"Q15201",
      "Tirunelveli":"Q15200",
      "Tirupathur":"Q66659621",
      "Tiruppur":"Q15202",
      "Tiruvannamalai":"Q15207",
      "Vellore":"Q15206",
      "Viluppuram":"Q15205",
      "Virudhunagar":"Q15209"
   },
   "RJ":{
      "Ajmer":"Q413037",
      "Alwar":"Q449690",
      "Banswara":"Q806969",
      "Baran":"Q2329717",
      "Barmer":"Q42016",
      "Bharatpur":"Q854861",
      "Bhilwara":"Q41991",
      "Bikaner":"Q778996",
      "Bundi":"Q670405",
      "Chittorgarh":"Q1075011",
      "Churu":"Q1090006",
      "Dausa":"Q1173042",
      "Dholpur":"Q1207709",
      "Dungarpur":"Q1265687",
      "Ganganagar":"Q1419696",
      "Hanumangarh":"Q1356112",
      "Jaipur":"Q1134781",
      "Jaisalmer":"Q1419708",
      "Jalore":"Q1460832",
      "Jhalawar":"Q1471417",
      "Jhunjhunu":"Q1471427",
      "Jodhpur":"Q1434965",
      "Karauli":"Q1419668",
      "Kota":"Q999432",
      "Nagaur":"Q1507174",
      "Pali":"Q46925",
      "Pratapgarh":"Q1585433",
      "Rajsamand":"Q596693",
      "Sawai Madhopur":"Q1507166",
      "Sikar":"Q12945777",
      "Sirohi":"Q205719",
      "Tonk":"Q915880",
      "Udaipur":"Q1321577"
   },
   "PB":{
      "Amritsar":"Q202822",
      "Barnala":"Q2353293",
      "Bathinda":"Q172488",
      "Faridkot":"Q172494",
      "Fatehgarh Sahib":"Q172485",
      "Fazilka":"Q188702",
      "Ferozepur":"Q172385",
      "Gurdaspur":"Q146708",
      "Hoshiarpur":"Q304800",
      "Jalandhar":"Q1817425",
      "Kapurthala":"Q172363",
      "Ludhiana":"Q172482",
      "Mansa":"Q172387",
      "Moga":"Q1946896",
      "Pathankot":"Q172269",
      "Patiala":"Q172391",
      "Rupnagar":"Q196508",
      "S.A.S. Nagar":"Q2037672",
      "Sangrur":"Q1945515",
      "Shahid Bhagat Singh Nagar":"Q202710",
      "Sri Muktsar Sahib":"Q1947359",
      "Tarn Taran":"Q2298993"
   },
   "PY":{
      "Karaikal":"Q639264",
      "Mahe":"Q639279",
      "Puducherry":"Q984035",
      "Yanam":"Q2126598"
   },
   "OR":{
      "Angul":"Q1772807",
      "Balangir":"Q804642",
      "Balasore":"Q2022279",
      "Bargarh":"Q808140",
      "Bhadrak":"Q685638",
      "Boudh":"Q2363639",
      "Cuttack":"Q2022256",
      "Deogarh":"Q2269639",
      "Dhenkanal":"Q1948389",
      "Gajapati":"Q1947292",
      "Ganjam":"Q776213",
      "Jagatsinghpur":"Q971581",
      "Jajpur":"Q2087771",
      "Jharsuguda":"Q569181",
      "Kalahandi":"Q1876588",
      "Kandhamal":"Q2085500",
      "Kendrapara":"Q2299172",
      "Kendujhar":"Q2085428",
      "Khordha":"Q662818",
      "Koraput":"Q1947300",
      "Malkangiri":"Q5122619",
      "Mayurbhanj":"Q1914546",
      "Nabarangapur":"Q2396798",
      "Nayagarh":"Q2367388",
      "Nuapada":"Q1810550",
      "Puri":"Q1817158",
      "Rayagada":"Q2577997",
      "Sambalpur":"Q1267306",
      "Subarnapur":"Q1473957",
      "Sundargarh":"Q2296047"
   },
   "NL":{
      "Dimapur":"Q634262",
      "Kiphire":"Q2597908",
      "Kohima":"Q953530",
      "Longleng":"Q1426783",
      "Mokokchung":"Q2175311",
      "Mon":"Q2339648",
      "Peren":"Q516294",
      "Phek":"Q590882",
      "Tuensang":"Q2571393",
      "Wokha":"Q681821",
      "Zunheboto":"Q2091461"
   },
   "MZ":{
      "Aizawl":"Q1947322",
      "Champhai":"Q1965256",
      "Hnahthial":"Q89360042",
      "Khawzawl":"Q89371656",
      "Kolasib":"Q1947343",
      "Lawngtlai":"Q2086209",
      "Lunglei":"Q1947352",
      "Mamit":"Q751531",
      "Saiha":"Q1821714",
      "Saitual":"Q89371650",
      "Serchhip":"Q2086190"
   },
   "ML":{
      "East Garo Hills":"Q2085455",
      "East Jaintia Hills":"Q15923776",
      "East Khasi Hills":"Q1945304",
      "North Garo Hills":"Q7055466",
      "Ribhoi":"Q1884672",
      "South Garo Hills":"Q2329228",
      "South West Garo Hills":"Q15961576",
      "South West Khasi Hills":"Q15923741",
      "West Garo Hills":"Q2329181",
      "West Jaintia Hills":"Q13181190",
      "West Khasi Hills":"Q2064752"
   },
   "MH":{
      "Ahmednagar":"Q401744",
      "Akola":"Q520510",
      "Amravati":"Q1771774",
      "Aurangabad":"Q592942",
      "Beed":"Q814037",
      "Bhandara":"Q1813857",
      "Buldhana":"Q47929",
      "Chandrapur":"Q1797274",
      "Dhule":"Q1797383",
      "Gadchiroli":"Q1804847",
      "Gondia":"Q1917227",
      "Hingoli":"Q2087615",
      "Jalgaon":"Q1797291",
      "Jalna":"Q1804863",
      "Kolhapur":"Q1797312",
      "Latur":"Q1948713",
      "Mumbai":"Q2341660",
      "Nagpur":"Q1797367",
      "Nanded":"Q692389",
      "Nandurbar":"Q1623525",
      "Nashik":"Q1797269",
      "Osmanabad":"Q1647186",
      "Palghar":"Q18003119",
      "Parbhani":"Q1797389",
      "Pune":"Q1797336",
      "Raigad":"Q2019683",
      "Ratnagiri":"Q1771768",
      "Sangli":"Q1425060",
      "Satara":"Q1135612",
      "Sindhudurg":"Q768332",
      "Solapur":"Q1797263",
      "Thane":"Q943099",
      "Wardha":"Q980608",
      "Washim":"Q1804858",
      "Yavatmal":"Q1804852"
   },
   "MP":{
      "Agar Malwa":"Q15732396",
      "Alirajpur":"Q2667586",
      "Anuppur":"Q2299093",
      "Ashoknagar":"Q2246416",
      "Balaghat":"Q641904",
      "Barwani":"Q2126754",
      "Betul":"Q1815279",
      "Bhind":"Q2341700",
      "Bhopal":"Q1797245",
      "Burhanpur":"Q2125592",
      "Chhatarpur":"Q2449785",
      "Chhindwara":"Q1986096",
      "Damoh":"Q2479331",
      "Datia":"Q2206266",
      "Dewas":"Q2025998",
      "Dhar":"Q2299069",
      "Dindori":"Q2398551",
      "Guna":"Q930027",
      "Gwalior":"Q2085310",
      "Harda":"Q2173003",
      "Hoshangabad":"Q620801",
      "Indore":"Q742938",
      "Jabalpur":"Q632093",
      "Jhabua":"Q2085336",
      "Katni":"Q746441",
      "Khandwa":"Q2085436",
      "Khargone":"Q2273900",
      "Mandla":"Q2341670",
      "Mandsaur":"Q1870014",
      "Morena":"Q2341467",
      "Narsinghpur":"Q2341616",
      "Neemuch":"Q2341713",
      "Niwari":"Q63563797",
      "Panna":"Q2341630",
      "Raisen":"Q1815223",
      "Rajgarh":"Q1833306",
      "Ratlam":"Q2299164",
      "Rewa":"Q526862",
      "Sagar":"Q2085421",
      "Satna":"Q2577924",
      "Sehore":"Q2299029",
      "Seoni":"Q2221184",
      "Shahdol":"Q2085464",
      "Shajapur":"Q2449803",
      "Sheopur":"Q620105",
      "Shivpuri":"Q2299042",
      "Sidhi":"Q2449793",
      "Singrauli":"Q2668638",
      "Tikamgarh":"Q2449760",
      "Ujjain":"Q892641",
      "Umaria":"Q620297",
      "Vidisha":"Q1815253"
   },
   "LA":{
      "Kargil":"Q1650798",
      "Leh":"Q1921210"
   },
   "KL":{
      "Alappuzha":"Q928959",
      "Ernakulam":"Q1356097",
      "Idukki":"Q301821",
      "Kannur":"Q2980652",
      "Kasaragod":"Q1419703",
      "Kollam":"Q1356124",
      "Kottayam":"Q1353354",
      "Kozhikode":"Q1142979",
      "Malappuram":"Q1030918",
      "Palakkad":"Q1535742",
      "Pathanamthitta":"Q634935",
      "Thiruvananthapuram":"Q162612",
      "Thrissur":"Q2429655",
      "Wayanad":"Q1364427"
   },
   "KA":{
      "Bagalkote":"Q1910231",
      "Ballari":"Q1791926",
      "Belagavi":"Q815464",
      "Bengaluru Rural":"Q806464",
      "Bengaluru Urban":"Q806463",
      "Bidar":"Q1790568",
      "Chamarajanagara":"Q862912",
      "Chikkaballapura":"Q1072629",
      "Chikkamagaluru":"Q743077",
      "Chitradurga":"Q165264",
      "Dakshina Kannada":"Q950571",
      "Davanagere":"Q1863214",
      "Dharwad":"Q1790904",
      "Gadag":"Q2353931",
      "Hassan":"Q956732",
      "Haveri":"Q765481",
      "Kalaburagi":"Q2641873",
      "Kodagu":"Q1553185",
      "Kolar":"Q2509866",
      "Koppal":"Q956387",
      "Mandya":"Q2768290",
      "Mysuru":"Q591781",
      "Raichur":"Q1430830",
      "Ramanagara":"Q427679",
      "Shivamogga":"Q2981389",
      "Tumakuru":"Q1301635",
      "Udupi":"Q1483337",
      "Uttara Kannada":"Q579205",
      "Vijayapura":"Q83108",
      "Yadgir":"Q1786949"
   },
   "JH":{
      "Bokaro":"Q2295925",
      "Chatra":"Q1979499",
      "Deoghar":"Q2030017",
      "Dhanbad":"Q2240791",
      "Dumka":"Q2577657",
      "East Singhbhum":"Q2452921",
      "Garhwa":"Q2302076",
      "Giridih":"Q2302065",
      "Godda":"Q638980",
      "Gumla":"Q2295865",
      "Hazaribagh":"Q1945416",
      "Jamtara":"Q2980986",
      "Khunti":"Q367344",
      "Koderma":"Q2085480",
      "Latehar":"Q2244762",
      "Lohardaga":"Q1948301",
      "Pakur":"Q2295930",
      "Palamu":"Q1797254",
      "Ramgarh":"Q2663612",
      "Ranchi":"Q1947380",
      "Sahibganj":"Q767878",
      "Saraikela-Kharsawan":"Q2362658",
      "Simdega":"Q2597889",
      "West Singhbhum":"Q1950527"
   },
   "JK":{
      "Anantnag":"Q2982349",
      "Bandipora":"Q2983553",
      "Baramulla":"Q1912057",
      "Budgam":"Q2594218",
      "Doda":"Q2298979",
      "Ganderbal":"Q2556028",
      "Jammu":"Q1947371",
      "Kathua":"Q2375700",
      "Kishtwar":"Q2321899",
      "Kulgam":"Q2321867",
      "Kupwara":"Q2297306",
      "Pulwama":"Q2085364",
      "Punch":"Q2983134",
      "Rajouri":"Q544279",
      "Ramban":"Q2321939",
      "Reasi":"Q2321956",
      "Samba":"Q1117086",
      "Shopiyan":"Q2073646",
      "Srinagar":"Q1506029",
      "Udhampur":"Q1947311"
   },
   "HP":{
      "Bilaspur":"Q3710724",
      "Chamba":"Q1060614",
      "Hamirpur":"Q5645337",
      "Kangra":"Q727232",
      "Kinnaur":"Q1862950",
      "Kullu":"Q2980880",
      "Lahaul and Spiti":"Q837595",
      "Mandi":"Q1892161",
      "Shimla":"Q1921404",
      "Sirmaur":"Q654331",
      "Solan":"Q2980937",
      "Una":"Q2301741"
   },
   "HR":{
      "Ambala":"Q2086226",
      "Bhiwani":"Q1852857",
      "Charkhi Dadri":"Q28172110",
      "Faridabad":"Q2086173",
      "Fatehabad":"Q2301753",
      "Gurugram":"Q1815766",
      "Hisar":"Q1815773",
      "Italians":"",
      "Jhajjar":"Q1948260",
      "Jind":"Q268605",
      "Kaithal":"Q614037",
      "Karnal":"Q607915",
      "Kurukshetra":"Q980118",
      "Mahendragarh":"Q684019",
      "Nuh":"Q2216696",
      "Palwal":"Q2724926",
      "Panchkula":"Q1898143",
      "Panipat":"Q2086163",
      "Rewari":"Q2301759",
      "Rohtak":"Q967388",
      "Sirsa":"Q526101",
      "Sonipat":"Q2241746",
      "Yamunanagar":"Q1873644"
   },
   "GJ":{
      "Ahmedabad":"Q401686",
      "Amreli":"Q257946",
      "Anand":"Q485683",
      "Aravalli":"Q12175285",
      "Banaskantha":"Q806125",
      "Bharuch":"Q854900",
      "Bhavnagar":"Q854963",
      "Botad":"Q14505072",
      "Chhota Udaipur":"Q5979243",
      "Dahod":"Q186518",
      "Dang":"Q1135616",
      "Devbhumi Dwarka":"Q14594717",
      "Gandhinagar":"Q1772860",
      "Gir Somnath":"Q15244465",
      "Jamnagar":"Q2982118",
      "Junagadh":"Q1797344",
      "Kheda":"Q1755463",
      "Kutch":"Q1063417",
      "Mahisagar":"Q5706885",
      "Mehsana":"Q2019694",
      "Morbi":"Q5979727",
      "Narmada":"Q1797230",
      "Navsari":"Q1797349",
      "Panchmahal":"Q1781463",
      "Patan":"Q1815269",
      "Porbandar":"Q1772815",
      "Rajkot":"Q1815245",
      "Sabarkantha":"Q1772856",
      "Surat":"Q1797317",
      "Surendranagar":"Q237535",
      "Tapi":"Q670165",
      "Vadodara":"Q578285",
      "Valsad":"Q1946743"
   },
   "CT":{
      "Balod":"Q16056266",
      "Baloda Bazar":"Q15663455",
      "Balrampur":"Q16056268",
      "Bametara":"Q16254159",
      "Bastar":"Q100152",
      "Bijapur":"Q100164",
      "Bilaspur":"Q100157",
      "Dakshin Bastar Dantewada":"Q100211",
      "Dhamtari":"Q100190",
      "Durg":"Q100182",
      "Gariaband":"Q16961365",
      "Gaurela Pendra Marwahi":"Q98304389",
      "Janjgir Champa":"Q2575633",
      "Jashpur":"Q2577551",
      "Kabeerdham":"Q2450255",
      "Kondagaon":"Q12420995",
      "Korba":"Q2299121",
      "Koriya":"Q2295896",
      "Mahasamund":"Q2450240",
      "Mungeli":"Q13476249",
      "Narayanpur":"Q2322000",
      "Raigarh":"Q2286310",
      "Raipur":"Q2295914",
      "Rajnandgaon":"Q2341800",
      "Sukma":"Q16933590",
      "Surajpur":"Q16938031",
      "Surguja":"Q1805075",
      "Uttar Bastar Kanker":"Q2310530"
   },
   "CH":{
      "Chandigarh":"Q5071071"
   },
   "BR":{
      "Araria":"Q42901",
      "Arwal":"Q42917",
      "Aurangabad":"Q43086",
      "Banka":"Q43097",
      "Begusarai":"Q49157",
      "Bhagalpur":"Q49155",
      "Bhojpur":"Q49153",
      "Buxar":"Q49161",
      "Darbhanga":"Q49160",
      "East Champaran":"Q49159",
      "Gaya":"Q49173",
      "Gopalganj":"Q49171",
      "Jamui":"Q49168",
      "Jehanabad":"Q49176",
      "Kaimur":"Q77367",
      "Katihar":"Q77568",
      "Khagaria":"Q49175",
      "Kishanganj":"Q77375",
      "Lakhisarai":"Q77505",
      "Madhepura":"Q77746",
      "Madhubani":"Q77474",
      "Munger":"Q77452",
      "Muzaffarpur":"Q77731",
      "Nalanda":"Q77633",
      "Nawada":"Q100067",
      "Patna":"Q100077",
      "Purnia":"Q100082",
      "Rohtas":"Q100085",
      "Saharsa":"Q100120",
      "Samastipur":"Q100117",
      "Saran":"Q100146",
      "Sheikhpura":"Q100093",
      "Sheohar":"Q100095",
      "Sitamarhi":"Q100144",
      "Siwan":"Q100131",
      "Supaul":"Q100139",
      "Vaishali":"Q100130",
      "West Champaran":"Q100124"
   },
   "AR":{
      "Anjaw":"Q15413",
      "Changlang":"Q15427",
      "Dibang Valley":"Q15446",
      "East Kameng":"Q15424",
      "East Siang":"Q15419",
      "Kamle":"Q48731073",
      "Kra Daadi":"Q21018627",
      "Kurung Kumey":"Q2449506",
      "Lepa Rada":"Q63563632",
      "Lohit":"Q15438",
      "Longding":"Q5627568",
      "Lower Dibang Valley":"Q2373368",
      "Lower Siang":"Q13602925",
      "Lower Subansiri":"Q15436",
      "Namsai":"Q21559824",
      "Pakke Kessang":"Q61439260",
      "Papum Pare":"Q15432",
      "Shi Yomi":"Q63563625",
      "Siang":"Q18642331",
      "Tawang":"Q15449",
      "Tirap":"Q15448",
      "Upper Dibang Valley":"Q15446",
      "Upper Siang":"Q15465",
      "Upper Subansiri":"Q15464",
      "West Kameng":"Q15459",
      "West Siang":"Q15453"
   },
   "AP":{
      "Anantapur":"Q15212",
      "Chittoor":"Q15213",
      "East Godavari":"Q15338",
      "Guntur":"Q15341",
      "Krishna":"Q15382",
      "Kurnool":"Q15381",
      "Prakasam":"Q15390",
      "S.P.S. Nellore":"Q15383",
      "Srikakulam":"Q15395",
      "Visakhapatnam":"Q15394",
      "Vizianagaram":"Q15392",
      "West Godavari":"Q15404",
      "Y.S.R. Kadapa":"Q15342"
   }
}

# State ISO Code -> WikidataId
STATES = {
   "WB":"Q1356",
   "UT":"Q1499",
   "UP":"Q1498",
   "TR":"Q13636",
   "TG":"Q677037",
   "TN":"Q1445",
   "SK":"Q1505",
   "RJ":"Q1437",
   "PB":"Q22424",
   "PY":"Q66743",
   "OR":"Q22048",
   "NL":"Q1599",
   "MZ":"Q1502",
   "ML":"Q1195",
   "MN":"Q1193",
   "MH":"Q1191",
   "MP":"Q1188",
   "LA":"Q200667",
   "KL":"Q1186",
   "KA":"Q1185",
   "JH":"Q1184",
   "JK": "Q66278313",
   "HP":"Q1177",
   "HR":"Q1174",
   "GJ":"Q1061",
   "GA":"Q1171",
   "DL":"Q1353",
   "DN": "Q77997266",
   "CT":"Q1168",
   "CH":"Q43433",
   "BR":"Q1165",
   "AS":"Q1164",
   "AR":"Q1162",
   "AP":"Q1159",
   "AN":"Q40888",
}
