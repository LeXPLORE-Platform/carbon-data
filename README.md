# LéXPLORE Carbon Data

## Project Information

The data is collected within the frame of the [LeXPLORE project](https://wp.unil.ch/lexplore/) on Lake Geneva. 
The data is used and displayed on the [Datalakes website](https://www.datalakes-eawag.ch/).

## Sample collection 

Sampling was conducted at the LéXPLORE platform near the city of Lausanne, Switzerland, where the maximum water depth is 
125 m (Wüest et al. 2021). Sampling for this study was conducted once per month from April 2022 to March 2023 during 
which a CTD cast was performed and water samples were collected from 1, 5, 10, 15, 20, and 50 m depth using a Niskin 
bottle. No sampling was conducted during January 2023. All water samples were filtered directly from the Niskin bottle 
using pre-combusted GF/F filters and collected into pre-combusted vials or bottles. DIC samples were collected into 
brand new 12 mL exetainer vials and stored at 4°C until analysis. Samples for 14C of DOC were collected into 250 or 
500 mL acid-washed amber Nalgene bottles and kept frozen until analysis. Samples for DOC concentration measurements 
were filtered into 40-mL borosilicate vials before being acidifed to pH 2 using HCl and sealed using acid-washed vial 
caps with silicone septa. 

## Concentration measurements

DIC concentrations were analyzed on a Shimadzu TOC-L Analyzer using the total inorganic carbon (IC) mode with a typical 
uncertainty of 1 mgC/L. DOC concentrations were also analyzed on a Shimadzu TOC-L Analyzer with a typical uncertainty of 
0.05 mg C/L. The DOC concentrations were determined using the high-temperature combustion method (Sharp et al. 2002). 
The instrument blank and DOC measurements were validated with low-carbon water (high-purity Milli-Q water), and 
reference materials NT170A and NT170B from the Umwelt Bundesamt. 

## Radiocarbon measurements

﻿Radiocarbon analyses were conducted using a MICADAS (MIni CArbon DAting System) Accelerator Mass spectrometer 
(AMS) equipped with a Gas Interface System (GIS) and CO2-accepting ion source at the Laboratory for Ion Beam Physics 
(LIP) in the Department of Physics at ETH Zurich (Synal and Wacker 2010; McIntyre et al. 2017). For DIC samples, 6 mL of 
sample water was transferred to a 12 mL exetainer vial and the headspace was purged with He for 3-4 minutes. Then 250 µl 
of phosphoric acid (85%) was added and the liberated CO2 introduced to the gas interface system (GIS) and measured with 
the gas ion source of MICADAS. C1 (IAEA) was used as a blank and C2 (IAEA) was used as a secondary reference material. 
For DO14C, samples were first freeze-dried to concentrate organic matter using a Christ Alpha 1-2 LDplus freeze dryer 
equipped with an oil-free diaphragm pump, and then acidifed to below pH 2 using phosphoric acid (85%) to remove DIC. 
Wet chemical oxidation (WCO) using aqueous persulfate was employed to convert DOC to CO2, after which the water was 
purged with He and 14C measured on the released CO2 as described above for DIC. Results for DO14C samples were corrected 
for constant contamination. Radiocarbon measurements are reported as age corrected ∆14C in per mil (‰) (Stenström et al. 
2011).

## Installation

:warning You need to have [git](https://git-scm.com/downloads) and [git-lfs](https://git-lfs.github.com/) installed in order to successfully clone the repository.

- Clone the repository to your local machine using the command: 

 `git clone https://renkulab.io/gitlab/lexplore/carbon-data.git`
 
 Note that the repository will be copied to your current working directory.

- Use Python 3 and install the requirements with:

 `pip install -r requirements.txt`

 The python version can be checked by running the command `python --version`. In case python is not installed or only an older version of it, it is recommend to install python through the anaconda distribution which can be downloaded [here](https://www.anaconda.com/products/individual). 

## Usage

### Adapt/Extend data processing pipeline

The python script `scripts/main.py` defines the different processing steps while the python script `scripts/sensors.py` contains the python class CarbonMeasurements with all the corresponding 
class methods to process the data. To add a new processing or visualization step, a new class method can be created in the `sensors.py` file and the step can be added in `main.py` file.
Python scripts are independent of the local file system.

## Data

The data can be found in the folder `data`. The data is structured as follows:

### Data Structure

- **Level 0**: Raw data collected from the different sensors.

- **Level 1**: Raw data stored to NetCDF file where attributes (such as sensors used, units, description of data, etc.) are added to the data, column with quality flags are added to the Level 1A data. Quality flag "1" indicates that the data point didn't pass the 
quality checks and further investigation is needed, quality flag "0" indicates that no further investiagion is needed.

## References

McIntyre, C. P., L. Wacker, N. Haghipour, T. M. Blattmann, S. Fahrni, M. Usman, T. I. Eglinton, and H. A. Synal. 2017. Online 13C and 14C Gas Measurements by EA-IRMS-AMS at ETH Zürich. Radiocarbon. Cambridge University Press. 893–903.

Sharp, J. H., C. A. Carlson, E. T. Peltzer, D. M. Castle-Ward, K. B. Savidge, and K. R. Rinker. 2002. Final dissolved organic carbon broad community intercalibration and preliminary use of DOC reference materials. Mar Chem 77: 239–253. doi:10.1016/S0304-4203(02)00002-6

Stenström, K. E., G. Skog, E. Georgiadou, J. Genberg, and A. Johansson. 2011. A guide to radiocarbon units and calculations.

Synal, H. A., and L. Wacker. 2010. AMS measurement technique after 30 years: Possibilities and limitations of low energy systems. Nucl Instrum Methods Phys Res B 268: 701–707. doi:10.1016/J.NIMB.2009.10.009

Wüest, A., D. Bouffard, | Jean Guillard, | Bastiaan, W. Ibelings, S. Lavanchy, M.-E. Perga, and N. Pasche. 2021. LéXPLORE: A floating laboratory on Lake Geneva offering unique lake research opportunities.doi:10.1002/wat2.1544
