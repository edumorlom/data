from wiki_parser import get_wikidata_id, get_place_name_from_url
output = []
with open("input.txt") as f:
    lines = f.readlines()
    for url in lines:
        print(url)
        try:
            place_name = get_place_name_from_url(url)
            wikidata_id = get_wikidata_id('https://en.wikipedia.org/wiki/' + place_name)
        except:
            wikidata_id = url
        output.append({"url": url, "wikidataId": wikidata_id})
        print(wikidata_id)
    
f_out = open("ids.txt", "w+")
f_out.write(str(output))