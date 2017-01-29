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
    slack-cli --help
    usage: slack-cli [-h] --token TOKEN --channel CHANNEL [--text TEXT]
                 [--parse PARSE] [--link_names LINK_NAMES]
                 [--attachments ATTACHMENTS] [--unfurl_links UNFURL_LINKS]
                 [--unfurl_media UNFURL_MEDIA] [--username USERNAME]
                 [--as_user AS_USER] [--icon_url ICON_URL]
                 [--icon_emoji ICON_EMOJI] [--thread_ts THREAD_TS]
                 [--reply_broadcast REPLY_BROADCAST]

    /bin/slack-cli [Args] [Options] Detailed options -h or --help

    optional arguments:
      -h, --help            show this help message and exit
      --token TOKEN         Authentication token. Requires scope: chat:write:bot
                            or chat:write:user
      --channel CHANNEL     Channel, private group, or IM channel to send message
                            to. Can be an encoded ID, or a name. See below for
                            more details.
      --text TEXT           Text of the message to send. See below for an
                            explanation of formatting. This field is usually
                            required, unless you're providing only attachments
                            instead.
      --parse PARSE         Text of the message to send. See below for an
                            explanation of formatting. This field is usually
                            required, unless you're providing only attachments
                            instead.Change how messages are treated. Defaults to
                            none. See below.
      --link_names LINK_NAMES
                            Find and link channel names and usernames.
      --attachments ATTACHMENTS
                            Structured message attachments.
      --unfurl_links UNFURL_LINKS
                            Pass true to enable unfurling of primarily text-based
                            content.
      --unfurl_media UNFURL_MEDIA
                            Pass false to disable unfurling of media content.
      --username USERNAME   Set your bot's user name. Must be used in conjunction
                            with as_user set to false, otherwise ignored. See
                            authorship below.
      --as_user AS_USER     Pass true to post the message as the authed user,
                            instead of as a bot. Defaults to false. See authorship
                            below.
      --icon_url ICON_URL   URL to an image to use as the icon for this message.
                            Must be used in conjunction with as_user set to false,
                            otherwise ignored. See authorship below.
      --icon_emoji ICON_EMOJI
                            Emoji to use as the icon for this message. Overrides
                            icon_url. Must be used in conjunction with as_user set
                            to false, otherwise ignored. See authorship below.
      --thread_ts THREAD_TS
                            Provide another message's ts value to make this
                            message a reply. Avoid using a reply's ts value; use
                            its parent instead.
      --reply_broadcast REPLY_BROADCAST
                            Used in conjunction with thread_ts and indicates
                            whether reply should be made visible to everyone in
                            the channel or conversation. Defaults to false.

    # It can also be specified by environment variable
    export SLACK_API_TOKEN='xoxp-xxxxxxxxxxxxxxxxx'
    export SLACK_API_CHANNEL = '#some_channel'
    export SLACK_API_TEXT = 'some message'
    export SLACK_API_{arg.upper()} = 'some value'

# License
MIT License
