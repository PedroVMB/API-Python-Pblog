from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class PostAnonRateThrottle(AnonRateThrottle):
    rate = '10/day'

class ImageAnonRateThrottle(AnonRateThrottle):
    rate = '10/day'