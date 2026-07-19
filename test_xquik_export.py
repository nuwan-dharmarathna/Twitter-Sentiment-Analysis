import unittest

from xquik_export import load_xquik_rows


class XquikExportTests(unittest.TestCase):
    def test_loads_json_array(self):
        rows = load_xquik_rows('[{"text":"Great update","username":"alice"}]')

        self.assertEqual(rows, [{"tweet": "Great update", "created_at": "", "username": "alice"}])

    def test_loads_nested_payload(self):
        rows = load_xquik_rows('{"data":[{"full_text":"Nested row","date":"2026-07-04"}]}')

        self.assertEqual(rows[0]["tweet"], "Nested row")
        self.assertEqual(rows[0]["created_at"], "2026-07-04")

    def test_loads_current_xquik_tweet_shape(self):
        rows = load_xquik_rows(
            '{"tweets":[{"text":"Current row","createdAt":"2026-07-18T08:00:00Z",'
            '"author":{"username":"xquik"}}]}'
        )

        self.assertEqual(
            rows,
            [
                {
                    "tweet": "Current row",
                    "created_at": "2026-07-18T08:00:00Z",
                    "username": "xquik",
                }
            ],
        )

    def test_loads_jsonl(self):
        rows = load_xquik_rows('{"tweet":"One"}\n{"body":"Two"}\n')

        self.assertEqual([row["tweet"] for row in rows], ["One", "Two"])

    def test_loads_csv_and_skips_blank_rows(self):
        rows = load_xquik_rows("tweet,username\nHello,alice\n,bob\n")

        self.assertEqual(rows, [{"tweet": "Hello", "created_at": "", "username": "alice"}])


if __name__ == "__main__":
    unittest.main()
