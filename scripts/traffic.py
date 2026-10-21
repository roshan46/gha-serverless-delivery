"""AWS CLI invocation avoids an additional unpinned SDK dependency."""
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

name, seconds = sys.argv[1], int(sys.argv[2])
deadline = time.monotonic() + seconds
errors = 0
with tempfile.TemporaryDirectory() as directory:
    output = Path(directory) / "response.json"
    while time.monotonic() < deadline:
        result = subprocess.run(["aws", "lambda", "invoke", "--function-name", name,
                                 "--qualifier", "live", str(output)], capture_output=True, text=True)
        if result.returncode:
            # First deployment has no alias yet. Bound this wait with the overall deadline.
            print("Alias unavailable or invoke failed; retrying", flush=True)
        else:
            meta = json.loads(result.stdout)
            errors += int("FunctionError" in meta)
        time.sleep(1)
print(f"Observed function errors: {errors}")
