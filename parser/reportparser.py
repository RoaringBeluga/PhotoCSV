import csv

from parser import photometers
import re

from utilities.misc import bugprint


class ReportParser:
    regex_set = None # Regex set for parsing the report
    equipment = None # Equipment that produced the report
    rows = None # Report parsing results

    def __init__(self):
        self.rows = [] # Nothing to see here... yet.


    def parse_equipment(self, page):
        # Search for the equipment signature in the page text
        for key, value in photometers.photometer_regexes.items():
            bugprint(f'Key: {key} Value: {value}')
            match = re.search(value, page)
            # Did we get the equipment? Return it and set the correct regex
            if match:
                self.regex_set = photometers.report_regexes[key]
                bugprint(f'RegEx set: {key}')
                self.equipment = key
                return key
        # No matching regex set found
        # Set self.equipment to None
        # TODO: Add checks for this in report parser
        self.equipment = None
        return None


    def write_csv(self, filename):
        # Writes data to the file <filename>
        with open(filename, mode='w') as outfile:
            fields = ['power', 'flux', 'CCT', 'Ra', 'PF', 'lambda', 'sample']
            csv_writer = csv.DictWriter(
                outfile,
                fieldnames=fields,
                delimiter=';',
                quotechar="'",
                quoting=csv.QUOTE_NONNUMERIC
            )
            csv_writer.writeheader()
            csv_writer.writerows(self.rows)

    def get_numeric_value(self, regex, data):
        # Returns numeric value from the report
        bugprint(f'\tusing RegEx: {regex}')
        match = re.search(regex, data).group()
        if match:
            match = re.search('[0-9.]+', match).group()
            match = re.sub(r'../utilities', r',', match)
            bugprint(f'\t\t{match}')
            return match
        else:
            bugprint(f'\t\t{match}')
            return None


    def get_string_value(self, regex_info, data):
        # Returns string value. <data> parameter has regex and cut positions in it
        # See: utilities/photometers.py
        bugprint(f'\tusing RegEx: {regex_info}')
        match = re.search(regex_info['regex'], data).group()
        if match:
            match = match[regex_info['cut']:]
            bugprint(f'\t\t{match}')
            return match
        else:
            bugprint(f'\t\t{match}')
            return None


    def parse_report(self, page_data):
        # bugprint(f'Page data: {page_data}')
        self.parse_equipment(page_data)
        # Bug out if there's no equipment info found
        if self.equipment is None:
            bugprint(f'Page data contains no recognized equipment info:\n{page_data}')
            return
        row_data = dict()
        bugprint('\t• Power')
        row_data['power'] = self.get_numeric_value(self.regex_set['power'], page_data)
        bugprint('\t• PF')
        row_data['PF'] = self.get_numeric_value(self.regex_set['PF'], page_data)
        bugprint('\t• flux')
        row_data['flux'] = self.get_numeric_value(self.regex_set['flux'], page_data)
        bugprint('\t• Ra')
        row_data['Ra'] = self.get_numeric_value(self.regex_set['Ra'], page_data)
        bugprint('\t• CCT')
        row_data['CCT'] = self.get_numeric_value(self.regex_set['CCT'], page_data)
        bugprint('\t• 𝝺')
        row_data['lambda'] = self.get_numeric_value(self.regex_set['lambda'], page_data)
        row_data['sample'] = self.get_string_value(self.regex_set['sample'], page_data).strip(' ')
        bugprint(f'Row data: {row_data}')
        self.rows.append(row_data)