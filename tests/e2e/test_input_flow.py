from playwright.sync_api import Page, expect

VALID_PESEL = "05251512319"
INVALID_PESEL_CHECKSUM = "05251512315"


def test_pesel_form_validation_flow(live_server, page: Page):
    page.goto(f"{live_server.url}")
    expect(page.locator("nav")).to_contain_text("PESEL Checker")

    pesel_input = page.get_by_label("PESEL Number")
    submit_button = page.locator('button[type="submit"]')

    pesel_input.fill(INVALID_PESEL_CHECKSUM)
    submit_button.click()

    error_message = page.get_by_role("alert")
    expect(error_message).to_be_visible()

    pesel_input.fill(VALID_PESEL)
    submit_button.click()

    expected_results = {"Gender": "Male", "Day": "15", "Month": "5", "Year": "2005"}

    for key, value in expected_results.items():
        row = page.get_by_role("listitem").filter(has_text=f"{key}:")
        expect(row).to_be_visible()
        expect(row).to_contain_text(value)
