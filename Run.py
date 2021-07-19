import time
import pandas as pd
import numpy as np
import csv
from multiprocessing import Process, Manager
from Scraper import Company, Insider, create_df

company_csv = pd.read_csv("tsx-top700.csv")
TSX_700 = company_csv["name"]
company_insiders = pd.read_csv("insider_names_remain.csv", index_col=0, header=None)


def get_all_insiders(companies):
    """
    Return a dictionary with the company name as the key and a list of insiders
    as the value
    """
    record = {}
    for comp in companies:
        # Try if the company can be found
        try:
            firm = Company(comp)
            record[comp] = firm.find_insiders()
        except Exception:
            record[comp] = ["Error"]
    return record


def get_all_insider_records(company_list, no):
    """
    """
    error = {}
    first_comp = company_list[0]
    first_insiders = company_insiders.loc[first_comp]
    first_result = _get_company_insider_records(first_comp, first_insiders)
    first_result[0].to_csv(f"C:/Users/zheng/PycharmProjects/Webscraper/Data"
                           f"/data_file_{no}.csv")
    error[first_comp] = first_result[1]
    error_df = pd.DataFrame.from_dict(error, orient="index")
    error_df.to_csv(f"C:/Users/zheng/PycharmProjects/Webscraper/Data"
                    f"/Error_Insiders_{no}.csv", mode="a", header=False)
    print(f"{first_comp} is done")
    for comp in company_list:
        insiders = company_insiders.loc[comp]
        if "Error" not in insiders.values:
            error = {}
            result = _get_company_insider_records(comp, insiders)
            result[0].to_csv(f"C:/Users/zheng/PycharmProjects/Webscraper/Data"
                             f"/data_file_{no}.csv", mode="a", header=False
                             )
            error[comp] = result[1]
            error_df = pd.DataFrame.from_dict(error, orient="index")
            error_df.to_csv(f"C:/Users/zheng/PycharmProjects/Webscraper/Data"
                            f"/Error_Insiders_{no}.csv", mode="a", header=False)
            print(f"{comp} is done")


def _get_company_insider_records(company_name, insider_list):
    """
    """
    df = create_df()
    error = []
    for insider in insider_list:
        if insider is not np.NaN:
            _insider = Insider(company_name, insider)
            result = _insider.find_transactions()
            if type(result) == pd.DataFrame:
                df = df.append(result, ignore_index=True)
            else:
                error.append(insider)
    return df, error


if __name__ == "__main__":
    # Writing dictionary into csv
    # with open('insider_names.csv', 'w') as csv_file:
    #     writer = csv.writer(csv_file)
    #     for key, value in result.items():
    #         writer.writerow([key, value])
    # manager = Manager()
    # error_ = manager.dict()
    # print(error_)
    error_ = ["The Toronto-Dominion Bank", "Bank of Nova Scotia, The",
             "First Quantum Minerals Ltd", "Canadian Tire Corporation, Limited",
             "The Descartes Systems Group Inc.", "OSISKO GOLD ROYALTIES LTD",
             "Maxar Technologies Ltd.", "Winpak Ltd", "Domtar Inc.",
             "The North West Company Inc.", "Badger Daylighting Inc.",
             "CNOOC Canada Inc.", "Cogeco Inc",
             "Village Farms International, Inc.",
             "Canadian General Investments, Limited",
             "Sierra Wireless, Inc.", "AbitibiBowater Inc.",
             "CanWel Building Materials Ltd.", "Discovery Silver Corp.",
             "Perpetua Resources Corp.", "Andrew Peller Limited",
             "GWR Global Water Resources Corp.", "The Westaim Corporation",
             "Vintage Wine Estates, Inc.", "Eskay Mining Corp",
             "Jervois Mining Limited", "Reconnaissance Energy Africa Ltd.",
             "Aris Gold Corporation", "AbraSilver Resource Corp.",
             "Quisitive Technology Solutions, Inc.", "Los Andes Copper Ltd.",
             "FOBI AI Inc.", "RIV Capital Inc.", "Quipt Home Medical Corp.",
             "The Real Brokerage Inc.",
             "Aberdeen Asia-Pacific Income Investment Company Limited",
             "Vizsla Silver Corp."]

    jobs = []
    list_1 = error_[1:9]
    list_2 = error_[17:18]
    # list_3 = error_[18:27]
    # list_4 = error_[27:]
    # print(list_1)
    # print(list_2)
    # print(list_3)
    # print(list_4)
    p_0 = Process(target=get_all_insider_records, args=(list_1, 0))
    p_1 = Process(target=get_all_insider_records, args=(list_2, 1))
    # p_2 = Process(target=get_all_insider_records, args=(list_3, 2))
    # p_3 = Process(target=get_all_insider_records, args=(list_4, 3))
    jobs.append(p_0)
    jobs.append(p_1)
    # jobs.append(p_2)
    # jobs.append(p_3)
    p_0.start()
    p_1.start()
    # p_2.start()
    # p_3.start()
    for proc in jobs:
        proc.join()

    # get_all_insider_records(TSX_700)
    # df = pd.DataFrame()
    # for i in range(4):
    #     new_df = pd.read_csv(f"C:/Users/zheng/PycharmProjects/Webscraper/Data"
    #                          f"/Error_Insiders_{i}.csv").iloc[:, 1:]
    #     df = df.append(new_df, ignore_index=True)
    # df.to_csv("error_insiders_v1.csv")

    # print(len(error))
    # result = get_all_insiders(error)
    # pd.DataFrame.from_dict(data=result, orient='index').\
    #     to_csv('insider_names_remain.csv', header=False)


