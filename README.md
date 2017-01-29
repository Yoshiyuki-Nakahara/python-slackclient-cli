# python-slack-cli
A command line interface for Slack

# Requirement
`$ pip install slackclient`
https://github.com/slackapi/python-slackclient

# Reference
  https://api.slack.com/methods/chat.postMessage

# Install
    curl https://raw.githubusercontent.com/Yoshiyuki-Nakahara/python-slack-cli/master/slack-cli -o /path/to/slack-cli
    chmod +x /path/to/slack-cli

# Usage
    slack-cli [-h]
        --token TOKEN
        --channel CHANNEL
        --text TEXT
        [--parse PARSE] [--link_names LINK_NAMES]
        [--attachments ATTACHMENTS] [--unfurl_links UNFURL_LINKS]
        [--unfurl_media UNFURL_MEDIA] [--username USERNAME]
        [--as_user AS_USER] [--icon_url ICON_URL]
        [--icon_emoji ICON_EMOJI] [--thread_ts THREAD_TS]
        [--reply_broadcast REPLY_BROADCAST]
    # It can also be specified by environment variable
    export SLACK_API_TOKEN='xoxp-xxxxxxxxxxxxxxxxx'
    export SLACK_API_CHANNEL = '#some_channel'
    export SLACK_API_TEXT = 'some message'
    export SLACK_API_{arg.upper()} = 'some value'

# License
MIT License
