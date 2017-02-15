
# If there is an API that understands the specification this code will be very short and it will dynamically change with specification change
def get():
    return {
        # unavailable: slackclient needs token
        # "api.test" : [
        #     {
        #         "Argument": "error",
        #         "Required": "Optional",
        #         "Description": "Error response to return"
        #     },
        #     {
        #         "Argument": "foo",
        #         "Required": "Optional",
        #         "Description": "example property to return"
        #     },
        # ],

        "auth.revoke" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token."
            },
            {
                "Argument": "test",
                "Required": "Optional",
                "Description": "Setting this parameter to 1 triggers a testing mode where the specified token will not actually be revoked.",
            },
        ],
        "auth.test" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: identify"
            },
        ],

        "bots.info" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token.Requires scope: users:read"
            },
            {
                "Argument": "bot",
                "Required": "Optional",
                "Description": "Bot user to get info on",
            },
        ],

        "channels.archive" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: channels:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to archive"
            },
        ],
        "channels.create" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: channels:write"
            },
            {
                "Argument": "name",
                "Required": "Required",
                "Description": "Name of channel to create"
            },
        ],
        "channels.history" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: channels:history"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to fetch history for."
            },
            {
                "Argument": "latest",
                "Required": "Optional",
                "Description": "End of time range of messages to include in results. default=now"
            },
            {
                "Argument": "oldest",
                "Required": "Optional",
                "Description": "Start of time range of messages to include in results. default=0"
            },
            {
                "Argument": "inclusive",
                "Required": "Optional",
                "Description": "Include messages with latest or oldest timestamp in results. default=0"
            },
            {
                "Argument": "count",
                "Required": "Optional",
                "Description": "Number of messages to return, between 1 and 1000. default=100"
            },
            {
                "Argument": "unreads",
                "Required": "Optional",
                "Description": "Include unread_count_display in the output? default=0"
            },
        ],
        "channels.info" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token.Requires scope: channels:read"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to get info on"
            },
        ],
        "channels.invite" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: channels:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to invite user to."
            },
            {
                "Argument": "user",
                "Required": "Required",
                "Description": "User to invite to channel."
            },
        ],
        "channels.join" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: channels:write"
            },
            {
                "Argument": "name",
                "Required": "Required",
                "Description": "Name of channel to join"
            },
        ],
        "channels.kick" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: channels:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to remove user from."
            },
            {
                "Argument": "user",
                "Required": "Required",
                "Description": "User to remove from channel."
            },
        ],
        "channels.leave" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: channels:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to leave"
            },
        ],
        "channels.list" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token.Requires scope: channels:read"
            },
            {
                "Argument": "exclude_archived",
                "Required": "Optional",
                "Description": "Don't return archived channels. default=false"
            },
        ],
        "channels.mark" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: channels:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to set reading cursor in."
            },
            {
                "Argument": "ts",
                "Required": "Required",
                "Description": "Timestamp of the most recently seen message."
            },
        ],
        "channels.rename" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: channels:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to rename"
            },
            {
                "Argument": "name",
                "Required": "Required",
                "Description": "New name for channel."
            },
        ],
        "channels.replies" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: channels:history"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to fetch thread from"
            },
            {
                "Argument": "thread_ts",
                "Required": "Required",
                "Description": "Unique identifier of a thread's parent message"
            },
        ],
        "channels.setPurpose" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: channels:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to set the purpose of"
            },
            {
                "Argument": "purpose",
                "Required": "Required",
                "Description": "The new purpose"
            },
        ],
        "channels.setTopic" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: channels:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to set the topic of"
            },
            {
                "Argument": "topic",
                "Required": "Required",
                "Description": "The new topic"
            },
        ],
        "channels.unarchive" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: channels:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to unarchive"
            },
        ],

        "chat.delete" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token.Requires scope: chat:write:bot or chat:write:user"
            },
            {
                "Argument": "ts",
                "Required": "Required",
                "Description": "Timestamp of the message to be updated."
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel containing the message to be updated."
            },
            {
                "Argument": "as_user",
                "Required": "Optional",
                "Description": "Pass true to update the message as the authed user. Bot users in this context are considered authed users."
            },
        ],
        "chat.meMessage" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: chat:write:user"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to send message to. Can be a public channel, private group or IM channel. Can be an encoded ID, or a name."
            },
            {
                "Argument": "text",
                "Required": "Required",
                "Description": "Text of the message to send."
            },
        ],
        "chat.postMessage": [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: chat:write:bot or chat:write:user"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See below for more details."
            },
            {
                "Argument": "text",
                "Required": "Required",
                "Description": "Text of the message to send. See below for an explanation of formatting. This field is usually required, unless you're providing only attachments instead."
            },
            {
                "Argument": "parse",
                "Required": "Optional",
                "Description": "Text of the message to send. See below for an explanation of formatting. This field is usually required, unless you're providing only attachments instead.Change how messages are treated. Defaults to none. See below."
            },
            {
                "Argument": "link_names",
                "Required": "Optional",
                "Description": "Find and link channel names and usernames."
            },
            {
                "Argument": "attachments",
                "Required": "Optional",
                "Description": "Structured message attachments."
            },
            {
                "Argument": "unfurl_links",
                "Required": "Optional",
                "Description": "Pass true to enable unfurling of primarily text-based content."
            },
            {
                "Argument": "unfurl_media",
                "Required": "Optional",
                "Description": "Pass false to disable unfurling of media content."
            },
            {
                "Argument": "username",
                "Required": "Optional",
                "Description": "Set your bot's user name. Must be used in conjunction with as_user set to false, otherwise ignored. See authorship below."
            },
            {
                "Argument": "as_user",
                "Required": "Optional",
                "Description": "Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See authorship below."
            },
            {
                "Argument": "icon_url",
                "Required": "Optional",
                "Description": "URL to an image to use as the icon for this message. Must be used in conjunction with as_user set to false, otherwise ignored. See authorship below."
            },
            {
                "Argument": "icon_emoji",
                "Required": "Optional",
                "Description": "Emoji to use as the icon for this message. Overrides icon_url. Must be used in conjunction with as_user set to false, otherwise ignored. See authorship below."
            },
            {
                "Argument": "thread_ts",
                "Required": "Optional",
                "Description": "Provide another message's ts value to make this message a reply. Avoid using a reply's ts value; use its parent instead."
            },
            {
                "Argument": "reply_broadcast",
                "Required": "Optional",
                "Description": "Used in conjunction with thread_ts and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to false."
            },
        ],
        "chat.update" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token.Requires scope: chat:write:bot or chat:write:user"
            },
            {
                "Argument": "ts",
                "Required": "Required",
                "Description": "Timestamp of the message to be updated."
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel containing the message to be updated."
            },
            {
                "Argument": "text",
                "Required": "Required",
                "Description": "New text for the message, using the default formatting rules."
            },
            {
                "Argument": "attachments",
                "Required": "Optional",
                "Description": "Structured message attachments."
            },
            {
                "Argument": "parse",
                "Required": "Optional",
                "Description": "Change how messages are treated. Defaults to client, unlike chat.postMessage."
            },
            {
                "Argument": "link_names",
                "Required": "Optional",
                "Description": "Find and link channel names and usernames. Defaults to none. This parameter should be used in conjunction with parse. To set link_names to 1, specify a parse mode of full."
            },
            {
                "Argument": "as_user",
                "Required": "Optional",
                "Description": "Pass true to update the message as the authed user. Bot users in this context are considered authed users."
            },
        ],

        "dnd.endDnd" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: dnd:write"
            },
        ],
        "dnd.endSnooze" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: dnd:write"
            },
        ],
        "dnd.info" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: dnd:read"
            },
            {
                "Argument": "user",
                "Required": "Optional",
                "Description": "User to fetch status for (defaults to current user)"
            },
        ],
        "dnd.setSnooze" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: dnd:write"
            },
            {
                "Argument": "num_minutes",
                "Required": "Required",
                "Description": "Number of minutes, from now, to snooze until."
            },
        ],
        "dnd.teamInfo" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: dnd:read"
            },
            {
                "Argument": "users",
                "Required": "Optional",
                "Description": "Comma-separated list of users to fetch Do Not Disturb status for"
            },
        ],

        "emoji.list" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: emoji:read"
            },
        ],

        "files.comments.add" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: files:write:user"
            },
            {
                "Argument": "file",
                "Required": "Required",
                "Description": "File to add a comment to."
            },
            {
                "Argument": "comment",
                "Required": "Required",
                "Description": "Text of the comment to add."
            },
            {
                "Argument": "channel",
                "Required": "Optional",
                "Description": "Channel id (encoded) of which location to associate with the new comment."
            },
        ],
        "files.comments.delete" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: files:write:user"
            },
            {
                "Argument": "file",
                "Required": "Required",
                "Description": "File to delete a comment from."
            },
            {
                "Argument": "id",
                "Required": "Required",
                "Description": "The comment to delete."
            },
        ],
        "files.comments.edit" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: files:write:user"
            },
            {
                "Argument": "file",
                "Required": "Required",
                "Description": "File containing the comment to edit."
            },
            {
                "Argument": "id",
                "Required": "Required",
                "Description": "The comment to edit."
            },
            {
                "Argument": "comment",
                "Required": "Required",
                "Description": "Text of the comment to edit."
            },
        ],

        "files.delete" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token.Requires scope: files:write:user"
            },
            {
                "Argument": "file",
                "Required": "Required",
                "Description": "ID of file to delete."
            },
        ],
        "files.info" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token.Requires scope: files:read"
            },
            {
                "Argument": "file",
                "Required": "Required",
                "Description": "Specify a file by providing its ID."
            },
            {
                "Argument": "count",
                "Required": "Optional",
                "Description": "Number of items to return per page. default=100"
            },
            {
                "Argument": "page",
                "Required": "Optional",
                "Description": "Page number of results to return. default=1"
            },
        ],
        "files.list" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token.Requires scope: files:read"
            },
            {
                "Argument": "users",
                "Required": "Optional",
                "Description": "Filter files created by a single user."
            },
            {
                "Argument": "channel",
                "Required": "Optional",
                "Description": "Filter files appearing in a specific channel, indicated by its ID."
            },
            {
                "Argument": "ts_from",
                "Required": "Optional",
                "Description": "Filter files created after this timestamp (inclusive). default=0"
            },
            {
                "Argument": "ts_to",
                "Required": "Optional",
                "Description": "Filter files created before this timestamp (inclusive). default=now"
            },
            {
                "Argument": "types",
                "Required": "Optional",
                "Description": "Filter files by type: /all - All files/spaces - Posts/snippets - Snippets/images - Image files/gdocs - Google docs/zips - Zip files/pdfs - PDF files/You can pass multiple values in the types argument, like types=spaces,snippets.The default value is all, which does not filter the list. default=all"
            },
            {
                "Argument": "count",
                "Required": "Optional",
                "Description": "Number of items to return per page. default=100"
            },
            {
                "Argument": "page",
                "Required": "Optional",
                "Description": "Page number of results to return. default=1"
            },
        ],
        "files.revokePublicURL" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token.Requires scope: files:write:user"
            },
            {
                "Argument": "file",
                "Required": "Required",
                "Description": "File to revoke"
            },
        ],
        "files.sharedPublicURL" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token.Requires scope: files:write:user"
            },
            {
                "Argument": "file",
                "Required": "Required",
                "Description": "File to share"
            },
        ],
        "files.upload" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token.Requires scope: files:write:user"
            },
            {
                "Argument": "file",
                "Required": "Optional",
    #            "Description": "File contents via multipart/form-data. If omitting this parameter, you must submit content."
                "Description": "File name to be uploaded"
            },
            {
                "Argument": "content",
                "Required": "Optional",
                "Description": "File contents via a POST variable. If omitting this parameter, you must provide a file."
            },
            {
                "Argument": "filetype",
                "Required": "Optional",
                "Description": "A file type identifier."
            },
            {
                "Argument": "filename",
                "Required": "Optional",
                "Description": "Filename of file"
            },
            {
                "Argument": "title",
                "Required": "Optional",
                "Description": "Title of file."
            },
            {
                "Argument": "initial_comment",
                "Required": "Optional",
                "Description": "Initial comment to add to file."
            },
            {
                "Argument": "channels",
                "Required": "Optional",
                "Description": "Comma-separated list of channel names or IDs where the file will be shared."
            },
        ],

        "groups.archive" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to archive"
            },
        ],
        "groups.close" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to close."
            },
        ],
        "groups.create" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "name",
                "Required": "Required",
                "Description": "Name of private channel to creat"
            },
        ],
        "groups.createChild" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to clone and archive."
            },
        ],
        "groups.history" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:history"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to fetch history for."
            },
            {
                "Argument": "latest",
                "Required": "Optional",
                "Description": "End of time range of messages to include in results. default=now"
            },
            {
                "Argument": "oldest",
                "Required": "Optional",
                "Description": "Start of time range of messages to include in results. default=0"
            },
            {
                "Argument": "inclusive",
                "Required": "Optional",
                "Description": "Include messages with latest or oldest timestamp in results. default=0"
            },
            {
                "Argument": "count",
                "Required": "Optional",
                "Description": "Number of messages to return, between 1 and 1000. default=100"
            },
            {
                "Argument": "unreads",
                "Required": "Optional",
                "Description": "Include unread_count_display in the output? default=0"
            },
        ],
        "groups.info" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:read"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to get info on"
            },
        ],
        "groups.invite" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to invite user to."
            },
            {
                "Argument": "user",
                "Required": "Required",
                "Description": "User to invite."
            },
        ],
        "groups.kick" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to remove user from."
            },
            {
                "Argument": "user",
                "Required": "Required",
                "Description": "User to remove from private channel."
            },
        ],
        "groups.leave" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to leave"
            },
        ],
        "groups.list" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:read"
            },
            {
                "Argument": "exclude_archived",
                "Required": "Optional",
                "Description": "Don't return archived private channels. default=0"
            },
        ],
        "groups.mark" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to set reading cursor in."
            },
            {
                "Argument": "ts",
                "Required": "Required",
                "Description": "Timestamp of the most recently seen message."
            },
        ],
        "groups.open" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to open."
            },
        ],
        "groups.open" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to rename."
            },
            {
                "Argument": "name",
                "Required": "Required",
                "Description": "New name for private channel."
            },
        ],
        "groups.rename" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to rename."
            },
            {
                "Argument": "name",
                "Required": "Required",
                "Description": "New name for private channel."
            },
        ],
        "groups.replies" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:history"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to fetch thread from"
            },
            {
                "Argument": "thread_ts",
                "Required": "Required",
                "Description": "Unique identifier of a thread's parent message"
            },
        ],
        "groups.replies" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:history"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to fetch thread from"
            },
            {
                "Argument": "thread_ts",
                "Required": "Required",
                "Description": "Unique identifier of a thread's parent message"
            },
        ],
        "groups.setPurpose" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to set the purpose of"
            },
            {
                "Argument": "purpose",
                "Required": "Required",
                "Description": "The new purpose"
            },
        ],
        "groups.setTopic" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to set the topic of"
            },
            {
                "Argument": "topic",
                "Required": "Required",
                "Description": "The new topic"
            },
        ],
        "groups.unarchive" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: groups:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Private channel to unarchive"
            },
        ],

        "im.close" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: im:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Direct message channel to close."
            },
        ],
        "im.history" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: im:history"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Direct message channel to fetch history for."
            },
            {
                "Argument": "latest",
                "Required": "Optional",
                "Description": "End of time range of messages to include in results. default=now"
            },
            {
                "Argument": "oldest",
                "Required": "Optional",
                "Description": "Start of time range of messages to include in results. default=0"
            },
            {
                "Argument": "inclusive",
                "Required": "Optional",
                "Description": "Include messages with latest or oldest timestamp in results. default=0"
            },
            {
                "Argument": "count",
                "Required": "Optional",
                "Description": "Number of messages to return, between 1 and 1000. default=100"
            },
            {
                "Argument": "unreads",
                "Required": "Optional",
                "Description": "Include unread_count_display in the output? default=0"
            },
        ],
        "im.list" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: im:read"
            },
        ],
        "im.mark" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: im:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Direct message channel to set reading cursor in"
            },
            {
                "Argument": "ts",
                "Required": "Required",
                "Description": "Timestamp of the most recently seen message."
            },
        ],
        "im.open" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: im:write"
            },
            {
                "Argument": "user",
                "Required": "Required",
                "Description": "User to open a direct message channel with."
            },
            {
                "Argument": "return_im",
                "Required": "Optional",
                "Description": "Boolean, indicates you want the full IM channel definition in the response."
            },
        ],
        "im.replies" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: im:history"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Direct message channel to fetch thread from"
            },
            {
                "Argument": "thread_ts",
                "Required": "Required",
                "Description": "Unique identifier of a thread's parent message"
            },
        ],

        "mpim.close" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: mpim:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "MPIM to close."
            },
        ],
        "mpim.history" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: mpim:history"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Multiparty direct message to fetch history for."
            },
            {
                "Argument": "latest",
                "Required": "Optional",
                "Description": "End of time range of messages to include in results. default=now"
            },
            {
                "Argument": "oldest",
                "Required": "Optional",
                "Description": "Start of time range of messages to include in results. default=0"
            },
            {
                "Argument": "inclusive",
                "Required": "Optional",
                "Description": "Include messages with latest or oldest timestamp in results. default=0"
            },
            {
                "Argument": "count",
                "Required": "Optional",
                "Description": "Number of messages to return, between 1 and 1000. default=100"
            },
            {
                "Argument": "unreads",
                "Required": "Optional",
                "Description": "Include unread_count_display in the output? default=0"
            },
        ],
        "mpim.list" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: mpim:read"
            },
        ],
        "mpim.mark" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: mpim:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "multiparty direct message channel to set reading cursor in."
            },
            {
                "Argument": "ts",
                "Required": "Required",
                "Description": "Timestamp of the most recently seen message."
            },
        ],
        "mpim.open" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: mpim:write"
            },
            {
                "Argument": "users",
                "Required": "Required",
                "Description": "Comma separated lists of users. The ordering of the users is preserved whenever a MPIM group is returned."
            },
        ],
        "mpim.replies" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: mpim:history"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Multiparty direct message channel to fetch thread from."
            },
            {
                "Argument": "thread_ts",
                "Required": "Required",
                "Description": "Unique identifier of a thread's parent message."
            },
        ],

        "oauth.access" : [
            {
                "Argument": "client_id",
                "Required": "Required",
                "Description": "Issued when you created your application."
            },
            {
                "Argument": "client_secret",
                "Required": "Required",
                "Description": "Issued when you created your application."
            },
            {
                "Argument": "code",
                "Required": "Required",
                "Description": "The code param returned via the OAuth callback."
            },
            {
                "Argument": "redirect_uri",
                "Required": "Optional",
                "Description": "This must match the originally submitted URI (if one was sent)."
            },
        ],

        "pins.add" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: pins:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to pin the item in."
            },
            {
                "Argument": "file",
                "Required": "Optional",
                "Description": "Channel to pin the item in."
            },
            {
                "Argument": "file_comment",
                "Required": "Optional",
                "Description": "File comment to pin."
            },
            {
                "Argument": "timestamp",
                "Required": "Optional",
                "Description": "Timestamp of the message to pin."
            },
        ],
        "pins.list" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: pins:read"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel to get pinned items for."
            },
        ],
        "pins.remove" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: pins:write"
            },
            {
                "Argument": "channel",
                "Required": "Required",
                "Description": "Channel where the item is pinned to."
            },
            {
                "Argument": "file",
                "Required": "Optional",
                "Description": "File to un-pin."
            },
            {
                "Argument": "file_comment",
                "Required": "Optional",
                "Description": "File comment to un-pin."
            },
            {
                "Argument": "timestamp",
                "Required": "Optional",
                "Description": "Timestamp of the message to un-pin."
            },
        ],

        "reactions.add" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: reactions:write"
            },
            {
                "Argument": "name",
                "Required": "Required",
                "Description": "Reaction (emoji) name."
            },
            {
                "Argument": "file",
                "Required": "Optional",
                "Description": "File to add reaction to."
            },
            {
                "Argument": "file_comment",
                "Required": "Optional",
                "Description": "File comment to add reaction to."
            },
            {
                "Argument": "channel",
                "Required": "Optional",
                "Description": "Channel where the message to add reaction to was posted."
            },
            {
                "Argument": "timestamp",
                "Required": "Optional",
                "Description": "Timestamp of the message to add reaction to."
            },
        ],
        "reactions.get" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: reactions:read"
            },
            {
                "Argument": "file",
                "Required": "Optional",
                "Description": "File to get reactions for."
            },
            {
                "Argument": "file_comment",
                "Required": "Optional",
                "Description": "File comment to get reactions for."
            },
            {
                "Argument": "channel",
                "Required": "Optional",
                "Description": "Channel where the message to get reactions for was posted."
            },
            {
                "Argument": "timestamp",
                "Required": "Optional",
                "Description": "Timestamp of the message to get reactions for."
            },
            {
                "Argument": "full",
                "Required": "Optional",
                "Description": "If true always return the complete reaction list."
            },
        ],
        "reactions.list" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: reactions:read"
            },
            {
                "Argument": "user",
                "Required": "Optional",
                "Description": "Show reactions made by this user. Defaults to the authed user."
            },
            {
                "Argument": "full",
                "Required": "Optional",
                "Description": "If true always return the complete reaction list."
            },
            {
                "Argument": "count",
                "Required": "Optional",
                "Description": "Number of items to return per page. default=100"
            },
            {
                "Argument": "page",
                "Required": "Optional",
                "Description": "Page number of results to return. default=1"
            },
        ],
        "reactions.remove" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: reactions:write"
            },
            {
                "Argument": "name",
                "Required": "Required",
                "Description": "Reaction (emoji) name."
            },
            {
                "Argument": "file",
                "Required": "Optional",
                "Description": "File to remove reaction from."
            },
            {
                "Argument": "file_comment",
                "Required": "Optional",
                "Description": "File comment to remove reaction from."
            },
            {
                "Argument": "channel",
                "Required": "Optional",
                "Description": "Channel where the message to remove reaction from was posted."
            },
            {
                "Argument": "timestamp",
                "Required": "Optional",
                "Description": "Timestamp of the message to remove reaction from."
            },
        ],

        "reminders.add" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: reminders:write"
            },
            {
                "Argument": "text",
                "Required": "Required",
                "Description": "The content of the reminder"
            },
            {
                "Argument": "time",
                "Required": "Required",
                "Description": 'When this reminder should happen: the Unix timestamp (up to five years from now), the number of seconds until the reminder (if within 24 hours), or a natural language description (Ex. "in 15 minutes," or "every Thursday")'
            },
            {
                "Argument": "user",
                "Required": "Optional",
                "Description": "The user who will receive the reminder. If no user is specified, the reminder will go to user who created it."
            },
        ],
        "reminders.complete" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: reminders:write"
            },
            {
                "Argument": "reminder",
                "Required": "Required",
                "Description": "The ID of the reminder to be marked as complet"
            },
        ],
        "reminders.delete" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: reminders:write"
            },
            {
                "Argument": "reminder",
                "Required": "Required",
                "Description": "The ID of the reminder"
            },
        ],
        "reminders.info" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: reminders:read"
            },
            {
                "Argument": "reminder",
                "Required": "Required",
                "Description": "The ID of the reminder"
            },
        ],
        "reminders.list" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: reminders:read"
            },
        ],

        "search.all" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: search:read"
            },
            {
                "Argument": "query",
                "Required": "Required",
                "Description": "Search query. May contains booleans, etc"
            },
            {
                "Argument": "sort",
                "Required": "Optional",
                "Description": "Return matches sorted by either score or timestamp. default=score"
            },
            {
                "Argument": "sort_dir",
                "Required": "Optional",
                "Description": "Change sort direction to ascending (asc) or descending (desc). default=desc"
            },
            {
                "Argument": "highlight",
                "Required": "Optional",
                "Description": "Pass a value of true to enable query highlight markers"
            },
            {
                "Argument": "count",
                "Required": "Optional",
                "Description": "Number of items to return per page. default=20"
            },
            {
                "Argument": "page",
                "Required": "Optional",
                "Description": "Page number of results to return. default=1"
            },
        ],
        "search.files" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: search:read"
            },
            {
                "Argument": "query",
                "Required": "Required",
                "Description": "Search query. May contains booleans, etc"
            },
            {
                "Argument": "sort",
                "Required": "Optional",
                "Description": "Return matches sorted by either score or timestamp. default=score"
            },
            {
                "Argument": "sort_dir",
                "Required": "Optional",
                "Description": "Change sort direction to ascending (asc) or descending (desc). default=desc"
            },
            {
                "Argument": "highlight",
                "Required": "Optional",
                "Description": "Pass a value of true to enable query highlight markers"
            },
            {
                "Argument": "count",
                "Required": "Optional",
                "Description": "Number of items to return per page. default=20"
            },
            {
                "Argument": "page",
                "Required": "Optional",
                "Description": "Page number of results to return. default=1"
            },
        ],
        "search.messages" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: search:read"
            },
            {
                "Argument": "query",
                "Required": "Required",
                "Description": "Search query. May contains booleans, etc"
            },
            {
                "Argument": "sort",
                "Required": "Optional",
                "Description": "Return matches sorted by either score or timestamp. default=score"
            },
            {
                "Argument": "sort_dir",
                "Required": "Optional",
                "Description": "Change sort direction to ascending (asc) or descending (desc). default=desc"
            },
            {
                "Argument": "highlight",
                "Required": "Optional",
                "Description": "Pass a value of true to enable query highlight markers"
            },
            {
                "Argument": "count",
                "Required": "Optional",
                "Description": "Number of items to return per page. default=20"
            },
            {
                "Argument": "page",
                "Required": "Optional",
                "Description": "Page number of results to return. default=1"
            },
        ],

        "stars.add" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: stars:write"
            },
            {
                "Argument": "file",
                "Required": "Optional",
                "Description": "File to add star to."
            },
            {
                "Argument": "file_comment",
                "Required": "Optional",
                "Description": "File comment to add star to."
            },
            {
                "Argument": "channel",
                "Required": "Optional",
                "Description": "Channel to add star to, or channel where the message to add star to was posted (used with timestamp)"
            },
            {
                "Argument": "timestamp",
                "Required": "Optional",
                "Description": "Timestamp of the message to add star to."
            },
        ],
        "stars.list" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: stars:read"
            },
            {
                "Argument": "count",
                "Required": "Optional",
                "Description": "Number of items to return per page. default=100"
            },
            {
                "Argument": "page",
                "Required": "Optional",
                "Description": "Page number of results to return. default=1"
            },
        ],
        "stars.remove" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: stars:write"
            },
            {
                "Argument": "file",
                "Required": "Optional",
                "Description": "File to remove star from."
            },
            {
                "Argument": "file_comment",
                "Required": "Optional",
                "Description": "File comment to remove star from."
            },
            {
                "Argument": "channel",
                "Required": "Optional",
                "Description": "Channel to remove star from, or channel where the message to remove star from was posted (used with timestamp)."
            },
            {
                "Argument": "timestamp",
                "Required": "Optional",
                "Description": "Timestamp of the message to remove star from."
            },
        ],

        "team.accessLogs" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: admin"
            },
            {
                "Argument": "count",
                "Required": "Optional",
                "Description": "Number of items to return per page. default=100"
            },
            {
                "Argument": "page",
                "Required": "Optional",
                "Description": "Page number of results to return. default=1"
            },
            {
                "Argument": "before",
                "Required": "Optional",
                "Description": "End of time range of logs to include in results (inclusive). default=now"
            },
        ],
        "team.billableInfo" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: admin"
            },
            {
                "Argument": "user",
                "Required": "Optional",
                "Description": "A user to retrieve the billable information for. Defaults to all users."
            },
        ],
        "team.info" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: team:read"
            },
        ],
        "team.integrationLogs" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: admin"
            },
            {
                "Argument": "service_id",
                "Required": "Optional",
                "Description": "Filter logs to this service. Defaults to all logs."
            },
            {
                "Argument": "app_id",
                "Required": "Optional",
                "Description": "Filter logs to this Slack app. Defaults to all logs."
            },
            {
                "Argument": "user",
                "Required": "Optional",
                "Description": "Filter logs generated by this user's actions. Defaults to all logs."
            },
            {
                "Argument": "change_type",
                "Required": "Optional",
                "Description": "Filter logs with this change type. Defaults to all logs."
            },
            {
                "Argument": "count",
                "Required": "Optional",
                "Description": "Number of items to return per page."
            },
            {
                "Argument": "page",
                "Required": "Optional",
                "Description": "Page number of results to return."
            },
        ],

        "team.profile.get" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: users.profile:read"
            },
            {
                "Argument": "visibility",
                "Required": "Optional",
                "Description": "Filter by visibility."
            },
        ],

        "usergroups.create" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: usergroups:write"
            },
            {
                "Argument": "name",
                "Required": "Required",
                "Description": "A name for the User Group. Must be unique among User Groups."
            },
            {
                "Argument": "handle",
                "Required": "Optional",
                "Description": "A mention handle. Must be unique among channels, users and User Groups."
            },
            {
                "Argument": "description",
                "Required": "Optional",
                "Description": "A short description of the User Group."
            },
            {
                "Argument": "channels",
                "Required": "Optional",
                "Description": "A comma separated string of encoded channel IDs for which the User Group uses as a default."
            },
            {
                "Argument": "include_count",
                "Required": "Optional",
                "Description": "Include the number of users in each User Group."
            },
        ],
        "usergroups.disable" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: usergroups:write"
            },
            {
                "Argument": "usergroup",
                "Required": "Required",
                "Description": "The encoded ID of the User Group to disable."
            },
            {
                "Argument": "include_count",
                "Required": "Optional",
                "Description": "Include the number of users in the User Group."
            },
        ],
        "usergroups.enable" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: usergroups:write"
            },
            {
                "Argument": "usergroup",
                "Required": "Required",
                "Description": "The encoded ID of the User Group to disable."
            },
            {
                "Argument": "include_count",
                "Required": "Optional",
                "Description": "Include the number of users in the User Group."
            },
        ],
        "usergroups.list" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: usergroups:read"
            },
            {
                "Argument": "include_disabled",
                "Required": "Optional",
                "Description": "Include disabled User Groups."
            },
            {
                "Argument": "include_count",
                "Required": "Optional",
                "Description": "Include the number of users in the User Group."
            },
            {
                "Argument": "include_users",
                "Required": "Optional",
                "Description": "Include the list of users for each User Group."
            },
        ],
        "usergroups.update" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: usergroups:write"
            },
            {
                "Argument": "usergroup",
                "Required": "Required",
                "Description": "The encoded ID of the User Group to update."
            },
            {
                "Argument": "name",
                "Required": "Optional",
                "Description": "A name for the User Group. Must be unique among User Groups."
            },
            {
                "Argument": "handle",
                "Required": "Optional",
                "Description": "A mention handle. Must be unique among channels, users and User Groups."
            },
            {
                "Argument": "description",
                "Required": "Optional",
                "Description": "A short description of the User Group."
            },
            {
                "Argument": "channels",
                "Required": "Optional",
                "Description": "A comma separated string of encoded channel IDs for which the User Group uses as a default."
            },
            {
                "Argument": "include_count",
                "Required": "Optional",
                "Description": "Include the number of users in the User Group."
            },
        ],

        "usergroups.users.list" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: usergroups:read"
            },
            {
                "Argument": "usergroup",
                "Required": "Required",
                "Description": "The encoded ID of the User Group to update."
            },
            {
                "Argument": "include_disabled",
                "Required": "Optional",
                "Description": "Allow results that involve disabled User Groups."
            },
        ],
        "usergroups.users.update" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: usergroups:write"
            },
            {
                "Argument": "usergroup",
                "Required": "Required",
                "Description": "The encoded ID of the User Group to update."
            },
            {
                "Argument": "users",
                "Required": "Required",
                "Description": "A comma separated string of encoded user IDs that represent the entire list of users for the User Group."
            },
            {
                "Argument": "include_count",
                "Required": "Optional",
                "Description": "Include the number of users in the User Group."
            },
        ],

        "users.deletePhoto" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: users.profile:write"
            },
        ],
        "users.getPresence" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: users:read"
            },
            {
                "Argument": "user",
                "Required": "Required",
                "Description": "User to get presence info on. Defaults to the authed user."
            },
        ],
        "users.identity" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: identity.basic"
            },
        ],
        "users.info" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: users:read"
            },
            {
                "Argument": "user",
                "Required": "Required",
                "Description": "User to get info on"
            },
        ],
        "users.list" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: users:read"
            },
            {
                "Argument": "presence",
                "Required": "Optional",
                "Description": "Whether to include presence data in the output"
            },
        ],
        "users.setActive" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: users:write"
            },
        ],
        "users.setPhoto" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: users.profile:write"
            },
            {
                "Argument": "image",
                "Required": "Required",
                "Description": "File contents via multipart/form-data."
            },
            {
                "Argument": "crop_x",
                "Required": "Optional",
                "Description": "X coordinate of top-left corner of crop box"
            },
            {
                "Argument": "crop_y",
                "Required": "Optional",
                "Description": "Y coordinate of top-left corner of crop box"
            },
            {
                "Argument": "crop_w",
                "Required": "Optional",
                "Description": "Width/height of crop box (always square)"
            },
        ],
        "users.setPresence" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: users:write"
            },
            {
                "Argument": "presence",
                "Required": "Required",
                "Description": "Either auto or away"
            },
        ],

        "users.profile.get" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: users.profile:read"
            },
            {
                "Argument": "user",
                "Required": "Optional",
                "Description": "User to retrieve profile info for"
            },
            {
                "Argument": "include_labels",
                "Required": "Optional",
                "Description": "Include labels for each ID in custom profile fields. default=false"
            },
        ],
        "users.profile.set" : [
            {
                "Argument": "token",
                "Required": "Required",
                "Description": "Authentication token. Requires scope: users.profile:write"
            },
            {
                "Argument": "user",
                "Required": "Optional",
                "Description": "ID of user to change. This argument may only be specified by team admins on paid teams."
            },
            {
                "Argument": "profile",
                "Required": "Optional",
                "Description": "Collection of key:value pairs presented as a URL-encoded JSON hash."
            },
            {
                "Argument": "name",
                "Required": "Optional",
                "Description": "Name of a single key to set. Usable only if profile is not passed."
            },
            {
                "Argument": "value",
                "Required": "Optional",
                "Description": "Value to set a single key to. Usable only if profile is not passed."
            },
        ],
    }
