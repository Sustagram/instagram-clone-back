def make_response_payload(data=None, message=None, is_success=True):
    return {
        "success": is_success,
        "message": message,
        "data": data
    }
