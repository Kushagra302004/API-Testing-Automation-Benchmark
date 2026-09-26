import logging, time, requests
logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self, base_url, token=None, timeout=5):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.headers = {"Accept": "application/json"}
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def _request(self, method, endpoint, **kwargs):
        url = self.base_url + endpoint
        headers = {**self.headers, **kwargs.pop("headers", {})}
        start = time.perf_counter()
        logger.info("%s %s", method, url)
        response = requests.request(method, url, headers=headers, timeout=self.timeout, **kwargs)
        logger.info("%s %s -> %s (%.3fs)", method, endpoint, response.status_code, time.perf_counter()-start)
        return response

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, data=None, **kwargs):
        return self._request("POST", endpoint, json=data, **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        return self._request("PUT", endpoint, json=data, **kwargs)

    def patch(self, endpoint, data=None, **kwargs):
        return self._request("PATCH", endpoint, json=data, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)
