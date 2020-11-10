# Used for parsing report PDF data
report_regexes = {
    'cms_2s_plus_zh': {
        'power': '功率: [0-9.]+W',
        'PF': r'功率因数: [0-9.]+\s',
        'flux': r'光通量: [0-9.]+\slm',
        'Ra': r'Ra=[-\s]*[0-9.]+[0-9]',
        'CCT': r'Tc=[\d]+K',
        'lambda': r'主波长: [0-9.]+nm',
        'sample': {'regex': r'产品型号:[\s]*[A-Z0-9-]+', 'cut': 5}
    },
    'cms_2s_plus_en': {
        'power': 'Power:[\s]*[0-9]+[.]{1}[0-9]{2}W',
        'PF': r'Factor:[\s]*[0-9.]+\s',
        'flux': r'Luminous Flux:[\s]*[0-9.]+[\s]*lm',
        'Ra': r'Ra=[-\s]*[0-9.]+[0-9]',
        'CCT': r'Tc=[\d]+K',
        'lambda': r'Dominant Wavelength:[\s]*[0-9]+[.]{1}[0-9]{1}nm',
        'sample': {'regex': r'Product Spec:[\s]*[A-Z0-9-\s]+[\s]{2}[\s]*}', 'cut': 13}
    },
    'everfine_haas_1200_zh': {
        'power': r'=[\s]*[\d.]+[\s]*W',
        'PF': r'PF[\s]*=[\s]*0[.][\d]{4}',
        'flux': r'=[\s]*[\d.]+[\s]*[l]*m',
        'Ra': r'Ra=[\s-]*[0-9.]+\s',
        'CCT': r'CCT=[\d]+K',
        'lambda': r'd=[-\s]*[\d.]+nm',
        'sample': {'regex': r'产品型号:[\s]*[A-Z0-9-]+', 'cut': 5}
    },
    'wolnic_maybe_en': {
        'power': r'Power:[\d.]+[\s]*W',
        'PF': r'Power Factor:0[.][\d]{4}',
        'flux': r'Flux:[\d.]+lm',
        'Ra': r'Ra=[0-9.]+',
        'CCT': r'Correlated Color Temperature:[0-9]+K',
        'lambda': r'Dominate Wavelength:[\d.]+nm',
        'sample': {'regex': r'Sample Name:[A-Z0-9-]+', 'cut': 12}
    }

}

# Used to determine the correct regex set for the report
photometer_regexes = {
    'cms_2s_plus_zh': r'创惠仪器[\s]*CMS-2S',
    'cms_2s_plus_en': r'Inventfine[\s]*CMS-2S',
    'everfine_haas_1200_zh': r'HAAS-1200',
    'wolnic_maybe_en': r'信华电器检测中心'
}

"""
When run from the command line, this script will dump regexes
into the YAML file named confid.yaml.
This functionality is just for fun.
"""
if __name__ == '__main__':
    import yaml
    config_info = dict()
    config_info['version_info'] = {
        'version': '1.0',
        'slug': 'Copyleft (L) 2020. All Rites Reversed.'
    }
    config_info['report_regexes'] = report_regexes
    config_info['photometer_regexes'] = photometer_regexes

    with open('config.yaml', mode='w') as config_dump:
        yaml.dump(
            config_info,
            config_dump,
            default_flow_style=False,
            encoding='utf-8'
        )
