import os, json
import glob
import pandas as pd

pobjects = list()

# Get existing items in project
with open('project.c3proj') as f:
    
    d = json.load(f)

    objects = d['objectTypes']
    
    if 'items' in objects:
        o = objects['items']
        pobjects.extend(o)
    
    if 'subfolders' in objects:
        for i in objects['subfolders']:
            o = i['items']
            pobjects.extend(o)    

# print(len(pobjects), pobjects)

dobjects = dict()
for o in pobjects:
    dobjects[o] = {}
    dobjects[o]['eventSheets'] = []

# print (dobjects)

def GroupTraverse(dict):
    pass

def BlockTraverse(dict):
    pass

os.chdir("eventSheets")
for file in glob.glob("*.json"):
    if 'uistate' not in file:
        with open(file) as f:
            d = json.load(f)
            sheetName = d['name']
            events = d['events'][-1]['children']
            for e in events:
                if e['eventType'] == 'block': # Block Traverse
                    conditions = e['conditions']
                    actions = e['actions']

                    def IsInEventSheet(key, sName):
                        if key in pobjects:
                            z = dobjects[key]['eventSheets']
                            if sheetName not in z:
                                z.append(sheetName)
                    
                    print('Conditions:')
                    for c in conditions :
                        IsInEventSheet(c['objectClass'], sheetName)
                    
                    print('Actions:')
                    for a in actions :
                        IsInEventSheet(c['objectClass'], sheetName)
                elif e['eventType'] == 'group': # Group Traverse
                    pass
        # break # revisa solo el primer archivo

for o, i in dobjects.items():
    print(o, i)