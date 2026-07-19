import unittest
from unittest.mock import patch

from app import app


class XquikExportRouteTests(unittest.TestCase):
    def test_analyzes_current_xquik_tweet_shape(self):
        client = app.test_client()
        payload = {
            "tweets": [
                {
                    "text": "A useful launch",
                    "createdAt": "2026-07-18T08:00:00Z",
                    "author": {"username": "xquik"},
                }
            ]
        }

        with patch("app.get_prediction", return_value="Positive Comment"):
            response = client.post("/xquik-export", json=payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {
                "count": 1,
                "results": [
                    {
                        "tweet": "A useful launch",
                        "sentiment": "Positive Comment",
                        "created_at": "2026-07-18T08:00:00Z",
                        "username": "xquik",
                    }
                ],
            },
        )


if __name__ == "__main__":
    unittest.main()
