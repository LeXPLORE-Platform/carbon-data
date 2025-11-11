# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
import pylake
from datetime import datetime, timedelta, timezone
from general_functions import GenericInstrument, get_bathymetry, pressure_correction

class CarbonMeasurements(GenericInstrument):
    def __init__(self, *args, **kwargs):
        super(CarbonMeasurements, self).__init__(*args, **kwargs)
        self.general_attributes = {
            "institution": "Eawag",
            "source": "Carbon measurements",
            "references": "LéXPLORE carbon measurements",
            "history": "See history on Renku",
            "conventions": "CF 1.7",
            "comment": "Carbon measurements collected on Lexplore Platform in Lake Geneva",
            "title": "LéXPLORE Carbon Measurements",
            "latitude": 46.5002275,
            "longitude": 6.66083528,
        }
        self.dimensions = {
            'time': {'dim_name': 'time', 'dim_size': None},
            'depth': {'dim_name': 'depth', 'dim_size': None}
        }
        self.variables = {
            'time': {'var_name': 'time', 'dim': ('time',), 'unit': 'seconds since 1970-01-01 00:00:00', 'long_name': 'time'},
            'depth': {'var_name': 'depth', 'dim': ('depth',), 'unit': 'm', 'long_name': 'Depth'},
            'DI14C': {'var_name': 'DI14C', 'dim': ('depth','time',), 'unit': '‰', 'long_name': '∆14C of dissolved inorganic carbon'},
            'DI14C_error': {'var_name': 'DI14C_error', 'dim': ('depth', 'time',), 'unit': '‰', 'long_name': 'Uncertainty in ∆14C of dissolved inorganic carbon'},
            'DO14C': {'var_name': 'DO14C', 'dim': ('depth', 'time',), 'unit': '‰', 'long_name': '∆14C of dissolved inorganic carbon'},
            'DO14C_error': {'var_name': 'DO14C_error', 'dim': ('depth', 'time',), 'unit': '‰', 'long_name': 'Uncertainty in ∆14C of dissolved inorganic carbon'},
            'DOC': {'var_name': 'DOC', 'dim': ('depth', 'time',), 'unit': 'mg/L', 'long_name': 'Concentration of dissolved organic carbon'},
            'DOC_error': {'var_name': 'DOC_error', 'dim': ('depth', 'time',), 'unit': 'mg/L', 'long_name': 'Uncertainty in concentration of dissolved organic carbon'},
            'DIC': {'var_name': 'DIC', 'dim': ('depth', 'time',), 'unit': 'mg/L', 'long_name': 'Concentration of dissolved inorganic carbon'},
            'DIC_error': {'var_name': 'DIC_error', 'dim': ('depth', 'time',), 'unit': 'mg/L', 'long_name': 'Uncertainty in concentration of dissolved inorganic carbon'},
        }

    def read_data(self, file):
        self.log.info("Reading data from {}".format(file), 1)
        try:
            df = pd.read_csv(file)
            df['date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
            df["time"] = df["date"].apply(lambda x: datetime.timestamp(x))
            df = df.sort_values(by='date')
            self.data["time"] = df['time'].unique()
            self.data["depth"] = df['Depth'].unique()
            for variable in self.variables:
                if len(self.variables[variable]["dim"]) == 2:
                    self.data[variable] = df.pivot(index='date', columns='Depth', values=variable).T
        except Exception as e:
            self.log.info("Failed to read data from {}".format(file), indent=1)
            print(e)
            return False
        return True
