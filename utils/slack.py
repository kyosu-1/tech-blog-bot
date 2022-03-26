from slack_sdk.webhook import WebhookClient, webhook_response


SlackWebhookResponse = webhook_response.WebhookResponse


def post_slack_by_webhook(url: str, text: str) -> SlackWebhookResponse:
    """send message to slack by webhook

    Args:
        url (str): webhook url
        text (str): message

    Returns:
        SlackWebhookResponse: response
    """
    webhook = WebhookClient(url)

    response = webhook.send(text=text)
    return response
