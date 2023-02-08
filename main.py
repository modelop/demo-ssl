import json

import modelop.schema.infer as infer
import modelop.stats.diagnostics as diagnostics
import modelop.utils as utils
from modelop_sdk.utils import dashboard_utils as dashboard_utils

DEPLOYABLE_MODEL = {}
JOB = {}
MODEL_METHODOLOGY = ""


# modelop.init
def init(job_json):
    global DEPLOYABLE_MODEL
    global JOB
    global MODEL_METHODOLOGY

    job = json.loads(job_json["rawJson"])
    DEPLOYABLE_MODEL = job["referenceModel"]
    MODEL_METHODOLOGY = DEPLOYABLE_MODEL.get("storedModel", {}).get("modelMetaData", {}).get("modelMethodology", "")

    JOB = job_json
    infer.validate_schema(job_json)


# modelop.metrics
def metrics(baseline) -> dict:
    result = {
        "Databricks SSL Cert":"Expired",
        "Internal Corp SSL":"Valid",
        "Datalake SSL":"Valid"
    }
    yield result