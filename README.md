# Verified Lambda delivery exercise

Read Lab 11 in the study module. Bootstrap separate sandbox development/production roles and storage, configure environment protection, and run a healthy baseline before injecting a fault.

The workflow tests and attests one ZIP, verifies provenance before each deployment, promotes identical bytes, and uses the SAM canary alarm to recover a failed release. A red job alone is not proof of rollback: verify the restored alias and healthy response.
