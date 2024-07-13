## CSV File Path
[csv path](https://github.com/mou-tw/DE_test/blob/main/files/20240713/EPL_Season.csv)


## Build Docker Images
```
docker build -t de_test . 
```

## Run API Parsing Python Script
```
docker run --rm -it -v `pwd`:/DE_TEST de_test python ent/football_api_parser.py -t competitions -pc PL -ft season -fd 2020,2021,2022,2023 -r EPL_Season
```

## Parameter and Description
| Parameter | Description | 
| :--- | ---- | 
| --type, -t |  Determine the type of data to request. The available options are ['competitions', 'persons', 'teams'].|  
| --particular_competition, -pc | List one particular competition. The available options are ['PL','ELC']. |  
| --parse_rule, -r | Choose the parsing logic. Currently, only EPL_Season is defined. |  
| --filter_type, -ft | Filter key |
| --filter_data, -fd | Filter value |  

