def notify_recruiter(user: dict, vm_score: float, config: dict):
    message = (
        f"Talent Alert:\n"
        f"User ID: {user['id']}\n"
        f"Email: {user['email']}\n"
        f"VM_MAGNITUDE: {vm_score:.2f}\n"
        f"Threshold: {config['vm_threshold']}\n"
        f"Recruiter Email: {config['recruiter_email']}\n"
    )
    print(message)

