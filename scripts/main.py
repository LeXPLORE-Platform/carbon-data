# -*- coding: utf-8 -*-
import os
import sys
import json
import yaml
from sensors import CarbonMeasurements
from general_functions import logger



log = logger("scripts/logs/main_lexplore_carbon_data")
log.initialise("Processing carbon data recorded at the Lexplore platform")

log.begin_stage("Collecting inputs")
with open("scripts/input_python.yaml", "r") as f:
    directories = yaml.load(f, Loader=yaml.FullLoader)

for directory in directories.values():
    if not os.path.exists(directory):
        os.makedirs(directory)

log.info("Reprocessing complete dataset from {}".format(directories["Level0_dir"]), indent=1)
files = os.listdir(directories["Level0_dir"])
files = [os.path.join(directories["Level0_dir"], f) for f in files]
files.sort()
log.end_stage()

log.begin_stage("Processing raw data")
log.info("Processing {} files.".format(len(files)))
for file in files:
    sensor = CarbonMeasurements(log=log)
    if sensor.read_data(file):
        sensor.export(directories["Level1_dir"], "L1_Carbon", output_period="file")
log.end_stage()
