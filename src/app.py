import os


def handler(event, context):
    if os.environ.get("FAIL_RELEASE") == "true":
        raise RuntimeError("Controlled canary failure")
    return {"statusCode": 200, "body": "healthy", "release": os.environ["RELEASE_ID"]}
