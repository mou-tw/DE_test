import argparse
import csv
import configparser
import logging
import json 

from utils import (map_args_to_url, check_valid_url, get_today_date_string, set_logger,
                   request_with_retries, get_target_parser, ensure_directory_exists
                   )

# define argparser object
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type" , type=str, choices=['competitions','persons','teams'], help="define query resources type")
parser.add_argument("-pc", "--particular_competition" , type=str, choices=['PL','ELC'], help="particular_competition")
parser.add_argument("-r",  "--parse_rule" , type=str, help="parse rule")
parser.add_argument("-ft", "--filter_type" , type=str, help="define filter type")
parser.add_argument("-fd", "--filter_data" , type=str, help="define filter data")

args_parser = parser.parse_args()

# define configparser object
config = configparser.ConfigParser()
config.read("/DE_TEST/configs/cfgs.ini")
token  = config.get('football_api','token')


class FootballAPIParser(object):
    def __init__(self, args_parser):
        self.args_parser = args_parser
        self.urls_check  = True
        self.save_dir = "/DE_TEST/files/" + get_today_date_string() + "/" 
        self.file_name = args_parser.parse_rule + ".csv"
        self.target_parser = get_target_parser(args_parser.parse_rule)
        self.file_cols = self.target_parser.get_course()
        set_logger(args_parser.parse_rule, get_today_date_string())
        logger = logging.getLogger(args_parser.parse_rule)
        logging.info(f"parameters : {args_parser}")

    def __parsing_args_to_urls(self):
        try:
            self.urls = map_args_to_url(self.args_parser)
            logging.info(f"done parsing urls : {self.urls}")
        except Exception as e:
            logging.exception("step: parsing_args_to_urls" ,exc_info=True)
            raise e
        return self
    
    def __check_url(self):
        try:
            for url in self.urls:
                if check_valid_url(url) == False:
                    self.urls_check = False
            if self.urls_check == False:
                raise(ValueError("url is not valid"))
            logging.info(f"done url checking ")
        except Exception as e:
            logging.exception("step: check urls" ,exc_info=True)
            raise e
        return self

    def __request_urls(self):
        try:
            self.query_data = []
            for url in self.urls:
                response = request_with_retries(url, headers={"X-Auth-Token":token})
                self.query_data.append(json.loads(response.text))
                logging.info(f"done requesting url: {url}")
            logging.info(f"done requesting urls ")
        except Exception as e:
            logging.exception("step: request urls" ,exc_info=True)
            raise e
        return self
    
    def __parse_data(self):
        try:
            self.parsed_data = []
            for data in self.query_data:
                pd = self.target_parser(data).parse_data()
                self.parsed_data = self.parsed_data + pd
            logging.info(f"done parsing datas ")
        except Exception as e:
            logging.exception("step: parse data" ,exc_info=True)
            raise e   
        return self

    def __save_file(self):
        try:
            ensure_directory_exists(self.save_dir)
            with open(self.save_dir + self.file_name, 'w') as csvfile:
                # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames=self.file_cols)
                # writing headers (field names)
                writer.writeheader()
                # writing data rows
                writer.writerows(self.parsed_data)
            logging.info(f"done saving datas, file path: {self.save_dir + self.file_name}")
        except Exception as e:
            logging.exception("step: save file" ,exc_info=True)
            raise e   
        return self


    def start_processing(self):
        self.__parsing_args_to_urls()\
            .__check_url()\
            .__request_urls()\
            .__parse_data()\
            .__save_file()

if __name__ == "__main__":
    ftp = FootballAPIParser(args_parser)
    ftp.start_processing()
