import untangleai
from untangleai.generate_report import generate_report
from untangleai.untangle_whatif import run_whatif_explanation

generate_report('xparams.yaml')
run_whatif_explanation('xparams.yaml')