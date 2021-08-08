from flask_testing import TestCase
from app import app
from flask import current_app, url_for
from random import uniform
import json


class MainTest(TestCase):

    def create_app(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config["TESTING"])

    def test_bacteria_growth_get(self):
        response = self.client.get(url_for("bacteria_growth"))
        self.assert200(response)

    def test_lact_pred_get(self):
        response = self.client.get(url_for("lact_pred"))
        self.assert200(response)

    def test_lact_pred_post(self):
        fake_lact = json.dumps({
            "lact_value": [2.591, 0.992, 4.415, 3.1925],
            "lact_single_target": 5.15
        })
        response = self.client.post(url_for("lact_pred"), data=fake_lact)
        self.assert200(response)

    def test_list_strep_pred_get(self):
        response = self.client.get(url_for("list_strep_pred"))
        self.assertRedirects(response, url_for("bacteria_growth"))

    def test_list_strep_pred_post(self):
        fake_list_strep = json.dumps({
            "strep_values": [2.591, 0.992, 4.415, 3.1925],
            "strep_target": 5.15
        })
        response = self.client.post(url_for("list_strep_pred"), data=fake_list_strep)
        self.assert200(response)

    def test_strep_pred_get(self):
        response = self.client.get(url_for("strep_pred"))
        self.assert200(response)

    def test_strep_pred_post(self):
        strep_lact = json.dumps({
            "strep_value": [2.591, 0.992, 4.415, 3.1925],
            "strep_single_target": 5.15
        })
        response = self.client.post(url_for("strep_pred"), data=strep_lact)
        self.assert200(response)



