import configparser

# define configparser object
config = configparser.ConfigParser()
config.read("/DE_TEST/configs/cfgs.ini")
url_base  = config.get("football_api","url")

def map_args_to_url(args_parser):
    """
    Maps the provided arguments to a URL based on the type and filter_type in args_parser.

    :param args_parser: An object containing the arguments to be parsed
    :return: A list of URLs based on the parsed arguments
    """
    match args_parser.type:
        case "competitions":
            tmp_url = parse_competitions_type_args(args_parser=args_parser)
        case "persons":
            pass
        case "teams":
            pass
        case _:
            pass

    if args_parser.filter_type:
        match args_parser.filter_type:
            case "season":
                ret = parse_season_args(args_parser=args_parser)
                ret = [tmp_url +'matches?season='+ i for i in ret]
            case _:
                pass

    return ret


def parse_competitions_type_args(args_parser):
    """
    Parse arguments for competitions type and construct the base URL.

    :param args_parser: An object containing the arguments to be parsed
    :return: A string representing the base URL for competitions
    """
    if args_parser.particular_competition:
        return url_base + "competitions/" +  args_parser.particular_competition + "/"
    else:
        return url_base + "competitions/"


def parse_season_args(args_parser):
    """
    Parse season filter arguments and split them into a list.

    :param args_parser: An object containing the arguments to be parsed
    :return: A list of season filter values
    :raises AssertionError: If filter_data is not provided
    """
    assert args_parser.filter_data != None , "filter data should be provided"
    data = args_parser.filter_data
    data_lst = data.split(",")
    return data_lst

