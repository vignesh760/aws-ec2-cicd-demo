
from pathlib import Path
import unittest

ROOT = Path(__file__).parent


class PortfolioTests(unittest.TestCase):

    def test_homepage_exists(self):
        self.assertTrue((ROOT / "index.html").is_file())

    def test_stylesheet_exists(self):
        self.assertTrue((ROOT / "style.css").is_file())

    def test_javascript_exists(self):
        self.assertTrue((ROOT / "script.js").is_file())

    def test_navigation_links_have_matching_sections(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")

        for section in ["about", "skills", "projects", "contact"]:
            with self.subTest(section=section):
                self.assertIn(f'href="#{section}"', html)
                self.assertIn(f'id="{section}"', html)

    def test_stylesheet_supports_mobile_layout(self):
        css = (ROOT / "style.css").read_text(encoding="utf-8")
        self.assertIn("@media", css)

    def test_copyright_year_is_dynamic(self):
        js = (ROOT / "script.js").read_text(encoding="utf-8")
        self.assertIn("getFullYear()", js)


if __name__ == "__main__":
    unittest.main(verbosity=2)
