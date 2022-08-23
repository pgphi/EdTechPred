import requests
import datetime

"""
The datasets are identified using the EIC codes as used for REMIT reporting and/or used for data provision to GIE. 
These EIC codes are available from the API section on AGSI+ and ALSI. Please note that the EIC code database is 
subject to updates and EIC codes used on AGSI+ or ALSI can change over time. For example : 
Facilities can change operator, new facilities can become operational or be decommissioned, 
and EIC codes (and types of code used) are undergoing an evaluation process by ACER (ACER Approved EIC code listing). 
If such changes would have occurred, we will be able to inform you trough the API mailing list.
"""

# Datasets of german gas providers further see: https://agsi.gie.eu/
uniper_url = "https://agsi.gie.eu/api?country=DE&company=21X000000001127H"
astora_url = "https://agsi.gie.eu/api?country=DE&company=21X000000001160J"
bayernugs_url = "https://agsi.gie.eu/api?country=DE&company=37X0000000000151"
bes_url = "https://agsi.gie.eu/api?country=DE&company=37X0000000000224"
edf_url = "https://agsi.gie.eu/api?country=DE&company=37X000000000152S"
enbw_url = "https://agsi.gie.eu/api?country=DE&company=11X0-0000-0667-8"
eneco_url = "https://agsi.gie.eu/api?country=DE&company=21X0000000010849"
equinor_url = "https://agsi.gie.eu/api?country=DE&company=21X000000001368W"
peisen_url = "https://agsi.gie.eu/api?country=DE&company=21X000000001297T"
ekb_url = "https://agsi.gie.eu/api?country=DE&company=21X000000001080H"
ewe_url = "https://agsi.gie.eu/api?country=DE&company=21X0000000011756"
hanse_url = "https://agsi.gie.eu/api?country=DE&company=21X0000000013805"
kge_url = "https://agsi.gie.eu/api?country=DE&company=21X000000001140P"
met_url = "https://agsi.gie.eu/api?country=DE&company=37X000000000047P"
mnd_url = "https://agsi.gie.eu/api?country=DE&company=37X000000000042Z"
nafta_url = "https://agsi.gie.eu/api?country=DE&company=21X0000000011748"
nuon_url = "https://agsi.gie.eu/api?country=DE&company=37X0000000000119"
omv_url = "https://agsi.gie.eu/api?country=DE&company=25X-OMVGASSTORA5"
rwe_url = "https://agsi.gie.eu/api?country=DE&company=21X000000001262B"
storengy_url = "https://agsi.gie.eu/api?country=DE&company=21X000000001072G"
swkiel_url = "https://agsi.gie.eu/api?country=DE&company=37X000000000051Y"
tep_url = "https://agsi.gie.eu/api?country=DE&company=21X000000001307F"
trianel_url = "https://agsi.gie.eu/api?country=DE&company=21X000000001310Q"
vng_url = "https://agsi.gie.eu/api?country=DE&company=21X000000001138C"

example_dataset = dict(last_page=142, total=30,
                       dataset="\u003Ca href=\u0022\/historical\/eu\u0022\u003EEU\u003C\/a\u003E \u003E \u003Ca "
                               "href=\u0022\/historical\/de\u0022\u003EDE\u003C\/a\u003E \u003E Uniper Energy Storage",
                       gas_day="2022-08-15", data=[
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-15", "gasInStorage": "43.3305", "injection": "471.52", "withdrawal": "0",
         "workingGasVolume": "60.8197", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.78", "full": "71.24", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-14", "gasInStorage": "42.8589", "injection": "585.48", "withdrawal": "0",
         "workingGasVolume": "60.8197", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.96", "full": "70.47", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-13", "gasInStorage": "42.2734", "injection": "581.95", "withdrawal": "0",
         "workingGasVolume": "60.8197", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.96", "full": "69.51", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-12", "gasInStorage": "41.6915", "injection": "642.04", "withdrawal": "0",
         "workingGasVolume": "60.8197", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "1.06", "full": "68.55", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-11", "gasInStorage": "41.0495", "injection": "644.74", "withdrawal": "0",
         "workingGasVolume": "60.5821", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "1.06", "full": "67.76", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-10", "gasInStorage": "40.4047", "injection": "615.43", "withdrawal": "0",
         "workingGasVolume": "60.5821", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "1.02", "full": "66.69", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-09", "gasInStorage": "39.7822", "injection": "637.65", "withdrawal": "0",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "E",
         "trend": "1.05", "full": "65.64", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-08", "gasInStorage": "39.1446", "injection": "637.65", "withdrawal": "0",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "1.05", "full": "64.58", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-07", "gasInStorage": "38.5069", "injection": "653.3", "withdrawal": "0",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "1.08", "full": "63.53", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-06", "gasInStorage": "37.8536", "injection": "662", "withdrawal": "0",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "1.09", "full": "62.45", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-05", "gasInStorage": "37.1916", "injection": "585.79", "withdrawal": "0",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.97", "full": "61.36", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-04", "gasInStorage": "36.6016", "injection": "367.17", "withdrawal": "5.5",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.6", "full": "60.39", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-03", "gasInStorage": "36.2399", "injection": "342.22", "withdrawal": "0",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.56", "full": "59.79", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-02", "gasInStorage": "35.8973", "injection": "377.86", "withdrawal": "2.1",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.62", "full": "59.23", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-08-01", "gasInStorage": "35.5216", "injection": "369.45", "withdrawal": "15.9",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.58", "full": "58.61", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-31", "gasInStorage": "35.168", "injection": "452.34", "withdrawal": "0",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.75", "full": "58.02", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-30", "gasInStorage": "34.7157", "injection": "428.92", "withdrawal": "0",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.71", "full": "57.28", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-29", "gasInStorage": "34.2868", "injection": "373.37", "withdrawal": "7.1",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.6", "full": "56.57", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-28", "gasInStorage": "33.9205", "injection": "400.29", "withdrawal": "12",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.64", "full": "55.96", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-27", "gasInStorage": "33.5323", "injection": "401.49", "withdrawal": "0",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.66", "full": "55.32", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-26", "gasInStorage": "33.1308", "injection": "419.43", "withdrawal": "0",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.69", "full": "54.66", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-25", "gasInStorage": "32.7113", "injection": "289.6", "withdrawal": "0",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.48", "full": "53.97", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-24", "gasInStorage": "32.4217", "injection": "253.7", "withdrawal": "0",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.42", "full": "53.49", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-23", "gasInStorage": "32.168", "injection": "249.53", "withdrawal": "0",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "0.41", "full": "53.07", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-22", "gasInStorage": "31.9185", "injection": "204.93", "withdrawal": "288.7",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "-0.14", "full": "52.66", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-21", "gasInStorage": "32.0022", "injection": "156.02", "withdrawal": "376.7",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "-0.36", "full": "52.8", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-20", "gasInStorage": "32.2229", "injection": "70.64", "withdrawal": "580",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "-0.84", "full": "53.16", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-19", "gasInStorage": "32.7323", "injection": "56.1", "withdrawal": "597.8",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "-0.89", "full": "54", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-18", "gasInStorage": "33.2741", "injection": "48.97", "withdrawal": "613.7",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "-0.93", "full": "54.9", "info": []},
        {"name": "Uniper Energy Storage", "code": "21X000000001127H", "url": "21X000000001127H\/DE",
         "gasDayStart": "2022-07-17", "gasInStorage": "33.8388", "injection": "101.2", "withdrawal": "301",
         "workingGasVolume": "60.6108", "injectionCapacity": "1329.64", "withdrawalCapacity": "1910.74", "status": "C",
         "trend": "-0.33", "full": "55.83", "info": []}])


def get_gas_info(url):
    """
    :param url: url from API of each gas storage in germany
    :return: return list of [current day, current gasinStorage in %, current withdraw in GWh/d and current trend in %]
    """

    try:
        response = requests.get(url, headers={'x-key': "eb50f4b9062b4cfcf3103359c54151a3"})
        data = response.json()
        data = data.get("data")  # list of dictionaries containing gas information from last 30 days
        # print(data)

        provider_name = data[0].get("name")
        cur_day = data[0].get("gasDayStart")  # YYYY-MM-DD
        cur_gasInStorage = data[0].get("full")  # In Percent %
        cur_withdraw = data[0].get("withdrawal")
        cur_trend = data[0].get("trend")  # Change in Percent %

        return [provider_name, cur_day, cur_gasInStorage, cur_withdraw, cur_trend]

    except: IndexError  # If IndexError due to request error return default values

    provider_name = "Coming"
    cur_day = datetime.datetime.today().strftime("%d-%m-%y")
    cur_gasInStorage = 100
    cur_withdraw = 0
    cur_trend = 0

    return [provider_name, cur_day, cur_gasInStorage, cur_withdraw, cur_trend]



print(get_gas_info(uniper_url))
