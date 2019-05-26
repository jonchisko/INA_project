import json
import pickle
import os

def playerID2dict(path2files):
    files = os.listdir(path2files)
    dict_id_pos = {}
    dict_matches = {}
    for i in range(len(files)):
        file = files[i]
        print(i/(len(files)))
        with open(path2files+"/"+file, "r") as f:
            if f.name.endswith("json"):
                dict_json = json.load(f)

                date = dict_json["startDate"].split("T")
                date = date[0]
                date = date.split("-")
                date = date[2] + "-" + date[1] + "-" + date[0]

                dateAway = str(dict_json["away"]["teamId"]) + "" + date
                dict_matches[dateAway] = dict_json["away"]["name"]

                dateHome = str(dict_json["home"]["teamId"]) + "" + date
                dict_matches[dateHome] = dict_json["home"]["name"]

                for player in dict_json["home"]["players"]:
                    id, pos, name = player["playerId"], player["position"], player["name"]
                    if not id in dict_id_pos:
                        dict_id_pos[id] = (name, pos)
    pickle.dump(dict_id_pos, open("id2posPickled.pickle", "wb"))
    pickle.dump(dict_matches, open("matches.pickle", "wb"))
    return dict_id_pos


if __name__ == '__main__':
    a = playerID2dict("./test_data")

