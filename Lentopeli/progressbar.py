def create_progress_bar (progres: float, length: int = 20) -> str:
    progress = max(0.0, min(100.0, progres))
    filled_length = int(length * (progress /100.0))
    bar = "|" * filled_length + "-" * (length - filled_length)
    return f"[{bar} {progress:.1f}%"

print(create_progress_bar( 50,20))


