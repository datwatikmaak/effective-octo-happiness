import configparser


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        if 'tox' not in self.config:
            return []

        if '\n' not in self.config['tox']['envlist']:
            return sorted([
                v.strip() for v in self.config['tox']['envlist'].split(",")
            ])

        con = []
        for line in self.config['tox']['envlist'].strip().splitlines():
            if ',' in line:
                con += line.split(',')
            else:
                con.append(line)
        return sorted([v for v in con if v != ''])

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        py_versions = {
            self.config[key]['basepython']
            for key in self.config.keys()
            if 'basepython' in self.config[key]
        }

        return list(py_versions)
