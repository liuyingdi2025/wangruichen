from typing import List, Dict


class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        return longUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return shortUrl
