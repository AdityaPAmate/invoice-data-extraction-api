import os
import psutil


def log_memory_usage(stage):
    """
    Prints the current RAM usage of the Django process.

    Args:
        stage (str): Name of the current processing stage.
    """
    process = psutil.Process(os.getpid())

    # Memory used by the current process (in MB)
    memory_mb = process.memory_info().rss / (1024 * 1024)

    print(f"\n{'=' * 60}")
    print(f"MEMORY CHECKPOINT : {stage}")
    print(f"Current RAM Usage : {memory_mb:.2f} MB")
    print(f"{'=' * 60}\n")