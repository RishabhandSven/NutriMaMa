def send_alert(alert_data: dict) -> bool:
    """
    Process and store emergency alerts in Redis and Firestore.

    Parameters:
    - alert_data: A dictionary containing alert information.

    Returns:
    - bool: True if the alert was successfully sent, False otherwise.
    """
    # Logic to send alert to Redis and Firestore
    # This is a placeholder for the actual implementation
    try:
        # Example: Store alert in Redis
        # redis_client.set(alert_data['id'], alert_data)

        # Example: Store alert in Firestore
        # firestore_client.collection('alerts').add(alert_data)

        return True
    except Exception as e:
        # Handle exceptions (e.g., logging)
        print(f"Error sending alert: {e}")
        return False