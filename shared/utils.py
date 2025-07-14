import logging

def log_request(request, logger_name='default'):
    logger = logging.getLogger(logger_name)

    user = request.user.username if request.user.is_authenticated else 'Anonymous'
    method = request.method
    path = request.get_full_path()
    get_data = dict(request.GET)
    post_data = dict(request.POST)
    ip_address = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')

    logger.info("Yangi so‘rov:")
    logger.info(f"Method: {method}")
    logger.info(f"URL: {path}")
    logger.info(f"GET: {get_data}")
    logger.info(f"POST: {post_data}")
    logger.info(f"User: {user}")
    logger.info(f"IP Address: {ip_address}")
    logger.info(f"User-Agent: {user_agent}")
    logger.info("-"*150)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')
