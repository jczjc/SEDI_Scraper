from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import numpy as np

path = "C:/Users/zheng/Downloads/chromedriver_win32/chromedriver.exe"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"

chrome_options = Options()
chrome_options.add_argument("headless")
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

start_url = "https://www.sedi.ca/sedi/SVTReportsAccessController \
                ?menukey=15.03.00&locale=en_CA"

# Xpath (Finding Insiders)
Insider_info_by_issuer_button = "/html/body/table/tbody/tr[3]/td/table/tbody\
/tr[1]/td/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td[1]/input"
next_button = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table\
/tbody/tr[2]/td/form/table/tbody/tr[8]/td[2]/input"
Issuer_name_box = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/\
td/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/font/input"
month_jan = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/form/table\
/tbody/tr[4]/td/table/tbody/tr[9]/td[2]/font/select[1]/option[2]"
day_1st = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/form\
/table/tbody/tr[4]/td/table/tbody/tr[9]/td[2]/font/select[2]/option[2]"
year_box = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/form\
/table/tbody/tr[4]/td/table/tbody/tr[9]/td[2]/font/input"
search_button = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td\
/form/table/tbody/tr[4]/td/table/tbody/tr[14]/td[2]/font/font/input"
view_result_button = "/html/body/table[1]/tbody/tr[3]/td/table/tbody\
/tr/td/table[9]/tbody/tr/td[1]/font/a"
insider_name = "//td[contains(b, 'Insider Name')]/following-sibling::td/font"
insider_rs = "//td[contains(b, 'Insider Relationship')]/fo\
llowing-sibling::td/font"
refine_search_button = "//input[contains(@value, 'Refine Search Criteria')]"
alphabets_from = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/form/\
table/tbody/tr[4]/td/table/tbody/tr[5]/td[2]/font/select[1]/option[{}]"
alphabets_to = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/form/\
table/tbody/tr[4]/td/table/tbody/tr[5]/td[2]/font/select[2]/option[{}]"

# Xpath (Finding Transaction Histories)
Insider_trans_detail_button = "/html/body/table/tbody/tr[3]/td/t\
able/tbody/tr[1]/td/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[1]/input"
Insider_family_name = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td\
/table/tbody/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[7]/td/\
table/tbody/tr/td[1]/select/option[2]"
fam_name_box = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table\
/tbody/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[7]/td\
/table/tbody/tr[1]/td[2]/input"
given_name_box = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table\
/tbody/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[7]/td/table/tbody\
/tr[2]/td[2]/input"
select_all_issuer_d = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/\
table/tbody/tr/td/table/tbody/tr[4]/td/form/table/tbody\
/tr[16]/td[2]/p[2]/font/input"
select_all_debt = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/\
table/tbody/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[14]/td[2]\
/p[2]/font/input"
select_all_equity = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table\
/tbody/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[15]/td[2]/p[2]/font/input"
select_all_3rd_ = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table\
/tbody/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[17]/td[2]/p[2]/font/input"
search_trans = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table\
/tbody/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[22]/td[3]/input"
view_insider = "//td[contains(font, '{}')]/preceding::td[contains(font," \
               "'View')][position() = 1]"
_id = "//td[contains(font, '{}')]/preceding::td[contains(font,\
 '{}')][position()=1]/preceding-sibling::td[2]/font"
_id_check = "//td[contains(font, '{}')]/preceding-sibling::td/font/a"
see_remarks = "/html/body/table[1]/tbody/tr[3]/td/table/tbody/tr/td\
/table[13]/tbody/tr/td[2]/font/input"
date_of_trans = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table\
/tbody/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[8]/td/table/tbody/tr[3]\
/td[1]/select/option[2]"
from_jan = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/\
tbody/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[8]/td/table/tbody/\
tr[3]/td[2]/select[1]/option[2]"
from_1st = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/\
tbody/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[8]/td/table/tbody/\
tr[3]/td[2]/select[2]/option[2]"
from_year = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]\
/td/table/tbody/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[8]/td/table\
/tbody/tr[3]/td[2]/input"
to_dec = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody\
/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[8]/td/table/tbody/tr[4]\
/td[2]/select[1]/option[13]"
to_31st = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody\
/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[8]/td/table/tbody/tr[4]/td[2]\
/select[2]/option[32]"
to_year = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody/tr\
/td/table/tbody/tr[4]/td/form/table/tbody/tr[8]/td/table\
/tbody/tr[4]/td[2]/input"
error = "//td[contains(font, 'Error')]"
to_june = "/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table\
/tbody/tr/td/table/tbody/tr[4]/td/form/table/tbody/tr[8]/td/table/tbody\
/tr[4]/td[2]/select[1]/option[7]"
to_22nd = "/html/body/table/tbody/tr[3]/td/table\
/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[4]/td\
/form/table/tbody/tr[8]/td/table/tbody/tr[4]/td[2]/select[2]/option[23]"

HEADERS = ['Legend', 'Issuer name', 'Insider Name',
           'Security designation', 'Transaction ID', 'Date of transaction',
           'Date of filing',
           'Ownership type (and registered holder, if applicable)',
           'Nature of transaction', 'Number or value acquired or disposed of',
           'Unit price or exercise price', 'Closing balance',
           "Insider's calculated balance", 'Conversion or exercise price',
           'Date of expiry or maturity',
           'Underlying security designation',
           'Equivalent number or value of underlying '
           'securities acquired or disposed of',
           'Closing balance of equivalent number or '
           'value of underlying securities',
           'General remarks']

HEADERS_MATCH = [2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 17, 18, 19]


class Company:
    """
    A top 700 company listed in TSX or TSXV

    === Attributes ===
    comp_name: The name of the company as provided in the CSV file
    insiders: The insiders of this company
    """
    # Attribute Types
    comp_name: str
    insiders: any([list, bool])

    def __init__(self, name) -> None:
        """
        Initiate an instance of Company.
        self.insiders is initially None.
        """
        self.comp_name = name
        self.insiders = None

    def find_insiders(self):
        """
        Return the list of insiders and let self.insiders refer to it if we
        have yet to find the list of insiders. Else, just return the insiders.
        """
        if self.insiders is None:
            # Get to the page with all insiders
            browser = webdriver.Chrome(executable_path=path,
                                       options=chrome_options)
            self._get_insiders_page(browser)

            # See if all data are loaded, if not, break down alphabetically
            try:
                browser.find_element_by_xpath("//td[contains(font, 'Error')]")
                refine = browser.find_element_by_xpath(refine_search_button)
                refine.click()
                self.insiders = _error_get_insiders(browser)

            # If loaded, carry on with the usual method
            except Exception:
                self.insiders = _no_error_get_insiders(browser)
            browser.quit()
        return self.insiders

    def _get_insiders_page(self, browser):
        """
        """
        browser.get(start_url)
        select_info_by_issuer = browser \
            .find_element_by_xpath(Insider_info_by_issuer_button)
        select_info_by_issuer.click()
        next_ = browser.find_element_by_xpath(next_button)
        next_.click()
        enter_name = browser.find_element_by_xpath(Issuer_name_box)
        enter_name.send_keys(self.comp_name)
        month = browser.find_element_by_xpath(month_jan)
        month.click()
        day = browser.find_element_by_xpath(day_1st)
        day.click()
        year = browser.find_element_by_xpath(year_box)
        year.clear()
        year.send_keys("2010")
        search = browser.find_element_by_xpath(search_button)
        search.click()
        view_company = browser.find_element_by_xpath(view_result_button)
        view_company.click()


def _no_error_get_insiders(browser):
    """

    """
    insider_list = []
    insiders = browser.find_elements_by_xpath(insider_name)
    insiders_rs = browser.find_elements_by_xpath(insider_rs)
    assert len(insiders) == len(insiders_rs)
    for i in range(len(insiders)):
        insiders_rs_str = insiders_rs[i].text
        if not ("1 -" in insiders_rs_str or "2 -" in insiders_rs_str):
            insider_list.append(insiders[i].text)
    return insider_list


def _error_get_insiders(browser):
    """
    """
    insider_list = []
    for num in range(2, 28):
        _from = browser.find_element_by_xpath(alphabets_from.format(num))
        _to = browser.find_element_by_xpath(alphabets_to.format(num))
        _from.click()
        _to.click()
        search = browser.find_element_by_xpath(search_button)
        search.click()
        # Check if there are insiders of that Alphabet
        try:
            browser.find_element_by_xpath("//td[contains(font, 'Error')]")
        except Exception:
            view_company = browser.find_element_by_xpath(view_result_button)
            view_company.click()
            insider_list = insider_list + \
                           _no_error_get_insiders(browser)
        refine = browser.find_element_by_xpath(refine_search_button)
        refine.click()
    return insider_list


class Insider(Company):
    """
    An insider in one of the top 700 companies listed on TSX or TSXV

    === Attributes ===
    family_name: The insider's family name. First box on SEDI
    given_name: The insider's given name. The second box on SEDI
    full_name: The insider's full name.
    transaction: A pandas dataframe storing all of the insider's transaction
                 history, or the status if there is an error.
    """
    # Attribute types
    family_name: str
    given_name: str
    full_name: str
    _id_: any([str, bool])
    transactions: any([pd.DataFrame, bool, str])

    def __init__(self, company: str, name: str):
        """
        Initiate an Insider Instance
        """
        Company.__init__(self, company)
        if ", " in name:
            name_list = name.split(", ")
            self.family_name = name_list[0]
            self.given_name = name_list[1]
        else:
            self.family_name = name
            self.given_name = name
        self.transactions = None
        self.full_name = name
        self._id_ = None

    def _verify_insider(self, browser):
        """
        Make sure that the data of the insider whom we are looking for is
        available for the particular time frame
        """
        try:
            view = browser.find_element_by_xpath(view_insider.format(
                self.comp_name))
            _id_ = browser.find_element_by_xpath(_id.format(self.comp_name,
                                                            self.full_name))
            self._id_ = _id_.text
            view.click()
            return self._id_
        except Exception:
            return "Error: Insider data not found for this time frame"

    def _verify_insider_id(self, browser):
        """
        """
        try:
            view = browser.find_element_by_xpath(_id_check.format(self._id_))
            view.click()
        except Exception:
            return "Error: Insider data not found for this time frame"

    def _get_transac_pg(self, browser):
        """
        Get to the page with all transactions and return the id number of the
        insider.
        """
        browser.get(start_url)
        insid_trans_button = browser. \
            find_element_by_xpath(Insider_trans_detail_button)
        insid_trans_button.click()
        next_ = browser.find_element_by_xpath(next_button)
        next_.click()
        insider_fam_name_option = browser. \
            find_element_by_xpath(Insider_family_name)
        insider_fam_name_option.click()
        fam_name = browser.find_element_by_xpath(fam_name_box)
        fam_name.send_keys(self.family_name)
        given_name = browser.find_element_by_xpath(given_name_box)
        given_name.send_keys(self.given_name)
        all_deriv_opt = browser.find_element_by_xpath(select_all_issuer_d)
        all_deriv_opt.click()
        all_debt_opt = browser.find_element_by_xpath(select_all_debt)
        all_debt_opt.click()
        all_equity_opt = browser.find_element_by_xpath(select_all_equity)
        all_equity_opt.click()
        all_3rd_d = browser.find_element_by_xpath(select_all_3rd_)
        all_3rd_d.click()
        search = browser.find_element_by_xpath(search_trans)
        search.click()
        # Should add if this insider has any transaction history at all, or
        # already included in get_transactions
        # Choose the insider matches with the company
        return self._verify_insider(browser)

    def _scrape_data(self, browser):
        """
        Ask for transaction remarks and scrape the all the data.
        Return a dataframe with all the data from the page.
        """
        df = create_df()
        try:  # Check for a blank page
            remarks = browser.find_element_by_xpath(see_remarks)
        except Exception:
            return "Error: A blank page was returned for transaction"
        remarks.click()
        tables = browser.find_elements_by_tag_name("table")
        _populate_df(tables, df, self.full_name)
        return _clean_df(df)

    def _load_data(self, browser):
        """
        """
        try:  # Check if there are too much data to load on the page
            browser.find_element_by_xpath(error)
        except Exception:  # Only if the page is fine or it is a blank page
            return self._scrape_data(browser)
        return self._error_load_data(browser)

    def _error_load_data(self, browser):
        """
        """
        df = create_df()
        _get_refine_pg(browser)
        for i in range(2020, 2021):
            year_from = browser.find_element_by_xpath(from_year)
            year_to = browser.find_element_by_xpath(to_year)
            year_from.clear()
            year_to.clear()
            year_from.send_keys(i)
            year_to.send_keys(i)
            search = browser.find_element_by_xpath(search_trans)
            search.click()
            result_1 = self._verify_insider_id(browser)
            if result_1 is None:
                data = self._scrape_data(browser)
                if type(data) == str:
                    print(data + f" {i}" + f" {self.full_name}")
                    browser.back()
                    refine = browser.find_element_by_xpath(refine_search_button)
                    refine.click()
                    continue
                else:
                    df = df.append(data, ignore_index=True)
            refine = browser.find_element_by_xpath(refine_search_button)
            refine.click()

        year_from = browser.find_element_by_xpath(from_year)
        year_to = browser.find_element_by_xpath(to_year)
        year_from.clear()
        year_to.clear()
        year_from.send_keys(2021)
        year_to.send_keys(2021)
        june_ = browser.find_element_by_xpath(to_june)
        june_.click()
        _22nd = browser.find_element_by_xpath(to_22nd)
        _22nd.click()
        search = browser.find_element_by_xpath(search_trans)
        search.click()
        result_1 = self._verify_insider_id(browser)
        if result_1 is None:
            data = self._scrape_data(browser)
            if type(data) == str:
                print(data + f" {2021}" + f" {self.full_name}")
            else:
                df = df.append(data, ignore_index=True)
        else:
            print(result_1 + f" {2021}" + f" {self.full_name}")
        return df

    def find_transactions(self):
        """
        Return the dictionary of transaction history let self.transactions refer
        to it if we have yet to find the history. Return it if already found.
        """
        if self.transactions is None:
            browser = webdriver.Chrome(executable_path=path,
                                       options=chrome_options)
            # Try to get the transaction history page for this insider
            _id_ = self._get_transac_pg(browser)
            # If getting transaction page is successful
            if _id_ != "Error: Insider data not found for this time frame":
                self.transactions = self._load_data(browser)
            # If anything goes wrong while finding transaction page
            else:
                self.transactions = _id_
            browser.quit()
        return self.transactions


def create_df():
    """
    """
    df = pd.DataFrame(columns=HEADERS)
    return df


# TODO: Test _populate_df
def _populate_df(web_elements, dataframe, name):
    """
    """
    for table in web_elements[10:]:
        row_text = table.text.strip()
        if row_text == "":
            continue
        elif row_text[0].isdigit() or \
                any(row_text[0] == char for char in "OA"):
            actual = ["", name, ""]
            row_data = table.find_elements_by_tag_name("td")
            counter = 0
            for data in row_data:
                if counter == 2:
                    actual = [data.text] + actual
                elif counter == 3:
                    actual[0] = actual[0] + data.text.strip()
                elif counter == 11:
                    actual[-1] = actual[-1] + data.text.strip()
                elif counter in HEADERS_MATCH:
                    actual.append(data.text.replace("\n", ""))
                counter += 1
            actual.append("")
            dataframe.loc[len(dataframe)] = actual
        elif "General remarks" in table.text:
            dataframe.loc[len(dataframe) - 1, "General remarks"] = table.text
        elif "Security designation" in table.text:
            dataframe.loc[len(dataframe), "Security designation"] = table.text
        elif "Issuer name" in table.text:
            dataframe.loc[len(dataframe), "Issuer name"] = table.text.strip()


def _clean_df(dataframe):
    """
    Populate the Security Designation column with the right designations,
    and populate the Issuer name column with the right issuer names,
    remove the excess columns with no data entry
    """
    dataframe["Security designation"].replace(r'^\s*$', np.NaN,
                                              regex=True, inplace=True)
    dataframe["Security designation"].fillna(method="ffill", inplace=True)
    dataframe["Issuer name"].replace(r'^\s*$', np.NaN,
                                     regex=True, inplace=True)
    dataframe["Issuer name"].fillna(method="ffill", inplace=True)
    return dataframe[dataframe['Transaction ID'].notna()].reset_index(drop=True)


def _get_refine_pg(browser):
    """
    """
    refine = browser.find_element_by_xpath(refine_search_button)
    refine.click()
    sort_by = browser.find_element_by_xpath(date_of_trans)
    sort_by.click()
    jan_ = browser.find_element_by_xpath(from_jan)
    jan_.click()
    first_ = browser.find_element_by_xpath(from_1st)
    first_.click()
    dec_ = browser.find_element_by_xpath(to_dec)
    dec_.click()
    _31st = browser.find_element_by_xpath(to_31st)
    _31st.click()


# error = ['Toronto-Dominion Bank (The)', 'Bank of Nova Scotia (The)',
# 'Newmont Corporation', 'Newcrest Mining Limited', 'Ceridian HCM Holding
# Inc.', 'First Quantum Minerals Ltd.', 'Canadian Tire Corporation Limited',
# 'Descartes Systems Group Inc. (The)', 'Genworth MI Canada Inc.', 'Osisko
# Gold Royalties Ltd.', 'Maxar Technologies Inc.', 'Winpak Ltd.', 'Domtar
# Corporation', 'Sprott Physical Silver Trust', 'Morneau Shepell Inc.',
# 'North West Company Inc.', 'PIMCO Monthly Income Fund (Canada)', 'Badger
# Daylighting Ltd.', 'CNOOC Limited', 'BMO Core Plus Bond Fund', 'Cogeco
# Inc.', 'Village Farms International Inc.', 'Canadian General Investments
# Limited', 'Sierra Wireless Inc.', 'Resolute Forest Products Inc.', 'CanWel
# Building Materials Group Ltd.', 'Royal Canadian Mint - Canadian Gold
# Reserves', 'Discovery Metals Corp.', 'Midas Gold Corp.', 'McEwen Mining
# Inc.', 'Andrew Peller Limited/Andrew Peller Limitee', 'Anglo Pacific Group
# PLC', 'Global Water Resources, Inc.', 'Westaim Corporation (The)', 'PIMCO
# Tactical Income Fund', 'Eskay Mining Corp.', 'Jervois Mining Ltd.',
# 'Reconnaisance Energy Africa Ltd.', 'Caldas Gold Corp.', 'CI First Asset
# Enhanced Short Duration Bond Fund', 'Abraplata Resource Corp.', 'Quisitive
# Technology Solutions Inc.', 'Purpose Gold Bullion Fund', 'Evolve Cyber
# Security Index Fund', 'Picton Mahoney Fortified Income Alternative Fund',
# 'Los Andes Copper Limited', 'Loop Insights Inc.', 'Canopy Rivers Inc.',
# 'Protech Home Medical Corp.', 'Real Brokerage Inc. (The)', 'Aberdeen
# Asia-Pacific Income Investment Company Ltd.', 'Purpose Core Dividend Fund',
# 'Vizsla Resources Corp.']

if __name__ == "__main__":
    # error = ['Toronto-Dominion Bank (The)', 'Bank of Nova Scotia (The)',
    # 'Newmont Corporation', 'Newcrest Mining Limited', 'Ceridian HCM Holding
    # Inc.', 'First Quantum Minerals Ltd.', 'Canadian Tire Corporation
    # Limited', 'Descartes Systems Group Inc. (The)', 'Genworth MI Canada
    # Inc.', 'Osisko Gold Royalties Ltd.', 'Maxar Technologies Inc.', 'Winpak
    # Ltd.', 'Domtar Corporation','Morneau
    # Shepell Inc.', 'North West Company Inc.', 'PIMCO Monthly Income Fund (
    # Canada)', 'Badger Daylighting Ltd.', 'CNOOC Limited', 'BMO Core Plus
    # Bond Fund', 'Cogeco Inc.', 'Village Farms International Inc.',
    # 'Canadian General Investments Limited', 'Sierra Wireless Inc.',
    # 'Resolute Forest Products Inc.', 'Royal Canadian Mint - Canadian Gold
    # Reserves', 'Discovery Metals Corp.', 'Midas Gold Corp.', 'McEwen Mining
    # Inc.', 'Andrew Peller Limited/Andrew Peller Limitee', 'Anglo Pacific
    # Group PLC', 'Global Water Resources, Inc.', 'Westaim Corporation (
    # The)', 'PIMCO Tactical Income Fund', 'Eskay Mining Corp.', 'Jervois
    # Mining Ltd.', 'Reconnaisance Energy Africa Ltd.', 'Caldas Gold Corp.',
    # 'CI First Asset Enhanced Short Duration Bond Fund', 'Abraplata Resource
    # Corp.', 'Quisitive Technology Solutions Inc.', 'Purpose Gold Bullion
    # Fund', 'Evolve Cyber Security Index Fund', 'Picton Mahoney Fortified
    # Income Alternative Fund', 'Los Andes Copper Limited', 'Canopy Rivers
    # Inc.', 'Protech Home Medical Corp.', 'Real Brokerage Inc. (The)',
    # 'Aberdeen Asia-Pacific Income Investment Company Ltd.', 'Purpose Core
    # Dividend Fund', 'Vizsla Resources Corp.'] df = pd.read_csv(
    # "tsx-top700.csv") # print(df) # print(len(error)) new_df =
    # pd.DataFrame() for company in df["name"]: if company in error: row =
    # df.loc[df["name"] == company] new_df = new_df.append(row,
    # ignore_index=True) new_df.to_csv("companies_not_able_to_find.csv")
    insider_1 = Insider("Royal Bank of Canada", "Nicholls, Paul Edward")
    result = insider_1.find_transactions()
    result.to_csv("trial.csv")
    insider_2 = Insider("Shopify Inc.", "Johnston, Colleen")
    result_2 = insider_2.find_transactions()
    # result.to_csv("cj.csv")
    result_2.to_csv("trial.csv", mode="a", header=False, index=False)
    # pd_ll = pd.DataFrame.from_dict({"TD": [1,2,3,4,5]}, orient="index")
    # print(pd_ll)
    # pd_ll.to_csv("error.csv")
    # pd_ll.to_csv("error.csv", mode="a", header=False)


s = {'Shopify Inc.': ['BVP VII Special Opportunity Fund L.P.', 'Deer VII & Co. Ltd.', 'FirstMark Capital I, L.P.', 'FirstMark Capital, LLC'], 'Royal Bank of Canada': ['MacLachlan, Graham Ross', 'Nicholls, Paul Edward', "O'Brien, David Peter", 'Pinto, Carlos', 'sellitto, Antonio', 'Steven, DeCicco', 'Stymiest, Barbara Gayle', 'Turcke, Maryann'], 'Canadian National Railway Company': ['Cascade Investment, L.L.C.', 'Gray, Denise', 'Howell, Justin M.', "O'CONNOR, JAMES E.", 'Quirke, Helen'], 'Enbridge Inc.': ['Cazalot, Jr., Clarence Peter', 'Cillis, Laura Ann', 'DuPont, Bonnie Dianne Rose', 'Leslie, David Arthur', "Levesque, D'Arcy Lloyd", 'Lewis, Melville George', 'Petty, Jr., George Kibbe', 'Roberts, Ernest F. H.', 'Szmurlo, Jr., Charles Joseph']}
