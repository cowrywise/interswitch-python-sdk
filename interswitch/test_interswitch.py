import pytest
from interswitch.api import InterSwitchAPI
from interswitch.exceptions import InterswitchAPIException
from interswitch.constants import Constants


class TestInterSwitch(object):
    def test_user_can_fetch_acces_token_from_passport(self):
        api = InterSwitchAPI(
            client_secret="FTbMeBD7MtkGBQJw1XoM74NaikuPL13Sxko1zb0DMjI=",
            client_id="IKIAF6C068791F465D2A2AA1A3FE88343B9951BAC9C3",
            env=Constants.ENV_SANDBOX,
            terminal_id="3ERT0001",
        )

        token = api.get_client_access_token()

        assert token is not None

    def test_api_raises_exception_for_invalid_credentials(self):
        api = InterSwitchAPI(
            client_secret="invalidsecret",
            client_id="invalidclientid",
            env=Constants.ENV_SANDBOX,
            terminal_id="3ERT0001",
        )

        with pytest.raises(InterswitchAPIException) as e_info:
            api.get_client_access_token()

        assert e_info.value.args[0] == "Bad credentials"

    def test_user_can_fetch_billers_from_api(self):
        api = InterSwitchAPI(
            client_secret="FTbMeBD7MtkGBQJw1XoM74NaikuPL13Sxko1zb0DMjI=",
            client_id="IKIAF6C068791F465D2A2AA1A3FE88343B9951BAC9C3",
            env=Constants.ENV_SANDBOX,
            terminal_id="3ERT0001",
        )

        result = api.get_billers()

        assert "billers" in result

    def test_user_can_fetch_bank_codes_from_api(self):
        api = InterSwitchAPI(
            client_secret="FTbMeBD7MtkGBQJw1XoM74NaikuPL13Sxko1zb0DMjI=",
            client_id="IKIAF6C068791F465D2A2AA1A3FE88343B9951BAC9C3",
            env=Constants.ENV_SANDBOX,
            terminal_id="3ERT0001",
        )

        result = api.get_bank_codes()
        assert "banks" in result

    def test_user_can_fetch_owner_of_account_number_from_api(self):
        # Test Details here https://sandbox.interswitchng.com/docbase/docs/quickteller-sva/test-details/
        api = InterSwitchAPI(
            client_secret="FTbMeBD7MtkGBQJw1XoM74NaikuPL13Sxko1zb0DMjI=",
            client_id="IKIAF6C068791F465D2A2AA1A3FE88343B9951BAC9C3",
            env=Constants.ENV_SANDBOX,
            terminal_id="3ERT0001",
        )

        result = api.name_enquiry("058", "0014261063")

        assert result["accountName"] == "EVANS  ERHOBAGA-AGOFURE"

    def test_user_can_transfer_money_to_another_bank_account(self):
        api = InterSwitchAPI(
            client_secret="FTbMeBD7MtkGBQJw1XoM74NaikuPL13Sxko1zb0DMjI=",
            client_id="IKIAF6C068791F465D2A2AA1A3FE88343B9951BAC9C3",
            env=Constants.ENV_SANDBOX,
            terminal_id="3ERT0001",
        )

        result = api.transfer_funds(
            initiating_entity_code="ERT",
            sender_last_name="Chi",
            sender_other_names="Chi",
            beneficiary_last_name="Danny",
            beneficiary_other_names="Samuel",
            initiation_amount="100000",
            initiation_channel="7",
            initiation_payment_method_code="CA",
            initiation_currency_code="566",
            terminating_payment_method_code="AC",
            terminating_amount="100000",
            terminating_currency_code="566",
            terminating_country_code="NG",
            terminating_account_number="0014261063",
            terminating_account_type="10",
            terminating_entity_code="058",
        )

        assert result["responseCode"] == "90000"
        res = api.query_transaction(result["transferCode"])

        assert res["transactionResponseCode"] == "90000"

    def test_user_can_fetch_biller_category_from_api(self):
        api = InterSwitchAPI(
            client_secret="FTbMeBD7MtkGBQJw1XoM74NaikuPL13Sxko1zb0DMjI=",
            client_id="IKIAF6C068791F465D2A2AA1A3FE88343B9951BAC9C3",
            env=Constants.ENV_SANDBOX,
            terminal_id="3ERT0001",
        )

        result = api.get_biller_categories()
        assert "categorys" in result

    def test_user_can_fetch_billers_in_category_from_api(self):
        api = InterSwitchAPI(
            client_secret="FTbMeBD7MtkGBQJw1XoM74NaikuPL13Sxko1zb0DMjI=",
            client_id="IKIAF6C068791F465D2A2AA1A3FE88343B9951BAC9C3",
            env=Constants.ENV_SANDBOX,
            terminal_id="3ERT0001",
        )

        result = api.get_billers_by_category(2)
        assert "billers" in result

    def test_user_can_fetch_biller_payment_itemsfrom_api(self):
        api = InterSwitchAPI(
            client_secret="FTbMeBD7MtkGBQJw1XoM74NaikuPL13Sxko1zb0DMjI=",
            client_id="IKIAF6C068791F465D2A2AA1A3FE88343B9951BAC9C3",
            env=Constants.ENV_SANDBOX,
            terminal_id="3ERT0001",
        )

        result = api.get_biller_payments(905)
        assert "paymentitems" in result

    def test_user_can_send_bill_payment_advice_via_api(self):
        api = InterSwitchAPI(
            client_secret="FTbMeBD7MtkGBQJw1XoM74NaikuPL13Sxko1zb0DMjI=",
            client_id="IKIAF6C068791F465D2A2AA1A3FE88343B9951BAC9C3",
            env=Constants.ENV_SANDBOX,
            terminal_id="3ERT0001",
        )

        result = api.send_bill_payment_advice(
            "90501", "0434556574", "2348056731576", "iswtester2@yahoo.com", 5000
        )

        assert result["responseCode"] == "90000"

    def test_user_can_inquiry_bill_payment_via_api(self):
        api = InterSwitchAPI(
            client_secret="FTbMeBD7MtkGBQJw1XoM74NaikuPL13Sxko1zb0DMjI=",
            client_id="IKIAF6C068791F465D2A2AA1A3FE88343B9951BAC9C3",
            env=Constants.ENV_SANDBOX,
            terminal_id="3ERT0001",
        )

        result = api.bill_payment_inquiry(
            "90501", "0434556574", "2348056731576", "iswtester2@yahoo.com"
        )
        assert result is not None

    def test_user_can_validate_customers_via_api(self):
        api = InterSwitchAPI(
            client_secret="FTbMeBD7MtkGBQJw1XoM74NaikuPL13Sxko1zb0DMjI=",
            client_id="IKIAF6C068791F465D2A2AA1A3FE88343B9951BAC9C3",
            env=Constants.ENV_SANDBOX,
            terminal_id="3ERT0001",
        )
        customers = [{"customerId": "0434556574", "paymentCode": "90501"}]
        result = api.customer_validation(customers)
        assert len(result["Customers"]) == 1
